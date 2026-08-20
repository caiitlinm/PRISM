# PRISM — coded dataset, all four labs

Structured content analysis of frontier AI safety frameworks. This directory holds
three CSVs derived from the JSONL runs under `study/`. **The JSONL is the primary
record; these CSVs are a reproducible derivation and can be rebuilt at any time:**

```sh
python study/scripts/build_tables.py --labs OpenAI "Google DeepMind" Anthropic xAI
```

Written 2026-08-14, extended to the full corpus 2026-08-15. Whoever picks this up
will not have the conversation that produced it, so everything needed to read the
tables is here.

---

## 1. Scope, and what is missing

**This dataset now covers all four labs** — OpenAI (2 versions), Google DeepMind (4),
Anthropic (9 RSP versions) and xAI (4). The two halves ran weeks apart under the
identical configuration recorded in `run_config.json`: same model, same codebook
bytes, same prompt hashes, same effort and batch settings. Three parameters were
raised on the second half (`A2 --max-tokens`, `B-change --max-tokens`, and streaming
on B-change) and all three are output ceilings rather than behavioural settings —
they change whether a call truncates, not what an untruncated call emits. Departures
6, D5 and D6 in `run_config.json` record the reasoning.

**Regenerating the tables over all 19 documents reproduced every first-half row
byte-identically** — 1,351 unit rows, 23,366 long rows, 1,669 wide rows, headers
unchanged. The superseded first-half CSVs are retained at
`results/first-half-superseded/` as the evidence for that claim.

**One model, one repeat.** No between-model or within-model agreement is computable
from this data. That is deliberate. Reliability comes from human coding downstream.
Nothing here has been adjudicated, resolved, or collapsed across coders — `model`
and `repeat` are columns precisely so that later coders append rows rather than
overwrite them.

| | |
|---|---|
| Documents | 19 |
| Units | 4,775 (OpenAI 622 · GDM 729 · Anthropic 2,902 · xAI 522) |
| Transitions | 18 (15 adjacent + 3 endpoint) |
| Crosswalk rows | 4,899 (1,316 first half + 3,583 second) |
| Model | `claude-sonnet-5`, resolved `claude-sonnet-5`, created 2026-06-29 |
| Codebook | Canonical v8, 14 live codes |
| Run dates | 2026-08-14 (OpenAI, GDM) and 2026-08-15 (Anthropic, xAI) |

`temperature` is **not** set: `claude-sonnet-5` rejects any non-default sampling
parameter with HTTP 400. Sampling ran at the model default, so the run is **not
deterministic** and cannot be reproduced token-for-token. Re-running the pipeline
will produce similar but not identical coding.

## 2. Files and grain

| File | Grain | Rows |
|---|---|---|
| `units.csv` | one row per unit | 1,351 |
| `coded_wide.csv` | one row per (unit_id, transition_id, model, repeat) | 1,669 |
| `coded_long.csv` | one row per (unit_id, transition_id, code_id, model, repeat) | 23,366 |

All three are UTF-8 **with BOM** (`utf-8-sig`), every field quoted, newlines inside
fields replaced with a single space. Excerpts are otherwise verbatim.

### Why `transition_id` is in the key

The brief specifies `coded_wide.csv` as one row per (unit_id, model, repeat). That
grain is not unique in this corpus. The endpoint pair means **GDM-FSF-v3-1's 281
units are coded twice** — once against GDM-FSF-v3-0 (adjacent) and once against
GDM-FSF-v1-0 (endpoint). Those are different codings against different prior
versions, and collapsing them would destroy the endpoint comparison. `transition_id`
is therefore part of the key in both coded tables.

`units.csv` cannot express this, being one row per unit. Its `transition_id` and
`prior_*` columns are populated from the **adjacent** transition only. For endpoint
context, join `coded_wide.csv` on `transition_id`.

### Which rows exist

`coded_wide.csv` has one row for every (unit, transition) the change pass produced,
plus one row per unit that takes part in no transition (with `transition_id` =
`"NONE"`). 1,316 change rows + 353 transition-less units = 1,669.

## 3. `units.csv` columns

