# Run plan — OpenAI and Google DeepMind

Stage 2 deliverable. Written 2026-08-14 against `manifest.jsonl`, the frozen
artifacts in `run_config.json`, and the Stage 1.6 measurements in `run_log.jsonl`.

Anthropic and xAI run later under the identical configuration. Where a choice in
this plan constrains that later run, it is called out.

**This plan is not approved. Three decisions are listed at the end and one of them
changes a pinned constant. Nothing runs until Checkpoint B clears.**

---

## 1. Scope

Six documents, two labs, from the nineteen in `manifest.jsonl`.

| Identifier | Lab | Version | Date | Pages | Words | A1 chunks |
|---|---|---|---|---|---|---|
| OAI-PF-2023 | OpenAI | none ("Beta") | 2023-12-18 | 27 | 6,623 | 2 |
| OAI-PF-v2 | OpenAI | Version 2 | 2025-04-15 | 22 | 9,674 | 3 |
| GDM-FSF-v1-0 | Google DeepMind | Version 1.0 | 2024-05-17 | 7 | 2,836 | 1 |
| GDM-FSF-v2-0 | Google DeepMind | Version 2.0 | 2025-02-04 | 9 | 3,684 | 1 |
| GDM-FSF-v3-0 | Google DeepMind | Version 3.0 | 2025-09-22 | 16 | 5,827 | 2 |
| GDM-FSF-v3-1 | Google DeepMind | Version 3.1 | 2026-04-17 | 20 | 7,705 | 3 |
| | | | | **101** | **36,349** | **12** |

Words are `.clean.txt`, which is what `build_batches.text_path()` reads.
`OAI-PF-2023` carries a hand-transcribed page 15; its page 6 scorecard is
excluded by analyst decision (see `study/review-protocol.md`).

## 2. Chains

`chains()` builds adjacent pairs per lab in manifest order, plus the endpoint pair
only where a lab has more than two documents. OpenAI has two, so its adjacent pair
*is* its endpoint pair and no separate endpoint run exists.

| Transition ID | Prior → target | Kind |
|---|---|---|
| `OAI-PF-2023_v2` | OAI-PF-2023 → OAI-PF-v2 | adjacent (also the endpoint) |
| `GDM-FSF-v1-0_v2-0` | GDM-FSF-v1-0 → GDM-FSF-v2-0 | adjacent |
| `GDM-FSF-v2-0_v3-0` | GDM-FSF-v2-0 → GDM-FSF-v3-0 | adjacent |
| `GDM-FSF-v3-0_v3-1` | GDM-FSF-v3-0 → GDM-FSF-v3-1 | adjacent |
| `GDM-FSF-v1-0_v3-1` | GDM-FSF-v1-0 → GDM-FSF-v3-1 | endpoint |

Four adjacent, one endpoint. The endpoint pair needs `--endpoint` on both
`build_batches.py` and the crosswalk path, and lands in `study/batches/a2/endpoint/`
and `study/batches/change/endpoint/`.

## 3. Unit estimate

Every downstream count depends on this and **none of it is measured yet except one
document.** A1 on GDM-FSF-v1-0 returned 111 units from 2,836 words — 39.1 units per
1,000 words. That single figure is projected across the rest.

| Document | Words | Est. units |
|---|---|---|
| OAI-PF-2023 | 6,623 | 259 |
| OAI-PF-v2 | 9,674 | 378 |
| GDM-FSF-v1-0 | 2,836 | **111 (measured)** |
| GDM-FSF-v2-0 | 3,684 | 144 |
| GDM-FSF-v3-0 | 5,827 | 228 |
| GDM-FSF-v3-1 | 7,705 | 301 |
| | | **1,421** |

GDM-FSF-v1-0 is the shortest and least tabular document in the corpus. OAI-PF-v2 is
the most table-dense, and tables segment into many short units, so 378 may be low.
**Treat every count and cost below as ±25% until Checkpoint C.** Real counts arrive
at Stage 3 and the B batch counts follow from them, not from this table.

