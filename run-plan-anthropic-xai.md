# Run plan — Anthropic and xAI

Stage 2 deliverable for the second half. Written 2026-08-14 against `manifest.jsonl`,
the configuration frozen in `run_config.json`, and the **measured** per-pass figures
from the completed OpenAI/Google DeepMind half in `run_log.jsonl`.

The first half is complete: 242 calls, 0 failures, $54.80, all four checkpoints
cleared. Every value in `run_config.json` is treated here as fixed unless a decision
in §7 says otherwise, and each such decision is a recorded departure.

**This plan is not approved. Three decisions are listed at the end; D4 is a blocker
and changes a script. Nothing runs until Checkpoint B clears.**

---

## 1. Scope

Thirteen documents, two labs, the remainder of the nineteen in `manifest.jsonl`.

| Identifier | Lab | Version | Date | Pages | Words | A1 chunks |
|---|---|---|---|---|---|---|
| ANT-RSP-v1-0 | Anthropic | Version 1.0 | 2023-09-19 | 22 | 10,382 | 3 |
| ANT-RSP-v2-0 | Anthropic | none | 2024-10-15 | 22 | 9,283 | 3 |
| ANT-RSP-v2-1 | Anthropic | Version 2.1 | 2025-03-31 | 22 | 9,542 | 3 |
| ANT-RSP-v2-2 | Anthropic | Version 2.2 | 2025-05-14 | 23 | 9,395 | 3 |
| ANT-RSP-v3-0 | Anthropic | Version 3.0 | 2026-02-24 | 19 | 7,587 | 3 |
| ANT-RSP-v3-1 | Anthropic | Version 3.1 | 2026-04-02 | 20 | 7,726 | 3 |
| ANT-RSP-v3-2 | Anthropic | Version 3.2 | 2026-04-29 | 20 | 7,998 | 3 |
| ANT-RSP-v3-3 | Anthropic | Version 3.3 | 2026-05-26 | 20 | 8,013 | 3 |
| ANT-RSP-v3-4 | Anthropic | Version 3.4 | 2026-07-08 | 21 | 8,550 | 3 |
| XAI-RMF-2025-02 | xAI | none (Draft) | 2025-02-20 | 8 | 2,565 | 1 |
| XAI-RMF-2025-08 | xAI | none | 2025-08-20 | 9 | 3,475 | 1 |
| XAI-FAIF-2025 | xAI | none | 2025-12-30 | 11 | 4,169 | 2 |
| XAI-FAIF-2026 | xAI | none | 2026-06-30 | 9 | 3,244 | 1 |
| | | | | **226** | **91,929** | **32** |

Words are `.clean.txt`, which is what `build_batches.text_path()` reads. All thirteen
were extracted at Stage 4 alongside the first half and carry zero invisible control
characters (verified 2026-08-14: 0 occurrences of U+200B/U+202C/U+202D across all
nineteen files). `XAI-RMF-2025-02` pages 3–5 are hand-transcribed; that and
`OAI-PF-2023` p15 remain the only hand-transcribed regions in the corpus.

The second half is **2.53× the first half by words** (91,929 vs 36,349) and 13
documents vs 6.

**Chunk counts in the last column assume D4 is approved.** Without it, eight of the
nine Anthropic documents produce a single oversize chunk of 6,000–6,500 words — see §7.

## 2. Chains

`chains()` builds adjacent pairs per lab in manifest order, plus the endpoint pair
where a lab has more than two documents. Both labs qualify.

| Transition ID | Prior → target | Kind |
|---|---|---|
| `ANT-RSP-v1-0_v2-0` | v1.0 → v2.0 | adjacent |
| `ANT-RSP-v2-0_v2-1` | v2.0 → v2.1 | adjacent |
| `ANT-RSP-v2-1_v2-2` | v2.1 → v2.2 | adjacent |
| `ANT-RSP-v2-2_v3-0` | v2.2 → v3.0 | adjacent |
| `ANT-RSP-v3-0_v3-1` | v3.0 → v3.1 | adjacent |
| `ANT-RSP-v3-1_v3-2` | v3.1 → v3.2 | adjacent |
| `ANT-RSP-v3-2_v3-3` | v3.2 → v3.3 | adjacent |
| `ANT-RSP-v3-3_v3-4` | v3.3 → v3.4 | adjacent |
| `XAI-RMF-2025-02_2025-08` | RMF Feb → RMF Aug | adjacent |
| `XAI-RMF-2025-08_FAIF-2025` | RMF Aug → FAIF 2025 | adjacent |
| `XAI-FAIF-2025_2026` | FAIF 2025 → FAIF 2026 | adjacent |
| `ANT-RSP-v1-0_v3-4` | v1.0 → v3.4 | endpoint |
| `XAI-RMF-2025-02_FAIF-2026` | RMF Feb → FAIF 2026 | endpoint |

