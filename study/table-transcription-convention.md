# Table transcription convention

For hand-repairing tables that `pdftotext -layout` scrambled. Applies to
`XAI-RMF-2025-02` pp. 3–5 and `OAI-PF-2023` p. 15.

Output is plain text, written into the `.norm.txt` file in place of the scrambled
region. The invisible-Unicode strip (`strip_invisibles.py`) runs **before** any
transcription, so `.norm.txt` already exists by the time you edit it; `.txt` stays
untouched as provenance. Do not use markdown pipe tables or preserve ASCII column
alignment — cells in these documents are multi-sentence paragraphs, and any format
relying on single-line rows or column position will re-scramble as soon as a cell
wraps.

---

## The convention

Each cell is one block. Row and column are stated as fields, never implied by
position.

```
<<TABLE table_id="Table 1" caption="Tracked Categories" page="5">>

<<CELL row="Biological and Chemical" col="Capability threshold that could lead to the risk" sub="High">>
The model can provide meaningful counterfactual assistance (relative to unlimited
access to baseline of tools available in 2021) to "novice" actors (anyone with a
basic relevant technical background) that enables them to create known biological
or chemical threats.
<</CELL>>

<<CELL row="Biological and Chemical" col="Associated risk of severe harm" sub="High">>
Significantly increased likelihood and frequency of biological or chemical terror
events by non-state actors using known reference-class threats.
<</CELL>>

<<CELL row="Biological and Chemical" col="Risk-specific safeguard guidelines" sub="High">>
- Require security controls meeting High standard (Appendix C.3)
- Require safeguards against misuse meeting High standard (Appendix C.1) before
  external deployment
<</CELL>>

<</TABLE>>
```

*(Illustration drawn from OAI-PF-v2 Table 1, which is sound and needs no repair.
Use it as the shape, not as content to copy.)*

### Rules

