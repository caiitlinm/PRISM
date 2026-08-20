# Extraction quality report

19 documents, 327 pages, all extracted with `pdftotext -layout`. Poppler 26.07.0.
No document was flagged as scanned at Stage 1, so all 19 were extracted; none were
OCR'd. Source PDFs verified byte-identical to originals by SHA-256 after copying.

**Method.** Per-page character counts come from `pdftotext -layout -f N -l N`. Table
regions were located two ways: by caption (`Table N:`) where documents use captions,
and by a layout detector that flags contiguous line runs carrying multi-space column
gaps, for the majority of documents that caption nothing. Every block the detector
found is listed in §2. I opened and read the regions quoted below; where I am
reporting on a block I did not read line by line, §2 says so.

---

## 0. Headline

Three things need hand work before coding, and one of them is not visible from the
text file alone:

1. **`XAI-RMF-2025-02` — both tables are genuinely scrambled by a DRAFT watermark.**
   Cell values are detached from their rows. This is the only document in the corpus
   with true cell-level corruption. Pages 3–5.
2. **`OAI-PF-2023` p15 — the Illustrative Scorecard is broken**, header row split and
   the word "Illustrative" rendered as a background watermark whose letters land
   inside the table body. This matters more than its size suggests: runbook §2.4
   names the 2023 Scorecard as the alignment counterpart for the 2025 per-category
   thresholds, so a mis-transcribed Scorecard propagates into C03.
3. **`OAI-PF-2023` p6 carries a 3102×3435 raster image contributing nothing to the
   text layer.** Whatever it depicts is absent from the extraction and I cannot tell
   what it is without looking at it.

Everything else extracted with column structure intact. There is a fourth,
cross-cutting issue — invisible Unicode control characters in five files, §6 — that
will not affect reading but will break verbatim evidence matching in your validator.

---

## 1. Character-count sanity check

Median characters per page, with outliers at <35% or >200% of median.

| Identifier | Pages | Total ch | Median/pp | Min | Max | Outlier pages |
|---|---|---|---|---|---|---|
| ANT-RSP-v1-0 | 22 | 79,768 | 3,661 | 1,351 | 5,223 | none |
| ANT-RSP-v2-0 | 22 | 71,249 | 3,672 | 121 | 4,177 | 1 (121), 3 (1,275), 4 (1,283) |
| ANT-RSP-v2-1 | 22 | 74,376 | 3,767 | 133 | 4,447 | 1 (133), 3 (952), 4 (1,252) |
| ANT-RSP-v2-2 | 23 | 86,536 | 3,951 | 144 | 4,855 | 1 (144), 3 (1,004), 4 (1,331), 23 (1,003) |
| ANT-RSP-v3-0 | 19 | 59,643 | 3,572 | 169 | 4,713 | 1 (169), 2 (729), 19 (850) |
| ANT-RSP-v3-1 | 20 | 70,509 | 3,741 | 154 | 5,480 | 1 (154), 2 (822), **10 (384)**, 20 (819) |
| ANT-RSP-v3-2 | 20 | 62,006 | 3,584 | 166 | 4,746 | 1 (166), 2 (768), **10 (367)** |
| ANT-RSP-v3-3 | 20 | 72,703 | 3,788 | 153 | 6,131 | 1 (153), 2 (884) |
| ANT-RSP-v3-4 | 21 | 76,944 | 3,750 | 153 | 6,091 | 1 (153), 2 (925) |
| GDM-FSF-v1-0 | 7 | 25,286 | 3,692 | 967 | 5,615 | 7 (967) |
| GDM-FSF-v2-0 | 9 | 32,903 | 3,875 | 277 | 5,191 | 9 (277) |
| GDM-FSF-v3-0 | 16 | 46,119 | 3,284 | 101 | 4,316 | 1 (101), 11 (669) |
| GDM-FSF-v3-1 | 20 | 62,382 | 3,318 | 97 | 4,630 | 1 (97), 16 (635) |
| OAI-PF-2023 | 27 | 57,252 | 1,940 | 34 | 5,150 | 1 (401), **8 (5,150)**, **9 (4,438)**, **11 (4,407)**, 27 (34) |
| OAI-PF-v2 | 22 | 79,595 | 3,942 | 67 | 5,856 | 1 (67) |
| XAI-FAIF-2025 | 11 | 29,562 | 2,779 | 1,261 | 3,420 | none |
| XAI-FAIF-2026 | 9 | 24,581 | 2,870 | 660 | 3,277 | 9 (660) |
| XAI-RMF-2025-02 | 8 | 22,500 | 2,757 | 1,305 | 3,144 | none |
| XAI-RMF-2025-08 | 9 | 25,190 | 2,841 | 2,141 | 3,264 | none |

