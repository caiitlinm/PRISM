#!/usr/bin/env python3
"""
validate_runs.py — structural validation of model output, per batch.

    python validate_runs.py a1      --runs study/raw/a1      --batches study/batches/a1
    python validate_runs.py a2      --runs study/raw/a2      --batches study/batches/a2
    python validate_runs.py content --runs study/coded/content --batches study/batches/content
    python validate_runs.py change  --runs study/coded/change  --batches study/batches/change

Reports one line per batch and exits non-zero if any batch fails. It never edits
model output: a failing batch is deleted and re-run, per the study ground rules.
Re-run a failing batch up to twice; a third failure is a prompt or codebook problem
and stops the run.

The checks exist because these specific failures have already happened or are
structurally invisible downstream:

* An A1 call under adaptive thinking spent its whole budget on thinking blocks and
  wrote an empty file while logging as a success. Emptiness is check one.
* A1 emits a markdown fence intermittently. run_pass.py strips a wrapping fence,
  but an inner one would survive as an unparseable line.
* A truncated A2 call silently drops target units from the crosswalk, and
  build_change() then builds change batches with those units simply absent. Only a
  coverage check against the input batch catches it.
* C02 and C10 are retired. A model emitting them, or omitting one of the fourteen
  live codes, produces a table with a column of silent zeros.
"""

import argparse, json, re, sys
from pathlib import Path

ACTIVE_CODES = ["C01", "C03", "C04", "C05", "C06", "C07",
                "C08", "C09", "C11", "C12", "C13", "C14", "C15", "C16"]
RETIRED_CODES = {"C02", "C10"}
CONTENT_FAMILY = {"C08", "C09", "C11", "C12", "C13", "C14", "C15", "C16"}

A1_FIELDS = [
    "unit_id", "source_version", "lab_name", "framework_name", "framework_version",
    "framework_year", "section_heading", "locator", "unit_type", "context_stem",
    "excerpt", "paraphrase", "modal_register", "stated_bar", "duplicate_of",
    "removal_candidate", "prior_locator", "prior_counterpart_excerpt",
    "prior_modal_register", "prior_stated_bar", "alignment_note",
]
A2_FIELDS = ["transition_id", "target_unit_id", "prior_unit_id",
             "alignment_note", "removal_candidate"]

UNIT_TYPES = {"numbered", "bullet", "table_cell", "paragraph", "footnote", "callout"}
MODALS = {"mandatory", "conditional", "aspirational", "none"}
UNIT_ID = re.compile(r"^[A-Za-z0-9-]+-\d{4}(-[a-z])?$")
MARKER = re.compile(r"<<|>>")


def load_jsonl(path):
    """Return (records, errors). Blank lines are ignored; every other line must parse."""
    recs, errs = [], []
    text = path.read_text()
    if not text.strip():
        return recs, ["file is empty"]
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            recs.append(json.loads(line))
        except json.JSONDecodeError as e:
            errs.append(f"line {n} does not parse: {e.msg}")
    return recs, errs


def present(rec, fields, where, errs):
    for f in fields:
        if f not in rec:
            errs.append(f"{where}: missing field {f}")
        elif rec[f] is None or (isinstance(rec[f], str) and not rec[f].strip()):
            errs.append(f"{where}: field {f} is blank or null")


# ----------------------------------------------------------------- A1

