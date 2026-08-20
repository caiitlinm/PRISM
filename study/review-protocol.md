# Review protocol — Stages 4 and 6

The checks the review packs must carry out, as briefed, amended for the corpus as
actually prepared. Two checks are removed; both removals are recorded here rather
than silently dropped, because both bear on the methods section.

Scope of this run: OpenAI and Google DeepMind. Anthropic and xAI follow under the
same protocol.

**Amendment, 2026-08-15 — one excluded passage on the Anthropic/xAI half.** A
394-word passage of `ANT-RSP-v1-0` (appendix eval task 2, "Write a simple LM worm
that will spread to totally undefended machines") is absent from the unit list
because `claude-sonnet-5` refuses to segment it: three attempts, deterministic, zero
output tokens. Only that task refuses; the other five eval tasks and the trailing
threat-models section segment normally, so the exclusion is the passage and not the
appendix. Chunk 3 was rebuilt as two batches around it, giving `ANT-RSP-v1-0` four A1
chunks rather than three.

Two consequences for review:

- **The `.03`/`.04` seam of `ANT-RSP-v1-0` is a real discontinuity**, with 394 words
  between the chunks. The seam check looks for repeated content across a seam and
  will correctly report none; do not read the gap as a dropped unit (Stage 4 check 8).
- **Absence of codes in that appendix is not evidence about the framework.** It is
  absence by model refusal. The appendix exists only in v1.0 and is gone by v2.0, so
  it is the largest block of removed content in the Anthropic chain; roughly 80 of its
  ~95 units survive and still align as removals, but the block is ~15 units short of
  what the document contains.

The excluded text is retained verbatim at `study/batches/a1.chunk3-superseded/`. Full
record, including the per-task localisation evidence, is in
`run_config.exclusions.ANT-RSP-v1-0_task2_lm_worm`.

---

## Stage 4 — unit review packs

One pack per document: `study/review/{ID}.units-review.md`.

This is the only validity check in the pipeline. Freezing units converts random
error into systematic error, so bad segmentation yields excellent reliability on
badly-cut units.

1. **Table coverage.** Units per table against cell count in the PDF. Flag any
   shortfall. Missing table cells are the most common failure and the hardest to
   spot, because the unit list looks complete on its own.
2. **`context_stem` audit.** Every unit where it is `"NONE"` and the excerpt is
   under 15 words or begins with a verb.
3. **`stated_bar` audit.** Every unit whose excerpt contains a digit, percentage
   or multiplier, with the extracted value. Flag those returning `"NONE"`.
4. **Rationale and framing retention.** Units beginning "we believe", "we
   revised", "in response to", "it is critical". The codebook codes explanatory
   and motivational language, so their absence means the segmenter dropped them
   as preamble.
5. **Suspicious units.** Under five words, or over 75.
6. **Hand-transcribed tables.** Every unit from a `<<CELL>>` block with its
   locator, confirming the markers were read as intended and that no marker
   syntax entered an excerpt.
7. **Chunk seams.** The boundary units where A1 chunks meet, since a model
   resuming mid-document sometimes re-emits the last unit of the prior chunk.
   Seams in this corpus:

   | Document | Chunks | Seam starts at |
   |---|---|---|
   | OAI-PF-2023 | 2 | `Mitigations` |
   | OAI-PF-v2 | 3 | `3 Measuring capabilities`, `5 Building trust` |
   | GDM-FSF-v3-0 | 2 | `2.2.3 Harmful Manipulation` |
   | GDM-FSF-v3-1 | 3 | `2.1.2 Deployment Mitigations`, `5.3 Past Updates and Changes` |
   | GDM-FSF-v1-0, GDM-FSF-v2-0 | 1 | none |

   The GDM-FSF-v3-0 seam was corrected before Stage 3 ran. It had landed on
   `1 (exploratory): Possesses`, a cell of Table 2.2.3.a that matched the
   top-level-numbered heading pattern, putting the boundary through the middle of
   that table so that neither A1 call could see a whole row. It now falls on the
   real section heading above the table. This had to be fixed before segmentation,
   not at this review: the remedy would be re-running A1 on the document, and units
   are segmented exactly once, ever.

### Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other
table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>`
markers — GDM-FSF-v3-0 contains none at all. Check 1 is therefore doing more work
than its wording suggests: for the GDM documents it is the *only* thing standing
between a mangled multi-column table and a set of frozen units that look plausible
individually. Count cells against the PDF for every table in those documents, not
just the ones that look suspect.

### Corpus-specific

8. **OAI-PF-v2 Table 1 `context_stem`.** Table 1 has its row labels offset onto
   each row's second line in the extraction. Check `context_stem` on every unit
   from that table specifically; it is the most code-dense table in the corpus and
   a stem failure there is invisible until it shows up as unexplained zeros on
   C09 and C13.

9. ~~**OAI-PF-2023 p6 / p15 scorecards.** Report whether A1 set `duplicate_of`
   between the two illustrative scorecards.~~ **REMOVED.**
   The page 6 risk-matrix graphic was excluded from the corpus by analyst decision
   of 2026-08-13 (`study/review/OAI-PF-2023-p6-image-classification.md`). Only the
   page 15 scorecard is in the corpus, so there is no second scorecard for
   `duplicate_of` to relate it to and the check cannot run. The decision document
   reaches the same conclusion: "the `duplicate_of` risk flagged at Checkpoint 3
   no longer applies."

---

## Stage 6 — alignment review

One pack per transition: `study/review/{TRANSITION}.align-review.md`.

1. Counts: aligned, `NONE`, removal candidates, many-to-one, one-to-many.
2. Every many-to-one and one-to-many group listed.
3. Alignments whose two excerpts share almost no vocabulary — either the most
   valuable (a renamed mechanism) or the most wrong.
4. Target units with `prior_unit_id: "NONE"` whose section heading matches a
   section present in the prior version — likely missed alignments.

### Corpus-specific, OAI-PF-2023_v2

5. **Scorecard to per-category thresholds.** Whether the 2023 Scorecard (page 15)
   aligned to the 2025 per-category thresholds. They are counterparts despite
   sharing no vocabulary, and C03's `architecture_replaced` cannot fire if that
   came back `NONE`. **This check stands** — the page 15 scorecard is in the
   corpus.

6. ~~**Aggregation rule.** Check that the page 6 aggregation rule — "the model
   score is the highest risk score in *any* category" — aligned to the 2025
   architecture that replaced it.~~ **REMOVED.**
   That sentence is the caption of the excluded page 6 graphic and is not present
   in the corpus in any form.

   **Consequence, for the methods section.** The exclusion decision records this
   itself: it "reverses the earlier position that page 6 should enter the corpus
   because its caption is the aggregate scoring gate and is load-bearing for the
   C03 `architecture_replaced` comparison against the 2025 per-category
   thresholds." The 2023 framework therefore enters the corpus without an explicit
   statement of its aggregate gate. C03 `architecture_replaced` on the
   OAI-PF-2023_v2 transition must now rest on check 5 alone — the scorecard-to-
   thresholds alignment — rather than on the aggregation rule that the 2025
   architecture actually replaced. If C03 does not fire on that transition, the
   absence is at least partly an artefact of this exclusion and should not be
   reported as a finding about the framework.

   The withdrawn transcription is preserved at
   `study/review/OAI-PF-2023-p6.draft.WITHDRAWN.txt`, so the decision is
   reversible; reversing it would require re-running A1 on OAI-PF-2023, which
   breaks the "segmented exactly once, ever" rule and must happen before
   Checkpoint C if at all.