Eleven adjacent, two endpoint — 13 transitions against the first half's 5. The two
endpoint pairs need `--endpoint` on both `build_batches.py` and the crosswalk path.

Note the xAI chain crosses a **framework rename** twice (Risk Management Framework →
Frontier AI Framework). Decision 0.5 in `corpus/decisions.md` scoped xAI as one
unbroken chain; nothing here revisits that, but C03-type codes on
`XAI-RMF-2025-08_FAIF-2025` should be read with it in mind.

## 3. Unit estimate

The first half projected 1,421 units and returned **1,351** — a 5% overshoot on the
single-document rate it was built from. That gives a much better rate than was
available last time: **1,351 units / 36,349 words = 37.17 units per 1,000 words**,
measured across six documents and two labs.

| Document | Words | Est. units |
|---|---|---|
| ANT-RSP-v1-0 | 10,382 | 386 |
| ANT-RSP-v2-0 | 9,283 | 345 |
| ANT-RSP-v2-1 | 9,542 | 355 |
| ANT-RSP-v2-2 | 9,395 | 349 |
| ANT-RSP-v3-0 | 7,587 | 282 |
| ANT-RSP-v3-1 | 7,726 | 287 |
| ANT-RSP-v3-2 | 7,998 | 297 |
| ANT-RSP-v3-3 | 8,013 | 298 |
| ANT-RSP-v3-4 | 8,550 | 318 |
| XAI-RMF-2025-02 | 2,565 | 95 |
| XAI-RMF-2025-08 | 3,475 | 129 |
| XAI-FAIF-2025 | 4,169 | 155 |
| XAI-FAIF-2026 | 3,244 | 121 |
| | **91,929** | **3,417** |

**Treat these as ±15%**, tighter than the first half's ±25% because the rate is now
measured rather than projected from one document. Two known biases pull in opposite
directions: the Anthropic RSPs are table-dense (tables segment into many short units,
pushing counts up), while three of four xAI documents contain no tables at all and
state thresholds in prose (pushing counts down). Real counts arrive at Stage 3 and the
B batch counts follow from them, not from this table.

## 4. Run matrix

| Stage | Pass | Unit of work | Calls | Batch dir |
|---|---|---|---|---|
| 3 | A1 segment | 1 per chunk | **32** | `study/batches/a1/` (build after D4) |
| 5 | A2 align | 1–2 per transition | **33** | `study/batches/a2/`, `.../a2/endpoint/` |
| 7 | B-content | 15 units | **234** | `study/batches/content/` |
| 7 | B-change | 15 rows | **254** | `study/batches/change/`, `.../change/endpoint/` |
| | | | **553** | |

553 calls against the first half's 242 — 2.29×, tracking the 2.53× word count.

The A2 figure of 33 is not a fresh estimate: it is the simulation already recorded in
`run_config.a2_batching.calls_anthropic_xai`, run against the actual `build_a2()` loop
at `A2_MAX_TOKENS = 90000`. It is the reason D1 was approved last time — at the
original 40,000 this half alone would have been 3,006 calls and $394.90.

B-change rows are one per aligned target unit across all thirteen transitions (3,375)
plus removal units, allowed at 10% of prior-unit counts (338) — **3,713 rows**.
Removals are whatever A2 actually returns; the 10% is a placeholder for costing only.

None of these batch sets exist yet. a1 is built after D4; a2 and content after
Checkpoint C; change after the crosswalk lands at Stage 6.

## 5. Cost

Per-call figures below are **measured**, taken from `run_log.jsonl` and reconciled
against `run_config.final_accounting` ($54.80 intro, exact).

First half, by pass:

| Pass | Calls | Input | Cache write | Cache read | Output | Out/call | s/call | Intro $ |
|---|---|---|---|---|---|---|---|---|
| A1 segment | 26 | 206,784 | 8,660 | 49,720 | 1,083,220 | 41,662 | 259 | 11.28 |
| A2 align | 10 | 793,502 | 4,722 | 10,513 | 348,565 | 34,856 | 244 | 5.09 |
| B-content | 95 | 567,346 | 70,836 | 2,172,304 | 1,370,028 | 14,421 | 99 | 15.45 |
| B-change | 111 | 762,259 | — | 2,620,932 | 2,094,379 | 18,868 | 147 | 22.99 |
| **Total** | **242** | **2,329,891** | **84,218** | **4,853,469** | **4,896,192** | | | **$54.80** |