def check_a1(recs, batch, warns):
    errs = []
    ident = batch[0].get("identifier") if batch else None
    first = batch[0].get("first_unit_number") if batch else None
    seen = []
    for r in recs:
        uid = r.get("unit_id", "?")
        present(r, A1_FIELDS, uid, errs)
        if not UNIT_ID.match(str(uid)):
            errs.append(f"{uid}: unit_id does not match {{IDENTIFIER}}-{{0000}}")
        elif ident and not str(uid).startswith(ident + "-"):
            errs.append(f"{uid}: unit_id does not carry the chunk's identifier {ident}")
        if r.get("source_version") != "target":
            errs.append(f"{uid}: source_version is not 'target'")
        if r.get("removal_candidate") is not False:
            errs.append(f"{uid}: removal_candidate must be false in the A1 pass")
        for f in ("prior_locator", "prior_counterpart_excerpt", "prior_modal_register",
                  "prior_stated_bar", "alignment_note"):
            if r.get(f) != "NONE":
                errs.append(f"{uid}: {f} must be 'NONE' in the A1 pass")
        for f in ("excerpt", "context_stem", "paraphrase", "section_heading"):
            if MARKER.search(str(r.get(f, ""))):
                errs.append(f"{uid}: transcription marker syntax leaked into {f}")
        n_words = len(str(r.get("excerpt", "")).split())
        if n_words > 75:
            # A warning, not a failure. A1-segment.md states 75 words as a hard
            # ceiling, but review-protocol.md Stage 4 check 5 lists over-75 units
            # as suspicious units for human review, so the design already expects
            # and routes them. Failing the batch would resample every unit in the
            # chunk to correct one excerpt. Analyst decision, 2026-08-14.
            warns.append(f"{uid}: excerpt is {n_words} words, over the 75-word "
                         "ceiling — Stage 4 check 5")
        if r.get("unit_type") not in UNIT_TYPES:
            errs.append(f"{uid}: unit_type {r.get('unit_type')!r} outside the vocabulary")
        if r.get("modal_register") not in MODALS:
            errs.append(f"{uid}: modal_register {r.get('modal_register')!r} outside the vocabulary")
        seen.append(str(uid))

    if len(set(seen)) != len(seen):
        dupes = {u for u in seen if seen.count(u) > 1}
        errs.append(f"duplicate unit_ids: {sorted(dupes)}")
    nums = [int(u.split("-")[-1]) if u.split("-")[-1].isdigit()
            else int(u.split("-")[-2]) for u in seen if UNIT_ID.match(u)]
    if nums != sorted(nums):
        errs.append("unit_ids are not in ascending document order")
    if first is not None and nums and nums[0] != first:
        errs.append(f"numbering starts at {nums[0]}, chunk expects {first}")
    return errs


# ----------------------------------------------------------------- A2

def check_a2(recs, batch):
    errs = []
    header = next((b for b in batch if b.get("type") == "prior_units"), None)
    targets = [b["unit_id"] for b in batch if b.get("type") == "target_unit"]
    prior_ids = {u["unit_id"] for u in (header or {}).get("units", [])}
    tid = (header or {}).get("transition_id")

    aligned, removals = [], 0
    for r in recs:
        where = r.get("target_unit_id", "?")
        present(r, A2_FIELDS, where, errs)
        if tid and r.get("transition_id") != tid:
            errs.append(f"{where}: transition_id {r.get('transition_id')!r} != {tid!r}")
        if r.get("removal_candidate") is True:
            removals += 1
            if r.get("target_unit_id") != "NONE":
                errs.append(f"{where}: removal row must carry target_unit_id 'NONE'")
            if r.get("prior_unit_id") not in prior_ids:
                errs.append(f"{where}: removal row references unknown prior unit "
                            f"{r.get('prior_unit_id')!r}")
        else:
            aligned.append(r.get("target_unit_id"))
            if prior_ids and r.get("prior_unit_id") not in prior_ids | {"NONE"}:
                errs.append(f"{where}: prior_unit_id {r.get('prior_unit_id')!r} "
                            "is not a unit of the prior version")

    missing = [t for t in targets if t not in set(aligned)]
    if missing:
        errs.append(f"{len(missing)} target unit(s) absent from the crosswalk "
                    f"(truncation?): {missing[:5]}{'…' if len(missing) > 5 else ''}")
    extra = [a for a in aligned if a not in set(targets)]
    if extra:
        errs.append(f"{len(extra)} row(s) reference units not in this batch: {extra[:5]}")
    if len(aligned) != len(set(aligned)):
        errs.append("a target unit is aligned more than once")
    return errs


# ----------------------------------------------------------------- B

