#!/usr/bin/env python3
"""
build_tables.py — derive the three output CSVs from the JSONL runs.

    python build_tables.py --labs OpenAI "Google DeepMind"

The JSONL runs are the primary record; these CSVs are a reproducible derivation
from them and can be rebuilt at any time. Nothing here computes agreement,
adjudicates a disagreement, applies a resolution rule, or collapses the coder
dimension — model and repeat stay as columns. Integrity flags are raised, never
resolved.

Output: results/units.csv, results/coded_wide.csv, results/coded_long.csv,
UTF-8 with BOM, every field quoted, newlines inside fields replaced with a space.
"""

import argparse, csv, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

CHANGE_FAMILY = ["C01", "C03", "C04", "C05", "C06", "C07"]
CONTENT_FAMILY = ["C08", "C09", "C11", "C12", "C13", "C14", "C15", "C16"]
ACTIVE_CODES = CHANGE_FAMILY + CONTENT_FAMILY

# Codebook v8 §3.2. The brief says "the nine direction-bearing codes"; that count
# predates the retirement of C02 (Threshold Tightening/Loosening, merged into C04
# on 7 August 2026) and C10 (Scope of Risks, retired 7 August 2026), both of which
# carried directions. Under v8 seven codes carry one. The codebook governs.
DIRECTION_CODES = ["C01", "C03", "C04", "C05", "C06", "C07", "C08"]
DIRECTION_VOCAB = {
    "C01": ["introduced", "expanded"],
    "C03": ["introduced", "removed", "reintroduced", "architecture_replaced"],
    "C04": ["tightened", "loosened"],
    "C05": ["added", "dropped", "reintroduced", "split", "merged"],
    "C06": ["narrowed", "broadened"],
    "C07": ["tightened", "loosened"],
    "C08": ["A-umbrella", "A-framing", "A-motivation"],   # multi-select
}
C04_FACETS = ["modality", "bar", "both"]

UNITS_COLS = ["unit_id", "lab", "identifier", "framework_version", "framework_year",
              "section_heading", "locator", "unit_type", "context_stem", "excerpt",
              "paraphrase", "modal_register", "stated_bar", "duplicate_of",
              "removal_candidate", "transition_id", "prior_unit_id",
              "prior_stated_bar", "prior_counterpart_excerpt", "prior_modal_register",
              "cosmetic_split"]

LAB_DIR = {"OpenAI": "openai", "Google DeepMind": "deepmind",
           "Anthropic": "anthropic", "xAI": "xai"}


