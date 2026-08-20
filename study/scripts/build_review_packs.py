#!/usr/bin/env python3
"""
build_review_packs.py — Stage 4 unit review packs, one per document.

    python build_review_packs.py --labs OpenAI "Google DeepMind"

Writes study/review/{IDENTIFIER}.units-review.md, implementing the checks in
study/review-protocol.md. This is the only validity check in the pipeline: freezing
units converts random error into systematic error, so badly-cut units yield
excellent reliability on the wrong thing.

Nothing here judges. Every check surfaces units for a human to read and returns
counts; none of them pass or fail a document, and none modify the frozen files.
"""

import argparse, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

LAB_DIR = {"OpenAI": "openai", "Google DeepMind": "deepmind",
           "Anthropic": "anthropic", "xAI": "xai"}

# Check 2: leading verbs that signal a unit whose subject lives in the parent stem.
LEAD_VERBS = {
    "ensure", "establish", "maintain", "provide", "conduct", "develop", "implement",
    "review", "monitor", "assess", "evaluate", "define", "apply", "publish", "report",
    "update", "deploy", "restrict", "require", "document", "track", "test", "measure",
    "mitigate", "verify", "notify", "escalate", "halt", "pause", "adopt", "follow",
    "create", "design", "perform", "determine", "identify", "consider", "include",
    "share", "disclose", "engage", "invest", "support", "protect", "secure", "limit",
    "prevent", "reduce", "continue", "work", "build", "run", "set", "keep", "use",
}
# Check 3 triggers on "a digit, percentage or multiplier", per review-protocol.md.
# Tier names are deliberately excluded even though stated_bar itself accepts them:
# "high", "low" and "critical" occur throughout ordinary prose in these documents
# ("high-impact capabilities"), and including them flagged 82 of GDM-FSF-v3-1's 281
# units against 11 on the protocol's own trigger. A review list nobody can read is
# not a check.
BAR_PAT = re.compile(r"\d|%|×", re.I)
# Check 4: rationale and motivational framing the codebook exists to capture.
FRAMING = ("we believe", "we revised", "we have revised", "in response to",
           "it is critical", "we recognise", "we recognize", "we expect",
           "our goal", "we aim", "this reflects", "we updated", "we have updated")
MARKER = re.compile(r"<<|>>")
TABLE_LOC = re.compile(r"\btable\b", re.I)


def load_units(corpus, d):
    p = Path(corpus) / LAB_DIR[d["lab"]] / "units" / f"{d['identifier']}.units.jsonl"
    if not p.exists():
        sys.exit(f"missing frozen units: {p}\nRun freeze_units.py first.")
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def words(s):
    return len(str(s).split())


def table_of(u):
    """
    The table a unit belongs to.

    Falls back to unit_type when no numbered label exists. GDM-FSF-v1-0 introduces
    all three of its tables as "the table below" and never numbers them, so keying
    on a "Table N" label alone reported zero tables for a document with three —
    silently emptying the one check that stands between a mangled layout table and
    plausible-looking frozen units.
    """
    for f in (u.get("locator", ""), u.get("section_heading", "")):
        m = re.search(r"(Table\s+[\w.\-]+)", str(f), re.I)
        if m:
            return m.group(1)
    if u.get("unit_type") == "table_cell":
        return f"(unnumbered) {u.get('section_heading') or u.get('locator') or '?'}"
    return None


def row(u, *extra):
    cells = [u["unit_id"], u.get("locator", ""), " ".join(str(u["excerpt"]).split())[:120]]
    return "| " + " | ".join(list(map(md, cells)) + [md(e) for e in extra]) + " |"