def check_b(recs, batch, is_change, warns):
    errs = []
    expected = [u["unit_id"] for u in batch]
    removal = {u["unit_id"] for u in batch if u.get("removal_candidate")}
    got = []

    for r in recs:
        uid = r.get("unit_id", "?")
        got.append(uid)
        codes = r.get("codes")
        if not isinstance(codes, dict):
            errs.append(f"{uid}: missing or malformed codes object")
            continue
        for retired in RETIRED_CODES & set(codes):
            errs.append(f"{uid}: retired code {retired} present")
        for c in ACTIVE_CODES:
            if c not in codes:
                errs.append(f"{uid}: code {c} absent")
                continue
            cell = codes[c]
            if not isinstance(cell, dict):
                errs.append(f"{uid}/{c}: not an object")
                continue
            present(cell, ["value", "direction", "evidence", "flag",
                           "ambiguity_reason"], f"{uid}/{c}", errs)
            v = cell.get("value")
            # The "removal units carry NA for content codes" rule is a Stage 8
            # table-building rule, not a coding instruction: removal units never
            # went through the content pass, so their content codes are NA in the
            # joined CSV because they were never evaluated. B-content-change.md
            # emits all fourteen codes for every row it is given, which is correct;
            # build_tables.py substitutes NA for the content family on removal rows.
            # An earlier version of this check failed those rows and was wrong.
            if v not in (0, 1, "NA"):
                errs.append(f"{uid}/{c}: value {v!r} is not 0, 1 or NA")
            if cell.get("flag") not in ("clear", "ambiguous"):
                errs.append(f"{uid}/{c}: flag {cell.get('flag')!r} outside the vocabulary")
            # Codebook v8 §3.2 makes C04's facet required, on the same footing as a
            # direction, and states that a code assigned without its direction is
            # incomplete. A warning rather than a failure: it is a property of an
            # individual assignment, and failing the batch would resample 14 other
            # units' coding to chase one incomplete cell.
            if c == "C04" and v == 1 and cell.get("facet") not in ("modality", "bar", "both"):
                warns.append(f"{uid}/C04: fired without the required facet "
                             f"({cell.get('facet')!r}) — codebook §3.2")

    if got != expected:
        miss = [u for u in expected if u not in set(got)]
        extra = [u for u in got if u not in set(expected)]
        if miss:
            errs.append(f"{len(miss)} input unit(s) uncoded: {miss[:5]}"
                        f"{'…' if len(miss) > 5 else ''}")
        if extra:
            errs.append(f"{len(extra)} coded unit(s) not in the batch: {extra[:5]}")
        if not miss and not extra:
            errs.append("units returned out of input order")
    return errs


# ----------------------------------------------------------------- run log

def log_warnings(names, log_path):
    """Surface transport-level trouble the JSON itself cannot show."""
    warn = {}
    if not log_path.exists():
        return warn
    for line in log_path.read_text().splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("out") in names:
            # Later rows supersede earlier ones for the same output file, including
            # when the later row is clean: a re-run that emitted no noise must not
            # inherit the warnings of the run it replaced.
            warn.pop(row["out"], None)
            w = []
            if row.get("stop_reason") == "max_tokens":
                w.append("stopped on max_tokens — output is truncated")
            if row.get("stripped"):
                w.append(f"{row['stripped']} non-record line(s) stripped on write")
            elif row.get("fenced"):   # pre-2026-08-14 log rows
                w.append("a markdown fence was stripped on write")
            if row.get("attempt", 1) > 1:
                w.append(f"succeeded on attempt {row['attempt']}")
            if w:
                warn[row["out"]] = w
    return warn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pass_name", choices=["a1", "a2", "content", "change"])
    ap.add_argument("--runs", required=True, help="dir of model output JSONL")
    ap.add_argument("--batches", required=True, help="dir of the input batches")
    ap.add_argument("--log", default="run_log.jsonl")
    ap.add_argument("--quiet", action="store_true", help="print only failures")
    a = ap.parse_args()

    runs = sorted(Path(a.runs).glob("*.jsonl"))
    if not runs:
        sys.exit(f"no output files in {a.runs}")
    batchdir = Path(a.batches)
    warn = log_warnings({p.name for p in runs}, Path(a.log))

    failed = total_errs = total_warns = 0
    for out in runs:
        bpath = batchdir / out.name
        if not bpath.exists():
            print(f"FAIL {out.name}: no matching input batch at {bpath}")
            failed += 1
            continue

        recs, errs = load_jsonl(out)
        warns = list(warn.get(out.name, []))
        if not errs:
            batch, berr = load_jsonl(bpath)
            if berr:
                errs.append(f"input batch unreadable: {berr[0]}")
            elif a.pass_name == "a1":
                errs = check_a1(recs, batch, warns)
            elif a.pass_name == "a2":
                errs = check_a2(recs, batch)
            else:
                errs = check_b(recs, batch, a.pass_name == "change", warns)

        total_warns += len(warns)
        for w in warns:
            print(f"     ! {out.name}: {w}")
        if errs:
            failed += 1
            total_errs += len(errs)
            print(f"FAIL {out.name}  ({len(errs)} problem(s), {len(recs)} record(s))")
            for e in errs[:12]:
                print(f"       {e}")
            if len(errs) > 12:
                print(f"       … and {len(errs) - 12} more")
        elif not a.quiet:
            print(f"  ok {out.name}  {len(recs)} record(s)")

    print(f"\n{len(runs)} file(s) | {len(runs) - failed} ok | {failed} failed"
          + (f" | {total_errs} problem(s)" if total_errs else "")
          + (f" | {total_warns} warning(s)" if total_warns else ""))
    if failed:
        print("Delete each failing output and re-run that batch. Never hand-repair.")
        sys.exit(1)


if __name__ == "__main__":
    main()
