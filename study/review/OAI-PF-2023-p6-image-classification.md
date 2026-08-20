# OAI-PF-2023 p6 — raster image: classification and DECISION

**Status: graphic EXCLUDED from the corpus by analyst decision, 2026-08-13.**
Page 6 prose is retained unchanged. No transcription is spliced for this page.

Files: `OAI-PF-2023-p6-06.jpg` (page render, 200 dpi) and
`OAI-PF-2023-p6-img-000.png` (the embedded raster, 3102×3435 px).
`OAI-PF-2023-p6-img-001.png` is the image's soft mask, not separate content.

---

## Decision

| Element | Disposition |
|---|---|
| Page 6 body prose ("Our rationale for grouping… more disruptive actions.") | **KEPT** — unchanged in `.norm.txt` |
| The risk-matrix graphic | **EXCLUDED** — not transcribed |
| The caption sentence beneath the graphic | **EXCLUDED** — not transcribed |

Rationale given: the graphic and its caption do not convey information useful to the
codebook.

**Note for the methods section.** This reverses the earlier position that page 6
should enter the corpus because its caption is the aggregate scoring gate and is
load-bearing for the C03 `architecture_replaced` comparison against the 2025
per-category thresholds. Under the decision recorded here, the 2023 framework enters
the corpus without that sentence in any form. Flagging once, for the record; the
decision stands and has been applied.

## Classification (unchanged)

**Case 3 — a table rendered as an image.** A labelled risk matrix with printed text in
its cells, not a diagram. Its content contributed nothing to `OAI-PF-2023.txt`: page 6
of the extraction holds the body paragraph and the running footer only.

The convention's prior expectation — "a 3102×3435 raster on page 6 of a 21-page policy
document is more likely to be a diagram than a table" — did not hold. (The document is
27 pages, not 21.)

## What the excluded graphic contains

Recorded here so the exclusion is reversible without re-deriving it.

- **Column headers:** `Low`, `Medium`, `High`, `Critical`
- **Row labels:** `Cybersecurity`, `CBRN`, `Persuasion`, `Model Autonomy`
- One cell per row is filled and carries a printed word; the other three are empty
  outlined boxes:
  - Cybersecurity → `Medium`
  - CBRN → `Low`
  - Persuasion → `Medium`
  - Model Autonomy → `Low`
- Below a horizontal rule, a row labelled `Post-Mitigation Model Score` with a single
  filled cell under `Medium`, reading `Medium`. The Low, High and Critical positions
  in that row have no box drawn at all.
- Caption printed in bold beneath the grid:
  `The model score is the highest risk score in *any* category`
  (asterisks are literal in the source, not italic markup)
- The word `Illustrative` runs diagonally across the graphic as a pale watermark.

The full draft transcription, drafted and then withdrawn, is preserved in
`OAI-PF-2023-p6.draft.WITHDRAWN.txt` should the decision be revisited.

## Consequence for page 15

With the p6 graphic excluded, `OAI-PF-2023` now contains only **one** illustrative
scorecard in the corpus — the page 15 table. The `duplicate_of` risk flagged at
Checkpoint 3 no longer applies, and the `[A1 REVIEW FLAG]` has been removed from the
page 15 draft.