**Reading these.** Most low outliers are benign and expected: page 1 is a cover page
in every Google-Docs-produced document (100–170 ch), page 2–4 are contents pages, and
final pages are short closers. `OAI-PF-2023` p27 at 34 characters is a back page
carrying only the running footer.

Three that are **not** benign:

- **`OAI-PF-2023` pages 8, 9, 11** run 2.3–2.7× the median. That is not a defect —
  it is where the risk-level tables live, and they extracted densely. Listed because
  they are outliers and you should know why.
- **`ANT-RSP-v3-1` p10 (384) and `ANT-RSP-v3-2` p10 (367)** are the only mid-document
  low outliers in the corpus. Both sit at ~10% of their document's median in the
  middle of the body. Worth a look; see §5.
- **`OAI-PF-2023` overall median of 1,940** is half the corpus norm. This is a
  design difference — the document is set on 1700×2200 pt pages with large type and
  heavy whitespace — not an extraction failure. Its per-page counts are internally
  consistent.

---

## 2. Table inventory

### 2.1 OpenAI

#### `OAI-PF-v2` — 5 captioned tables, 19 detected blocks. **Structure preserved.**

This document uses LaTeX captions, and the caption is emitted *after* the table body
in reading order. Table 1 spans pages 4–6 with its caption on page 6; if you search
for the caption and read forward you will find nothing and wrongly conclude the table
is missing. It is not.

**Table 1: Tracked Categories** (pp. 4–6, ~5 columns). Runbook §1.2 singles this out
as holding most of the threshold language. Column boundaries hold:

```
                      [Critical] A tool-augmented          Finding and executing end-
                      model can identify and de-           to-end exploits for all soft- • Until we have specified
                      velop functional zero-day            ware could lead to catastro-    safeguards and security
                      exploits of all severity lev-        phe from unilateral actors,     controls standards that
                      els in many hardened real-           hacking military or indus-      would   meet a Critical
```

Two caveats, neither fatal. First, LaTeX hyphenation splits words across lines
(`de-velop`, `constrain-ing`, `catastro-phe`) throughout the table — this is in the
PDF, not an extraction artifact, but it will affect verbatim excerpt matching.
Second, and more consequential for you, the row-label column is vertically offset
from its row:

```
                      [High] The model’s impact            This milestone suggests AI
 AI Self-             is equivalent to giving every        self-improvement may be • Require security con-
 improvement:         OpenAI researcher a highly           performant mid-career re-   trols meeting High stan-
 The ability of an    research engineer assistant,         search, operations, and se-
```

`AI Self-improvement:` begins on the row's *second* line. Runbook §2.2 item 2 warns
that a bullet like "Require security controls meeting High standard" is uncodeable
without its row label — this is exactly that case, and a naive segmenter will attach
the label to the wrong unit. Not scrambled, but needs care at A1.

Page furniture also lands inside the table: footnote 5 and the page number `5` appear
between the page-4 and page-5 portions of Table 1.

**Table 2: Research Categories** (p. 8, 2 columns). Clean:

```
 Research Category                                         Potential response

 Sandbagging: ability and propensity to respond to         Adopt elicitation approach that overcomes
 safety or capability evaluations in a way that signifi-   sandbagging, or use a conservative upper
 cantly diverges from performance under real condi-        bound of the model’s non-sandbagged evalu-
 tions, undermining the validity of such evaluations.      ation results
```

**Table 3: Types of safeguards** (p. 12, 2 columns). Clean; both columns read down
correctly side by side. **Tables 4 and 5** (pp. 19–20, 3 columns — Claim / Potential
safeguards / Efficacy) clean:

```
     Claim               Potential safeguards                        Potential safeguard effi
     Alignment           • Generalization from specified or          • Red-teamers create bot
     Alignment           • Instruction following, instruction hi-    • Large scale usage or t
     Architecture        • Limiting internet access and other tool   • Testing and red-teamin
```

**Verdict: no hand transcription required.** Watch the row-label offset in Table 1.

#### `OAI-PF-2023` — no captions, 7 detected blocks. **One table broken.**

Risk-level tables on pp. 8, 9, 11 (Cybersecurity, CBRN/Persuasion, Model Autonomy)
extracted cleanly at 3 columns:

```
Risk level   Definition                                                    Rationale for threshold

Low          Model assistance for cyberattacks, if any, is meaningful      Non-programming tasks represent a sizable bottleneck
             only for non-programming uses, e.g., translation,             for threat actors; however, the skills involved are not
             targeted distillation of confidential information, and/or     terribly specialized and the benefit comes often from
```

**The Illustrative Scorecard (p. 15) is broken.** Three separate problems:

```
     Tracked Risk Category        Pre-mitigation risk level

                      Post-mitigation risk level 

                                                                                                                       e
                                  Determine pre-mitigation risk level using best   Determine overall risk level after mitigations are
                                  known capability elicitation techniques          in place using best known capability elicitation

                                                                                                                    i v
                                                                                                      t
     Cybersecurity                Low                                              Low

                                      ra
     CBRN                         Low                                              Low

     Persuasion

                                   st
```

1. The header row is split — `Post-mitigation risk level` is orphaned onto its own
   line, detached from the two-column header it belongs to.
2. The word **"Illustrative"** is set as a large background watermark, and its
   letters extract as free-floating fragments — `e`, `i v`, `t`, `ra`, `st` — landing
   between and inside table rows.
3. The `Persuasion` row's values are separated from the label by watermark debris.

**This one needs hand transcription**, and it is the highest-value cell block in the
corpus to get right: runbook §2.4 names the 2023 Scorecard as the counterpart to the
2025 per-category thresholds, and C03's `architecture_replaced` cannot fire if that
alignment fails.

### 2.2 Anthropic — 9 documents, 4–10 blocks each. **All structure preserved.**

No captioned tables in any RSP. The recurring tables are the ASL/capability-threshold
grids (pp. 6–9 depending on version) and the Appendix A competitor-commitment tables
(pp. 16–17), plus the glossary grid (p. 18 in v2.x).

`ANT-RSP-v1-0` ASL table (p. 4, 4 columns) — columns hold, **but note the row-label
column is contaminated by a side annotation**:

```
AI Safety    Dangerous Capabilities                 Containment Measures                             Deployment Measures
Level                                               Required to store model weights                  Required for internal/external use

ASL-2        No capabilities likely to cause        Evaluate for ASL-3 warning signs when            Follow current deployment best
             catastrophe, although early            training, using methods and Evaluation           practices e.g. model cards,
Our          indications of these capabilities.     Protocol described below.                        acceptable use policies, misuse
current      For example, an AI system that                                                          escalation procedures, vulnerability
safety       can provide bioweapon-related          Harden security against opportunistic            reporting, harm refusal techniques,
level        information that couldn’t be found     attackers.                                       T&S tooling, and partner safety
```

The words `Our / current / safety / level` running down the left are a marginal
callout in the PDF pointing at the ASL-2 row. In the text they interleave with
column 1 and read as part of the cell. Worth a manual note at A1 so the callout
becomes its own unit rather than corrupting the ASL-2 row label.

`ANT-RSP-v3-4` capability-threshold table (p. 8, ~5 columns) — three columns hold
cleanly across a long block:

```
 Automated R&D in key domains.                  We will:                                     A frontier developer should make a strong argument that:
  AI systems that can fully automate,
   or otherwise dramatically                    ●   Resource and complete                    ●     No user or team of users (including those backed by top-tier states) will
    accelerate, the work of large,                     significant “moonshot R&D                      b ecome significantly more likely to cause catastrophic harm via their usage
     top-tier teams of human                            for security” projects, to                     of product surfaces or via theft of model weights.
```

Two cosmetic artifacts here: a one-space-per-line **indentation staircase** in
column 1 (`Automated`, ` AI systems`, `  or otherwise`, `   accelerate`), and the
spurious space in `b ecome`. Both trace to the same root cause as §6. Neither
destroys structure.

