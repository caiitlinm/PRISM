# Stage 6 alignment review — ANT-RSP-v3-0_v3-1

Prior **278** units · target **301** units · **301** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 301 | 100% |
| Aligned to a prior unit | 291 | 97% |
| `prior_unit_id: NONE` | 10 | 3% |
| Removal candidates | 0 | — |
| Prior units serving >1 target (many-to-one) | 22 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v3-0-0001 | 2 | ANT-RSP-v3-1-0001, ANT-RSP-v3-1-0002 | Our Responsible Scaling Policy (RSP) is our voluntary framework for ma |
| many-to-one | ANT-RSP-v3-0-0002 | 2 | ANT-RSP-v3-1-0003, ANT-RSP-v3-1-0004 | We have always intended for our RSP to be a living document. We will c |
| many-to-one | ANT-RSP-v3-0-0005 | 2 | ANT-RSP-v3-1-0007, ANT-RSP-v3-1-0008 | We lay this out in a table that maps capability thresholds to the miti |
| many-to-one | ANT-RSP-v3-0-0006 | 2 | ANT-RSP-v3-1-0009, ANT-RSP-v3-1-0010 | This approach represents a change from our previous RSP, driven by a c |
| many-to-one | ANT-RSP-v3-0-0008 | 2 | ANT-RSP-v3-1-0012, ANT-RSP-v3-1-0013 | But from a societal perspective, what matters is the risk to the ecosy |
| many-to-one | ANT-RSP-v3-0-0011 | 2 | ANT-RSP-v3-1-0016, ANT-RSP-v3-1-0017 | We aspire to advance the latter through a mixture of example-setting,  |
| many-to-one | ANT-RSP-v3-0-0012 | 2 | ANT-RSP-v3-1-0018, ANT-RSP-v3-1-0019 | Frontier Safety Roadmaps are a new requirement under our RSP. These wi |
| many-to-one | ANT-RSP-v3-0-0021 | 2 | ANT-RSP-v3-1-0028, ANT-RSP-v3-1-0029 | Our RSP is only one part of our overall approach to safety. For instan |
| many-to-one | ANT-RSP-v3-0-0022 | 2 | ANT-RSP-v3-1-0030, ANT-RSP-v3-1-0031 | Further, the RSP may serve some regulatory requirements, but it is not |
| many-to-one | ANT-RSP-v3-0-0024 | 2 | ANT-RSP-v3-1-0033, ANT-RSP-v3-1-0034 | "Catastrophic risk" as used in our RSP refers generally to risks of th |
| many-to-one | ANT-RSP-v3-0-0026 | 2 | ANT-RSP-v3-1-0036, ANT-RSP-v3-1-0037 | This section outlines our recommendations for what it would take, at a |
| many-to-one | ANT-RSP-v3-0-0027 | 2 | ANT-RSP-v3-1-0038, ANT-RSP-v3-1-0039 | The left column identifies capability thresholds that would call for h |
| many-to-one | ANT-RSP-v3-0-0030 | 2 | ANT-RSP-v3-1-0042, ANT-RSP-v3-1-0043 | In particular, we cannot unilaterally and unconditionally commit to st |
| many-to-one | ANT-RSP-v3-0-0031 | 2 | ANT-RSP-v3-1-0044, ANT-RSP-v3-1-0045 | We use these recommendations as the north star for our risk mitigation |
| many-to-one | ANT-RSP-v3-0-0035 | 2 | ANT-RSP-v3-1-0049, ANT-RSP-v3-1-0050 | This leaves flexibility in how risk thresholds are evaluated and how s |
| many-to-one | ANT-RSP-v3-0-0039 | 2 | ANT-RSP-v3-1-0054, ANT-RSP-v3-1-0055 | We expect that the recommendations for industry-wide safety will evolv |
| many-to-one | ANT-RSP-v3-0-0071 | 2 | ANT-RSP-v3-1-0087, ANT-RSP-v3-1-0088 | Our working operationalization is to trigger this risk threshold at th |
| many-to-one | ANT-RSP-v3-0-0072 | 2 | ANT-RSP-v3-1-0089, ANT-RSP-v3-1-0090 | This capability threshold is intended to reflect our definition of hig |
| many-to-one | ANT-RSP-v3-0-0084 | 2 | ANT-RSP-v3-1-0104, ANT-RSP-v3-1-0105 | Even malicious employees and other insiders with maximal levels of acc |
| many-to-one | ANT-RSP-v3-0-0090 | 2 | ANT-RSP-v3-1-0111, ANT-RSP-v3-1-0112 | Maintaining and reporting on this Roadmap is part of our work under th |
| many-to-one | ANT-RSP-v3-0-0092 | 2 | ANT-RSP-v3-1-0114, ANT-RSP-v3-1-0115 | Our Frontier Safety Roadmap is subject to change. Some changes may sim |
| many-to-one | ANT-RSP-v3-0-0096 | 2 | ANT-RSP-v3-1-0119, ANT-RSP-v3-1-0120 | Our current Frontier Safety Roadmap is available at anthropic.com/resp |
| alternates | ANT-RSP-v3-1-0186 | — | chose ANT-RSP-v3-0-0162, also considered ANT-RSP-v3-0-0163, ANT-RSP-v3-0-0164 | A model is "highly capable" if we conclude that it crosses the thresho |
| alternates | ANT-RSP-v3-1-0196 | — | chose ANT-RSP-v3-0-0174, also considered ANT-RSP-v3-0-0173 | At a minimum, a reviewing organization itself may not have a financial |
| alternates | ANT-RSP-v3-1-0219 | — | chose ANT-RSP-v3-0-0197, also considered ANT-RSP-v3-0-0198, ANT-RSP-v3-0-0199 | (1) as needed, proposing updates to this policy; (2) approving relevan |
| alternates | ANT-RSP-v3-1-0220 | — | chose ANT-RSP-v3-0-0200, also considered ANT-RSP-v3-0-0201, ANT-RSP-v3-0-0202 | (4) overseeing the implementation of this policy, including the alloca |
| alternates | ANT-RSP-v3-1-0256 | — | chose ANT-RSP-v3-0-0237, also considered ANT-RSP-v3-0-0238 | ASL definition changed: The term "ASL" now refers to groups of technic |
| alternates | ANT-RSP-v3-1-0296 | — | chose ANT-RSP-v3-0-0277, also considered ANT-RSP-v3-0-0278 | This update is a comprehensive rewrite of our RSP. For a summary of ch |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.02 | ANT-RSP-v3-1-0088 | We would consider scenario (2) to have occurred where (a) we obser | ANT-RSP-v3-0-0071 | Our working operationalization is to trigger this risk threshold a |
| 0.08 | ANT-RSP-v3-1-0087 | We will consider this threshold to be met if we determine that eit | ANT-RSP-v3-0-0071 | Our working operationalization is to trigger this risk threshold a |

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| ANT-RSP-v3-1-0166 | 3.4. Procedures | We may also use this feedback to improve or refine the report itself. |
| ANT-RSP-v3-1-0238 | Appendix A: Commitments Related to Competitors | Further, the commitments below do not preclude us from taking cautionary action, |
| ANT-RSP-v3-1-0239 | Appendix A: Commitments Related to Competitors | Mitigating the risks from our models is a top priority for us, and we would stro |
| ANT-RSP-v3-1-0297 | Changelog | This revision addresses the following points: (1) how we operationalize the Auto |
| ANT-RSP-v3-1-0298 | Changelog | These changes are mostly clarificatory in nature; we don't see them as significa |
| ANT-RSP-v3-1-0299 | Changelog | Change (1) reflects further discussion of our operationalization of the capabili |
| ANT-RSP-v3-1-0300 | Changelog | This update also includes minor edits for style or clarity. |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**9 of 278 prior units (3%).**

| prior section heading | orphaned units |
|---|---|
| 4. Governance | 4 |
| 3.6. External Review | 2 |
| 1. Our Recommendations for Industry-Wide Safety | 1 |
| 3.3. Contents | 1 |
| Changelog | 1 |
