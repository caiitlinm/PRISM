# Stage 6 alignment review — ANT-RSP-v3-3_v3-4

Prior **313** units · target **334** units · **334** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 334 | 100% |
| Aligned to a prior unit | 322 | 96% |
| `prior_unit_id: NONE` | 12 | 4% |
| Removal candidates | 0 | — |
| Prior units serving >1 target (many-to-one) | 14 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v3-3-0179 | 3 | ANT-RSP-v3-4-0185, ANT-RSP-v3-4-0186, ANT-RSP-v3-4-0332 | We will publish a public version of our Risk Report. We will aim to mi |
| many-to-one | ANT-RSP-v3-3-0045 | 2 | ANT-RSP-v3-4-0045, ANT-RSP-v3-4-0046 | We use these recommendations as the north star for our risk mitigation |
| many-to-one | ANT-RSP-v3-3-0065 | 2 | ANT-RSP-v3-4-0066, ANT-RSP-v3-4-0067 | This column summarizes commitments drawn from other sections of this p |
| many-to-one | ANT-RSP-v3-3-0094 | 2 | ANT-RSP-v3-4-0096, ANT-RSP-v3-4-0097 | We would consider scenario (2) to have occurred where (a) we observe o |
| many-to-one | ANT-RSP-v3-3-0101 | 2 | ANT-RSP-v3-4-0102, ANT-RSP-v3-4-0103 | Achieve an "eyes on everything" state for our internal AI development. |
| many-to-one | ANT-RSP-v3-3-0106 | 2 | ANT-RSP-v3-4-0108, ANT-RSP-v3-4-0109 | A frontier developer should make a strong argument that: No user or te |
| many-to-one | ANT-RSP-v3-3-0130 | 2 | ANT-RSP-v3-4-0136, ANT-RSP-v3-4-0330 | A Risk Report will cover all publicly deployed models at the time of i |
| many-to-one | ANT-RSP-v3-3-0136 | 2 | ANT-RSP-v3-4-0142, ANT-RSP-v3-4-0331 | Note that unlike system cards, Risk Reports will not be published with |
| many-to-one | ANT-RSP-v3-3-0186 | 2 | ANT-RSP-v3-4-0194, ANT-RSP-v3-4-0333 | This means working with one or more third-party organizations that wil |
| many-to-one | ANT-RSP-v3-3-0197 | 2 | ANT-RSP-v3-4-0205, ANT-RSP-v3-4-0206 | Have significant experience and expertise regarding evaluations for da |
| many-to-one | ANT-RSP-v3-3-0232 | 2 | ANT-RSP-v3-4-0238, ANT-RSP-v3-4-0239 | Internal transparency: We will share final, unredacted Risk Reports wi |
| many-to-one | ANT-RSP-v3-3-0281 | 2 | ANT-RSP-v3-4-0288, ANT-RSP-v3-4-0289 | Less prescriptive evaluation methodology: We have replaced some specif |
| many-to-one | ANT-RSP-v3-3-0296 | 2 | ANT-RSP-v3-4-0304, ANT-RSP-v3-4-0305 | These include expanding the duties of the Responsible Scaling Officer; |
| many-to-one | ANT-RSP-v3-3-0305 | 2 | ANT-RSP-v3-4-0314, ANT-RSP-v3-4-0315 | The model capabilities and threat models corresponding with the ASL-3  |
| alternates | ANT-RSP-v3-4-0111 | — | chose ANT-RSP-v3-3-0108, also considered ANT-RSP-v3-3-0109 | Accomplishing this would likely mean security roughly in line with RAN |
| alternates | ANT-RSP-v3-4-0137 | — | chose ANT-RSP-v3-3-0131, also considered ANT-RSP-v3-3-0130 | It will cover all publicly deployed models as of the coverage date, as |
| alternates | ANT-RSP-v3-4-0153 | — | chose ANT-RSP-v3-3-0146, also considered ANT-RSP-v3-3-0147 | We will describe how we identify, evaluate, and mitigate catastrophic  |
| alternates | ANT-RSP-v3-4-0235 | — | chose ANT-RSP-v3-3-0225, also considered ANT-RSP-v3-3-0226, ANT-RSP-v3-3-0227 | (1) as needed, proposing updates to this policy; (2) approving relevan |
| alternates | ANT-RSP-v3-4-0236 | — | chose ANT-RSP-v3-3-0228, also considered ANT-RSP-v3-3-0229, ANT-RSP-v3-3-0230 | (4) overseeing the implementation of this policy, including the alloca |
| alternates | ANT-RSP-v3-4-0267 | — | chose ANT-RSP-v3-3-0260, also considered ANT-RSP-v3-3-0261 | Earlier editions of our RSP defined "AI Safety Levels" with specific l |
| alternates | ANT-RSP-v3-4-0269 | — | chose ANT-RSP-v3-3-0261, also considered ANT-RSP-v3-3-0262 | (For example, our initial Risk Report uses this distinction.) However, |
| alternates | ANT-RSP-v3-4-0331 | — | chose ANT-RSP-v3-3-0136, also considered ANT-RSP-v3-3-0130 | We aim to hold our Risk Reports to a higher standard of thoroughness a |
| alternates | ANT-RSP-v3-4-0332 | — | chose ANT-RSP-v3-3-0179, also considered ANT-RSP-v3-3-0180 | It requires us to publicly disclose, at a high level, when we make red |
| alternates | ANT-RSP-v3-4-0333 | — | chose ANT-RSP-v3-3-0186, also considered ANT-RSP-v3-3-0196,ANT-RSP-v3-3-0203 | It clarifies that external review of our Risk Reports can involve mult |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

Nothing flagged.

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| ANT-RSP-v3-4-0145 | 3.1. Scope and Timing | A Risk Report may include information about Anthropic's models and risk prepared |
| ANT-RSP-v3-4-0192 | 3.5. Publication and Redactions | We will disclose the existence of each redaction made in the public version of t |
| ANT-RSP-v3-4-0215 | 3.6.2. Timing and access | All sections of the Risk Report will be shared with at least one external review |
| ANT-RSP-v3-4-0324 | Changelog | This update makes five changes: |
| ANT-RSP-v3-4-0325 | Changelog | It revises the Automated R&D capability threshold in light of further issues tha |
| ANT-RSP-v3-4-0326 | Changelog | We would not: in this case there could be a strong argument for expecting the tr |
| ANT-RSP-v3-4-0327 | Changelog | This threshold is intended to capture the onset of dramatic recursive self-impro |
| ANT-RSP-v3-4-0328 | Changelog | It now requires that fully unredacted Risk Reports be shared with at least 200 A |
| ANT-RSP-v3-4-0329 | Changelog | We will continue to share minimally-redacted Risk Reports with this latter group |
| ANT-RSP-v3-4-0334 | Changelog | It also contains minor typo and formatting corrections. |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**6 of 313 prior units (2%).**

| prior section heading | orphaned units |
|---|---|
| 4. Governance | 4 |
| Table: Capability/usage thresholds and mitigations | 1 |
| 3.3. Contents | 1 |