| Column | Values |
|---|---|
| `unit_id` | `{IDENTIFIER}-{0000}`, suffixed `-a`/`-b` where the 75-word ceiling forced a split |
| `lab` | `OpenAI` · `Google DeepMind` |
| `identifier` | `OAI-PF-2023` · `OAI-PF-v2` · `GDM-FSF-v1-0` · `GDM-FSF-v2-0` · `GDM-FSF-v3-0` · `GDM-FSF-v3-1` |
| `framework_version` | as printed in the document; `NONE` where unlabelled |
| `framework_year` | publication year |
| `section_heading` | nearest enclosing heading, verbatim |
| `locator` | subsection, table/cell reference, bullet path, or footnote number; `N/A` where the document offers none |
| `unit_type` | `numbered` · `bullet` · `table_cell` · `paragraph` · `footnote` · `callout` |
| `context_stem` | parent stem the unit depends on for sense; `NONE` if self-contained |
| `excerpt` | verbatim, ≤75 words (one unit exceeds — see §6) |
| `paraphrase` | one neutral sentence |
| `modal_register` | `mandatory` · `conditional` · `aspirational` · `none` |
| `stated_bar` | trigger value quoted verbatim; `NONE` if none stated |
| `duplicate_of` | earliest unit stating the same proposition; `NONE` otherwise |
| `removal_candidate` | `true` · `false` |
| `transition_id` | adjacent transition this unit belongs to; `NONE` if none |
| `prior_unit_id` | counterpart in the prior version; `NONE` if unaligned |
| `prior_stated_bar`, `prior_counterpart_excerpt`, `prior_modal_register` | the counterpart's values; `NONE` where unaligned |

## 4. The codes

Fourteen live codes. **C02 and C10 are permanently retired and never reissued** —
C02 *Threshold Tightening/Loosening* merged into C04 on 7 August 2026; C10 *Scope of
Risks* retired 7 August 2026. They must not appear in any row.

| Family | Codes |
|---|---|
| change | C01, C03, C04, C05, C06, C07 |
| content | C08, C09, C11, C12, C13, C14, C15, C16 |

### Direction vocabularies — closed lists, codebook v8 §3.2

**Seven codes carry a direction.** (The brief says nine; that count predates the
retirement of C02 and C10, both of which carried one. The codebook governs.)

| Code | Permitted direction values |
|---|---|
| C01 | `introduced` · `expanded` |
| C03 | `introduced` · `removed` · `reintroduced` · `architecture_replaced` |
| C04 | `tightened` · `loosened` — **plus a required facet**: `modality` · `bar` · `both` |
| C05 | `added` · `dropped` · `reintroduced` · `split` · `merged` |
| C06 | `narrowed` · `broadened` |
| C07 | `tightened` · `loosened` |
| C08 | multi-select, one or more of `A-umbrella` · `A-framing` · `A-motivation` |

C09 and C11–C16 carry no direction and record `NA`. **A code assigned without its
direction is incomplete** — this is not derivable from the data, which is why it is
written down here.

For C04's divergent case (language firms up while the bar loosens, or the reverse):
record the direction of the **bar**, set facet to `both`, and flag the passage
ambiguous. See codebook §3.3.

### Sentinel values — read this before filtering anything

**No cell in any of the three files is empty.** Missingness is encoded as literal
strings, and there are four of them plus one value that only looks like one.

| String | Meaning | Where it appears |
|---|---|---|
| `NONE` | the field legitimately has no value | text fields |
| `NA` | **not applicable — never evaluated** | code values, directions, facets |
| `N/A` | the document offers no locator | `locator` only |
| `none` | **a real coded value, not missingness** | `modal_register` |

**`none` is not missing.** 770 units carry `modal_register = none`, meaning the
excerpt uses no mandatory, conditional or aspirational language. That is an
observation about the text. Treating it as missing deletes 57% of the corpus.

**`prior_modal_register` mixes both, distinguished only by case.** `NONE` (745
rows) means there is no prior unit — the target was unaligned. `none` (296 rows)
means there *is* a prior unit and its register is none. **A case-insensitive read
collapses these and turns 296 real observations into missing data.**

`N/A` in `locator` and `NONE` elsewhere mean the same thing; the two spellings come
from different lines of the A1 prompt and are preserved as the segmenter emitted
them rather than normalised after the fact.

**In `coded_long.csv`, `direction = NA` is ambiguous.** It covers both codes that
never carry a direction (C09, C11–C16 — 11,683 rows) and direction-bearing codes
that did not fire (11,321 rows). Disambiguate with `code_id`; the column alone
cannot tell you which.

### `NA` versus `0` — the distinction that is not guessable from the data

