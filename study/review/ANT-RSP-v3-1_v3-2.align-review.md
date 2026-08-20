# Stage 6 alignment review — ANT-RSP-v3-1_v3-2

Prior **301** units · target **313** units · **313** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 313 | 100% |
| Aligned to a prior unit | 309 | 99% |
| `prior_unit_id: NONE` | 4 | 1% |
| Removal candidates | 0 | — |
| Prior units serving >1 target (many-to-one) | 7 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v3-1-0219 | 3 | ANT-RSP-v3-2-0226, ANT-RSP-v3-2-0227, ANT-RSP-v3-2-0228 | (1) as needed, proposing updates to this policy; (2) approving relevan |
| many-to-one | ANT-RSP-v3-1-0220 | 3 | ANT-RSP-v3-2-0229, ANT-RSP-v3-2-0230, ANT-RSP-v3-2-0231 | (4) overseeing the implementation of this policy, including the alloca |
| many-to-one | ANT-RSP-v3-1-0022 | 2 | ANT-RSP-v3-2-0022, ANT-RSP-v3-2-0023 | Risk Reports are another new requirement. Risk Reports will provide de |
| many-to-one | ANT-RSP-v3-1-0094 | 2 | ANT-RSP-v3-2-0095, ANT-RSP-v3-2-0096 | Resource and complete significant "moonshot R&D for security" projects |
| many-to-one | ANT-RSP-v3-1-0095 | 2 | ANT-RSP-v3-2-0097, ANT-RSP-v3-2-0098 | Achieve an "eyes on everything" state for our internal AI development. |
| many-to-one | ANT-RSP-v3-1-0100 | 2 | ANT-RSP-v3-2-0103, ANT-RSP-v3-2-0104 | A frontier developer should make a strong argument that: No user or te |
| many-to-one | ANT-RSP-v3-1-0146 | 2 | ANT-RSP-v3-2-0150, ANT-RSP-v3-2-0151 | Risk analyses. We will provide our reasoning and conclusions regarding |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | ANT-RSP-v3-2-0095 | We will: | ANT-RSP-v3-1-0094 | Resource and complete significant "moonshot R&D for security" proj |
| 0.08 | ANT-RSP-v3-2-0151 | Our analyses will include: | ANT-RSP-v3-1-0146 | Risk analyses. We will provide our reasoning and conclusions regar |

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| ANT-RSP-v3-2-0195 | 3.6. External Review | In addition, upon the LTBT's request, we will conduct a public or private extern |
| ANT-RSP-v3-2-0203 | 3.6.1. Selecting external reviewers | In selecting external reviewers, we will consult with the Board and obtain the a |
| ANT-RSP-v3-2-0232 | 4. Governance | Long Term Benefit Trust: We will regularly brief the LTBT on plans and developme |
| ANT-RSP-v3-2-0313 | Changelog | This update authorizes the LTBT to request external review of Risk Reports, give |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**1 of 301 prior units (0%).**

| prior section heading | orphaned units |
|---|---|
| Changelog | 1 |