## 4. Run matrix

| Stage | Pass | Unit of work | Calls | Batch dir |
|---|---|---|---|---|
| 3 | A1 segment | 1 per chunk | **12** | `study/batches/a1/` (built) |
| 5 | A2 align | 1–2 per transition | **7** | `study/batches/a2/`, `.../a2/endpoint/` |
| 7 | B-content | 15 units | **95** | `study/batches/content/` |
| 7 | B-change | 15 rows | **96** | `study/batches/change/`, `.../change/endpoint/` |
| | | | **210** | |

B-change rows are one per aligned target unit across all five transitions (1,352)
plus removal units, allowed at 10% of prior-unit counts (85). Removals are whatever
A2 actually returns; the 10% is a placeholder for costing only.

Only the A1 batches exist today. The other three sets are built after their inputs
freeze — a2 after Checkpoint C, content after Checkpoint C, change after the
crosswalk lands at Stage 6.

## 5. Cost

Measured per-call figures from `run_log.jsonl`, not estimates: a 15-unit B-content
call at effort medium used 5,829 uncached input, 23,612 cached read and 15,377
output tokens in 111.3 s and stopped on `end_turn`. A1 on GDM-FSF-v1-0 used 7,291
input and 42,593 output for 111 units — 384 output tokens per unit.

| Pass | Calls | Input | Cache write | Cache read | Output | Intro $ | Standard $ |
|---|---|---|---|---|---|---|---|
| A1 segment | 12 | 86,659 | — | — | 545,267 | 5.63 | 8.44 |
| A2 align | 7 | 500,712 | 23,612 | 141,672 | 81,120 | 1.90 | 2.85 |
| B-content | 95 | 553,755 | 23,612 | 2,219,528 | 1,460,815 | 16.22 | 24.33 |
| B-change | 96 | 839,376 | 23,612 | 2,243,140 | 1,476,192 | 16.95 | 25.42 |
| **Total** | **210** | **1,980,502** | **70,836** | **4,604,340** | **3,563,394** | **$40.70** | **$61.04** |

Intro pricing is $2/$10 per MTok and **expires 2026-08-31** — seventeen days out.
Standard is $3/$15. Cache write bills at 1.25× input, cache read at 0.1×.

Two consequences worth stating plainly. Running this half before 31 August saves
about $20. And the Anthropic/xAI half will almost certainly bill at standard rates —
that is a budget difference, not a confound, since price does not touch output.

Spend to date is $3.60, all calibration.

## 6. Wall clock and concurrency

Per-call latency measured: 111.3 s for a B call, 264.8 s for the largest A1 call.
The B passes are 191 of the 210 calls and dominate everything.

| Concurrency | A1 | A2 | B | Total |
|---|---|---|---|---|
| 4 | 14 min | ~6 min | 89 min | **~1.8 h** |
| 8 | 7 min | ~6 min | 44 min | **~1.0 h** |
| 12 | 5 min | ~6 min | 30 min | **~0.7 h** |

A2 barely moves because it is 7 calls that all run at once.

Rate limits have not been tested — every calibration call ran at concurrency 1, and
`stats["throttled"]` has never been non-zero. Overshooting is recoverable rather
than fatal: `run_pass.py` honours a `retry-after` header when the server sends one,
falls back to exponential backoff with jitter, ramps workers 3 s apart to dodge
acceleration limits, and resumes on rerun because a batch with an existing output
file is skipped. **Recommend starting at 8.** If 429s appear in the first minute,
kill it and restart at 4; the completed batches are kept.

## 7. Decisions needed at Checkpoint B

### D1 — `A2_MAX_TOKENS` must change from 40,000 to 90,000

This is the one finding in Stage 2 that is not a formality.

`build_a2()` puts the entire prior-version unit list in a header repeated on every
batch, then fills each batch with target units up to `A2_MAX_TOKENS`. At an
estimated 186 tokens per unit record, the header alone is 48,174 tokens for
OAI-PF-2023 and 42,408 for GDM-FSF-v3-0 — **larger than the whole 40,000-token
budget.** When that happens the loop flushes after every single target unit, so each
call carries a 48,000-token header to align one unit.