Appendix A tables (`Scenario` / `Commitment`, pp. 16–17) clean in all versions.

**Verdict: no hand transcription required for any Anthropic document.**

### 2.3 Google DeepMind — 4 documents. **All structure preserved.**

`GDM-FSF-v2-0` has two captioned tables (Table 1: Misuse CCLs, p. 5; Table 2:
Deceptive Alignment CCLs, p. 7). `GDM-FSF-v3-0` has five (2.2.1.a, 2.2.2.a, 2.2.3.a,
3.2.1.a, 4.a). `GDM-FSF-v3-1` has four (2.2.1.a, 2.2.2.a, 2.2.3.a, 3.2.2.a).
`GDM-FSF-v1-0` captions nothing but carries 13 detected blocks including the
mitigation-level tables (pp. 3–4) and the CCL grid (p. 5).

These are the cleanest tables in the corpus. `GDM-FSF-v3-1` Table 2.2.1.a:

```
    Critical Capability Level          Recommended security level and rationale

    CBRN uplift level 1:               Security level 2+
    Provides low to medium
    resourced actors uplift in         The difficulty of building defenses against certain CBRN threats
    reference scenarios                means the exfiltration, unauthorized modification, and leak of model
    resulting in additional8           weights with this capability could be highly damaging.
```

`GDM-FSF-v2-0` Table 1 at 3 columns:

```
    Risk domain9          Critical capability level         Recommended security level and rationale

    CBRN: Risks of        CBRN uplift 1: Can be used        Security controls and detections at a level generally
    models assisting in   to significantly assist a         aligned with RAND SL 2
```

One note: footnote reference markers fuse to the preceding word (`Risk domain9`,
`additional8`, `Security level 413`). Harmless to read, but `Security level 413` is
"Security level 4" plus footnote 13, not level 413 — a segmenter extracting
`stated_bar` could take the wrong number. Affects all four GDM documents and
`GDM-FSF-v3-0` p14 in particular.

**Verdict: no hand transcription required.**

### 2.4 xAI — 4 documents. **One document broken; three have no tables at all.**

`XAI-RMF-2025-08`, `XAI-FAIF-2025` and `XAI-FAIF-2026` contain **no tables**. Zero
tabular lines detected in all three; their thresholds are stated in prose:

```
Thresholds: Our risk acceptance criteria for system deployment is maintaining a dishonesty
rate of less than 1 out of 2 on MASK. We plan to add additional thresholds tied to other
benchmarks.
```

This is a real structural difference between xAI and the other three labs, not an
extraction artifact — worth knowing before you interpret a low table-derived unit
count for xAI as missing data.

**`XAI-RMF-2025-02` has two tables and both are scrambled.** The document carries a
diagonal DRAFT watermark; its letters extract as isolated fragments that land inside
table cells and between rows.

Table 1, Benchmark / Threshold / Reference score (pp. 3–4):

```
  Benchmark                             Threshold     Reference score

  D    WMDP-Bio: multiple-choice           X%

      LAB-Bench6 ProtocolQA:            X%             79% by human experts
       multiple-choice questions on          (e.g. 50%)     (multiple-choice)

      Cybench8: professional-level      X%             Leading model performance of 35%
       Capture the Flag challenges           (e.g. 30%)     (pass@10) as of 2024

      WMDP-Cyber9: multiple-choice    X%
       questions on proxies of hazardous  (e.g. 50%)
        cybersecurity knowledge
                                                               T
                                                               55.3% by GPT-4 (zero-shot)
```

The `WMDP-Cyber` row's reference score, `55.3% by GPT-4 (zero-shot)`, is displaced
below a watermark `T` and detached from its row. The `WMDP-Bio` row carries a stray
`D` in the label column and its reference score is missing from position entirely.

Table 2, Benchmark / Thresholds (p. 5):

```
  Benchmark                     Thresholds

D Model Alignment
   between Statements
    and Knowledge
     (MASK)

  Utility Functions
                                  <X% lying on MASK
```

