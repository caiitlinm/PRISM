# Inventory — frontier AI safety framework corpus

Source folder: `/Users/caitlinam/Desktop/VScode/PRISM/corpus/` (unmodified; read-only)
Scanned: 2026-08-13. **Revised 2026-08-13** after checkpoint-1 answers and the
addition of Anthropic RSP 2024-10-15.
20 PDFs found, 19 in scope, 1 out of scope.
Text extraction for this stage was done to `/tmp/prism-scan/`, not to the source folder.

---

## 0. Working directory — RESOLVED

Confirmed: working directory is `/Users/caitlinam/Desktop/VScode/PRISM/study/`.

```
PRISM/
  corpus/          ← SOURCE, untouched (also holds your decisions.md and runbook)
  study/
    inventory.md
    extraction-report.md
    corpus/        ← built tree; keeps the runbook's corpus/openai/… paths intact
      manifest.jsonl
      openai/ anthropic/ deepmind/ xai/
```

Not yet created — Stage 2 has not begun.

---

## 0b. Checkpoint-1 answers as applied

| Flag | Your decision | Status |
|---|---|---|
| §0 working dir | `PRISM/study/` | Applied above |
| F1 Beta | Keep `OAI-PF-2023` — temporality over lab's own label | Applied |
| F3 June 2026 xAI | Published; duplicate `2.3` is an xAI typo; treat as standalone version | Applied — stays in chain, typo noted for Stage 4 |
| F8 Anthropic v2.0 | Added to `corpus` | Received — **but it carries no version label; see F11** |
| F9 xAI collision | Month suffixes | Applied — `XAI-RMF-2025-02`, `XAI-RMF-2025-08`; see F13 for a loose end |
| F5 GDM v1.0 date | Resolve via metr.org/fsp | Resolved → 2024-05-17 |
| F6 xAI draft date | Resolve via metr.org/fsp | Resolved → 2025-02 |
| F2 new code `FAIF` | Approved | Applied |
| F11 Anthropic 2024 label | `ANT-RSP-v2-0` — it is v2.0 per Anthropic's website | Applied; basis recorded in manifest |
| F12 scope | Four labs only; drop Frontier Compliance Framework | Applied; written into `corpus/decisions.md` §0.5 |
| F13 xAI suffixes | Suffix only where required | Applied — FAIF pair stays bare |