| | Meaning |
|---|---|
| `0` | the code was evaluated against this unit and did not fire |
| `1` | the code fired |
| `NA` | **the code was never evaluated for this row** |

`NA` appears in exactly two places:

- **Change codes on units in no transition** (353 rows). The earliest version in a
  chain has no prior version, so no change code can apply.
- **Content codes on removal rows** (50 rows). A removal unit is a *prior*-version
  unit that vanished; it carries change codes only. It never went through the
  content pass, so coding it `0` would understate content prevalence in the prior
  version.

Treating `NA` as `0` will bias every prevalence figure downward. Treating it as
missing-at-random will bias them the other way. It is neither: it is *not
applicable*.

## 5. `coded_wide.csv` and `coded_long.csv`

`coded_wide.csv`: `unit_id`, `transition_id`, `model`, `repeat`,
`removal_candidate`, then one value column per code (`C01`, `C03`–`C09`, `C11`–`C16`),
one `{code}_direction` column for each of the seven direction-bearing codes,
`C04_facet`, and `c07_requires_c14`.

`coded_long.csv`: `unit_id`, `transition_id`, `code_id`, `model`, `repeat`, `value`,
`direction`, `facet`, `evidence`, `flag`, `ambiguity_reason`, `code_family`.

`evidence` is the quoted span justifying the assignment and **survives in full** —
it is what makes a disputed assignment checkable. `flag` is `clear` or `ambiguous`;
where `ambiguous`, `ambiguity_reason` states why.

`c07_requires_c14` is an **integrity flag, not an adjudication**: `true` where
C07 = 1 and C14 = 0, which codebook §3.4 does not permit. It is raised and left
raised. Nothing was resolved and no value was altered. **In this dataset it is
`false` on every row** — all 11 rows with C07 = 1 also carry C14 = 1.

## 6. Known limitations

- **One unit exceeds the 75-word ceiling.** `GDM-FSF-v3-0-0069-a`, 85 words: a
  single sentence with no internal sentence boundary. Flagged in the Stage 4 review
  pack rather than re-segmented, since units freeze once and re-running would
  resample every unit in the chunk.
- **The OAI-PF-2023 page 6 risk matrix is excluded from the corpus** by analyst
  decision of 2026-08-13, including its caption stating the aggregate scoring rule.
  The 2023 framework therefore enters without an explicit statement of its aggregate
  gate. If C03 `architecture_replaced` does not fire on `OAI-PF-2023_v2`, that
  absence is **at least partly an artefact of this exclusion and should not be
  reported as a finding about the framework**. See `study/review-protocol.md`.
- **Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed.** Every
  other table in the corpus reached the segmenter as pdftotext column layout with no
  structural markers, including all 23 tables across the nine Anthropic RSPs. Table coverage was checked in the Stage 4 packs, but a dropped cell in an
  untagged table is not detectable from the unit list alone.
- **31 of 50 removal rows carry no change code.** The aligner flagged the object as
  removed; no removal-type change code fired. Worth inspecting before these rows
  enter any prevalence count.
- **95 of 310 C04 assignments carry no facet (31%).** Codebook §3.2 makes the facet
  (`modality` · `bar` · `both`) required for C04, on the same footing as a
  direction, and states that a code assigned without its direction is incomplete.
  These are `NA` in the raw model output, not lost in the table build. Treat them as
  incomplete assignments rather than as C04 with an unknown facet. **The rate is
  comparable across halves — 29 of 75 (39%) on OpenAI/GDM, 66 of 235 (28%) on
  Anthropic/xAI — so this is a property of the instrument, not a cross-lab
  confound.** The second-half validator emits these as warnings; they were
  deliberately not re-run, because re-running only the second half would have coded
  the two halves to different standards.