Here the watermark `D` has **fused into the cell text** (`D‭Model Alignment`), and the
threshold `<X% lying on MASK` sits against the `Utility Functions` row when it belongs
to the MASK row above it. A coder reading this file would attribute the wrong
threshold to the wrong benchmark, and nothing about the output looks wrong.

**Both tables need hand transcription.** I have not attempted to repair them.

---

## 3. Multi-column pages

**No document in the corpus uses multi-column body text.** All 19 are single-column
prose with tables. The apparent "columns" the detector reports are table columns, not
page columns, and reading order is therefore not at risk from column interleaving.

The closest thing to a multi-column page is `OAI-PF-v2` p. 12 and Table 3 on p. 12,
which set two side-by-side lists under paired headers. Reading order survives — each
line reads left cell then right cell, consistently:

```
   Potential claims:                                     Potential claims:
 • Usage Monitoring: If a model does not refuse             • Value Alignment: The model consistently
   and provides assistance to harmful tasks,                  applies human values in novel settings
```

Note that this pairing means a naive line-based segmenter will merge a left-column
bullet with an unrelated right-column bullet into one unit. Not a reading-order
failure, but a segmentation hazard on that page.

---

## 4. Footnotes

**Present and page-attached in all 19 documents.** Footnote text extracts at the
bottom of the page carrying the reference, not gathered into an endnote block, and
not dropped. Verified by inspecting page tails across all four labs.

`GDM-FSF-v3-1` p. 9 tail:

```
RAND’s, we are referring to the security goals and principles in the RAND framework, rather than the benchmarks
(i.e. concrete measures) also described in the RAND report. As the authors point out, the “security level benchmarks
represent neither a complete standard nor a compliance regime—they are provided for informational purposes only
and should inform security teams’ decisions rather than supersede them.”
```

Two caveats:

- **Footnote blocks can land mid-page when a page break falls inside a table.** In
  `GDM-FSF-v2-0` p. 4→5, footnotes 4–8 appear *between* two halves of the same body
  paragraph. The text is all there and in page order; it just interrupts a sentence.
  Same pattern in `OAI-PF-v2` inside Table 1.
- **Reference markers fuse to the preceding word** (`Risk domain9`, `WMDP-Cyber9`,
  `additional8`). Noted in §2.3 because of the `stated_bar` risk.

Since your Stage 5 spec keeps footnote text, no action is needed here beyond
awareness that a footnote may interrupt a table region.

---

## 5. Ranked list of pages to inspect by hand

Worst first.

| # | Document | Page(s) | Why |
|---|---|---|---|
| 1 | `XAI-RMF-2025-02` | **3–4** | Table 1 scrambled. `WMDP-Cyber` reference score detached from its row and displaced below a watermark `T`; `WMDP-Bio` reference score missing from position; stray `D` in the label column. Needs transcription. |
| 2 | `XAI-RMF-2025-02` | **5** | Table 2 scrambled. Watermark `D` fused into the `Model Alignment (MASK)` cell; threshold `<X% lying on MASK` sits against the wrong row. Needs transcription. |
| 3 | `OAI-PF-2023` | **15** | Illustrative Scorecard: header row split, "Illustrative" watermark letters (`e`, `i v`, `t`, `ra`, `st`) inside the table body, `Persuasion` row separated from its values. Needs transcription. High downstream weight — runbook §2.4 alignment counterpart. |
| 4 | `OAI-PF-2023` | **6** | Carries a 3102×3435 px raster image with no text-layer contribution. Page extracts one paragraph plus footer. **Open the PDF and see what the image is** — if it is content rather than decoration, it is silently absent from the corpus. |
| 5 | `OAI-PF-v2` | **4–6** | Table 1 (Tracked Categories). Structure is sound, but the row-label column is vertically offset onto each row's second line, and footnote 5 plus a page number land inside the table. Highest-density threshold content in the OpenAI chain; confirm every cell produced units per runbook §2.2 item 1. |
| 6 | `ANT-RSP-v3-1` | **10** | 384 characters against a document median of 3,741 — the largest unexplained mid-document low outlier in the corpus. |
| 7 | `ANT-RSP-v3-2` | **10** | 367 characters against a median of 3,584. Same position as #6 in the adjacent version, so likely the same page design in both — confirm once and it resolves both. |
| 8 | `ANT-RSP-v1-0` | **4** | ASL table: the marginal callout `Our / current / safety / level` interleaves into column 1 and reads as part of the ASL-2 row label. |
| 9 | `OAI-PF-v2` | **12** | Paired side-by-side bullet lists under `Potential claims:` headers. Reading order is fine; the hazard is a segmenter merging a left bullet with an unrelated right bullet. |
| 10 | `GDM-FSF-v3-0` | **14** | `Security level 413` is "Security level 4" + footnote 13. Check `stated_bar` here and wherever a level number precedes a footnote marker across all four GDM documents. |
| 11 | `OAI-PF-2023` | **8, 9, 11** | High outliers (2.3–2.7× median). Expected — these hold the risk-level tables and extracted densely. Listed for completeness; I found no defect. |