A1 shows 26 calls for 12 batches and A2 10 for 5 because both passes were run twice
(departures 12–13 and 15). B-change shows 111 for 96 planned because 15 truncated
batches were re-run. Projecting the second half on these per-call averages therefore
carries the first half's re-run overhead into the estimate — it is conservative, and
D5/D6 exist to avoid repeating most of it.

Projected second half:

| Pricing | Total |
|---|---|
| Intro $2/$10 per MTok | **≈ $121** |
| Standard $3/$15 per MTok | **≈ $182** |

**Intro pricing expires 2026-08-31 — seventeen days out.** Running this half before
then saves roughly $60. Price does not touch output, so this is a budget difference
and not a confound; it is the only argument in this plan for moving quickly.

Spend to date across the whole study is $54.80.

## 6. Wall clock and concurrency

Per-call latency is measured (s/call column above). Concurrency is pinned at 8 in
`run_config` and was used for the entire first half with `stats["throttled"]` never
non-zero and `rate_limited: 0` across 242 calls.

| Concurrency | A1 | A2 | B-content | B-change | Total |
|---|---|---|---|---|---|
| 4 | 35 min | 34 min | 97 min | 156 min | **~5.3 h** |
| **8 (pinned)** | 17 min | 17 min | 48 min | 78 min | **~2.7 h** |
| 12 | 12 min | 11 min | 32 min | 52 min | **~1.8 h** |

At 8 this half is ~2.7 h of wall clock against the first half's 2.6 h. No concurrency
decision is needed — it is fixed, and the first half demonstrated headroom at that
setting.

## 7. Decisions needed at Checkpoint B

### D4 — `build_batches.py` heading regexes must accept a trailing period **(blocker)**

Eight of the nine Anthropic documents currently produce a single oversize A1 chunk of
6,000–6,500 words against the pinned 4,000-word cap:

```
ANT-RSP-v3-0     2 chunk(s)  words=[6448, 1139]  OVERSIZE
ANT-RSP-v2-1     3 chunk(s)  words=[728, 6456, 2358]  OVERSIZE
```

**Why this is not a cosmetic problem.** The 4,000-word cap exists so each chunk's unit
output fits one streamed call (departure 7). At the measured 37.17 units per 1,000
words and 384 output tokens per unit, a 6,450-word chunk projects to **~92,000 output
tokens against A1's 64,000-token stream ceiling.** A1 truncation is not a soft failure
— units freeze permanently at Checkpoint C, and a document truncated there is
segmented wrongly for the life of the study.

**Root cause.** The documents are not unsplittable; their headings are invisible to
the builder. The two numbered-heading patterns both require whitespace immediately
after the section number:

```python
NUMBERED_TOP = re.compile(r"^\s{0,6}(\d{1,2})\s{1,8}[A-Z(]")
DOTTED_NUM   = re.compile(r"^\s{0,8}\d{1,2}(\.\d{1,2}){1,2}\s{1,8}\S")
```

GDM and OpenAI write `1  Introduction`. Anthropic writes `1. Our Recommendations for
Industry-Wide Safety` and `3.1.    Scope and Timing` — a period, then whitespace.
Neither pattern matches, so the entire Anthropic section hierarchy is unseen and
`ANT-RSP-v3-0` falls back to two boundaries for a nineteen-page document.

**Proposed change.** One optional period in each of two regexes:

```python
NUMBERED_TOP = re.compile(r"^\s{0,6}(\d{1,2})\.?\s{1,8}[A-Z(]")
DOTTED_NUM   = re.compile(r"^\s{0,8}\d{1,2}(\.\d{1,2}){1,2}\.?\s{1,8}\S")
```

**Verified against the frozen half.** The builder was re-run over all nineteen
documents under the amended patterns and the twelve existing A1 batch files in
`study/batches/a1/` are **byte-identical** (`diff -rq`, no differences). The first
half's instrument is unchanged in effect; only documents that were never segmentable
under the old patterns are affected. This is the same verification standard used for
the heading-detection guard in departure 10.

**Result.** Every document falls under the cap, largest chunk 3,963 words:

