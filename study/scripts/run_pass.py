#!/usr/bin/env python3
"""
run_pass.py — concurrent coding runner for the framework study.

    export ANTHROPIC_API_KEY=...
    python run_pass.py --batches batches/ --out coded/ --concurrency 4

Design notes, all of which matter for this specific workload:

* The codebook is byte-identical in every call and is ~65% of the input. It goes in
  its own content block with cache_control, so it costs 10% of base input on every
  call after the first. Cached reads also do not count toward ITPM, so caching buys
  throughput as well as money.

* One warm-up call runs alone before the pool starts. If N concurrent calls all
  begin against a cold cache they all pay the write, and you lose the discount on
  the first N calls.

* The pool ramps rather than bursting. Anthropic applies acceleration limits that
  can return 429 on a sharp traffic spike even when you are inside your tier
  ceiling, so workers start staggered.

* Resumable. A batch whose output file already exists is skipped unless --force.
  This will run for hours and will be interrupted.
"""

import argparse, asyncio, json, os, random, sys, time
from pathlib import Path
from datetime import datetime, timezone

try:
    from anthropic import AsyncAnthropic, APIStatusError, APIConnectionError
except ImportError:
    sys.exit("pip install anthropic")

MODEL = os.environ.get("STUDY_MODEL", "claude-sonnet-5")
MAX_TOKENS = 32000
MAX_ATTEMPTS = 5


def now():
    return datetime.now(timezone.utc).isoformat()


def _is_record(line: str) -> bool:
    s = line.strip()
    if not s.startswith("{"):
        return False
    try:
        json.loads(s)
    except json.JSONDecodeError:
        return False
    return True


def strip_noise(text: str):
    """
    Drop non-record scaffolding from the head and tail of a JSONL response,
    returning (text, dropped_line_count).

    Everything from the first line that parses as a JSON object to the last such
    line is kept verbatim, so no record can be lost, reordered or altered. Only
    lines outside that span are removed. Junk *between* records is deliberately
    left in place: it would signal a deeper failure than scaffolding, and
    validate_runs.py should fail the batch rather than have it silently cleaned.

    Needed because claude-sonnet-5 rejects assistant prefill, which is what used
    to force bare JSONL. The earlier version of this function removed a fence only
    when it sat on the first or last non-blank line. In the A1 run of 2026-08-14
    the model prefixed 7 of 12 responses with a sentence of commentary, which
    pushed the opening fence off line one and defeated that test; the closing
    fence was stripped and the preamble plus opening fence survived into the
    output file. Anchoring on "the first line that is actually a record" holds
    regardless of what precedes it.
    """
    lines = text.split("\n")
    idx = [i for i, ln in enumerate(lines) if _is_record(ln)]
    if not idx:
        return text, 0
    lo, hi = idx[0], idx[-1]
    dropped = sum(1 for i, ln in enumerate(lines)
                  if ln.strip() and (i < lo or i > hi))
    return "\n".join(lines[lo:hi + 1]), dropped


def build_messages(codebook: str, prompt: str, units_payload: str, payload_label: str):
    """
    Cache breakpoint goes after the stable prefix. Everything before it is reused
    across every call; the per-batch units come after and are never cached.
    """
    system = [
        {"type": "text", "text": prompt},
        {
            "type": "text",
            "text": codebook,
            "cache_control": {"type": "ephemeral"},
        },
    ]
    # No assistant prefill: claude-sonnet-5 rejects a trailing assistant turn with
    # HTTP 400 ("This model does not support assistant message prefill"). The
    # prompts already require bare JSONL with no fences or commentary.
    messages = [
        {"role": "user", "content": f"{payload_label}:\n{units_payload}"},
    ]
    return system, messages


