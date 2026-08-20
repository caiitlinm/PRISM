# Stage 6 alignment review — ANT-RSP-v2-0_v2-1

Prior **338** units · target **322** units · **324** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 322 | 100% |
| Aligned to a prior unit | 310 | 96% |
| `prior_unit_id: NONE` | 12 | 4% |
| Removal candidates | 2 | — |
| Prior units serving >1 target (many-to-one) | 13 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v2-0-0023 | 2 | ANT-RSP-v2-1-0016, ANT-RSP-v2-1-0017 | We may deploy or store a model if either of the following criteria are |
| many-to-one | ANT-RSP-v2-0-0091 | 2 | ANT-RSP-v2-1-0071, ANT-RSP-v2-1-0074 | Autonomous AI Research and Development (AI R&D): The ability to either |
| many-to-one | ANT-RSP-v2-0-0093 | 2 | ANT-RSP-v2-1-0072, ANT-RSP-v2-1-0075 | At minimum, the ASL-3 Security Standard is required, although we expec |
| many-to-one | ANT-RSP-v2-0-0094 | 2 | ANT-RSP-v2-1-0073, ANT-RSP-v2-1-0076 | We also expect a strong affirmative case (made with accountability for |
| many-to-one | ANT-RSP-v2-0-0098 | 2 | ANT-RSP-v2-1-0081, ANT-RSP-v2-1-0082 | We will test for this checkpoint and, by the time we reach it, we aim  |
| many-to-one | ANT-RSP-v2-0-0179 | 2 | ANT-RSP-v2-1-0159, ANT-RSP-v2-1-0160 | The following groups are out of scope for the ASL-3 Security Standard  |
| many-to-one | ANT-RSP-v2-0-0183 | 2 | ANT-RSP-v2-1-0164, ANT-RSP-v2-1-0165 | Security frameworks: Align to and, as needed, extend industry-standard |
| many-to-one | ANT-RSP-v2-0-0213 | 2 | ANT-RSP-v2-1-0190, ANT-RSP-v2-1-0191 | To summarize the commitments and procedures outlined above, we may dep |
| many-to-one | ANT-RSP-v2-0-0233 | 2 | ANT-RSP-v2-1-0206, ANT-RSP-v2-1-0207 | We consider implementation of the ASL-3 Security Standard alone suffic |
| many-to-one | ANT-RSP-v2-0-0239 | 2 | ANT-RSP-v2-1-0213, ANT-RSP-v2-1-0214 | Transparency: We will share summaries of Capability Reports and Safegu |
| many-to-one | ANT-RSP-v2-0-0254 | 2 | ANT-RSP-v2-1-0230, ANT-RSP-v2-1-0231 | Public disclosures: We will publicly release key information related t |
| many-to-one | ANT-RSP-v2-0-0301 | 2 | ANT-RSP-v2-1-0276, ANT-RSP-v2-1-0277 | Autonomous AI Research and Development: The ability to either: (1) Ful |
| many-to-one | ANT-RSP-v2-0-0329 | 2 | ANT-RSP-v2-1-0306, ANT-RSP-v2-1-0307 | Rather than detailing specific operational and technical safeguards, w |
| alternates | ANT-RSP-v2-1-0002 | — | chose ANT-RSP-v2-0-0002, also considered ANT-RSP-v2-0-0003 | We are now updating our RSP to account for the lessons we've learned o |
| alternates | ANT-RSP-v2-1-0004 | — | chose ANT-RSP-v2-0-0005, also considered ANT-RSP-v2-0-0006 | As model capabilities increase, so will the need for stronger safeguar |
| alternates | ANT-RSP-v2-1-0005 | — | chose ANT-RSP-v2-0-0007, also considered ANT-RSP-v2-0-0008 | To determine when a model has become sufficiently advanced such that i |
| alternates | ANT-RSP-v2-1-0009 | — | chose ANT-RSP-v2-0-0012, also considered ANT-RSP-v2-0-0013 | We will first conduct preliminary assessments to determine whether a m |
| alternates | ANT-RSP-v2-1-0011 | — | chose ANT-RSP-v2-0-0015, also considered ANT-RSP-v2-0-0016 | If, however, we are unable to make the required showing, we will act a |
| alternates | ANT-RSP-v2-1-0013 | — | chose ANT-RSP-v2-0-0018, also considered ANT-RSP-v2-0-0019 | For the ASL-3 Deployment Standard, we will evaluate whether it is robu |
| alternates | ANT-RSP-v2-1-0021 | — | chose ANT-RSP-v2-0-0027, also considered ANT-RSP-v2-0-0028 | As frontier AI models advance, we believe they will bring about transf |
| alternates | ANT-RSP-v2-1-0026 | — | chose ANT-RSP-v2-0-0033, also considered ANT-RSP-v2-0-0034 | We are now updating our RSP to account for the lessons we've learned o |
| alternates | ANT-RSP-v2-1-0027 | — | chose ANT-RSP-v2-0-0035, also considered ANT-RSP-v2-0-0036 | First, our approach to risk should be proportional. Central to our pol |
| alternates | ANT-RSP-v2-1-0030 | — | chose ANT-RSP-v2-0-0039, also considered ANT-RSP-v2-0-0040 | Second, our approach to risk should be iterative. Since the frontier o |
| alternates | ANT-RSP-v2-1-0031 | — | chose ANT-RSP-v2-0-0041, also considered ANT-RSP-v2-0-0042 | We will thus regularly measure the capability of our models and adjust |
| alternates | ANT-RSP-v2-1-0033 | — | chose ANT-RSP-v2-0-0044, also considered ANT-RSP-v2-0-0045 | Third, our approach to risk should be exportable. To demonstrate that  |
| alternates | ANT-RSP-v2-1-0035 | — | chose ANT-RSP-v2-0-0047, also considered ANT-RSP-v2-0-0048 | In the long term, we hope that our policy may offer relevant insights  |
| alternates | ANT-RSP-v2-1-0038 | — | chose ANT-RSP-v2-0-0051, also considered ANT-RSP-v2-0-0052 | Further, we conduct research to understand the broader societal impact |
| alternates | ANT-RSP-v2-1-0039 | — | chose ANT-RSP-v2-0-0053, also considered ANT-RSP-v2-0-0054 | At Anthropic, we are committed to developing AI responsibly and transp |
| alternates | ANT-RSP-v2-1-0044 | — | chose ANT-RSP-v2-0-0059, also considered ANT-RSP-v2-0-0060 | We actively welcome feedback on our policy and suggestions for improve |
| alternates | ANT-RSP-v2-1-0045 | — | chose ANT-RSP-v2-0-0061, also considered ANT-RSP-v2-0-0062 | AI Safety Level Standards (ASL Standards) are core to our risk mitigat |
| alternates | ANT-RSP-v2-1-0046 | — | chose ANT-RSP-v2-0-0063, also considered ANT-RSP-v2-0-0064 | As model capabilities increase, so will the need for stronger safeguar |
| alternates | ANT-RSP-v2-1-0053 | — | chose ANT-RSP-v2-0-0071, also considered ANT-RSP-v2-0-0072 | At present, all of our models must meet the ASL-2 Deployment and Secur |
| alternates | ANT-RSP-v2-1-0063 | — | chose ANT-RSP-v2-0-0082, also considered ANT-RSP-v2-0-0083 | Below, we specify the Capability Thresholds and their corresponding Re |
| alternates | ANT-RSP-v2-1-0064 | — | chose ANT-RSP-v2-0-0084, also considered ANT-RSP-v2-0-0085 | In developing these standards, we have weighed the risks and benefits  |
| alternates | ANT-RSP-v2-1-0065 | — | chose ANT-RSP-v2-0-0086, also considered ANT-RSP-v2-0-0087 | We will conduct assessments to inform when to implement the Required S |
| alternates | ANT-RSP-v2-1-0072 | — | chose ANT-RSP-v2-0-0093, also considered ANT-RSP-v2-0-0094 | The ASL-3 Security Standard is required. In addition, we will develop  |
| alternates | ANT-RSP-v2-1-0079 | — | chose ANT-RSP-v2-0-0095, also considered ANT-RSP-v2-0-0096 | We will consider it sufficient to rule out the possibility that a mode |
| alternates | ANT-RSP-v2-1-0092 | — | chose ANT-RSP-v2-0-0108, also considered ANT-RSP-v2-0-0109 | We will conduct either pre- or post-deployment testing, including spec |
| alternates | ANT-RSP-v2-1-0094 | — | chose ANT-RSP-v2-0-0113, also considered ANT-RSP-v2-0-0114 | We recognize the potential risks of highly persuasive AI models. While |
| alternates | ANT-RSP-v2-1-0115 | — | chose ANT-RSP-v2-0-0127, also considered ANT-RSP-v2-0-0128 | "Effective Compute" is a scaling-trend-based metric that accounts for  |
| alternates | ANT-RSP-v2-1-0152 | — | chose ANT-RSP-v2-0-0174, also considered ANT-RSP-v2-0-0175 | Trusted users: Establish criteria for determining when it may be appro |
| alternates | ANT-RSP-v2-1-0189 | — | chose ANT-RSP-v2-0-0207, also considered ANT-RSP-v2-0-0208, ANT-RSP-v2-0-0209, ANT-RS | In parallel with upgrading a model to the Required Safeguards, we will |
| alternates | ANT-RSP-v2-1-0250 | — | chose ANT-RSP-v2-0-0272, also considered ANT-RSP-v2-0-0273 | Anthropic's Board of Directors approves the RSP and receives Capabilit |
| alternates | ANT-RSP-v2-1-0268 | — | chose ANT-RSP-v2-0-0291, also considered ANT-RSP-v2-0-0292 | Infrastructure: Standard security infrastructure, monitoring software, |
| alternates | ANT-RSP-v2-1-0304 | — | chose ANT-RSP-v2-0-0326, also considered ANT-RSP-v2-0-0327 | Although still an aspirational goal, the science of evaluations is not |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | ANT-RSP-v2-1-0279 | Model Autonomy checkpoint: The ability to perform a wide range of  | ANT-RSP-v2-0-0303 | We roughly estimate that the 2018-2024 average scaleup was around  |
| 0.00 | ANT-RSP-v2-1-0282 | We treat these lists as sensitive, but we plan to share them with  | ANT-RSP-v2-0-0298 | We are uncertain how to choose a specific threshold, but we mainta |
| 0.00 | ANT-RSP-v2-1-0286 | September 19, 2023 (RSP v1.0) RSP-2023 (aka RSP v1.0): Initial ver | ANT-RSP-v2-0-0307 | Combined, these have an effective rate of scaling of 35 x/year. |
| 0.00 | ANT-RSP-v2-1-0295 | AI R&D threshold added: We added a new threshold for AI systems th | ANT-RSP-v2-0-0317 | We now believe that these capabilities - at the levels we initiall |
| 0.00 | ANT-RSP-v2-1-0296 | Such capabilities could lead to rapid, unpredictable advances in A | ANT-RSP-v2-0-0318 | AI R&D threshold added: We added a new threshold for AI systems th |
| 0.00 | ANT-RSP-v2-1-0297 | Testing for Capability Thresholds: Rather than using prespecified  | ANT-RSP-v2-0-0319 | Such capabilities could lead to rapid, unpredictable advances in A |
| 0.00 | ANT-RSP-v2-1-0298 | Predefined tests may miss emerging risks or be overly conservative | ANT-RSP-v2-0-0320 | Testing for Capability Thresholds: Rather than using prespecified  |
| 0.00 | ANT-RSP-v2-1-0300 | Adjusted evaluation cadence: We adjusted the comprehensive assessm | ANT-RSP-v2-0-0322 | Our most accurate tests change frequently enough that it is more p |
| 0.00 | ANT-RSP-v2-1-0304 | Although still an aspirational goal, the science of evaluations is | ANT-RSP-v2-0-0326 | We have found that specific methodologies may become outdated when |
| 0.02 | ANT-RSP-v2-1-0281 | We are uncertain how to choose a specific threshold, but we mainta | ANT-RSP-v2-0-0305 | We primarily view this level of model autonomy as a checkpoint on  |
| 0.02 | ANT-RSP-v2-1-0302 | Less prescriptive evaluation methodology: We have replaced some sp | ANT-RSP-v2-0-0324 | We found that a three-month cadence forced teams to prioritize con |
| 0.02 | ANT-RSP-v2-1-0288 | Key improvements include new capability thresholds to indicate whe | ANT-RSP-v2-0-0309 | October 15, 2024 RSP-2024: This update introduces a more flexible  |
| 0.03 | ANT-RSP-v2-1-0283 | This comparison is hard to make in practice; this note is to clari | ANT-RSP-v2-0-0299 | We treat these lists as sensitive, but we plan to share them with  |
| 0.03 | ANT-RSP-v2-1-0290 | This change allows for more targeted application of safeguards bas | ANT-RSP-v2-0-0312 | ASL definition changed: The term "ASL" now refers to groups of tec |
| 0.04 | ANT-RSP-v2-1-0284 | The 35x/year scaleup estimate is based on assuming the rate of inc | ANT-RSP-v2-0-0300 | This comparison is hard to make in practice; this note is to clari |
| 0.04 | ANT-RSP-v2-1-0287 | RSP-2024: This update introduces a more flexible and nuanced appro | ANT-RSP-v2-0-0308 | September 19, 2023 RSP-2023 (aka RSP v1.0): Initial version. |
| 0.04 | ANT-RSP-v2-1-0299 | Our most accurate tests change frequently enough that it is more p | ANT-RSP-v2-0-0321 | Predefined tests may miss emerging risks or be overly conservative |
| 0.05 | ANT-RSP-v2-1-0165 | This includes: | ANT-RSP-v2-0-0183 | Security frameworks: Align to and, as needed, extend industry-stan |
| 0.05 | ANT-RSP-v2-1-0291 | ARA threshold now a checkpoint: We replaced our previous autonomou | ANT-RSP-v2-0-0313 | This change allows for more targeted application of safeguards bas |
| 0.05 | ANT-RSP-v2-1-0303 | We have found that specific methodologies may become outdated when | ANT-RSP-v2-0-0325 | Less prescriptive evaluation methodology: We have replaced some sp |
| 0.06 | ANT-RSP-v2-1-0293 | We previously considered these capabilities as a trigger for incre | ANT-RSP-v2-0-0315 | Rather than triggering higher safety standards automatically, reac |
| 0.07 | ANT-RSP-v2-1-0285 | Combined, these have an effective rate of scaling of 35 x/year. | ANT-RSP-v2-0-0306 | The 35x/year scaleup estimate is based on assuming the rate of inc |
| 0.07 | ANT-RSP-v2-1-0280 | We primarily view this level of model autonomy as a checkpoint on  | ANT-RSP-v2-0-0304 | Model Autonomy checkpoint: The ability to perform a wide range of  |
| 0.08 | ANT-RSP-v2-1-0289 | ASL definition changed: The term "ASL" now refers to groups of tec | ANT-RSP-v2-0-0310 | Key improvements include new capability thresholds to indicate whe |
| 0.08 | ANT-RSP-v2-1-0292 | Rather than triggering higher safety standards automatically, reac | ANT-RSP-v2-0-0314 | ARA threshold now a checkpoint: We replaced our previous autonomou |
| 0.08 | ANT-RSP-v2-1-0294 | We now believe that these capabilities - at the levels we initiall | ANT-RSP-v2-0-0316 | We previously considered these capabilities as a trigger for incre |

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| ANT-RSP-v2-1-0069 | 2. Capability Thresholds and Required Safeguards | CBRN-4: The ability to substantially uplift CBRN development capabilities of mod |
| ANT-RSP-v2-1-0070 | 2. Capability Thresholds and Required Safeguards | We expect this threshold will require the ASL-4 Deployment and Security Standard |
| ANT-RSP-v2-1-0077 | 2. Capability Thresholds and Required Safeguards | These Capability Thresholds represent our current understanding of the most pres |
| ANT-RSP-v2-1-0078 | 2. Capability Thresholds and Required Safeguards | For each threshold, we will identify and describe the corresponding Required Saf |
| ANT-RSP-v2-1-0274 | Appendix C: Detailed Capability Thresholds | CBRN-4: The ability to substantially uplift CBRN development capabilities of mod |
| ANT-RSP-v2-1-0275 | Appendix C: Detailed Capability Thresholds | We currently define this as uplifting a team of people with skills equivalent to |
| ANT-RSP-v2-1-0317 | Changelog | RSP-2025: This update clarifies which Capability Thresholds would require enhanc |
| ANT-RSP-v2-1-0318 | Changelog | New Capability Thresholds: We have added a new capability threshold related to C |
| ANT-RSP-v2-1-0319 | Changelog | We have also disaggregated our existing AI R&D capability thresholds, separating |
| ANT-RSP-v2-1-0320 | Changelog | Iterative Commitment: We have adopted a general commitment to reevaluate our Cap |
| ANT-RSP-v2-1-0321 | Changelog | We have decided not to maintain a commitment to define ASL-N+1 evaluations by th |
| ANT-RSP-v2-1-0322 | Changelog | We believe it is more practical and sensible instead to commit to reconsidering  |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**40 of 338 prior units (12%).**

| prior section heading | orphaned units |
|---|---|
| Introduction | 10 |
| 2. Capability Thresholds and Required Safeguards | 7 |
| Executive Summary | 6 |
| 5. Follow-Up Capability Assessment | 5 |
| 1. Background | 3 |
| Changelog | 2 |
| 3. Capability Assessment / 3.2. Comprehensive Assessment | 1 |
| 4.1. ASL-3 Deployment Standard | 1 |
| fn14 | 1 |
| 7. Governance and Transparency / 7.1. Internal Governance | 1 |
| 7. Governance and Transparency / 7.2. Transparency and External Input | 1 |
| Appendix A: Glossary | 1 |
| Appendix B: ASL-2 Standard | 1 |