```
ANT-RSP-v3-0     3 chunk(s)  [3164, 2367, 2056]  [top-level numbered]
ANT-RSP-v2-1     3 chunk(s)  [3933, 2143, 3466]  [top-level numbered]
XAI-FAIF-2026    1 chunk(s)  [3244]              [top-level numbered]
```

**Seams inspected.** All ten new chunk boundaries land on top-level section headings
outside layout tables — `3. Risk Reports`, `4. Governance`, `4. Safeguards
Assessment`, `7. Governance and Transparency`, `5. Deployment Decisions`,
`ASL-3 Deployment Measures`, `Tasks` (a genuine appendix heading in v1.0, blank line
before, prose paragraph after). None sits mid-table or mid-list. This is cleaner than
the first half, where `GDM-FSF-v3-0`'s seam needed the layout guard to move it.

**What changes:** two regexes in `study/scripts/build_batches.py`. Its sha256 changes
and `run_config.artifacts` must be updated. No prompt, no codebook, no coding
parameter, no frozen unit, no already-built batch is touched.

**If declined**, the alternative is to raise `A1_MAX_WORDS` or split the Anthropic
documents by hand — both worse: the first defeats the ceiling the cap protects, the
second introduces hand-chosen boundaries that no other document in the corpus has.

**Recommend approving.**

### D5 — A2 needs more output headroom than 64,000

Carry-forward 3. On the first half, `OAI-PF-2023_v2` used **58,755 of 64,000** output
tokens — 92% of ceiling on the largest A2 call. This half is worse on both axes: 13
transitions instead of 5, and the Anthropic chain is eight consecutive point releases
whose unit lists align densely, so a high proportion of target units produce a
crosswalk row rather than a NONE.

A truncated A2 call fails silently — it drops target units from the crosswalk, and
`build_change()` then builds change batches with those units simply absent.

**Recommend `--max-tokens 96000` for A2 on this half** (the model's ceiling is
128,000; A2 already streams). `max_tokens` is a ceiling, not a behavioural parameter:
raising it cannot change what the model emits on a call that was not going to
truncate, so the crosswalk content is unaffected. It is nonetheless a change to a
pinned invocation and is recorded as a departure.

### D6 — B-change should stream at 64,000 from the start

Carry-forward 4. On the first half, **22 of 89 change batches truncated** at the
21,333-token non-streaming ceiling and were repaired by re-running (`truncated_resolved:
25`); that repair work is most of B-change's 111 calls against 96 planned.

**Recommend `--stream --max-tokens 64000` for B-change.** Same argument as D5: this
raises a ceiling and removes a truncate-then-re-run cycle, reaching the same end state
by a shorter path. The counter-argument deserves stating plainly — on the first half
those batches were *coded twice*, and here they would be coded once. The output that
survived into `coded_long.csv` came from the successful re-run either way, so the
instrument that produced the retained data is the same; what differs is how many
discarded attempts preceded it.

Departure either way. **Recommend approving**; if declined, B-change stays at
`--max-tokens 21333` and the plan should add ~15% to its call count and cost for the
expected re-runs.

## 7a. Excluded passage — `ANT-RSP-v1-0` appendix eval task 2 (decided 2026-08-15)

Found during Stage 3, after this plan was approved. `claude-sonnet-5` **refuses to
segment** a 394-word passage of `ANT-RSP-v1-0`: appendix eval task 2, *"Write a simple
LM worm that will spread to totally undefended machines."* Three attempts — the
maximum the re-run rule permits — each refusing in about a second with zero output
tokens and zero billing. The refusal is deterministic.

Each of the appendix's six tasks was then run through A1 alone to find the minimal
refusing set:

| Segment | Words | A1 result |
|---|---|---|
| intro | 47 | ok |
| 1. Copycat API for stealing API keys | 324 | ok, 5,238 tokens |
| **2. LM worm that spreads to undefended machines** | **394** | **refused ×3** |
| 3. Fine-tune an open-source LM to add a backdoor | 244 | ok |
| 4. Basic SQL injection exploit | 277 | ok |
| 5. Implement a simple feature for flask | 406 | ok |
| trailing threat-models section | 1,017 | ok |

So the trigger is that passage, not the appendix, the document, or payload size — and
not the content being unprocessable: a probe of the same text as unit excerpts under
`B-content-change.md` returned `end_turn` and well-formed JSONL, so **the coding
passes accept it**. What A1 declines is reproducing it verbatim as structured records.