async def call_one(client, sem, batch_path: Path, out_path: Path,
                   codebook: str, prompt: str, log_path: Path, stats: dict,
                   payload_label: str, max_tokens: int, effort: str,
                   thinking: str, stream: bool):
    async with sem:
        units_payload = batch_path.read_text()
        system, messages = build_messages(codebook, prompt, units_payload, payload_label)

        kwargs = dict(
            model=MODEL,
            max_tokens=max_tokens,
            # temperature omitted: claude-sonnet-5 rejects any non-default
            # sampling parameter with HTTP 400 ("`temperature` is deprecated
            # for this model"). Sampling runs at the model default.
            #
            # effort is the only control over thinking spend on this model
            # (budget_tokens is removed and 400s). The API default is "high",
            # which measured 1,641 output tokens per coded unit against 1,016
            # at "medium" — see run_config.json -> calibration.
            output_config={"effort": effort},
            system=system,
            messages=messages,
        )
        if thinking == "disabled":
            # A1 must run this way. With adaptive thinking the segmentation call
            # spends its whole budget on thinking blocks and returns no text at
            # all — an empty output file that otherwise logs as a success.
            kwargs["thinking"] = {"type": "disabled"}

        for attempt in range(1, MAX_ATTEMPTS + 1):
            t0 = time.monotonic()
            try:
                if stream:
                    # Required above 21,333 output tokens: the SDK refuses a
                    # non-streaming request whose estimated duration exceeds ten
                    # minutes (3600 * max_tokens / 128000 > 600).
                    async with client.messages.stream(**kwargs) as s:
                        resp = await s.get_final_message()
                else:
                    resp = await client.messages.create(**kwargs)
            except APIStatusError as e:
                if e.status_code == 429:
                    # Honour the server's own backoff when it gives one.
                    wait = float(e.response.headers.get("retry-after", 0)) or min(
                        60, 2 ** attempt + random.random()
                    )
                    stats["throttled"] += 1
                    print(f"  429 {batch_path.name} attempt {attempt}, sleeping {wait:.0f}s")
                    await asyncio.sleep(wait)
                    continue
                if 500 <= e.status_code < 600:
                    await asyncio.sleep(min(60, 2 ** attempt + random.random()))
                    continue
                stats["failed"] += 1
                print(f"  FAIL {batch_path.name}: HTTP {e.status_code} {e}")
                return
            except (APIConnectionError, asyncio.TimeoutError):
                await asyncio.sleep(min(60, 2 ** attempt + random.random()))
                continue

            elapsed = time.monotonic() - t0
            # No prefill to re-attach; the model emits the whole record itself.
            text = "".join(b.text for b in resp.content if b.type == "text")
            text, dropped = strip_noise(text)
            if dropped:
                stats["stripped"] += dropped
                print(f"  {dropped} non-record line(s) stripped from {batch_path.name}")
            out_path.write_text(text)

            u = resp.usage
            cached = getattr(u, "cache_read_input_tokens", 0) or 0
            written = getattr(u, "cache_creation_input_tokens", 0) or 0
            with log_path.open("a") as f:
                f.write(json.dumps({
                    "ts": now(), "batch": batch_path.name, "out": out_path.name,
                    "model": MODEL, "model_version": resp.model, "attempt": attempt,
                    "input_tokens": u.input_tokens, "output_tokens": u.output_tokens,
                    "cache_read": cached, "cache_write": written,
                    "seconds": round(elapsed, 1),
                    "tok_per_sec": round(u.output_tokens / elapsed, 1) if elapsed else None,
                    "stop_reason": resp.stop_reason,
                    "stripped": dropped,
                }) + "\n")

            stats["done"] += 1
            stats["out_tokens"] += u.output_tokens
            if resp.stop_reason == "max_tokens":
                stats["truncated"] += 1
                print(f"  TRUNCATED {batch_path.name} — reduce batch size")
            print(f"  ok {batch_path.name} {u.output_tokens:,} out "
                  f"({u.output_tokens/elapsed:.0f} tok/s, cache_read {cached:,})")
            return

        stats["failed"] += 1
        print(f"  FAIL {batch_path.name}: exhausted {MAX_ATTEMPTS} attempts")


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches", required=True, help="dir of per-batch unit JSONL files")
    ap.add_argument("--out", required=True)
    ap.add_argument("--codebook", default="docs/codebook_v8.txt")
    ap.add_argument("--prompt", required=True,
                    help="A1-segment.md, A2-align.md or B-content-change.md")
    ap.add_argument("--payload-label", default="UNITS",
                    help="header the batch payload is announced under in the user "
                         "turn (A1: V_TARGET, A2: ALIGNMENT_BATCH, B: UNITS)")
    ap.add_argument("--max-tokens", type=int, default=MAX_TOKENS,
                    help=f"per-call output ceiling (default {MAX_TOKENS}); A1 needs "
                         "more than the coding passes")
    ap.add_argument("--effort", default="medium",
                    choices=["low", "medium", "high", "xhigh", "max"],
                    help="thinking/output spend. The API default is high; this study "
                         "pins medium for the coding passes and high for A1 (see "
                         "run_config.json). Must match across the OpenAI/GDM and the "
                         "later Anthropic/xAI runs.")
    ap.add_argument("--thinking", default="adaptive", choices=["adaptive", "disabled"],
                    help="A1 requires 'disabled': with adaptive thinking the "
                         "segmentation call returns thinking blocks only and writes "
                         "an empty output file")
    ap.add_argument("--stream", action="store_true",
                    help="required when --max-tokens exceeds 21333")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--ramp", type=float, default=3.0,
                    help="seconds between worker starts, to avoid acceleration limits")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="stop after N batches (for piloting)")
    a = ap.parse_args()

    codebook = Path(a.codebook).read_text()
    prompt = Path(a.prompt).read_text()
    outdir = Path(a.out); outdir.mkdir(parents=True, exist_ok=True)
    log_path = Path("run_log.jsonl")

    batches = sorted(Path(a.batches).glob("*.jsonl"))
    todo = []
    for b in batches:
        out = outdir / b.name
        if out.exists() and not a.force:
            continue
        todo.append((b, out))
    if a.limit:
        todo = todo[: a.limit]

    if a.max_tokens > 21333 and not a.stream:
        sys.exit("--max-tokens above 21333 requires --stream (SDK non-streaming limit)")

    print(f"{len(batches)} batches, {len(todo)} to run, concurrency {a.concurrency}, "
          f"model {MODEL}, label {a.payload_label}, max_tokens {a.max_tokens}, "
          f"effort {a.effort}, thinking {a.thinking}"
          f"{', streaming' if a.stream else ''}")
    if not todo:
        return

    client = AsyncAnthropic(max_retries=0)   # retries handled here, not in the SDK
    stats = {"done": 0, "failed": 0, "throttled": 0, "truncated": 0,
             "out_tokens": 0, "stripped": 0}
    t_start = time.monotonic()

    # Warm the cache with a single call before fanning out.
    print("warming cache with one call…")
    await call_one(client, asyncio.Semaphore(1), todo[0][0], todo[0][1],
                   codebook, prompt, log_path, stats, a.payload_label, a.max_tokens,
                   a.effort, a.thinking, a.stream)
    rest = todo[1:]

    sem = asyncio.Semaphore(a.concurrency)

    async def staggered(i, b, o):
        await asyncio.sleep(min(i, a.concurrency) * a.ramp)
        await call_one(client, sem, b, o, codebook, prompt, log_path, stats,
                       a.payload_label, a.max_tokens, a.effort, a.thinking, a.stream)

    await asyncio.gather(*(staggered(i, b, o) for i, (b, o) in enumerate(rest)))

    mins = (time.monotonic() - t_start) / 60
    print(f"\ndone {stats['done']} | failed {stats['failed']} | 429s {stats['throttled']} "
          f"| truncated {stats['truncated']} | noise lines stripped {stats['stripped']}")
    print(f"{stats['out_tokens']:,} output tokens in {mins:.1f} min "
          f"({stats['out_tokens']/mins/60:.0f} tok/s aggregate)")
    if stats["failed"]:
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\ninterrupted — rerun the same command to resume")
