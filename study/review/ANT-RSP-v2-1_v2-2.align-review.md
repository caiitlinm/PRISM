# Stage 6 alignment review — ANT-RSP-v2-1_v2-2

Prior **322** units · target **348** units · **403** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 348 | 100% |
| Aligned to a prior unit | 345 | 99% |
| `prior_unit_id: NONE` | 3 | 1% |
| Removal candidates | 55 | — |
| Prior units serving >1 target (many-to-one) | 26 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v2-1-0175 | 4 | ANT-RSP-v2-2-0192, ANT-RSP-v2-2-0193, ANT-RSP-v2-2-0194, ANT-RSP-v2-2-0345 | We will implement robust insider risk controls to mitigate most inside |
| many-to-one | ANT-RSP-v2-1-0002 | 2 | ANT-RSP-v2-2-0002, ANT-RSP-v2-2-0003 | We are now updating our RSP to account for the lessons we've learned o |
| many-to-one | ANT-RSP-v2-1-0003 | 2 | ANT-RSP-v2-2-0004, ANT-RSP-v2-2-0005 | Background. AI Safety Level Standards (ASL Standards) are a set of tec |
| many-to-one | ANT-RSP-v2-1-0004 | 2 | ANT-RSP-v2-2-0006, ANT-RSP-v2-2-0007 | As model capabilities increase, so will the need for stronger safeguar |
| many-to-one | ANT-RSP-v2-1-0005 | 2 | ANT-RSP-v2-2-0008, ANT-RSP-v2-2-0009 | To determine when a model has become sufficiently advanced such that i |
| many-to-one | ANT-RSP-v2-1-0009 | 2 | ANT-RSP-v2-2-0013, ANT-RSP-v2-2-0014 | We will first conduct preliminary assessments to determine whether a m |
| many-to-one | ANT-RSP-v2-1-0011 | 2 | ANT-RSP-v2-2-0016, ANT-RSP-v2-2-0017 | If, however, we are unable to make the required showing, we will act a |
| many-to-one | ANT-RSP-v2-1-0013 | 2 | ANT-RSP-v2-2-0019, ANT-RSP-v2-2-0020 | For the ASL-3 Deployment Standard, we will evaluate whether it is robu |
| many-to-one | ANT-RSP-v2-1-0021 | 2 | ANT-RSP-v2-2-0028, ANT-RSP-v2-2-0029 | As frontier AI models advance, we believe they will bring about transf |
| many-to-one | ANT-RSP-v2-1-0026 | 2 | ANT-RSP-v2-2-0034, ANT-RSP-v2-2-0035 | We are now updating our RSP to account for the lessons we've learned o |
| many-to-one | ANT-RSP-v2-1-0031 | 2 | ANT-RSP-v2-2-0040, ANT-RSP-v2-2-0041 | We will thus regularly measure the capability of our models and adjust |
| many-to-one | ANT-RSP-v2-1-0035 | 2 | ANT-RSP-v2-2-0045, ANT-RSP-v2-2-0046 | In the long term, we hope that our policy may offer relevant insights  |
| many-to-one | ANT-RSP-v2-1-0038 | 2 | ANT-RSP-v2-2-0049, ANT-RSP-v2-2-0050 | Further, we conduct research to understand the broader societal impact |
| many-to-one | ANT-RSP-v2-1-0039 | 2 | ANT-RSP-v2-2-0051, ANT-RSP-v2-2-0052 | At Anthropic, we are committed to developing AI responsibly and transp |
| many-to-one | ANT-RSP-v2-1-0044 | 2 | ANT-RSP-v2-2-0057, ANT-RSP-v2-2-0058 | We actively welcome feedback on our policy and suggestions for improve |
| many-to-one | ANT-RSP-v2-1-0046 | 2 | ANT-RSP-v2-2-0060, ANT-RSP-v2-2-0061 | As model capabilities increase, so will the need for stronger safeguar |
| many-to-one | ANT-RSP-v2-1-0064 | 2 | ANT-RSP-v2-2-0079, ANT-RSP-v2-2-0080 | In developing these standards, we have weighed the risks and benefits  |
| many-to-one | ANT-RSP-v2-1-0065 | 2 | ANT-RSP-v2-2-0081, ANT-RSP-v2-2-0082 | We will conduct assessments to inform when to implement the Required S |
| many-to-one | ANT-RSP-v2-1-0072 | 2 | ANT-RSP-v2-2-0089, ANT-RSP-v2-2-0090 | The ASL-3 Security Standard is required. In addition, we will develop  |
| many-to-one | ANT-RSP-v2-1-0077 | 2 | ANT-RSP-v2-2-0095, ANT-RSP-v2-2-0096 | These Capability Thresholds represent our current understanding of the |
| many-to-one | ANT-RSP-v2-1-0092 | 2 | ANT-RSP-v2-2-0110, ANT-RSP-v2-2-0111 | We will conduct either pre- or post-deployment testing, including spec |
| many-to-one | ANT-RSP-v2-1-0152 | 2 | ANT-RSP-v2-2-0171, ANT-RSP-v2-2-0172 | Trusted users: Establish criteria for determining when it may be appro |
| many-to-one | ANT-RSP-v2-1-0210 | 2 | ANT-RSP-v2-2-0229, ANT-RSP-v2-2-0230 | (4) overseeing implementation of this policy, including the allocation |
| many-to-one | ANT-RSP-v2-1-0218 | 2 | ANT-RSP-v2-2-0238, ANT-RSP-v2-2-0239 | Further, we will track and investigate any reported or otherwise ident |
| many-to-one | ANT-RSP-v2-1-0269 | 2 | ANT-RSP-v2-2-0289, ANT-RSP-v2-2-0290 | External validation like SOC 2 compliance and continuous vulnerability |
| many-to-one | ANT-RSP-v2-1-0312 | 2 | ANT-RSP-v2-2-0333, ANT-RSP-v2-2-0334 | For any general access systems, we still require passing intensive red |
| alternates | ANT-RSP-v2-2-0101 | — | chose ANT-RSP-v2-1-0082, also considered ANT-RSP-v2-1-0083 | (2) share an update on our progress around that time; and (3) begin te |
| alternates | ANT-RSP-v2-2-0248 | — | chose ANT-RSP-v2-1-0230, also considered ANT-RSP-v2-1-0231 | Public disclosures: We will publicly release key information related t |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.07 | ANT-RSP-v2-2-0193 | We define "basic insider risk" as risk from an insider who does no | ANT-RSP-v2-1-0175 | We will implement robust insider risk controls to mitigate most in |

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