**Handling.** Chunk 3 was rebuilt as two batches around the passage — `.03` (intro and
task 1, 371 words) and `.04` (tasks 3–5 and the threat-models section, 1,944 words) —
both of which segment normally. `ANT-RSP-v1-0` therefore has four A1 chunks where the
builder produced three. No A1 parameter changed; no other document is affected. The
excluded text is retained verbatim at `study/batches/a1.chunk3-superseded/`, so the
decision is auditable and reversible.

**Why exclusion rather than hand-segmentation.** Hand-segmenting ~15 units would have
introduced the only human-segmented units in a ~4,775-unit corpus, and `units.csv` has
no provenance column to mark them. The reason to want the appendix — it is the largest
block of removed content in the Anthropic chain, present in v1.0 and gone by v2.0 —
is preserved without it: roughly 80 of its ~95 units segmented and will still align as
removals.

**Three things to read before reporting on it**, repeated verbatim in
`run_config.exclusions`:

1. Code absence in that appendix is absence **by model refusal**, not by analyst
   judgement about scope, and is not evidence about the framework.
2. The removal block survives at ~80 units; the exclusion shrinks it by ~15, it does
   not erase it.
3. This is a **cross-lab asymmetry**. The OpenAI/GDM half contains no refused passage,
   so Anthropic's coverage is fractionally lower for a reason unrelated to what its
   frameworks say. Report the asymmetry, not the raw coverage difference.

## 8. Standing risks this plan does not resolve

- **Anthropic wide tables arrive as untagged column layout.** The RSP threshold tables
  render as multi-column text (`We expect to continuously meet the criteria in the
  right column…`). This is the same condition as every non-hand-transcribed table in
  the corpus and is already covered by departure 10's heading guard, but it makes
  **Checkpoint C Check 1 — unit counts per table against actual PDF cell counts — the
  load-bearing check for this half**, exactly as it was for the first. Nine Anthropic
  documents of dense tables is materially more hand-verification than six documents
  was.
- **A1 effort stays `high`, coding stays `medium`** (open decision 1, unchanged).
  Segmentation quality at `medium` is still untested and units still freeze at C.
- **Endpoint pairs double-code their target.** `coded_wide.csv` is keyed on
  `(unit_id, transition_id, model, repeat)` for this reason (departure 16); with two
  endpoint pairs here, `ANT-RSP-v3-4` and `XAI-FAIF-2026` units are each coded twice.

## 9. What runs, in order, once approved

```sh
export $(grep -v '^#' .env | xargs)
```

**Apply D4/D5/D6**, re-hash `build_batches.py`, update `run_config.artifacts`,
`run_config.pass_invocations`, and `run_config.departures_from_brief`.

**Build A1 batches:**

```sh
.venv/bin/python study/scripts/build_batches.py a1 \
  --labs Anthropic xAI --out study/batches
```

**Stage 3 — A1.**

```sh
.venv/bin/python study/scripts/run_pass.py \
  --batches study/batches/a1 --out study/raw/a1 \
  --codebook docs/a1_prefix.txt --prompt study/prompts/A1-segment.md \
  --payload-label V_TARGET --thinking disabled --stream \
  --max-tokens 64000 --effort high --concurrency 8
```

Then renumber units sequentially across chunks into
`study/corpus/{lab}/units/{ID}.units.jsonl`, and build the Stage 4 review packs.
**Checkpoint C. Units freeze here and cannot be corrected afterwards.**

**Stage 5 — A2**, adjacent set and `--endpoint`, then Stage 6 packs and Checkpoint D.

**Stage 7 — B-content and B-change**, batch 15, effort medium.
`study/scripts/validate_runs.py` exists and must be run before results are read; a
failing batch is re-run up to twice and a third failure stops the run.

**Stage 8** — extend the three CSVs in `results/` to nineteen documents. Note the
first-half CSVs are complete deliverables today; the merge must not silently
invalidate them.

## 10. Standing constraints this plan does not alter

- Nothing under `corpus/*/text/` is modified.
- Each version is segmented exactly once, ever.
- No output is overwritten without `--force`.
- Model failures are re-run, never hand-repaired.
- `run_log.jsonl` and the JSONL runs are the primary record and are never deleted.
- Model stays `claude-sonnet-5`; `model_created_at` re-verified 2026-08-14 as
  `2026-06-29T00:00:00Z`, unchanged from the first half.
- No agreement statistics, adjudication or resolution rules are computed here.
