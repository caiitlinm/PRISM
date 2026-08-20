#!/usr/bin/env python3
"""
build_align_packs.py — assemble crosswalks from validated A2 output and emit the
Stage 6 alignment review packs.

    python build_align_packs.py --labs OpenAI "Google DeepMind"

Two outputs:
  study/crosswalk/{TRANSITION}.crosswalk.jsonl   (and endpoint/ for the endpoint pair)
  study/review/{TRANSITION}.align-review.md

The crosswalk files are what build_change() reads; the packs implement the checks
in review-protocol.md Stage 6. Nothing here judges an alignment or edits one.
"""

import argparse, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

STOP = set("""a an the and or of to in for on at by with from as is are was were be been
being that this these those it its our we will shall may can could would should must
not no if then than such other any all each per which who whom whose when where how
have has had do does did but into over under more most less least new""".split())
LAB_DIR = {"OpenAI": "openai", "Google DeepMind": "deepmind",
           "Anthropic": "anthropic", "xAI": "xai"}


def content_words(s):
    return {w for w in re.findall(r"[a-z]{3,}", str(s).lower()) if w not in STOP}


def jaccard(a, b):
    A, B = content_words(a), content_words(b)
    return len(A & B) / len(A | B) if (A | B) else 0.0


def md(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def load_units(corpus, ident, lab):
    p = Path(corpus) / LAB_DIR[lab] / "units" / f"{ident}.units.jsonl"
    return {json.loads(l)["unit_id"]: json.loads(l)
            for l in p.read_text().splitlines() if l.strip()}


def assemble(raw_dir, out_dir):
    """Concatenate a transition's A2 batches, in batch order, into one crosswalk."""
    by_tid = defaultdict(list)
    for p in sorted(Path(raw_dir).glob("*.jsonl")):
        rows = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
        if rows:
            by_tid[rows[0]["transition_id"]].extend(rows)
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    written = {}
    for tid, rows in by_tid.items():
        p = Path(out_dir) / f"{tid}.crosswalk.jsonl"
        p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        written[tid] = rows
    return written


def pack(tid, rows, prior_u, target_u, out_path):
    aligned = [r for r in rows if not r["removal_candidate"]]
    removals = [r for r in rows if r["removal_candidate"]]
    linked = [r for r in aligned if r["prior_unit_id"] != "NONE"]
    none = [r for r in aligned if r["prior_unit_id"] == "NONE"]

    L = [f"# Stage 6 alignment review — {tid}", "",
         f"Prior **{len(prior_u)}** units · target **{len(target_u)}** units · "
         f"**{len(rows)}** crosswalk rows.", "",
         "Alignment decides which units are eligible for change codes at all. "
         "A prior unit that is neither aligned nor flagged as a removal is invisible "
         "to every later step.", ""]

    def sect(n, t, blurb=""):
        L.extend([f"## Check {n} — {t}", ""] + ([blurb, ""] if blurb else []))

    def table(hdr, rws, empty="Nothing flagged."):
        if not rws:
            L.extend([empty, ""]); return
        L.append("| " + " | ".join(hdr) + " |")
        L.append("|" + "|".join(["---"] * len(hdr)) + "|")
        L.extend(rws); L.append("")

    # ---- 1 counts
    pc = Counter(r["prior_unit_id"] for r in linked)
    many_to_one = {k: v for k, v in pc.items() if v > 1}
    tc = Counter(r["target_unit_id"] for r in linked)
    one_to_many = {k: v for k, v in tc.items() if v > 1}
    sect(1, "Counts")
    L.extend(["| Measure | n | % of target rows |", "|---|---|---|",
              f"| Target rows | {len(aligned)} | 100% |",
              f"| Aligned to a prior unit | {len(linked)} | {len(linked)/max(1,len(aligned))*100:.0f}% |",
              f"| `prior_unit_id: NONE` | {len(none)} | {len(none)/max(1,len(aligned))*100:.0f}% |",
              f"| Removal candidates | {len(removals)} | — |",
              f"| Prior units serving >1 target (many-to-one) | {len(many_to_one)} | — |",
              f"| Target units with >1 prior (one-to-many) | {len(one_to_many)} | — |", ""])

    # ---- 2 groups
    sect(2, "Many-to-one groups, and targets with alternates",
         "A prior unit serving several targets means the later version split it.\n\n"
         "**One-to-many cannot occur and is not reported.** A2-align.md emits one row "
         "per target unit with a single `prior_unit_id`, so a target can never carry "
         "two priors; where more than one could be the counterpart, the alternates go "
         "in `alignment_note`. Those rows are listed below instead — they are the "
         "schema's actual representation of a merge.")
    rws = []
    for pid, n in sorted(many_to_one.items(), key=lambda x: -x[1]):
        tids = [r["target_unit_id"] for r in linked if r["prior_unit_id"] == pid]
        rws.append(f"| many-to-one | {pid} | {n} | {md(', '.join(tids[:6]))}"
                   f"{'…' if n > 6 else ''} | {md(prior_u.get(pid,{}).get('excerpt','')[:70])} |")
    for r in aligned:
        if r.get("alignment_note", "NONE") != "NONE" and r["prior_unit_id"] != "NONE":
            rws.append(f"| alternates | {r['target_unit_id']} | — | "
                       f"chose {r['prior_unit_id']}, also considered "
                       f"{md(r['alignment_note'][:44])} | "
                       f"{md(target_u.get(r['target_unit_id'],{}).get('excerpt','')[:70])} |")
    table(["kind", "unit", "n", "counterparts", "excerpt"], rws)

    # ---- 3 low vocabulary overlap
    sect(3, "Alignments sharing almost no vocabulary",
         "Either the most valuable alignments in the study — a renamed mechanism, a "
         "threshold restated in different units, an architecture replaced by a "
         "structurally different one — or the most wrong. Read every one.")
    scored = []
    for r in linked:
        p, t = prior_u.get(r["prior_unit_id"]), target_u.get(r["target_unit_id"])
        if not p or not t:
            continue
        j = jaccard(p["excerpt"], t["excerpt"])
        if j < 0.10:
            scored.append((j, r, p, t))
    scored.sort(key=lambda x: x[0])
    table(["overlap", "target", "target excerpt", "prior", "prior excerpt"],
          [f"| {j:.2f} | {r['target_unit_id']} | {md(t['excerpt'][:66])} | "
           f"{r['prior_unit_id']} | {md(p['excerpt'][:66])} |"
           for j, r, p, t in scored[:40]])
    if len(scored) > 40:
        L.extend([f"_{len(scored)-40} further alignments below 0.10 overlap not shown._", ""])

    # ---- 4 likely missed alignments
    # The strongest missed-alignment signal is the aligner contradicting itself:
    # naming a candidate counterpart in alignment_note while recording NONE.
    contra = []
    for r in none:
        if r.get("alignment_note", "NONE") != "NONE":
            t = target_u.get(r["target_unit_id"], {})
            alt = r["alignment_note"]
            p = prior_u.get(alt.split(",")[0].strip(), {})
            contra.append(f"| {r['target_unit_id']} | {md(t.get('excerpt','')[:64])} | "
                          f"{md(alt[:26])} | {md(p.get('excerpt','')[:64])} |")
    L.extend(["## Check 4a — NONE with an alternate named", "",
              "`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row "
              "asserts that nothing in the prior version addresses this object while "
              "naming something that might. **These are the most likely missed "
              "alignments in the transition.**", ""])
    table(["target", "target excerpt", "named alternate", "that unit's excerpt"], contra)

    sect(4, "`prior_unit_id: NONE` where the section exists in the prior version",
         "A target unit under a heading the prior version also has, yet aligned to "
         "nothing. Likely a missed alignment rather than genuinely new material.")
    prior_sections = {re.sub(r"\W+", " ", str(u.get("section_heading", "")).lower()).strip()
                      for u in prior_u.values()}
    prior_sections.discard("")
    miss = []
    for r in none:
        t = target_u.get(r["target_unit_id"])
        if not t:
            continue
        s = re.sub(r"\W+", " ", str(t.get("section_heading", "")).lower()).strip()
        if s and s in prior_sections:
            miss.append(f"| {r['target_unit_id']} | {md(t.get('section_heading',''))} | "
                        f"{md(t['excerpt'][:80])} |")
    table(["target", "section heading (present in prior)", "excerpt"], miss)

    # ---- orphaned prior units
    referenced = {r["prior_unit_id"] for r in rows if r["prior_unit_id"] != "NONE"}
    orphans = [u for uid, u in prior_u.items() if uid not in referenced]
    L.extend(["## Orphaned prior units", "",
              "Neither aligned to a target nor flagged as a removal, so absent from "
              "the change pass entirely. Most are ordinary rewording or dropped "
              "rationale, which Step A3 excludes by design. **Scan for anything "
              "category-, threshold-, governance- or architecture-level.**", "",
              f"**{len(orphans)} of {len(prior_u)} prior units "
              f"({len(orphans)/max(1,len(prior_u))*100:.0f}%).**", ""])
    by_sec = Counter(str(u.get("section_heading", "?")) for u in orphans)
    table(["prior section heading", "orphaned units"],
          [f"| {md(k)} | {v} |" for k, v in by_sec.most_common(20)],
          "No orphaned prior units.")

    # ---- 5 corpus-specific
    if tid == "OAI-PF-2023_v2":
        sect(5, "Scorecard to per-category thresholds",
             "**This check stands** (the p6 aggregation-rule graphic was excluded from "
             "the corpus; the p15 Scorecard is in). C03 `architecture_replaced` on this "
             "transition rests on this alignment alone.")
        sc = {uid for uid, u in prior_u.items()
              if "scorecard" in (str(u.get("section_heading", "")) + str(u.get("locator", ""))).lower()}
        rws = []
        for r in rows:
            if r["prior_unit_id"] in sc:
                t = target_u.get(r["target_unit_id"], {})
                rws.append(f"| {r['prior_unit_id']} | "
                           f"{md(prior_u[r['prior_unit_id']]['excerpt'][:60])} | "
                           f"{'REMOVAL' if r['removal_candidate'] else r['target_unit_id']} | "
                           f"{md(t.get('excerpt','')[:60])} |")
        table(["prior (scorecard)", "prior excerpt", "target", "target excerpt"], rws,
              "**No scorecard unit appears in the crosswalk at all.** C03 "
              "`architecture_replaced` has no evidence path on this transition.")
        L.extend([f"_{len(sc)} scorecard units in the prior version; "
                  f"{len({r['prior_unit_id'] for r in rows if r['prior_unit_id'] in sc})} "
                  "appear in the crosswalk. Units 0133–0145 are an explicitly "
                  "illustrative template carrying placeholder values, and should not "
                  "align; 0112–0114 carry the architecture claim._", ""])

    out_path.write_text("\n".join(L))
    return {"transition": tid, "rows": len(rows), "aligned": len(linked),
            "none": len(none), "removals": len(removals),
            "many_to_one": len(many_to_one), "one_to_many": len(one_to_many),
            "low_overlap": len(scored), "likely_missed": len(miss),
            "contradictory": len(contra),
            "orphans": len(orphans), "prior_units": len(prior_u)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--labs", nargs="+", required=True)
    ap.add_argument("--corpus", default="study/corpus")
    ap.add_argument("--raw", default="study/raw/a2")
    ap.add_argument("--crosswalk", default="study/crosswalk")
    ap.add_argument("--out", default="study/review")
    a = ap.parse_args()

    # Reuse build_batches' own chain construction rather than parsing identifiers back
    # out of transition_id: the id is lossy by design (it strips the shared prefix),
    # and re-deriving it by string surgery is exactly how the GDM-FSF-v3-0_1 bug got in.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from build_batches import chains, transition_id

    manifest = [json.loads(l) for l in
                (Path(a.corpus) / "manifest.jsonl").read_text().splitlines() if l.strip()]
    lab_of = {d["identifier"]: d["lab"] for d in manifest}
    docs = [d for d in manifest if d["lab"] in a.labs]
    adjacent, endpoint = chains(docs)
    pair_of = {transition_id(p["identifier"], t["identifier"]):
               (p["identifier"], t["identifier"]) for p, t in adjacent + endpoint}

    # The stale-output guard below has to know every transition the study can produce,
    # not just this invocation's. study/crosswalk/ accumulates across halves — the
    # OpenAI/GDM crosswalks are still there when the Anthropic/xAI half runs, and
    # build_tables globs the whole directory, so they must stay. Checking against the
    # requested labs alone turned those legitimate files into a hard exit. Validate
    # against every lab in the manifest and skip the ones this run does not own; a
    # transition belonging to no lab at all is still an error.
    all_adj, all_ep = chains(manifest)
    known = {transition_id(p["identifier"], t["identifier"])
             for p, t in all_adj + all_ep}

    built = {}
    built.update(assemble(a.raw, a.crosswalk))
    ep_raw, ep_out = Path(a.raw) / "endpoint", Path(a.crosswalk) / "endpoint"
    if ep_raw.exists():
        built.update(assemble(ep_raw, ep_out))

    Path(a.out).mkdir(parents=True, exist_ok=True)
    print(f"{'transition':<24}{'rows':>6}{'algn':>6}{'NONE':>6}{'rem':>5}"
          f"{'m→1':>5}{'lowvoc':>8}{'NONE+alt':>9}{'missed':>8}{'orphan':>8}")
    for tid, rows in sorted(built.items()):
        if tid not in pair_of:
            if tid in known:
                continue          # another half's transition; not this run's to rebuild
            sys.exit(f"crosswalk {tid} is not a transition of any lab in the manifest — "
                     "stale output? Expected one of: " + ", ".join(sorted(known)))
        prior_id, target_id = pair_of[tid]
        pu = load_units(a.corpus, prior_id, lab_of[prior_id])
        tu = load_units(a.corpus, target_id, lab_of[target_id])
        s = pack(tid, rows, pu, tu, Path(a.out) / f"{tid}.align-review.md")
        print(f"{tid:<24}{s['rows']:>6}{s['aligned']:>6}{s['none']:>6}{s['removals']:>5}"
              f"{s['many_to_one']:>5}{s['low_overlap']:>8}"
              f"{s['contradictory']:>9}{s['likely_missed']:>8}{s['orphans']:>8}")
    print(f"\n{len(built)} transition(s). Crosswalks in {a.crosswalk}/, packs in {a.out}/")


if __name__ == "__main__":
    main()