Simulated against the actual loop:

| `A2_MAX_TOKENS` | This run: calls | Input tokens | Intro $ | Later half: calls | Intro $ |
|---|---|---|---|---|---|
| **40,000 (current)** | 688 | 31,436,418 | **63.68** | 3,006 | **394.90** |
| 60,000 | 15 | 825,654 | 2.46 | 1,840 | 262.48 |
| **90,000 (proposed)** | **7** | **500,712** | **1.81** | **33** | **7.56** |
| 120,000 | 5 | 410,130 | 1.63 | 19 | 5.63 |

Left at 40,000 the alignment pass costs more than the rest of the study combined and
still produces the same crosswalk. The later Anthropic/xAI half is worse — nine RSP
versions give bigger prior-unit headers, and A2 alone would run to $395.

90,000 rather than 120,000 because the marginal saving is $0.18 and 90,000 keeps
more transitions off the single-call extreme, which matters for D2.

**What changes:** one constant in `study/scripts/build_batches.py`. Its sha256
changes and `run_config.json` must be updated. No prompt, no codebook, no coding
parameter, no already-built batch is touched — the a1 batches are unaffected. The
later labs must use 90,000 as well.

### D2 — A2 needs `--stream --max-tokens 64000`

At 90,000 the largest A2 call emits 301 crosswalk rows. A row is about 43 tokens of
text, but **thinking tokens per A2 row have never been measured** — the only figure
in hand is the B pass, where thinking was 57% of output.

| Tokens per row | Largest A2 call | Fits `--max-tokens 21333`? |
|---|---|---|
| 60 | 18,060 | yes, 15% headroom |
| 100 | 30,100 | no |
| 150 | 45,150 | no |

The currently pinned A2 invocation is `--max-tokens 21333 --effort medium`, no
streaming. That survives only the optimistic column. Streaming at 64,000 covers all
three and costs nothing — it is the same configuration A1 already runs under, and
`run_pass.py` supports it today.

Recommend `--payload-label ALIGNMENT_BATCH --stream --max-tokens 64000 --effort medium`.
A truncated A2 call is not a soft failure: it silently drops target units from the
crosswalk, and `build_change()` would then build change batches with the missing
units simply absent.

### D3 — does A2 get the codebook, or a stable prefix?

Not a cost question — either way it is under a dollar. It is a contamination
question and I do not have a rule for it.

A1 was deliberately given `docs/a1_prefix.txt` instead of the codebook, so that unit
boundaries could not be shaped by which codes exist. The same argument applies to
alignment: the crosswalk decides which units receive change codes at all, and an
aligner that knows the code set could align so as to make codes fireable. But the
brief pins "codebook as the cached prefix", A1 is already a recorded departure from
that, and a second one is the analyst's call rather than mine.

`run_pass.py` defaults `--codebook` to the codebook, so **doing nothing means A2
sees it.** Recommend an `a2_prefix.txt` on the A1 precedent, but this needs a
ruling either way, and it must hold for the later labs.

---

## 8. What runs, in order, once approved

```sh
export $(grep -v '^#' .env | xargs)
```

**Stage 3 — A1.** Batches already built.

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

**Stage 5 — A2**, both the adjacent set and `--endpoint`, then the Stage 6 review
packs and Checkpoint D.

**Stage 7 — B-content and B-change**, batch 15, effort medium, `--max-tokens 21333`.
`scripts/validate_runs.py` does not exist and must be written before this stage; a
failing batch is re-run up to twice and a third failure stops the run.

## 9. Standing constraints this plan does not alter

- Nothing under `corpus/*/text/` is modified.
- Each version is segmented exactly once, ever.
- No output is overwritten without `--force`.
- Model failures are re-run, never hand-repaired.
- `run_log.jsonl` and the JSONL runs are the primary record and are never deleted.
- No agreement statistics, adjudication or resolution rules are computed here.
