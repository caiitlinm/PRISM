#!/usr/bin/env python3
"""
build_batches.py — produce the variable payload files run_pass.py consumes.

One subcommand per pass. Every batch filename encodes its {SCOPE} so the
downstream grammar coded/{SCOPE}.{content|change}.{model}.r{n}.jsonl can be
parsed back: the scope is the filename with its trailing .{digits}.jsonl removed.

    python study/scripts/build_batches.py a1      --labs OpenAI "Google DeepMind"
    python study/scripts/build_batches.py a2      --labs OpenAI "Google DeepMind"
    python study/scripts/build_batches.py content --labs OpenAI "Google DeepMind"
    python study/scripts/build_batches.py change  --labs OpenAI "Google DeepMind"

a1 reads corpus text. a2 reads frozen units. content reads frozen units.
change reads frozen units plus the crosswalk. Each pass therefore requires the
previous one's output to exist, which is the intended checkpoint ordering.

Payload labels expected by run_pass.py --payload-label:
    a1 -> V_TARGET      a2 -> ALIGNMENT_BATCH      content/change -> UNITS
"""

import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "study"
CORPUS = STUDY / "corpus"
MANIFEST = CORPUS / "manifest.jsonl"

LAB_DIR = {
    "Anthropic": "anthropic",
    "OpenAI": "openai",
    "Google DeepMind": "deepmind",
    "xAI": "xai",
}

# 8000 was the requested chunk size, but A1 emits ~907 chars per unit at ~38 units
# per 1000 words, so an 8000-word chunk needs ~110k output tokens — close to the
# 128k ceiling with no margin. 4000 words lands near 55k, comfortably streamable.
A1_MAX_WORDS = 4000
# build_a2 repeats the whole prior-unit list as a header on every batch, so the
# budget must clear that header with room for a useful number of target units. At
# ~186 tokens per unit record the header is 48k tokens for OAI-PF-2023 and 42k for
# GDM-FSF-v3-0 — both larger than the original 40000, which made the fill loop
# flush after every single target unit: 688 calls and $63.68 for this run's five
# transitions, 3,006 calls and $394.90 for the Anthropic/xAI half, producing an
# identical crosswalk. 90000 gives 7 and 33 calls respectively. Raised at
# Checkpoint B, 2026-08-14; the later labs must use the same value.
A2_MAX_TOKENS = 90000
# 25 truncated at effort medium (21 of 25 units completed against the 21,333-token
# non-streaming ceiling). 15 units ~= 15,240 output tokens, ~29% headroom.
B_BATCH_UNITS = 15

# Offline, deterministic token estimate. Deliberately not the count_tokens API:
# batch composition must be reproducible weeks later without a network call, and
# both ceilings above sit far below the model's 1M context, so precision buys
# nothing. Divisor is conservative (real English JSON runs nearer 4 chars/token).
CHARS_PER_TOKEN = 3.5


def est_tokens(s: str) -> int:
    return int(len(s) / CHARS_PER_TOKEN)


# ----------------------------------------------------------------- manifest

def load_manifest(labs):
    docs = [json.loads(l) for l in MANIFEST.read_text().splitlines() if l.strip()]
    docs = [d for d in docs if d["lab"] in labs]
    docs.sort(key=lambda d: (d["lab"], d["date"]))
    return docs


def by_lab(docs):
    out = {}
    for d in docs:
        out.setdefault(d["lab"], []).append(d)
    return out


VERSION_TOK = re.compile(r"^(v\d+|\d{4})$", re.I)


def transition_id(prior_id: str, target_id: str) -> str:
    """
    {prior_id}_{target suffix}, where the suffix is the target identifier with the
    labs' shared prefix removed at a hyphen boundary. Reproduces the specified
    form: OAI-PF-2023 -> OAI-PF-v2 gives OAI-PF-2023_v2.

    The walk stops at the first token that opens a version or a year, even when the
    two identifiers share it. Versions like v3-0 and v3-1 occupy two hyphen tokens,
    so stripping purely on equality cut inside the version and produced
    GDM-FSF-v3-0_1 for GDM-FSF-v3-0 -> GDM-FSF-v3-1. That form is ambiguous and
    inconsistent with every other transition. It affects one transition in the
    OpenAI/GDM run and six in the Anthropic/xAI half (four consecutive RSP v3
    steps, RSP v2-1 -> v2-2, and XAI-RMF-2025-02 -> -08), and transition_id must be
    identical across the two halves, so it is fixed before any A2 pass runs.
    """
    parts_p, parts_t = prior_id.split("-"), target_id.split("-")
    i = 0
    while (i < min(len(parts_p), len(parts_t)) and parts_p[i] == parts_t[i]
           and not VERSION_TOK.match(parts_p[i])):
        i += 1
    return f"{prior_id}_{'-'.join(parts_t[i:]) or target_id}"