Items 1–3 are the ones I would not code without fixing. Item 4 is unknown until
someone looks. Items 5–10 are checks, not known defects.

---

## 6. Cross-cutting: invisible control characters

Not part of your five headings, but it will bite the validator in runbook §2.7, which
requires that every `value: 1` carry evidence appearing **verbatim** in the unit
record. Five files contain invisible Unicode that makes visually identical strings
compare unequal.

| Identifier | U+202D/U+202C | U+200B | Genuine word splits |
|---|---|---|---|
| ANT-RSP-v2-2 | **2,918** | 0 | 7 |
| XAI-RMF-2025-02 | **742** | 0 | 0 |
| ANT-RSP-v3-4 | 0 | **2,498** | 7 |
| ANT-RSP-v3-3 | 0 | **2,361** | 7 |
| ANT-RSP-v3-1 | 0 | **2,281** | 8 |
| ANT-RSP-v3-2 | 0 | 216 | 0 |
| ANT-RSP-v3-0 | 0 | 210 | 0 |
| ANT-RSP-v2-1 | 0 | 127 | 0 |
| GDM-FSF-v3-1 | 0 | 95 | 0 |
| GDM-FSF-v3-0 | 0 | 64 | 0 |
| GDM-FSF-v2-0 | 0 | 40 | 0 |
| XAI-FAIF-2025 | 0 | 33 | 0 |
| XAI-FAIF-2026 | 0 | 23 | 0 |
| others | 0 | 0–1 | 0 |

U+202D/U+202C are left-to-right override and pop-directional-formatting; in
`ANT-RSP-v2-2` and `XAI-RMF-2025-02` they wrap nearly every line. U+200B is a
zero-width space. Both are emitted by the Google Docs PDF renderer and are invisible
in any editor.

The same encoding also produces the spurious intra-word spaces — `b ecome`,
`p erspective`, `B ackground`, `w ww.anthropic.com` — 7–8 per affected file. These
are visible, and unlike the control characters they change the token stream.

I have **not** stripped any of this, because Stage 5 as you specified it removes cover
pages, contents, headers and page numbers, and says nothing about character
normalisation. Flagging it as a decision for Stage 5: whether `.clean.txt` should also
normalise U+202D/U+202C/U+200B and repair the ~29 intra-word splits. My
recommendation is yes for the control characters (they are pure noise and invisible,
so nothing can be lost) and **no** for the intra-word splits without review, since
repairing them mechanically means editing words.

The per-page form feeds (`\f`, one per page, count matches page count in all 19 files)
are pdftotext's page separators and are useful — they are how §1's per-page counts
were derived. Keep them.

---

## 7. Per-document verdict