1. **One block per cell**, with one exception below. Never merge cells, even where
   the PDF visually spans one across two columns. If a cell genuinely spans, repeat
   the block once per column with identical content and add `spans="true"`.

   **Row-label cells.** Do not emit a block for a row-label cell that contains only
   the label — the label is already carried in every `row=` attribute of that row,
   and A1 treats row and column labels as context rather than units, so a block
   would produce a spurious unit. **But** where the first-column cell carries
   substantive prose beyond the label (e.g. OpenAI Table 1's *"Biological and
   Chemical: The ability of an AI model to accelerate and expand access to
   biological and chemical research…"*), that prose is codeable content: emit it as
   a block, and use the short label alone in the other cells' `row=`. Decide this
   per table and record which way you went.
2. **`row` and `col` are the header labels verbatim**, exactly as printed. These
   become `section_heading` and `context_stem` in Pass 1, so a paraphrased label
   silently changes what a downstream coder sees.
3. **`sub` is optional** — use it where a row is subdivided (High / Critical tiers
   in OpenAI's Table 1, threshold levels in xAI's). Omit the attribute entirely if
   there is no subdivision; do not write `sub=""`.
4. **Cell text is verbatim.** Hard-wrap freely — line breaks inside a block carry no
   meaning and Pass 1 will normalise them. Do not fix typos, do not expand
   abbreviations, do not convert curly quotes.
5. **Preserve bullets inside a cell** as `- ` lines. A1 rule 2 makes each bullet its
   own unit, so this distinction is load-bearing: collapsing three bullets into a
   paragraph turns three units into one.

   **Items set as separate paragraphs rather than bullets** — several distinct
   metric/threshold pairs in one cell, say — take `items="paragraphs"` on the
   `<<CELL>>` and stay as plain lines separated by a blank line. Do not add `- `
   markers: the document did not use bullets, and inserting them edits the document
   in order to describe it. A1 treats each paragraph in such a cell as its own unit,
   which matters because distinct thresholds carry distinct `stated_bar` values and
   a merged cell can only record one.
6. **Empty cells:** write the block with `<<EMPTY>>` as the body. Don't omit it —
   an omitted block is indistinguishable from a transcription you forgot.
7. **Footnote markers** stay inline as printed (`5`, `†`). Footnote *text* stays
   where it already is in the extracted file; don't move it into the cell.
8. **Blocks in reading order** — left to right, then top to bottom.
9. **Tables spanning a page break.** Emit one `<<TABLE>>` block per page, sharing a
   `table_id`, with `continued="true"` on the second and subsequent blocks. A *cell*
   split by the break is reassembled into a single block and placed in the first
   table block — the cell is the unit, the page is a rendering artefact. Transcribe
   the continuation page even if it falls outside the page range you were given;
   report that you did.
10. **Header rows carrying descriptions.** Where a column header holds a label plus
    a descriptive sentence defining that level, emit the sentence as a cell with
    `row="Level definition"`. These definitions are codeable content — the codebook
    names graded-tier tables and their content explicitly — so losing them would
    strip the tiers of their meaning. Do not fold the sentence into the `col=`
    attribute.

### Where to put it in the file

Replace the scrambled region of the `.norm.txt` only — never `.txt`, which is the
untouched extraction and your provenance record. Leave a marker so the edit is
traceable:

```
[TRANSCRIBED BY HAND — original extraction scrambled, see extraction-report.md §5]
<<TABLE ...>>
...
<</TABLE>>
[END HAND TRANSCRIPTION]
```

Then log it in `manifest.jsonl` — add `"hand_transcribed": ["p3", "p4", "p5"]` to
that document's entry. If a result later looks strange for one lab, this is how you
check whether transcription is implicated.

---

## Required addition to the A1 prompt

A1 does not currently know about these markers. Add to its SCOPE section:

> **Hand-transcribed tables.** Some tables appear in an explicit block format:
> `<<TABLE table_id="..." caption="..." page="..." continued="...">>` containing
> `<<CELL row="..." col="..." sub="..." items="..." spans="...">>` blocks. Treat each
> `<<CELL>>` as a table cell under segmentation rule 2:
>
> - if it contains `- ` bulleted items, each bullet is a unit;
> - if it carries `items="paragraphs"`, each blank-line-separated paragraph is a unit;
> - otherwise the cell is one unit.
>
> Set `unit_type` to `table_cell`, `section_heading` to the table caption, and
> `context_stem` to the row and column labels combined (e.g. "Biological and
> Chemical / Capability threshold / High"). Set `locator` to
> `{table_id} / {row} / {col}`, adding `/ {sub}` where present. The marker syntax
> itself is never part of an excerpt. A cell whose body is `<<EMPTY>>` produces no
> unit. Lines marked `[TRANSCRIBED BY HAND …]` / `[END HAND TRANSCRIPTION]` are not
> units. Two `<<TABLE>>` blocks sharing a `table_id`, the second marked
> `continued="true"`, are one table split across a page break — do not treat the
> continuation as a new section. A cell marked `spans="true"` appears once per
> column with identical content; assign `duplicate_of` to all but the first.

---

## The three specific cases

### XAI-RMF-2025-02, pp. 3–5

The straightforward one, though tedious. Work from the PDF on screen, not from the
scrambled text — reading the corrupted version first will anchor you to the wrong
row associations, which is precisely the error being repaired.

Transcribe the benchmark-to-threshold pairings **last**, and check each against the
PDF a second time. The report flags `WMDP-Cyber` as detached from its row and
`<X% lying on MASK` as sitting against the wrong one. Those two pairings are the
entire reason this repair is happening.

### OAI-PF-2023, p. 15 — Illustrative Scorecard

Higher stakes and lower certainty. This is the alignment counterpart for the 2025
per-category thresholds, so C03's `architecture_replaced` assignment depends on the
transcription being right.

Two things to decide as you go, and to write down:

- **If the scorecard is partly graphical** — colour bands, shaded cells, a matrix
  with no prose in some cells — transcribe what is *printed*, and use
  `<<EMPTY>>` where a cell carries only a colour or mark. Then add a plain-text note
  outside the table describing what the graphic conveys. Do not translate a colour
  into words inside a cell; that is interpretation, and it will be coded as though
  the document said it.
- **The word "Illustrative"** is a watermark, not content. It does not appear in any
  cell.

### OAI-PF-2023, p. 6 — the raster image

Classified as a table rendered as an image: a 4×4 risk matrix with a
Post-Mitigation Model Score row. **It enters the corpus**, transcribed under this
convention.

The deciding fact is the caption — *"The model score is the highest risk score in
any category"* — which appears nowhere else in the document's text. That is an
aggregation rule, and it is the aggregate gate that the 2025 per-category
thresholds replaced. Omitting page 6 would leave the 2023 framework in the corpus
without its scoring rule, and would remove the evidence the downstream comparison
depends on.

- **Unselected cells are `<<EMPTY>>`, not omitted.** They generate no units, so
  the verbosity costs nothing, and rule 6 exists so that an absent block never has
  to be distinguished from a forgotten one.
- **The caption is a cell**, not a note outside the table. It states a rule, so it
  must be codeable. Use `row="Caption"` with the column label the caption governs,
  or `col="(whole table)"` if it governs all of them.
- **Page 6 and page 15 are different illustrative examples**, not one figure
  appearing twice — p6 shows Cybersecurity at Medium and omits Unknown Unknowns;
  p15 shows Low/Low and includes it. Give them distinct `table_id` values including
  the page number, and record both in the manifest. Flag this pair for A1 review:
  a segmenter meeting two illustrative scorecards in one document is likely to set
  `duplicate_of` on the second, which would drop a genuine unit from analysis.