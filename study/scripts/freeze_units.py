#!/usr/bin/env python3
"""
freeze_units.py — merge validated A1 chunk output into one frozen unit file per
document, renumbering sequentially across chunks.

    python freeze_units.py --runs study/raw/a1 --labs OpenAI "Google DeepMind"

Writes study/corpus/{lab}/units/{IDENTIFIER}.units.jsonl. Refuses to overwrite an
existing unit file without --force, because these files are frozen at Checkpoint C
and every version is segmented exactly once, ever.

Why renumbering is needed. build_batches stamps each chunk with a first_unit_number
estimated from words, so chunk N+1's numbering assumes a unit count for chunk N that
the model has not produced yet. In the 2026-08-14 run GDM-FSF-v3-0 chunk 01 ended at
-0122 and chunk 02 began at -0129: a gap of six. Renumbering closes the gaps and
makes the sequence a true document-order index.

What is deliberately NOT done here: nothing is dropped, merged, split, re-excerpted
or edited. Only unit_id is rewritten, and duplicate_of is remapped to follow it.
Seam duplicates are reported for the Stage 4 review pack, never removed — that is a
judgment for the analyst, not this script.
"""

import argparse, json, re, sys
from collections import defaultdict
from pathlib import Path

LAB_DIR = {"OpenAI": "openai", "Google DeepMind": "deepmind",
           "Anthropic": "anthropic", "xAI": "xai"}
SPLIT_ID = re.compile(r"^(?P<base>.+)-(?P<num>\d{4})(?:-(?P<suffix>[a-z]))?$")


def parse_id(uid):
    m = SPLIT_ID.match(uid)
    if not m:
        sys.exit(f"unparseable unit_id: {uid!r}")
    return m.group("base"), int(m.group("num")), m.group("suffix")


def chunk_key(p):
    """GDM-FSF-v3-0.02.jsonl -> ('GDM-FSF-v3-0', 2)."""
    stem = p.name[: -len(".jsonl")]
    ident, _, n = stem.rpartition(".")
    return ident, int(n)


def norm(s):
    return " ".join(str(s).split()).lower()