def chains(docs):
    """Adjacent pairs per lab, plus the endpoint pair when it is not already one."""
    adjacent, endpoint = [], []
    for lab, ds in by_lab(docs).items():
        for a, b in zip(ds, ds[1:]):
            adjacent.append((a, b))
        if len(ds) > 2:
            endpoint.append((ds[0], ds[-1]))
    return adjacent, endpoint


def doc_meta(d):
    return {
        "identifier": d["identifier"],
        "lab_name": d["lab"],
        "framework_name": d["framework"],
        "framework_version": d.get("version", "NONE"),
        "framework_year": int(d["date"][:4]),
    }


# ----------------------------------------------------------------- paths

def text_path(d):
    return CORPUS / LAB_DIR[d["lab"]] / "text" / f"{d['identifier']}.clean.txt"


def read_doc_lines(d):
    """
    Read a corpus document as lines, normalising the extractor's page breaks.

    pdftotext emits U+000C FORM FEED at each page boundary and the corpus also
    carries U+2028 LINE SEPARATOR. str.splitlines() treats both as breaks, but a
    heading immediately after a page break then has a *text* line before it rather
    than a blank one, which defeats heading detection. Mapping the form feed to a
    blank line restores the separation the printed page actually had. The corpus
    files themselves are never modified.
    """
    raw = text_path(d).read_text()
    return raw.replace("\f", "\n\n").replace(" ", "\n").split("\n")


def units_path(d):
    return CORPUS / LAB_DIR[d["lab"]] / "units" / f"{d['identifier']}.units.jsonl"


def read_units(d):
    p = units_path(d)
    if not p.exists():
        sys.exit(f"missing frozen units: {p}\nRun the A1 pass for {d['identifier']} first.")
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def write_batches(outdir: Path, scope: str, records_per_batch, width: int):
    outdir.mkdir(parents=True, exist_ok=True)
    written = []
    for i, records in enumerate(records_per_batch, start=1):
        p = outdir / f"{scope}.{i:0{width}d}.jsonl"
        p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
        written.append(p)
    return written