def md(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def pack(d, units, seams, out_path):
    ident = d["identifier"]
    L = [f"# Stage 4 unit review — {ident}", "",
         f"{d['lab']} · {d['framework']} · {d.get('version','NONE')} · {d['date']} · "
         f"{d['pages']} pages", "",
         f"**{len(units)} units.** Frozen at `study/corpus/{LAB_DIR[d['lab']]}/units/"
         f"{ident}.units.jsonl`.", "",
         "Units freeze at Checkpoint C and cannot be corrected afterwards. Every "
         "section below lists units to read, not verdicts.", ""]

    def sect(n, title, blurb=""):
        L.extend([f"## Check {n} — {title}", ""] + ([blurb, ""] if blurb else []))

    def table(hdr, rows, empty="Nothing flagged."):
        if not rows:
            L.extend([empty, ""]); return
        L.append("| " + " | ".join(hdr) + " |")
        L.append("|" + "|".join(["---"] * len(hdr)) + "|")
        L.extend(rows); L.append("")

    # ---- 1. table coverage
    by_table = defaultdict(list)
    for u in units:
        t = table_of(u)
        if t:
            by_table[t].append(u)
    sect(1, "Table coverage",
         "Units per table. **Count these against the cell count in the PDF.** A "
         "shortfall is the most common failure and the hardest to see, because the "
         "unit list looks complete on its own.")
    table(["Table", "Units", "Distinct row/col locators", "First unit"],
          [f"| {md(t)} | {len(us)} | {len({u.get('locator','') for u in us})} | "
           f"{us[0]['unit_id']} |" for t, us in sorted(by_table.items())],
          "No units carry a table locator.")

    # ---- 2. context_stem audit
    flagged = []
    for u in units:
        if u.get("context_stem") != "NONE":
            continue
        exc = str(u["excerpt"]).strip()
        first = re.sub(r"[^a-z]", "", exc.split()[0].lower()) if exc.split() else ""
        why = []
        if words(exc) < 15:
            why.append(f"{words(exc)} words")
        if first in LEAD_VERBS:
            why.append(f"opens on '{first}'")
        if why:
            flagged.append(row(u, "; ".join(why)))
    sect(2, "`context_stem` = NONE on units that look dependent",
         "Downstream coders see only the unit record. A short unit, or one opening "
         "on a bare verb, usually depends on a parent stem that must be carried here.")
    table(["unit_id", "locator", "excerpt", "why"], flagged)

    # ---- 3. stated_bar audit
    missed = [row(u, md(u.get("stated_bar", "")))
              for u in units
              if BAR_PAT.search(str(u["excerpt"])) and u.get("stated_bar") == "NONE"]
    caught = [u for u in units if u.get("stated_bar") != "NONE"]
    sect(3, "`stated_bar` audit",
         f"{len(caught)} units carry a bar. Listed below are units whose excerpt "
         "contains a number, percentage, multiplier or tier name but returned NONE.")
    table(["unit_id", "locator", "excerpt", "stated_bar"], missed,
          "Every unit containing a quantity or tier name extracted a bar.")

    # ---- 4. rationale and framing retention
    # The protocol says "units beginning" with these phrases, but its stated purpose
    # is detecting whether rationale survived segmentation at all, and in practice
    # the framing sits mid-sentence: matching only sentence-initial returned zero
    # for GDM-FSF-v3-0 and v3-1, both of which carry it in 11 units. Matching
    # anywhere is a superset of the protocol and serves the purpose; the position
    # column preserves the literal reading.
    keep = []
    for u in units:
        e = " ".join(str(u["excerpt"]).split()).lower()
        if any(p in e for p in FRAMING):
            keep.append(row(u, "initial" if e.startswith(FRAMING) else "mid-unit"))
    sect(4, "Rationale and framing retention",
         "The codebook codes explanatory and motivational language, so these must "
         "survive segmentation. Their **absence** is the finding: if this table is "
         "empty and the document argues for its own choices, the segmenter dropped "
         "them as preamble.")
    table(["unit_id", "locator", "excerpt", "position"], keep,
          "**No rationale or framing units found.** Confirm against the PDF that the "
          "document genuinely contains none.")

    # ---- 5. suspicious units
    susp = [row(u, words(u["excerpt"]))
            for u in units if words(u["excerpt"]) < 5 or words(u["excerpt"]) > 75]
    sect(5, "Suspicious units", "Under five words, or over 75.")
    table(["unit_id", "locator", "excerpt", "words"], susp)

    # ---- 6. hand-transcribed tables
    ht = d.get("hand_transcribed", [])
    leaked = [row(u) for u in units
              if any(MARKER.search(str(u.get(f, "")))
                     for f in ("excerpt", "context_stem", "paraphrase", "section_heading"))]
    sect(6, "Hand-transcribed tables",
         f"Transcribed pages in this document: {', '.join(ht) if ht else 'none'}.")
    if ht:
        rows = [f"| {md(t)} | {len(us)} | {us[0]['unit_id']} |"
                for t, us in sorted(by_table.items())]
        table(["Table", "Units", "First unit"], rows)
    L.extend(["Marker syntax leaking into a unit field:", ""])
    table(["unit_id", "locator", "excerpt"], leaked,
          "No `<<…>>` marker syntax in any unit field.")

    # ---- 7. chunk seams
    sect(7, "Chunk seams",
         "A model resuming mid-document sometimes re-emits the last unit of the "
         "prior chunk. Read the units either side of each seam.")
    if seams:
        table(["Between", "First unit after seam", "Section", "Re-emitted"],
              [f"| {md(s['between'][0])} → {md(s['between'][1])} | "
               f"{s['first_unit_of_next']} | {md(s.get('first_section',''))} | "
               f"{md(s['repeated_from_prior_chunk'] or 'none detected')} |"
               for s in seams])
    else:
        L.extend(["Single chunk; no seam.", ""])

    # ---- 8. corpus-specific
    if ident == "OAI-PF-v2":
        t1 = [u for u in units if (table_of(u) or "").lower().startswith("table 1")]
        sect(8, "OAI-PF-v2 Table 1 `context_stem`",
             "Table 1 has its row labels offset onto each row's second line in the "
             "extraction. It is the most code-dense table in the corpus, and a stem "
             "failure here is invisible until it surfaces as unexplained zeros on "
             "C09 and C13. **Check every row.**")
        table(["unit_id", "locator", "excerpt", "context_stem"],
              [row(u, md(u.get("context_stem", ""))) for u in t1],
              "No units carry a Table 1 locator — itself a finding.")

    # ---- untagged tables
    L.extend(["## Untagged tables", "",
              "Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. "
              "Every other table in the corpus reaches A1 as pdftotext column layout "
              "with no `<<TABLE>>` markers, so Check 1 is the only thing standing "
              "between a mangled multi-column table and units that look plausible "
              "one at a time.", "",
              f"Tables detected here: **{len(by_table)}**. "
              f"Transcribed pages: {', '.join(ht) if ht else '**none — all layout-derived**'}.",
              ""])

    # ---- summary
    L.extend(["## Counts", "",
              "| Measure | Value |", "|---|---|",
              f"| Units | {len(units)} |",
              f"| Tables detected | {len(by_table)} |",
              f"| Units in tables | {sum(len(v) for v in by_table.values())} |",
              f"| `context_stem` = NONE | {sum(1 for u in units if u.get('context_stem')=='NONE')} |",
              f"| `stated_bar` populated | {len(caught)} |",
              f"| `duplicate_of` populated | {sum(1 for u in units if u.get('duplicate_of')!='NONE')} |",
              f"| Median excerpt words | {sorted(words(u['excerpt']) for u in units)[len(units)//2]} |",
              ""])
    unit_types = Counter(u.get("unit_type") for u in units)
    L.extend(["| unit_type | n |", "|---|---|"]
             + [f"| {k} | {v} |" for k, v in unit_types.most_common()] + [""])

    out_path.write_text("\n".join(L))
    return {"identifier": ident, "units": len(units), "tables": len(by_table),
            "stem_flagged": len(flagged), "bar_missed": len(missed),
            "framing": len(keep), "suspicious": len(susp), "leaked": len(leaked)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--labs", nargs="+", required=True)
    ap.add_argument("--corpus", default="study/corpus")
    ap.add_argument("--freeze-report", default="study/review/freeze-report.json")
    ap.add_argument("--out", default="study/review")
    a = ap.parse_args()

    manifest = [json.loads(l) for l in
                (Path(a.corpus) / "manifest.jsonl").read_text().splitlines() if l.strip()]
    docs = [d for d in manifest if d["lab"] in a.labs]
    seams_by_doc = {r["identifier"]: r["seams"]
                    for r in json.load(open(a.freeze_report))}

    Path(a.out).mkdir(parents=True, exist_ok=True)
    print(f"{'document':<16}{'units':>6}{'tables':>8}{'stem?':>7}{'bar?':>6}"
          f"{'framing':>9}{'susp':>6}{'leaked':>8}")
    for d in docs:
        units = load_units(a.corpus, d)
        out = Path(a.out) / f"{d['identifier']}.units-review.md"
        s = pack(d, units, seams_by_doc.get(d["identifier"], []), out)
        print(f"{s['identifier']:<16}{s['units']:>6}{s['tables']:>8}"
              f"{s['stem_flagged']:>7}{s['bar_missed']:>6}{s['framing']:>9}"
              f"{s['suspicious']:>6}{s['leaked']:>8}")
    print(f"\n{len(docs)} pack(s) written to {a.out}/")


if __name__ == "__main__":
    main()