- **One 394-word passage of `ANT-RSP-v1-0` is excluded from the unit list.** It is
  appendix eval task 2 ("Write a simple LM worm that will spread to totally
  undefended machines"), which `claude-sonnet-5` refuses to segment — three
  attempts, deterministic, zero output tokens. Only that task refuses; the other five
  eval tasks segment normally, so the exclusion is the passage, not the appendix.
  **Absence of codes there is absence by model refusal and is not evidence about the
  framework.** The appendix exists only in v1.0 and is gone by v2.0, making it the
  largest removed-content block in the Anthropic chain; roughly 80 of its ~95 units
  survive and still align as removals, so the block is ~15 units short rather than
  missing. It is also a **cross-lab asymmetry** — no OpenAI/GDM passage was refused,
  so Anthropic's coverage is fractionally lower for reasons unrelated to its
  frameworks. The text is retained verbatim at
  `study/batches/a1.chunk3-superseded/`; the full record with per-task evidence is
  `run_config.exclusions.ANT-RSP-v1-0_task2_lm_worm`.

- **132 rows are flagged `cosmetic_split = true`, and the flag is a null result.**
  A1 segments each version independently — it must, since each version is segmented
  exactly once — so nothing keeps granularity consistent across versions. In 66
  many-to-one alignments the target excerpts concatenate to *exactly* the prior
  excerpt: the text did not change, only the cut points did. Because the target
  excerpt is then a strict subset of the prior excerpt, these rows could have been
  read by the change coder as narrowed or deleted content. **They were not.** Change
  codes fire on flagged rows at 7.6% against an 8.8% baseline — slightly below, not
  above — with only 10 firings across all 132 rows (C08 × 9, C06 × 1). Filtering on
  the flag is available but is not required to avoid inflation. The caveat is small
  n: 10 firings cannot distinguish "never fooled" from "rarely fooled". The effect
  is unevenly distributed by construction (4% of many-to-one on the first half
  against 29% on the second, concentrated in Anthropic's near-identical point
  releases), which is why it was measured rather than assumed. See
  `run_config.cosmetic_splits_finding` and `study/review/cosmetic-splits.json`.
- **Unaligned target rate varies widely** — 21% on the GDM v3-0→v3-1 point release
  up to 62% of prior units orphaned on OAI-PF-2023→v2. Much of this is by design
  (Step A3 excludes ordinary rewording from removal rows), but it means "no
  counterpart" is not evenly informative across transitions.

## 7. Provenance

| Artifact | sha256 |
|---|---|
| `docs/codebook_v8.txt` | `a156350f1bf94be86fc8e7e7831c70a25ea96d7ea876e4210ebadebcee0bd585` |
| `docs/a1_prefix.txt` | `fe707219f8986f35d2c09725bdc415c3ff4525c85142bd4912a2460ed079244b` |
| `docs/a2_prefix.txt` | `f64b1891947a05e88c98f967556641d269bba8af7bc4bb1519770112e68c3fce` |
| `study/prompts/A1-segment.md` | `c8714d6eefd2f637235ef28770fb730c0091812ffbe9ea0d7ed190d85bdf83e5` |
| `study/prompts/A2-align.md` | `972f421c89bffd9049120b43c9678cfeb1ee9cea929e41d50d3df9948045a635` |
| `study/prompts/B-content-change.md` | `bcd0ba9748bcfe018908b62e16570bf4180ab87427c6fe9ed4028b5cfb330b23` |
| `study/scripts/run_pass.py` | `7deeb243ae924a46106ab4024854ed4e6d3be0b5b900746eb3449c67c9a08673` |
| `study/scripts/build_batches.py` | `07b4ce810ce1d206cd3104a45eaa2f32c15905d0861b143dc4c65ee1ae98cd13` |
| `study/scripts/validate_runs.py` | `d32af0ebccced3e8d3afb174c0a391668300bfcceed619447a08c7fec3e66b12` |
| `study/scripts/freeze_units.py` | `15787e4ddeab719e275d0701ab3fe338f6b5e043ddc3c245969a185f60c9e9ca` |
| `study/scripts/build_review_packs.py` | `e9989c81ef27e46b8bf8812682c91e88e816d3aa57f40e66f6908368e03af211` |
| `study/scripts/build_align_packs.py` | `e7c813073328e89365dd3e1d4b7167c75ab53f0b6bc7433d84445b679985c14c` |
| `study/scripts/build_tables.py` | `87bb8952005c4a7a964f518b763f62597025635c3b685bbf2c00b815d4a0f568` |

Full configuration, calibration measurements and **25 recorded departures from the
brief** are in `run_config.json`. Per-call token counts, timings and stop reasons
are in `run_log.jsonl`. The frozen unit files are hashed individually under
`run_config.checkpoint_c.frozen_files`; verify them before appending any coder.

Superseded runs are retained, never deleted: `study/raw/a1.run1-invalid/`,
`study/raw/a2.run1-superseded/`, `study/coded/change.truncated-run1/`. Each carries
a README explaining why it was replaced.