def chunked(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


# ----------------------------------------------------------------- A1

TABLE_OPEN = re.compile(r"^<<TABLE\b")
TABLE_CLOSE = re.compile(r"^<</TABLE>>")
# The trailing period is optional: GDM and OpenAI write "1  Introduction", Anthropic
# writes "1. Our Recommendations" and "3.1.    Scope and Timing". Without it the whole
# Anthropic section hierarchy is invisible and eight of nine RSPs produce a single
# 6,000-6,500 word chunk, over the A1_MAX_WORDS ceiling. Analyst decision D4,
# 2026-08-14; re-running the builder over all nineteen documents left the twelve
# frozen OpenAI/GDM a1 batches byte-identical.
NUMBERED_TOP = re.compile(r"^\s{0,6}(\d{1,2})\.?\s{1,8}[A-Z(]")
DOTTED_NUM = re.compile(r"^\s{0,8}\d{1,2}(\.\d{1,2}){1,2}\.?\s{1,8}\S")
BARE_HEADING = re.compile(r"^\s{0,8}[A-Z][A-Za-z0-9 ,&/'’()-]{2,58}$")
MIN_CHUNK_WORDS = 200          # anything smaller is merged forward

# An interior run of three or more spaces is pdftotext -layout rendering columns.
LAYOUT_ROW = re.compile(r"\S {3,}\S")
LAYOUT_WINDOW, LAYOUT_NEED = 6, 4


def _in_layout_table(lines, i):
    """
    True when line i sits inside a table that carries no <<TABLE>> markers.

    Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3-5 were hand-transcribed, so every
    other table in the corpus reaches us as pdftotext column layout that table_mask
    cannot see. Their cells match the heading patterns: GDM-FSF-v3-0 line 455,
    "1 (exploratory): Possesses", is a cell of Table 2.2.3.a and matched
    NUMBERED_TOP on the "(" branch, putting a chunk boundary through the middle of
    the table. Neither A1 call could then see the whole row.
    """
    lo, hi = max(0, i - LAYOUT_WINDOW), min(len(lines), i + LAYOUT_WINDOW + 1)
    return sum(1 for j in range(lo, hi) if LAYOUT_ROW.search(lines[j])) >= LAYOUT_NEED


def table_mask(lines):
    """True for every line inside a <<TABLE>> … <</TABLE>> block, inclusive."""
    mask, inside = [False] * len(lines), False
    for i, ln in enumerate(lines):
        if TABLE_OPEN.match(ln):
            inside = True
        mask[i] = inside
        if TABLE_CLOSE.match(ln):
            inside = False
    return mask


def _is_heading_line(ln):
    """Headings are short and unpunctuated; this rejects footnote prose that also
    begins with a digit ("1 Our focus in this document is on catastrophic risk.")."""
    s = ln.strip()
    return 0 < len(s) <= 70 and not s.endswith(('.', ';', ':', ','))


def boundary_sets(lines):
    """
    Candidate section boundaries, coarsest first. Never returns a line inside a
    <<TABLE>> block, so a hand-transcribed table can never be split.
    """
    mask = table_mask(lines)

    def pick(rx, extra=None):
        return [i for i, ln in enumerate(lines)
                if not mask[i] and not _in_layout_table(lines, i)
                and rx.match(ln) and _is_heading_line(ln)
                and (extra is None or extra(i, ln))]

    top = pick(NUMBERED_TOP)
    dotted = pick(DOTTED_NUM)
    # A heading sits on its own line after a break. Body text follows, but not
    # necessarily on the very next line — these documents blank-separate headings.
    bare = pick(BARE_HEADING,
                lambda i, ln: (i == 0 or not lines[i - 1].strip())
                and any(lines[j].strip() for j in range(i + 1, min(i + 4, len(lines)))))

    out = []
    if len(top) >= 3:
        out.append(("top-level numbered", top))
    if len(bare) >= 3:
        out.append(("bare headings", bare))
    if len(top) + len(dotted) >= 3:
        out.append(("numbered + subsections", sorted(set(top + dotted))))
    allb = sorted(set(top + dotted + bare))
    if allb:
        out.append(("all headings", allb))
    return out or [("whole document", [])]


def _chunk_by(lines, starts, max_words):
    bounds = sorted(set([0] + list(starts) + [len(lines)]))
    sections = [(a, b) for a, b in zip(bounds, bounds[1:]) if b > a]
    chunks, cur, cur_w = [], [], 0
    for a, b in sections:
        w = len(" ".join(lines[a:b]).split())
        if cur and cur_w + w > max_words:
            chunks.append((cur, cur_w))
            cur, cur_w = [], 0
        cur.append((a, b))
        cur_w += w
    if cur:
        chunks.append((cur, cur_w))

    # Merge a runt (usually a title line above the first real heading) forward.
    merged = []
    for spans, w in chunks:
        if merged and w < MIN_CHUNK_WORDS:
            merged[-1] = (merged[-1][0] + spans, merged[-1][1] + w)
        elif merged and merged[-1][1] < MIN_CHUNK_WORDS:
            merged[-1] = (merged[-1][0] + spans, merged[-1][1] + w)
        else:
            merged.append((spans, w))
    return merged


def section_starts(lines, max_words):
    """Choose the coarsest boundary set that keeps every chunk within max_words."""
    options = boundary_sets(lines)
    best = None
    for label, starts in options:
        chunks = _chunk_by(lines, starts, max_words)
        if best is None:
            best = (label, chunks)
        if all(w <= max_words for _, w in chunks):
            return label, chunks
    return best


def build_a1(docs, outdir):
    made = []
    for d in docs:
        lines = read_doc_lines(d)
        strategy, chunk_spans = section_starts(lines, A1_MAX_WORDS)
        chunks = [spans for spans, _ in chunk_spans]

        meta = doc_meta(d)
        records = []
        running = 1
        for n, ch in enumerate(chunks, start=1):
            body = "\n".join("\n".join(lines[a:b]) for a, b in ch)
            words = len(body.split())
            records.append([{
                **meta,
                "chunk": n,
                "chunk_count": len(chunks),
                "first_unit_number": running,
                "word_count": words,
                "text": body,
            }])
            # Hint only; Stage 3 renumbers across chunks and verifies the seams.
            running += max(1, words // 30)

        paths = []
        for n, rec in enumerate(records, start=1):
            p = outdir / f"{d['identifier']}.{n:02d}.jsonl"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(rec[0], ensure_ascii=False) + "\n")
            paths.append(p)
        over = [r[0]["word_count"] for r in records if r[0]["word_count"] > A1_MAX_WORDS]
        made.append((d["identifier"], len(paths), strategy,
                     [r[0]["word_count"] for r in records], over))
    return made


# ----------------------------------------------------------------- A2

def build_a2(pairs, outdir, tag=""):
    made = []
    for prior, target in pairs:
        tid = transition_id(prior["identifier"], target["identifier"])
        prior_units = read_units(prior)
        target_units = read_units(target)

        context = [{k: u[k] for k in
                    ("unit_id", "section_heading", "locator", "context_stem",
                     "excerpt", "paraphrase") if k in u}
                   for u in prior_units]
        header = {"type": "prior_units", "transition_id": tid,
                  "prior_identifier": prior["identifier"],
                  "target_identifier": target["identifier"],
                  "units": context}
        overhead = est_tokens(json.dumps(header, ensure_ascii=False))

        batches, cur, cur_tok = [], [], overhead
        for u in target_units:
            rec = {"type": "target_unit", **{k: u[k] for k in
                   ("unit_id", "section_heading", "locator", "context_stem",
                    "excerpt", "paraphrase") if k in u}}
            t = est_tokens(json.dumps(rec, ensure_ascii=False))
            if cur and cur_tok + t > A2_MAX_TOKENS:
                batches.append(cur)
                cur, cur_tok = [], overhead
            cur.append(rec)
            cur_tok += t
        if cur:
            batches.append(cur)

        paths = write_batches(outdir, tid, [[header] + b for b in batches], 2)
        made.append((tid, len(paths), len(target_units), len(prior_units),
                     overhead, tag))
    return made


# ----------------------------------------------------------------- B-content

CONTENT_PRIOR_FIELDS = {
    "prior_unit_id": "NONE", "prior_locator": "NONE",
    "prior_counterpart_excerpt": "NONE", "prior_modal_register": "NONE",
    "prior_stated_bar": "NONE", "alignment_note": "NONE",
    "transition_id": "NONE", "removal_candidate": False,
}


def build_content(docs, outdir):
    made = []
    for d in docs:
        units = read_units(d)
        recs = [{**u, **CONTENT_PRIOR_FIELDS} for u in units]
        paths = write_batches(outdir, d["identifier"],
                              list(chunked(recs, B_BATCH_UNITS)), 3)
        made.append((d["identifier"], len(paths), len(recs)))
    return made


# ----------------------------------------------------------------- B-change

def crosswalk_path(tid, endpoint=False):
    base = STUDY / "crosswalk" / ("endpoint" if endpoint else "")
    return base / f"{tid}.crosswalk.jsonl"


def build_change(pairs, outdir, endpoint=False):
    made = []
    for prior, target in pairs:
        tid = transition_id(prior["identifier"], target["identifier"])
        cw_path = crosswalk_path(tid, endpoint)
        if not cw_path.exists():
            sys.exit(f"missing crosswalk: {cw_path}\nRun the A2 pass for {tid} first.")
        rows = [json.loads(l) for l in cw_path.read_text().splitlines() if l.strip()]

        pri = {u["unit_id"]: u for u in read_units(prior)}
        tgt = {u["unit_id"]: u for u in read_units(target)}

        recs = []
        for r in rows:
            p = pri.get(r["prior_unit_id"])
            if r.get("removal_candidate"):
                # The coded unit is the prior-version unit that vanished. Its own
                # span is the prior-version evidence the change-family gate needs.
                if p is None:
                    sys.exit(f"{tid}: removal row references unknown prior unit "
                             f"{r['prior_unit_id']}")
                base = dict(p)
                prior_side = p
            else:
                t = tgt.get(r["target_unit_id"])
                if t is None:
                    sys.exit(f"{tid}: row references unknown target unit "
                             f"{r['target_unit_id']}")
                base = dict(t)
                prior_side = p
            recs.append({
                **base,
                "transition_id": tid,
                "prior_unit_id": r["prior_unit_id"],
                "prior_locator": (prior_side or {}).get("locator", "NONE"),
                "prior_counterpart_excerpt": (prior_side or {}).get("excerpt", "NONE"),
                "prior_modal_register": (prior_side or {}).get("modal_register", "NONE"),
                "prior_stated_bar": (prior_side or {}).get("stated_bar", "NONE"),
                "alignment_note": r.get("alignment_note", "NONE"),
                "removal_candidate": bool(r.get("removal_candidate", False)),
            })

        paths = write_batches(outdir, tid, list(chunked(recs, B_BATCH_UNITS)), 3)
        made.append((tid, len(paths), len(recs),
                     sum(1 for r in recs if r["removal_candidate"])))
    return made


# ----------------------------------------------------------------- main

def main():
    global CORPUS
    ap = argparse.ArgumentParser()
    ap.add_argument("pass_name", choices=["a1", "a2", "content", "change"])
    ap.add_argument("--labs", nargs="+", default=["OpenAI", "Google DeepMind"])
    ap.add_argument("--out", default=str(STUDY / "batches"))
    ap.add_argument("--corpus", default=str(CORPUS),
                    help="corpus root; override to build from a scratch units tree "
                         "without touching the frozen one")
    ap.add_argument("--batch-size", type=int, default=B_BATCH_UNITS,
                    help=f"units per coding batch (default {B_BATCH_UNITS}); must "
                         "match across the OpenAI/GDM and later Anthropic/xAI runs")
    ap.add_argument("--a1-max-words", type=int, default=A1_MAX_WORDS,
                    help=f"words per A1 chunk (default {A1_MAX_WORDS}); sized so each "
                         "chunk's unit output fits one streamed call")
    ap.add_argument("--endpoint", action="store_true",
                    help="a2/change only: build the v_first->v_last pairs instead")
    a = ap.parse_args()
    CORPUS = Path(a.corpus)
    globals()["B_BATCH_UNITS"] = a.batch_size
    globals()["A1_MAX_WORDS"] = a.a1_max_words

    docs = load_manifest(a.labs)
    if not docs:
        sys.exit(f"no manifest entries for labs {a.labs}")
    out = Path(a.out)
    adjacent, endpoint = chains(docs)

    if a.pass_name == "a1":
        for ident, n, strat, wcs, over in build_a1(docs, out / "a1"):
            note = f"  OVERSIZE section(s): {over}" if over else ""
            print(f"  {ident:<16} {n} chunk(s)  words={wcs}  headings={strat}{note}")

    elif a.pass_name == "a2":
        pairs = endpoint if a.endpoint else adjacent
        sub = (out / "a2" / "endpoint") if a.endpoint else (out / "a2")
        if not pairs:
            print("  no endpoint pairs (every lab has 2 documents or fewer)")
            return
        for tid, n, nt, np_, oh, _ in build_a2(pairs, sub, "endpoint" if a.endpoint else ""):
            print(f"  {tid:<26} {n} batch(es)  target={nt} prior={np_} "
                  f"context~{oh:,}tok")

    elif a.pass_name == "content":
        for ident, n, nu in build_content(docs, out / "content"):
            print(f"  {ident:<16} {n} batch(es)  {nu} units")

    elif a.pass_name == "change":
        pairs = endpoint if a.endpoint else adjacent
        sub = (out / "change" / "endpoint") if a.endpoint else (out / "change")
        if not pairs:
            print("  no endpoint pairs (every lab has 2 documents or fewer)")
            return
        for tid, n, nr, nrem in build_change(pairs, sub, a.endpoint):
            print(f"  {tid:<26} {n} batch(es)  {nr} rows ({nrem} removal)")


if __name__ == "__main__":
    main()