def freeze(ident, paths, out_path, force):
    if out_path.exists() and not force:
        print(f"  skip {ident}: {out_path} exists (pass --force to replace)")
        return None

    chunks = []
    for p in paths:
        recs = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
        if not recs:
            sys.exit(f"{p} is empty — validate before freezing")
        chunks.append((p, recs))

    # Seam check deferred until after renumbering, so it can report the ids that
    # actually appear in the frozen file.

    # Renumber. The parts of a split unit (-a, -b, …) share one new number, so the
    # sequence counts units of analysis rather than records.
    #
    # Old unit_ids are only meaningful within their own chunk. build_batches stamps
    # each chunk with a first_unit_number estimated from word counts, and the model
    # numbers from there, so when a chunk emits more units than estimated the next
    # chunk's range overlaps it. GDM-FSF-v3-1 did exactly this on 2026-08-14: chunk
    # 01 ran to -0124 while chunk 02 began at -0118, seven ids of overlap carrying
    # completely different text. The overlap is an artefact of the estimate and says
    # nothing about the units, so the map is keyed per chunk and collisions are only
    # an error inside a single chunk.
    out, per_chunk_map = [], []
    n, prev_group = 0, None
    for ci, (path, recs) in enumerate(chunks):
        cmap = {}
        for r in recs:
            base, num, suffix = parse_id(r["unit_id"])
            if base != ident:
                sys.exit(f"{ident}: unit {r['unit_id']!r} carries identifier {base!r}")
            if r["unit_id"] in cmap:
                sys.exit(f"{ident}: {path.name} repeats unit_id {r['unit_id']!r}")
            if not (suffix and prev_group == num):
                n += 1
            prev_group = num
            new = f"{ident}-{n:04d}" + (f"-{suffix}" if suffix else "")
            cmap[r["unit_id"]] = new
            out.append({**r, "unit_id": new, "_chunk": ci})
        per_chunk_map.append(cmap)

    # duplicate_of points at a unit_id in the same chunk's numbering.
    dangling = []
    for r in out:
        d = r.get("duplicate_of", "NONE")
        if d != "NONE":
            resolved = per_chunk_map[r["_chunk"]].get(d)
            if resolved:
                r["duplicate_of"] = resolved
            else:
                dangling.append((r["unit_id"], d))
                r["duplicate_of"] = "NONE"
    # Seam check, on renumbered ids: does the head of chunk N+1 re-emit the tail of
    # chunk N? A bare excerpt match is not enough — table boilerplate recurs
    # legitimately. GDM-FSF-v3-0 has a cell reading exactly "Security level 2" in
    # both Table 2.2.2.a and Table 2.2.3.a, on either side of a perfectly clean
    # seam. A genuine re-emission repeats the locator too, so require that, or an
    # excerpt long enough that recurrence would not be coincidence.
    seams = []
    for ci in range(len(chunks) - 1):
        a = [r for r in out if r["_chunk"] == ci][-3:]
        b = [r for r in out if r["_chunk"] == ci + 1][:3]
        tail = {(norm(r["excerpt"]), norm(r.get("locator", ""))) for r in a}
        tail_text = {norm(r["excerpt"]) for r in a}
        dupes = [r["unit_id"] for r in b
                 if (norm(r["excerpt"]), norm(r.get("locator", ""))) in tail
                 or (norm(r["excerpt"]) in tail_text
                     and len(str(r["excerpt"]).split()) >= 12)]
        seams.append({"between": [chunks[ci][0].name, chunks[ci + 1][0].name],
                      "first_unit_of_next": b[0]["unit_id"],
                      "first_section": b[0].get("section_heading", ""),
                      "first_excerpt": b[0]["excerpt"][:90],
                      "repeated_from_prior_chunk": dupes})

    for r in out:
        del r["_chunk"]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in out))
    return {"identifier": ident, "chunks": len(chunks), "units": len(out),
            "first": out[0]["unit_id"], "last": out[-1]["unit_id"],
            "seams": seams, "dangling_duplicate_of": dangling}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="study/raw/a1")
    ap.add_argument("--corpus", default="study/corpus")
    ap.add_argument("--labs", nargs="+", required=True)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--report", default="study/review/freeze-report.json")
    a = ap.parse_args()

    manifest = [json.loads(l) for l in
                (Path(a.corpus) / "manifest.jsonl").read_text().splitlines() if l.strip()]
    wanted = {d["identifier"]: d for d in manifest if d["lab"] in a.labs}

    by_doc = defaultdict(list)
    for p in sorted(Path(a.runs).glob("*.jsonl")):
        ident, n = chunk_key(p)
        by_doc[ident].append((n, p))

    reports = []
    for ident in sorted(by_doc):
        if ident not in wanted:
            continue
        paths = [p for _, p in sorted(by_doc[ident])]
        out = (Path(a.corpus) / LAB_DIR[wanted[ident]["lab"]] / "units"
               / f"{ident}.units.jsonl")
        rep = freeze(ident, paths, out, a.force)
        if rep is None:
            continue
        reports.append(rep)
        print(f"  {ident:<16}{rep['chunks']} chunk(s)  {rep['units']:>4} units  "
              f"{rep['first']} -> {rep['last']}")
        for s in rep["seams"]:
            if s["repeated_from_prior_chunk"]:
                print(f"       SEAM REPEAT {s['between'][0]} -> {s['between'][1]}: "
                      f"{s['repeated_from_prior_chunk']}")
        if rep["dangling_duplicate_of"]:
            print(f"       {len(rep['dangling_duplicate_of'])} duplicate_of reference(s) "
                  "pointed outside the document and were set to NONE")

    if reports:
        Path(a.report).parent.mkdir(parents=True, exist_ok=True)
        Path(a.report).write_text(json.dumps(reports, indent=2, ensure_ascii=False) + "\n")
        total = sum(r["units"] for r in reports)
        print(f"\n{len(reports)} document(s), {total} units frozen. Report: {a.report}")


if __name__ == "__main__":
    main()