def flat(v):
    """CSV cells carry no newlines; the excerpt must otherwise survive verbatim."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    return re.sub(r"\s*\n\s*", " ", str(v))


def writer(path, cols):
    f = open(path, "w", newline="", encoding="utf-8-sig")
    w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL,
                       extrasaction="ignore")
    w.writeheader()
    return f, w


def read_jsonl_dir(d):
    out = []
    p = Path(d)
    if not p.exists():
        return out
    for f in sorted(p.glob("*.jsonl")):
        out.extend(json.loads(l) for l in f.read_text().splitlines() if l.strip())
    return out


def read_batches(d):
    """Batch records carry the unit fields the coder saw; coded output carries only ids."""
    return {r["unit_id"]: r for r in read_jsonl_dir(d)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--labs", nargs="+", required=True)
    ap.add_argument("--corpus", default="study/corpus")
    ap.add_argument("--batches", default="study/batches")
    ap.add_argument("--coded", default="study/coded")
    ap.add_argument("--out", default="results")
    ap.add_argument("--model", default=None, help="defaults to the model in run_log.jsonl")
    ap.add_argument("--repeat", type=int, default=1)
    a = ap.parse_args()

    model = a.model
    if not model:
        rows = [json.loads(l) for l in Path("run_log.jsonl").read_text().splitlines() if l.strip()]
        model = rows[-1]["model"]

    manifest = [json.loads(l) for l in
                (Path(a.corpus) / "manifest.jsonl").read_text().splitlines() if l.strip()]
    docs = [d for d in manifest if d["lab"] in a.labs]
    Path(a.out).mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------------------- units.csv
    units, per_doc = {}, Counter()
    for d in docs:
        p = Path(a.corpus) / LAB_DIR[d["lab"]] / "units" / f"{d['identifier']}.units.jsonl"
        for l in p.read_text().splitlines():
            if not l.strip():
                continue
            u = json.loads(l)
            units[u["unit_id"]] = {**u, "lab": d["lab"], "identifier": d["identifier"]}
            per_doc[d["identifier"]] += 1

    # units.csv is one row per frozen unit. A1 leaves transition_id and the prior_*
    # fields as "NONE", so they are filled from the crosswalk — but only from the
    # ADJACENT transition. The endpoint pair means GDM-FSF-v3-1's units belong to two
    # transitions at once, which one row per unit cannot express; that context lives
    # in coded_wide.csv and coded_long.csv, keyed by transition_id.
    xwalk = {}
    for f_ in sorted(Path("study/crosswalk").glob("*.crosswalk.jsonl")):
        for l in f_.read_text().splitlines():
            if not l.strip():
                continue
            r = json.loads(l)
            key = r["prior_unit_id"] if r["removal_candidate"] else r["target_unit_id"]
            if key != "NONE":
                xwalk[key] = r

    # Cosmetic splits (analyst decision D7, 2026-08-15). A1 segments each version
    # independently — it must, since each version is segmented exactly once, ever — so
    # nothing keeps granularity consistent across versions. Where two versions share
    # near-identical text, ordinary jitter surfaces as a many-to-one alignment whose
    # target excerpts concatenate back to exactly the prior excerpt. The text did not
    # change; only the cut points did. But the target excerpt is a strict SUBSET of the
    # prior excerpt, which reads to a change coder as narrowed or deleted content, so
    # these rows can carry change codes that describe an artefact of segmentation.
    #
    # They are coded normally and flagged here rather than corrected: re-segmenting is
    # barred after Checkpoint C, and altering the coding input would have made the two
    # halves non-comparable. The test is exact — normalised concatenation equality, no
    # judgement — so the flag is reproducible from the frozen units and the crosswalks.
    #
    # This matters because the effect is not evenly spread: 4% of many-to-one on the
    # OpenAI/GDM half against 29% on the Anthropic/xAI half, concentrated in Anthropic's
    # near-identical point releases. Reporting raw change counts across labs without
    # netting these out overstates how much Anthropic revised its framework.
    def _norm(s):
        return re.sub(r"\W+", "", str(s)).lower()

    cosmetic = set()
    for f_ in sorted(Path("study/crosswalk").rglob("*.crosswalk.jsonl")):
        groups = defaultdict(list)
        for l in f_.read_text().splitlines():
            if not l.strip():
                continue
            r = json.loads(l)
            p, t = r.get("prior_unit_id"), r.get("target_unit_id")
            if p and p != "NONE" and t and t != "NONE":
                groups[(r["transition_id"], p)].append(t)
        for (tid, p), targets in groups.items():
            if len(targets) < 2 or p not in units:
                continue
            joined = _norm("".join(units[t]["excerpt"] for t in sorted(targets)
                                   if t in units))
            if joined == _norm(units[p]["excerpt"]):
                cosmetic.update((tid, t) for t in targets)

    f, w = writer(Path(a.out) / "units.csv", UNITS_COLS)
    for uid in sorted(units):
        u = dict(units[uid])
        r = xwalk.get(uid)
        if r:
            prior = units.get(r["prior_unit_id"], {})
            u.update({"transition_id": r["transition_id"],
                      "prior_unit_id": r["prior_unit_id"],
                      "removal_candidate": r["removal_candidate"],
                      "prior_stated_bar": prior.get("stated_bar", "NONE"),
                      "prior_counterpart_excerpt": prior.get("excerpt", "NONE"),
                      "prior_modal_register": prior.get("modal_register", "NONE")})
            u["cosmetic_split"] = (r["transition_id"], uid) in cosmetic
        w.writerow({c: flat(u.get(c, "NONE")) for c in UNITS_COLS})
    f.close()

    # ------------------------------------------------- coded content and change
    content_batches = read_batches(Path(a.batches) / "content")
    change_batches = {}
    for sub in ("change", "change/endpoint"):
        for r in read_jsonl_dir(Path(a.batches) / sub):
            change_batches[(r["transition_id"], r["unit_id"])] = r

    content_codes = {r["unit_id"]: r["codes"] for r in read_jsonl_dir(Path(a.coded) / "content")}

    # Change output carries only unit_id, so pair each coded file with its batch to
    # recover the transition. A unit appears once per transition it takes part in,
    # and GDM-FSF-v3-1's units take part in two (the adjacent step and the endpoint
    # pair), so transition_id is part of the key.
    change_codes = {}
    for sub in ("change", "change/endpoint"):
        cdir, bdir = Path(a.coded) / sub, Path(a.batches) / sub
        for cf in sorted(cdir.glob("*.jsonl")):
            bf = bdir / cf.name
            if not bf.exists():
                sys.exit(f"coded file {cf} has no matching batch at {bf}")
            brecs = [json.loads(l) for l in bf.read_text().splitlines() if l.strip()]
            crecs = [json.loads(l) for l in cf.read_text().splitlines() if l.strip()]
            if len(brecs) != len(crecs):
                sys.exit(f"{cf.name}: {len(crecs)} coded rows against {len(brecs)} input units")
            for b, c in zip(brecs, crecs):
                if b["unit_id"] != c["unit_id"]:
                    sys.exit(f"{cf.name}: order mismatch, {c['unit_id']} against {b['unit_id']}")
                change_codes[(b["transition_id"], b["unit_id"])] = (c["codes"], b)

    # ----------------------------------------------------------- coded_wide.csv
    wide_cols = (["unit_id", "transition_id", "model", "repeat", "removal_candidate",
                  "cosmetic_split"]
                 + ACTIVE_CODES
                 + [f"{c}_direction" for c in DIRECTION_CODES]
                 + ["C04_facet", "c07_requires_c14"])
    long_cols = ["unit_id", "transition_id", "code_id", "model", "repeat", "value",
                 "direction", "facet", "evidence", "flag", "ambiguity_reason",
                 "code_family", "cosmetic_split"]
    fw, ww = writer(Path(a.out) / "coded_wide.csv", wide_cols)
    fl, wl = writer(Path(a.out) / "coded_long.csv", long_cols)

    def cell(codes, cid):
        c = (codes or {}).get(cid) or {}
        return (c.get("value", "NA"), c.get("direction", "NA"), c.get("evidence", "NONE"),
                c.get("flag", "NONE"), c.get("ambiguity_reason", "NA"))

    n_wide = n_long = 0
    integrity = 0
    untagged = Counter()
    seen_content = set()

    # Every (unit, transition) the change pass produced, joined to its content codes.
    keys = sorted(change_codes) + [("NONE", u) for u in sorted(units)
                                   if u not in {k[1] for k in change_codes}]
    for tid, uid in keys:
        ch, brec = change_codes.get((tid, uid), (None, None))
        removal = bool((brec or {}).get("removal_candidate"))
        # Removal units were never evaluated for content: NA, not 0. Coding them 0
        # would understate content prevalence in the prior version.
        co = None if removal else content_codes.get(uid)
        if not removal and uid in content_codes:
            seen_content.add(uid)

        # D7: True where this unit is one part of a text-identical split. The change
        # codes on such a row may describe A1's cut points rather than a revision.
        cos = (tid, uid) in cosmetic
        row = {"unit_id": uid, "transition_id": tid, "model": model,
               "repeat": a.repeat, "removal_candidate": flat(removal),
               "cosmetic_split": flat(cos)}
        fired = 0
        for cid in ACTIVE_CODES:
            src = ch if cid in CHANGE_FAMILY else co
            v, d, ev, fl_, ar = cell(src, cid)
            if src is None:
                v, d, ev, fl_, ar = "NA", "NA", "NONE", "NONE", "NA"
            row[cid] = flat(v)
            if cid in DIRECTION_CODES:
                row[f"{cid}_direction"] = flat(d)
            if cid == "C04":
                row["C04_facet"] = flat((src or {}).get("C04", {}).get("facet", "NA"))
            if v == 1:
                fired += 1
            wl.writerow({"unit_id": uid, "transition_id": tid, "code_id": cid,
                         "model": model, "repeat": a.repeat, "value": flat(v),
                         "direction": flat(d),
                         "facet": flat((src or {}).get(cid, {}).get("facet", "NA")),
                         "evidence": flat(ev), "flag": flat(fl_),
                         "ambiguity_reason": flat(ar),
                         "code_family": "change" if cid in CHANGE_FAMILY else "content",
                         "cosmetic_split": flat(cos)})
            n_long += 1
        # Integrity check only. C07 governance tightening/loosening should not fire
        # where C14 governance content did not. Flagged, never resolved.
        bad = row.get("C07") == "1" and row.get("C14") == "0"
        row["c07_requires_c14"] = "true" if bad else "false"
        integrity += bad
        ww.writerow(row)
        n_wide += 1
        ident = units.get(uid, {}).get("identifier", "?")
        if fired == 0:
            untagged[ident] += 1

    fw.close(); fl.close()

    # --------------------------------------------------------------- reporting
    print(f"model {model}, repeat {a.repeat}\n")
    print(f"  units.csv       {len(units):>6} rows")
    print(f"  coded_wide.csv  {n_wide:>6} rows")
    print(f"  coded_long.csv  {n_long:>6} rows\n")
    print("units per document:")
    for k, v in sorted(per_doc.items()):
        print(f"  {k:<16}{v:>5}")
    print(f"\nc07_requires_c14 raised: {integrity}")
    print("\nuntagged rate — share of rows carrying zero codes:")
    for k in sorted(per_doc):
        tot = sum(1 for (t, u) in keys if units.get(u, {}).get("identifier") == k)
        n = untagged.get(k, 0)
        print(f"  {k:<16}{n:>5} / {tot:<5} {n/tot*100 if tot else 0:>5.1f}%")


if __name__ == "__main__":
    main()