| target | target excerpt | named alternate | that unit's excerpt |
|---|---|---|---|
| ANT-RSP-v2-2-0346 | The model capabilities and threat models corresponding with the  | ANT-RSP-v2-1-0175, ANT-RSP | We will implement robust insider risk controls to mitigate most  |
| ANT-RSP-v2-2-0347 | and the relatively small number of employees who might be capabl | ANT-RSP-v2-1-0175 | We will implement robust insider risk controls to mitigate most  |
| ANT-RSP-v2-2-0348 | For AI R&D-4, the threat models generally do not depend on model | ANT-RSP-v2-1-0072 | The ASL-3 Security Standard is required. In addition, we will de |

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| ANT-RSP-v2-2-0346 | Changelog | The model capabilities and threat models corresponding with the ASL-3 Security S |
| ANT-RSP-v2-2-0347 | Changelog | and the relatively small number of employees who might be capable of model theft |
| ANT-RSP-v2-2-0348 | Changelog | For AI R&D-4, the threat models generally do not depend on model weight theft an |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**3 of 322 prior units (1%).**

| prior section heading | orphaned units |
|---|---|
| 2. Capability Thresholds and Required Safeguards | 1 |
| 4.1. ASL-3 Deployment Standard | 1 |
| 7. Governance and Transparency / 7.2. Transparency and External Input | 1 |
