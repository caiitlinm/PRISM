# Stage 6 alignment review — ANT-RSP-v3-2_v3-3

Prior **313** units · target **313** units · **313** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 313 | 100% |
| Aligned to a prior unit | 308 | 98% |
| `prior_unit_id: NONE` | 5 | 2% |
| Removal candidates | 0 | — |
| Prior units serving >1 target (many-to-one) | 3 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v3-2-0067 | 3 | ANT-RSP-v3-3-0066, ANT-RSP-v3-3-0067, ANT-RSP-v3-3-0068 | AI systems with the ability to significantly help threat actors (for e |
| many-to-one | ANT-RSP-v3-2-0106 | 2 | ANT-RSP-v3-3-0108, ANT-RSP-v3-3-0109 | Accomplishing this would likely mean security roughly in line with RAN |
| many-to-one | ANT-RSP-v3-2-0134 | 2 | ANT-RSP-v3-3-0137, ANT-RSP-v3-3-0138 | When we publicly deploy a model that we determine is significantly mor |
| alternates | ANT-RSP-v3-3-0045 | — | chose ANT-RSP-v3-2-0045, also considered ANT-RSP-v3-2-0046 | We use these recommendations as the north star for our risk mitigation |
| alternates | ANT-RSP-v3-3-0101 | — | chose ANT-RSP-v3-2-0097, also considered ANT-RSP-v3-2-0098 | Achieve an "eyes on everything" state for our internal AI development. |
| alternates | ANT-RSP-v3-3-0137 | — | chose ANT-RSP-v3-2-0134, also considered ANT-RSP-v3-2-0135 | Separate from our publication of Risk Reports, we will publish an anal |
| alternates | ANT-RSP-v3-3-0179 | — | chose ANT-RSP-v3-2-0178, also considered ANT-RSP-v3-2-0179 | We will publish a public version of our Risk Report. We will aim to mi |
| alternates | ANT-RSP-v3-3-0197 | — | chose ANT-RSP-v3-2-0197, also considered ANT-RSP-v3-2-0198 | Have significant experience and expertise regarding evaluations for da |
| alternates | ANT-RSP-v3-3-0200 | — | chose ANT-RSP-v3-2-0201, also considered ANT-RSP-v3-2-0202 | Do not have conflicts of interest with respect to Anthropic. At a mini |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.02 | ANT-RSP-v3-3-0067 | That is, a well-resourced team could, using the model, accomplish  | ANT-RSP-v3-2-0067 | AI systems with the ability to significantly help threat actors (f |
| 0.09 | ANT-RSP-v3-3-0068 | In particular, weapons with the potential to cause events with con | ANT-RSP-v3-2-0067 | AI systems with the ability to significantly help threat actors (f |

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| ANT-RSP-v3-3-0069 | Table: Capability/usage thresholds and mitigations | For example, a program with millions of dollars available and support from recen |
| ANT-RSP-v3-3-0070 | Table: Capability/usage thresholds and mitigations | We are focused on the sorts of teams that would be realistic for real-world thre |
| ANT-RSP-v3-3-0071 | Table: Capability/usage thresholds and mitigations | E.g., in a world with access only to the best AI models as of 2023. |
| ANT-RSP-v3-3-0072 | Table: Capability/usage thresholds and mitigations | E.g., hundreds. |
| ANT-RSP-v3-3-0313 | Changelog | May 26, 2026 (RSP v3.3) This update (1) revises our threshold for novel chemical |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**9 of 313 prior units (3%).**

| prior section heading | orphaned units |
|---|---|
| Table: Capability/usage thresholds and mitigations | 3 |
| 1. Our Recommendations for Industry-Wide Safety | 1 |
| 3.1. Scope and Timing | 1 |
| 3.3. Contents | 1 |
| 3.4. Procedures | 1 |
| 3.5. Publication and Redactions | 1 |
| 3.6.1. Selecting external reviewers | 1 |