| Identifier | Tables | Structure | Action |
|---|---|---|---|
| ANT-RSP-v1-0 | 4 blocks | Preserved | Note p4 marginal callout |
| ANT-RSP-v2-0 | 8 blocks | Preserved | None |
| ANT-RSP-v2-1 | 10 blocks | Preserved | None |
| ANT-RSP-v2-2 | 10 blocks | Preserved | Control chars (§6) |
| ANT-RSP-v3-0 | 8 blocks | Preserved | None |
| ANT-RSP-v3-1 | 8 blocks | Preserved | Check p10; control chars |
| ANT-RSP-v3-2 | 8 blocks | Preserved | Check p10 |
| ANT-RSP-v3-3 | 10 blocks | Preserved | Control chars |
| ANT-RSP-v3-4 | 10 blocks | Preserved | Control chars |
| GDM-FSF-v1-0 | 13 blocks | Preserved | None |
| GDM-FSF-v2-0 | 2 captioned + 7 blocks | Preserved | Footnote-marker fusion |
| GDM-FSF-v3-0 | 5 captioned + 8 blocks | Preserved | Check p14 `stated_bar` |
| GDM-FSF-v3-1 | 4 captioned + 6 blocks | Preserved | Footnote-marker fusion |
| OAI-PF-2023 | 7 blocks | **p15 broken** | **Transcribe p15**; inspect p6 image |
| OAI-PF-v2 | 5 captioned + 19 blocks | Preserved | Row-label offset in Table 1 |
| XAI-FAIF-2025 | none | n/a | None |
| XAI-FAIF-2026 | none | n/a | None |
| XAI-RMF-2025-02 | 2, **both broken** | **Scrambled** | **Transcribe both** |
| XAI-RMF-2025-08 | none | n/a | None |

**16 of 19 documents need no table repair. 2 documents hold 3 tables requiring hand
transcription. 1 page holds an image of unknown content.**

*(Superseded in part at Stage 7: the p6 image is now identified and, by decision of
2026-08-13, excluded — see §8.2. Net position: 2 documents hold 3 tables requiring
hand transcription.)*

---

## 8. Carried forward to A1 unit review (runbook §2.2)

Three items that are not extraction defects but will misfire at segmentation if
nobody is looking for them. None can be fixed in the text; all are review instructions.

### 8.1 Tables spanning a page break, in the *undamaged* documents

Where a table crosses a page break, the extraction interleaves the page footer — and
sometimes a running header or section heading — into the middle of the table. **No
content is lost.** The risk is narrower and easier to miss: `section_heading` can be
mis-assigned on the continuation rows, because the nearest preceding heading-like line
is page furniture rather than the table's own caption.

Documents and regions to check specifically:

| Document | Table crosses |
|---|---|
| ANT-RSP-v3-0 | p7→p8, p8→p9 |
| ANT-RSP-v3-1 | p7→p8, p8→p9 |
| ANT-RSP-v3-2 | p7→p8, p8→p9 |
| ANT-RSP-v3-3 | p7→p8, p8→p9, p9→p10 |
| ANT-RSP-v3-4 | p7→p8, p8→p9, p9→p10 |
| GDM-FSF-v3-0 | p13→p14 |
| OAI-PF-v2 | Table 1, pp. 4–6 (confirmed by hand: footnote 5 and a bare page number `5` sit inside the table) |

The Anthropic v3.x capability-threshold tables are the ones that matter most — they
run across three pages and hold the threshold language.

### 8.2 The OAI-PF-2023 p6 graphic is excluded — RESOLVED, no A1 action

The page 6 raster was classified at Stage 7 as a table rendered as an image: a risk
matrix (Low/Medium/High/Critical across Cybersecurity, CBRN, Persuasion, Model
Autonomy, plus a Post-Mitigation Model Score row), captioned
`The model score is the highest risk score in *any* category`.

**By analyst decision of 2026-08-13 the graphic and its caption are excluded from the
corpus.** They were judged not to carry information useful to the codebook. Page 6's
body prose ("Our rationale for grouping and naming these specific risk categories…
the need for broader, more disruptive actions.") is retained unchanged — it extracted
cleanly and was never at risk.

Two consequences:

1. **`OAI-PF-2023` now holds only one illustrative scorecard in the corpus**, the p15
   table. The `duplicate_of` hazard raised at Checkpoint 3 no longer exists, and the
   `[A1 REVIEW FLAG]` has been removed from the p15 transcription.
2. **The 2023 framework enters the corpus without an aggregate scoring rule in any
   form.** The sentence above appears nowhere else in the document's text. It was
   previously identified as load-bearing for the C03 `architecture_replaced`
   comparison against the 2025 per-category thresholds — the claim that an aggregate
   gate was replaced by per-category ones. Recorded here for the methods section; the
   decision stands.

The full withdrawn transcription is preserved at
`review/OAI-PF-2023-p6.draft.WITHDRAWN.txt`, and the classification and decision at
`review/OAI-PF-2023-p6-image-classification.md`, so the exclusion is reversible
without re-deriving anything.