METR (https://metr.org/fsp) corroborates GDM FSF v1.0 as "May 2024" and the xAI draft
as "Feb 2025", both consistent with the in-document and filename evidence. Dates are
now recorded as resolved rather than `UNKNOWN`. Note METR gives month granularity for
both; the day component still comes from the sibling documents (GDM) and the filename
plus PDF creation date (xAI).

---

## 1. Document table

Version, date and framework name are read from the document body unless the
Confidence column says otherwise. Page count from `pdfinfo`. "Text layer" from
`pdftotext -layout` character yield against page count.

| # | Original filename | Lab | Framework name (as stated) | Version (as stated) | Date | Pages | Text layer | Proposed identifier | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `responsible-scaling-policy.pdf` | Anthropic | Anthropic's Responsible Scaling Policy | Version 1.0 | 2023-09-19 ("Effective September 19, 2023") | 22 | Real — 79,768 ch / 3,625 cpp | `ANT-RSP-v1-0` | Direct. Version in title, running footer and cover. |
| 1b | `Anthropic Responsible Scaling Policy 2024-10-15.pdf` | Anthropic | Responsible Scaling Policy | **NONE** — cover reads "Responsible Scaling Policy / Effective October 15, 2024" with no version number. Its own changelog calls it **"RSP-2024"** | 2024-10-15 ("Effective October 15, 2024") | 22 | Real — 71,249 ch / 3,239 cpp | `ANT-RSP-2024` ⚠️ *see F11* | Date direct. **No version label exists in this document.** Later RSPs retroactively call it "v2.0"; this one does not. |
| 2 | `Anthropicâ__s Responsible Scaling Policy (version 2.1).pdf` | Anthropic | Responsible Scaling Policy | Version 2.1 | 2025-03-31 ("Effective March 31, 2025") | 22 | Real — 74,376 ch / 3,380 cpp | `ANT-RSP-v2-1` | Direct. |
| 3 | `Anthropicâ__s Responsible Scaling Policy (version 2.2).pdf` | Anthropic | Responsible Scaling Policy | Version 2.2 | 2025-05-14 ("Effective May 14, 2025") | 23 | Real — 86,536 ch / 3,762 cpp | `ANT-RSP-v2-2` | Direct. |
| 4 | `Anthropicâ__s Responsible Scaling Policy (version 3.0).pdf` | Anthropic | Responsible Scaling Policy | Version 3.0 | 2026-02-24 ("Effective February 24, 2026") | 19 | Real — 59,643 ch / 3,139 cpp | `ANT-RSP-v3-0` | Direct; corroborated by in-document changelog. |
| 5 | `Anthropicâ__s Responsible Scaling Policy (version 3.1).pdf` | Anthropic | Responsible Scaling Policy | Version 3.1 | 2026-04-02 ("Effective April 2, 2026") | 20 | Real — 70,509 ch / 3,525 cpp | `ANT-RSP-v3-1` | Direct; corroborated by changelog. |
| 6 | `Anthropicâ__s Responsible Scaling Policy (version 3.2).pdf` | Anthropic | Responsible Scaling Policy | Version 3.2 | 2026-04-29 ("Effective April 29, 2026") | 20 | Real — 62,006 ch / 3,100 cpp | `ANT-RSP-v3-2` | Direct; corroborated by changelog. |
| 7 | `Anthropicâ__s Responsible Scaling Policy (version 3.3).pdf` | Anthropic | Responsible Scaling Policy | Version 3.3 | 2026-05-26 ("Effective May 26, 2026") | 20 | Real — 72,703 ch / 3,635 cpp | `ANT-RSP-v3-3` | Direct; corroborated by changelog. |
| 8 | `RSP v3.4 clean.pdf` | Anthropic | Responsible Scaling Policy | Version 3.4 | 2026-07-08 ("Effective July 8, 2026") | 21 | Real — 76,944 ch / 3,664 cpp | `ANT-RSP-v3-4` | Direct. Filename says "clean" — see flag F7. |
| 9 | `openai-preparedness-framework-beta.pdf` | OpenAI | Preparedness Framework (Beta) | `(Beta)` — see flag F1 | 2023-12-18 (cover page) | 27 | Real — 57,252 ch / 2,120 cpp. Vector Type 3 fonts with ToUnicode, **not** a scan, despite 27 MB and 1700×2200 pt pages | `OAI-PF-2023` *(provisional)* | Lab inferred: the body says "OpenAI's processes"; there is no masthead. Version treatment needs your decision. |
| 10 | `preparedness-framework-v2 (1).pdf` | OpenAI | Preparedness Framework | Version 2 | 2025-04-15 ("Version 2. Last updated: 15th April, 2025") | 22 | Real — 79,595 ch / 3,617 cpp | `OAI-PF-v2` | Direct. |
| 11 | `fsf-technical-report (1).pdf` | Google DeepMind | Frontier Safety Framework | Version 1.0 | 2024-05-17 — **not stated in this document**; day from FSF 2.0/3.0 "Past versions", month/year confirmed by METR ("May 2024") | 7 | Real — 25,286 ch / 3,612 cpp | `GDM-FSF-v1-0` | Version direct. Lab direct ("Google DeepMind" appears). Date external — see F5. |
| 12 | `Frontier Safety Framework 2.0.pdf` | Google DeepMind | Frontier Safety Framework | Version 2.0 | 2025-02-04 ("4th February 2025", page 1 header) | 9 | Real — 32,903 ch / 3,655 cpp | `GDM-FSF-v2-0` | Direct. |
| 13 | `frontier-safety-framework_3.pdf` | Google DeepMind | Frontier Safety Framework | Version 3.0 | 2025-09-22 ("Published: September 22, 2025") | 16 | Real — 46,119 ch / 2,882 cpp | `GDM-FSF-v3-0` | Version and date direct. **Lab inferred**: document says "Google", never "Google DeepMind". |
| 14 | `frontier-safety-framework_3-1.pdf` | Google DeepMind | Frontier Safety Framework | Version 3.1 | 2026-04-17 ("Published: April 17, 2026") | 20 | Real — 62,382 ch / 3,119 cpp | `GDM-FSF-v3-1` | Version and date direct. **Lab inferred**: same as #13. |
| 15 | `2025.02.20-RMF-Draft.pdf` | xAI | xAI Risk Management Framework (Draft) | NONE | 2025-02-20 — **not stated in this document**; month/year confirmed by METR ("Feb 2025"), day from filename and PDF creation date. See F6 | 8 | Real — 22,500 ch / 2,812 cpp, but carries a DRAFT watermark that interleaves into the text (see F10) | `XAI-RMF-2025-02` | Lab, framework, draft status direct. Date external. Month suffix per your F9 decision. |
| 16 | `2025-08-20-xai-risk-management-framework.pdf` | xAI | xAI Risk Management Framework | NONE | 2025-08-20 ("Last updated: August 20, 2025") | 9 | Real — 25,190 ch / 2,798 cpp | `XAI-RMF-2025-08` | Direct. Month suffix per your F9 decision. |
| 17 | `2025-12-31-xai-frontier-artificial-intelligence-framework.pdf` | xAI | xAI Frontier Artificial Intelligence Framework ("FAIF") | NONE | 2025-12-30 ("Last updated: December 30, 2025") | 11 | Real — 29,562 ch / 2,687 cpp | `XAI-FAIF-2025` ⚠️ *see F13* | Direct. **Note the filename says 2025-12-31; the document says December 30.** Table uses the document. New framework code — see F2. |
| 18 | `xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf` | xAI | xAI Frontier Artificial Intelligence Framework ("FAIF") | NONE | 2026-06-30 ("Effective Date: 30 June 2026") | 9 | Real — 24,581 ch / 2,731 cpp | `XAI-FAIF-2026` ⚠️ *see F13* | Body direct. Confirmed published per your F3 decision; duplicate `2.3` numbering is an xAI typo, carried through as-is. |
| — | `Codebook_Canonical_11_August_v8_final - with Quick Tests 12Aug2026.docx.pdf` | n/a | AI Safety Framework Coding Codebook, Canonical v8 | v8 (rev. 12 Aug 2026) | 2026-08-12 | 20 | Real — 68,574 ch | **excluded** | Not a framework document. This is your instrument. See flag F4. |

No two files are byte-identical (SHA-256 checked across all 19).

---

## 2. Proposed chains

Chronological by the document's own stated date. These are the comparison orders.

### Anthropic — 9 documents, 8 transitions
```
ANT-RSP-v1-0  2023-09-19
     ↓
ANT-RSP-2024  2024-10-15   ⚠ F11: document carries no version label
     ↓
ANT-RSP-v2-1  2025-03-31
     ↓
ANT-RSP-v2-2  2025-05-14
     ↓                                    ⚠ 9-month interval; nothing published between?
ANT-RSP-v3-0  2026-02-24
     ↓
ANT-RSP-v3-1  2026-04-02
     ↓
ANT-RSP-v3-2  2026-04-29
     ↓
ANT-RSP-v3-3  2026-05-26
     ↓
ANT-RSP-v3-4  2026-07-08
```
Chronological order is unambiguous: every date is stated in-document, and the
changelog in v3.0–v3.4 reproduces the full sequence, which cross-checks each one.

### OpenAI — 2 documents, 1 transition
```
OAI-PF-2023  2023-12-18   (Beta)
     ↓
OAI-PF-v2    2025-04-15   Version 2
```
This is the runbook's designated pilot transition (Part 2). Note the two identifiers
use different version conventions — that is forced by the grammar, but see F1.

### Google DeepMind — 4 documents, 3 transitions
```
GDM-FSF-v1-0  date not stated in document (2024-05-17 per siblings)   ⚠ F5
     ↓
GDM-FSF-v2-0  2025-02-04
     ↓
GDM-FSF-v3-0  2025-09-22
     ↓
GDM-FSF-v3-1  2026-04-17
```
Order is certain even with F5 unresolved: v1.0 self-describes as "our first version",
and v2.0 and v3.0 both list "Version 1.0 (17 May 2024)" under *Past versions*. Only
the exact date is in question, not the position.

### xAI — 4 documents, 3 transitions
```
XAI-RMF-2025-02  2025-02-20   Risk Management Framework (Draft)
     ↓
XAI-RMF-2025-08  2025-08-20   Risk Management Framework
     ↓                                    ← framework renamed RMF → FAIF here
XAI-FAIF-2025    2025-12-30   Frontier AI Framework
     ↓
XAI-FAIF-2026    2026-06-30   Frontier AI Framework
```
The rename at the third position is a real discontinuity, not a filing error: the
Aug 2025 RMF and the Dec 2025 FAIF share 88.5% of their vocabulary, so the Dec 2025
document is a direct lineal successor under a new name. By contrast the June 2026
document shares only 41.6% with its predecessor — a substantial rewrite. Your
runbook's C03 `architecture_replaced` direction is likely to be in play there.

**Total across all labs: 19 documents, 15 adjacent transitions**, plus 4 endpoint
runs (one per lab) if you follow runbook Part 4.

---

## 3. Flags

F1, F3, F5, F6, F8, F9 are **closed** by your checkpoint-1 answers (recorded in §0b).
F4, F7 were acknowledgements only. F2 remains open. F10 carries into Stage 4.
F11–F13 are new, raised by the v2.0 file you added and by the METR check.

### F11 — The Anthropic 2024 document carries no version label *(decision needed — NEW)*
The file you added is the right document — effective October 15, 2024, matching the
"RSP v2.0" line in the later changelogs. But **the document itself never says "2.0"**.
Its cover reads only:

> Responsible Scaling Policy
> Effective October 15, 2024

and its own changelog names it **"RSP-2024"**, not v2.0:

> `October 15, 2024`
> `RSP-2024: This update introduces a more flexible and nuanced approach…`

For contrast, the same changelog writes the previous entry as
`RSP-2023 (aka RSP v1.0): Initial version.` — so "v2.0" is a label applied
*retrospectively*, by the v3.x changelogs and by METR, not by this document.

Applying your grammar strictly: VERSION is `NONE` → fall back to publication year →
**`ANT-RSP-2024`**. That is what I have entered. It produces a chain that mixes
conventions:

```
ANT-RSP-v1-0 → ANT-RSP-2024 → ANT-RSP-v2-1 → ANT-RSP-v3-0 → …
```

The alternative is `ANT-RSP-v2-0`, which reads consistently and matches how every
downstream reference — Anthropic's own later documents, METR, and probably your
methods section — names this version.

**Recommendation: `ANT-RSP-v2-0`.** Your F1 answer said you care about temporality
rather than what the lab calls it, and the year fallback exists for documents with no
version identity at all. This document has a version identity; it is just asserted by
its successors instead of itself, and v2.1 is otherwise a point release off a base
that no identifier names. I would treat this as the grammar's collision-style case —
where you decide rather than the rule deciding — and record the basis in the manifest.
But it is a deviation from the literal rule, so I have not applied it.

### F12 — The corpus does not match your decision 0.2 *(decision needed — NEW)*
Your `decisions.md` §0.2 scopes the study to "all published updates from METER
database". METR's page lists **twelve labs**: Anthropic, OpenAI, Google DeepMind,
Meta, Microsoft, Amazon, xAI, Nvidia, Magic, NAVER, G42 and Cohere. The source folder
holds four. Documents on METR with no counterpart in the folder include:

| Lab | Document | METR date |
|---|---|---|
| Anthropic | **Frontier Compliance Framework** | Jun 2026 |
| Meta | Advanced AI Scaling Framework v2.0 | 2026-04-08 |
| Microsoft | Frontier Governance Framework | Feb 2026 |
| Amazon | Frontier Model Safety Framework | 2025-02-10 |
| Nvidia | Frontier AI Risk Assessment | 2025-02-17 |
| Magic, NAVER, G42, Cohere | entries present, not enumerated in my fetch | — |

Two distinct issues here:

1. **Scope.** If 0.2 is meant literally, the corpus is missing six-plus labs and the
   cross-lab comparison in runbook Part 6 is not yet supportable. If you have
   deliberately narrowed to the four largest, that narrowing should be written into
   `decisions.md`, because as drafted it says otherwise.
2. **The Anthropic Frontier Compliance Framework (Jun 2026) is the sharper problem.**
   It sits inside the window your RSP chain already covers, under the same lab. If it
   is a *separate* framework it needs its own chain and a new FRAMEWORK code; if it
   *supersedes or splits from* the RSP, then the RSP v3.2→v3.3→v3.4 transitions may be
   mis-specified. I cannot tell which from here.

**Recommendation: decide scope explicitly before Stage 2**, because identifiers and
directory layout both key on it. Adding labs later is cheap — new directories, no
change to existing identifiers. Discovering that the Anthropic chain is wrong after
coding is not. Nvidia, Magic, NAVER, G42 and Cohere would each need a new LAB code if
you include them; I have not invented any.

I can proceed with the four labs present and treat this as documented-incomplete —
just confirm that is the intent.

### F13 — xAI suffix consistency *(minor; confirm)*
Your month-suffix decision resolves the RMF pair. The two FAIF documents do not
collide, so under the grammar they stay bare: `XAI-FAIF-2025`, `XAI-FAIF-2026`. The
xAI chain therefore mixes suffixed and unsuffixed identifiers:

```
XAI-RMF-2025-02 → XAI-RMF-2025-08 → XAI-FAIF-2025 → XAI-FAIF-2026
```

**Recommendation: leave it as above** — apply the disambiguator only where the
grammar requires it, so an identifier's shape stays meaningful. Say so if you would
rather have `XAI-FAIF-2025-12` / `XAI-FAIF-2026-06` for uniformity within the lab.

Separately, for the record: METR labels these xAI documents "Risk Management Framework
v1.0", "Frontier Artificial Intelligence Framework v2.0". **None of those version
numbers appear in the documents themselves.** I have not adopted them, per your rule
to read identity off the document. Flagging because your decision 0.2 points at METR,
so the discrepancy is worth knowing about — but adopting METR's labels here would also
create a `v1.0`/`v2.0` sequence with no `v1`→`v2` document between them.

---

## 3b. Original flags, for reference

### F1 — OpenAI Beta: is "(Beta)" a version label? *(decision needed)*
The document's own label is "(Beta)", never a number. Two readings:
- **"(Beta)" is a version label** → normalise to `OAI-PF-beta`.
- **"(Beta)" is a release-stage marker, not a version label** → VERSION is `NONE`,
  fall through to publication year → `OAI-PF-2023`.

**Recommendation: `OAI-PF-2023`.** Two reasons. It reads as a maturity marker in the
same slot where v2 later puts "Version 2", and your runbook §1.1 already writes this
document as `OAI-PF-2023.pdf` in its worked example — so choosing it keeps the runbook
literal. I have used it provisionally in the table; say the word and it becomes
`OAI-PF-beta`.

### F2 — New framework code `FAIF` required *(notification, per your rule)*
xAI's Dec 2025 and June 2026 documents are titled *Frontier Artificial Intelligence
Framework*, abbreviated FAIF in their own text. This is not PF, RSP, FSF or RMF. Per
your instruction to tell you about additions, I propose **`FAIF`**.

The alternative is to fold them under `RMF` on continuity grounds, treating the rename
as cosmetic. I recommend against that: the documents self-identify as FAIF throughout
and the June 2026 one is a near-total rewrite, so collapsing the names would hide a
real transition behind an identifier that says nothing changed. No new LAB codes are
needed — all six labs present map to your existing list.

### F3 — The June 2026 xAI document may not be a published artefact *(decision needed)*
`xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf` has the PDF
metadata title **"Privileged/Confidential DRAFT working FRAMEWORK DOC"**. The body
carries no draft marker and states "Effective Date: 30 June 2026", so on its face it
is a final document. Against that:
- the metadata says otherwise;
- the section numbering is broken — `2.3` appears twice, once as "Systemic risk
  acceptance determination" and again as "Safety mitigations", with no `2.5`;
- the filename's `99c40684` hash suffix is consistent with a direct-from-storage
  download rather than a published URL.

Most likely the metadata is a stale Google Docs working title left on an otherwise
final export. But I can't establish that from the document, and your 0.2 decision
scopes the corpus to "all published updates from METER database" — so the test is
whether this document appears there. **Recommendation: verify against METER before
including it.** I have left it in the chain pending your check. If it is not a
published version, dropping it takes xAI to 3 documents and 2 transitions.

### F4 — The codebook PDF is in the source folder *(acknowledgement)*
`Codebook_Canonical_11_August_v8_final…pdf` is your coding instrument, not a corpus
document, and your `decisions.md` §0.1 names it as the frozen codebook. **Excluded
from the corpus.** Flagging only so you know it was seen and deliberately skipped —
per runbook §1.1 it belongs beside `decisions.md`, not under a lab.

### F5 — GDM FSF v1.0 carries no date *(inference; confirm)*
The document states no publication date anywhere. FSF 2.0 and FSF 3.0 both list
"Version 1.0 (17 May 2024)" under *Past versions*. So **2024-05-17** is well
evidenced, but from sibling documents rather than the document itself. Per your rule
this would be `UNKNOWN`; I have recorded it as inferred-with-source rather than
`UNKNOWN` because it does not affect the identifier (`GDM-FSF-v1-0` comes from the
version label) or the chain position. Confirm and it goes into `manifest.jsonl` as
`2024-05-17`; otherwise it goes in as `UNKNOWN`.

### F6 — xAI RMF Draft carries no date *(inference; confirm)*
No date in the body. Filename says `2025.02.20`; PDF creation date is
2025-02-20 23:37 EST. The document says it expects "an updated version of this policy
within three months", and the next RMF is dated 2025-08-20 — six months later, which
neither confirms nor contradicts. Evidence here is weaker than F5: filename and file
metadata are both external to the document. **Recommendation: record the date as
`UNKNOWN` in the manifest with `2025-02-20` in a separate `date_inferred` field**, so
the provenance record does not assert something the document does not say. Note this
date also drives the identifier, via the year fallback — but 2025 holds under any
plausible reading.

### F7 — `RSP v3.4 clean.pdf` filename says "clean" *(acknowledgement)*
The document itself is unambiguous: Version 3.4, effective July 8, 2026, and its
changelog runs consistently from v1.0. "clean" almost certainly means a clean copy
with tracked changes accepted. No action needed, but the filename is the only one in
the set suggesting a pre-publication state, so it is recorded here.

### F8 — Missing Anthropic RSP v2.0 *(gap)*
The changelogs in v3.0 through v3.4 all list **"October 15, 2024 (RSP v2.0)"**, and
v2.1's own executive summary refers back to an update that is v2.0. The document is
not in the source folder. This breaks the chain at its largest structural change:
v1.0→v2.1 spans the ASL restructure, and coding it as a single transition attributes
two documents' worth of change to one. **Recommendation: obtain v2.0 before coding
Anthropic.** If it cannot be obtained, the v1.0→v2.1 transition should be reported as
spanning a missing version rather than silently chained.

There is also a 9-month interval between v2.2 (2025-05-14) and v3.0 (2026-02-24) with
nothing between. The changelogs list no intervening version, so this is most likely a
genuine publication gap rather than a second hole — but it is the one interval I
cannot positively rule out, so worth a glance at METER while you are checking F3.

### F9 — Identifier collision: the two xAI RMF documents *(decision needed)*
`2025.02.20-RMF-Draft.pdf` and `2025-08-20-xai-risk-management-framework.pdf` both
carry no version label and both fall in 2025, so both resolve to `XAI-RMF-2025`. Per
your instruction I have **not invented a disambiguator**. These are genuinely
different documents — 30.2% vocabulary overlap, and the February one self-describes as
a draft throughout.

Options, in the order I would consider them:
1. `XAI-RMF-2025-draft` / `XAI-RMF-2025` — marks the status the document asserts.
2. `XAI-RMF-2025-02` / `XAI-RMF-2025-08` — month suffix; extends the grammar least.
3. Exclude the draft, if your 0.2 rule ("published updates") does not cover a draft.

I lean to (2) if both stay in: it is mechanical, and it will generalise if any other
lab ever publishes twice in a year without version labels. But (3) may be the right
call on your own scoping rule — a document that calls itself a draft eight times is
arguably not a published update. **This one is yours; the whole xAI chain keys on it.**

### F10 — Watermark contamination in the xAI RMF Draft *(extraction, previewed)*
`2025.02.20-RMF-Draft.pdf` has a DRAFT watermark whose letters extract as stray
characters interleaved into the body text — a bare `T` and `AF` appear mid-paragraph
on page 1. This is a Stage 4 matter and I will detail it there; noting it now because
it is visible already and may bear on the F9 decision.

### Near-duplicates
No exact duplicates (SHA-256). The highest similarity pairs are consecutive Anthropic
RSP versions — v3.3↔v3.4 at 96.5%, v3.1↔v3.2 at 95.8% — which is expected for point
releases and is exactly the "near-empty transition is itself a result" case your
runbook §0.2 anticipates. **No pair looks like the same document downloaded twice.**

---

## 4. Summary

| Lab | Documents | Transitions | Open flags |
|---|---|---|---|
| Anthropic | 9 | 8 | — |
| Google DeepMind | 4 | 3 | — |
| OpenAI | 2 | 1 | — |
| xAI | 4 | 3 | F10 (watermark → Stage 4) |
| **Total** | **19** | **15** | |

Excluded: 1 codebook; Anthropic Frontier Compliance Framework (per decision 0.5);
eight METR labs outside the four-lab scope. `META`, `MSFT`, `AMZN` go unused.

**All identity flags closed.** Checkpoint 1 satisfied; Stages 2–4 may proceed. The
only item carrying forward is F10, the DRAFT watermark in `XAI-RMF-2025-02`, which is
an extraction matter and belongs in `extraction-report.md`.

### Final identifiers

| Identifier | Original filename |
|---|---|
| `ANT-RSP-v1-0` | `responsible-scaling-policy.pdf` |
| `ANT-RSP-v2-0` | `Anthropic Responsible Scaling Policy 2024-10-15.pdf` |
| `ANT-RSP-v2-1` | `Anthropicâ__s Responsible Scaling Policy (version 2.1).pdf` |
| `ANT-RSP-v2-2` | `Anthropicâ__s Responsible Scaling Policy (version 2.2).pdf` |
| `ANT-RSP-v3-0` | `Anthropicâ__s Responsible Scaling Policy (version 3.0).pdf` |
| `ANT-RSP-v3-1` | `Anthropicâ__s Responsible Scaling Policy (version 3.1).pdf` |
| `ANT-RSP-v3-2` | `Anthropicâ__s Responsible Scaling Policy (version 3.2).pdf` |
| `ANT-RSP-v3-3` | `Anthropicâ__s Responsible Scaling Policy (version 3.3).pdf` |
| `ANT-RSP-v3-4` | `RSP v3.4 clean.pdf` |
| `OAI-PF-2023` | `openai-preparedness-framework-beta.pdf` |
| `OAI-PF-v2` | `preparedness-framework-v2 (1).pdf` |
| `GDM-FSF-v1-0` | `fsf-technical-report (1).pdf` |
| `GDM-FSF-v2-0` | `Frontier Safety Framework 2.0.pdf` |
| `GDM-FSF-v3-0` | `frontier-safety-framework_3.pdf` |
| `GDM-FSF-v3-1` | `frontier-safety-framework_3-1.pdf` |
| `XAI-RMF-2025-02` | `2025.02.20-RMF-Draft.pdf` |
| `XAI-RMF-2025-08` | `2025-08-20-xai-risk-management-framework.pdf` |
| `XAI-FAIF-2025` | `2025-12-31-xai-frontier-artificial-intelligence-framework.pdf` |
| `XAI-FAIF-2026` | `xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf` |

Codes added beyond your original lists: **`FAIF`** (framework) only. No new LAB codes.
