# Stage 6 alignment review — ANT-RSP-v1-0_v3-4

Prior **355** units · target **334** units · **350** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 334 | 100% |
| Aligned to a prior unit | 112 | 34% |
| `prior_unit_id: NONE` | 222 | 66% |
| Removal candidates | 16 | — |
| Prior units serving >1 target (many-to-one) | 31 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v1-0-0161 | 6 | ANT-RSP-v3-4-0023, ANT-RSP-v3-4-0134, ANT-RSP-v3-4-0185, ANT-RSP-v3-4-0238, ANT-RSP-v3-4-0239, ANT-RSP-v3-4-0332 | Publicly share evaluation results after model deployment where possibl |
| many-to-one | ANT-RSP-v1-0-0163 | 5 | ANT-RSP-v3-4-0180, ANT-RSP-v3-4-0181, ANT-RSP-v3-4-0234, ANT-RSP-v3-4-0235, ANT-RSP-v3-4-0304 | Responsible Scaling Officer. There is a designated member of staff res |
| many-to-one | ANT-RSP-v1-0-0162 | 5 | ANT-RSP-v3-4-0182, ANT-RSP-v3-4-0237, ANT-RSP-v3-4-0322, ANT-RSP-v3-4-0328, ANT-RSP-v3-4-0329 | Share results of ASL evaluations promptly with Anthropic's governing b |
| many-to-one | ANT-RSP-v1-0-0166 | 5 | ANT-RSP-v3-4-0240, ANT-RSP-v3-4-0241, ANT-RSP-v3-4-0242, ANT-RSP-v3-4-0244, ANT-RSP-v3-4-0245 | Implement a non-compliance reporting policy for our Responsible Scalin |
| many-to-one | ANT-RSP-v1-0-0101 | 4 | ANT-RSP-v3-4-0059, ANT-RSP-v3-4-0063, ANT-RSP-v3-4-0072, ANT-RSP-v3-4-0109 | Capabilities that significantly increase risk of misuse catastrophe: A |
| many-to-one | ANT-RSP-v1-0-0150 | 4 | ANT-RSP-v3-4-0184, ANT-RSP-v3-4-0251, ANT-RSP-v3-4-0252, ANT-RSP-v3-4-0285 | Follow an "Update Process" for this document, including approval by th |
| many-to-one | ANT-RSP-v1-0-0002 | 3 | ANT-RSP-v3-4-0001, ANT-RSP-v3-4-0002, ANT-RSP-v3-4-0003 | With this document we are making a public commitment to a concrete fra |
| many-to-one | ANT-RSP-v1-0-0148 | 3 | ANT-RSP-v3-4-0028, ANT-RSP-v3-4-0233, ANT-RSP-v3-4-0303 | The ASLs specify what has to be true substantively of our models and o |
| many-to-one | ANT-RSP-v1-0-0013 | 3 | ANT-RSP-v3-4-0049, ANT-RSP-v3-4-0267, ANT-RSP-v3-4-0270 | Central to our plan is the concept of AI safety levels (ASL), which ar |
| many-to-one | ANT-RSP-v1-0-0075 | 3 | ANT-RSP-v3-4-0113, ANT-RSP-v3-4-0296, ANT-RSP-v3-4-0297 | We do not believe that merely possessing today’s models poses signific |
| many-to-one | ANT-RSP-v1-0-0164 | 3 | ANT-RSP-v3-4-0152, ANT-RSP-v3-4-0165, ANT-RSP-v3-4-0243 | Each quarter, they will share a report on implementation status to our |
| many-to-one | ANT-RSP-v1-0-0033 | 3 | ANT-RSP-v3-4-0155, ANT-RSP-v3-4-0307, ANT-RSP-v3-4-0323 | Misuse: AI systems are dual-use technologies, and so as they become mo |
| many-to-one | ANT-RSP-v1-0-0112 | 3 | ANT-RSP-v3-4-0295, ANT-RSP-v3-4-0312, ANT-RSP-v3-4-0313 | By “non-state attackers” we mean both persistent and opportunistic non |
| many-to-one | ANT-RSP-v1-0-0021 | 2 | ANT-RSP-v3-4-0011, ANT-RSP-v3-4-0257 | Anthropic’s commitment to follow the ASL scheme thus implies that we c |
| many-to-one | ANT-RSP-v1-0-0005 | 2 | ANT-RSP-v3-4-0029, ANT-RSP-v3-4-0030 | This work is complementary to our work on other areas of AI safety, in |
| many-to-one | ANT-RSP-v1-0-0010 | 2 | ANT-RSP-v3-4-0035, ANT-RSP-v3-4-0075 | We have in mind events of the magnitude of thousands of deaths or hund |
| many-to-one | ANT-RSP-v1-0-0025 | 2 | ANT-RSP-v3-4-0055, ANT-RSP-v3-4-0056 | Rather than try to define all future ASLs and their safety measures no |
| many-to-one | ANT-RSP-v1-0-0206 | 2 | ANT-RSP-v3-4-0068, ANT-RSP-v3-4-0069 | Critical catastrophic misuse risk: AI models have become the primary s |
| many-to-one | ANT-RSP-v1-0-0120 | 2 | ANT-RSP-v3-4-0073, ANT-RSP-v3-4-0110 | Specifically, we will implement measures designed to harden our securi |
| many-to-one | ANT-RSP-v1-0-0121 | 2 | ANT-RSP-v3-4-0074, ANT-RSP-v3-4-0111 | The full set of security measures that we commit to (and have already  |
| many-to-one | ANT-RSP-v1-0-0034 | 2 | ANT-RSP-v3-4-0080, ANT-RSP-v3-4-0081 | Autonomy and replication: As AI systems continue to scale, they may be |
| many-to-one | ANT-RSP-v1-0-0035 | 2 | ANT-RSP-v3-4-0085, ANT-RSP-v3-4-0116 | Such systems could become a source of catastrophic risk even if no one |
| many-to-one | ANT-RSP-v1-0-0122 | 2 | ANT-RSP-v3-4-0088, ANT-RSP-v3-4-0115 | Internal compartmentalization: We will limit access to training techni |
| many-to-one | ANT-RSP-v1-0-0142 | 2 | ANT-RSP-v3-4-0090, ANT-RSP-v3-4-0103 | These logs are monitored for abnormal activity, including harmful use  |
| many-to-one | ANT-RSP-v1-0-0030 | 2 | ANT-RSP-v3-4-0193, ANT-RSP-v3-4-0194 | We also welcome input on this document from other groups working on AI |
| many-to-one | ANT-RSP-v1-0-0172 | 2 | ANT-RSP-v3-4-0283, ANT-RSP-v3-4-0284 | Model evaluations: Evaluations are tests that are designed to detect d |
| many-to-one | ANT-RSP-v1-0-0175 | 2 | ANT-RSP-v3-4-0286, ANT-RSP-v3-4-0287 | Timing: During model training and fine-tuning, Anthropic will conduct  |
| many-to-one | ANT-RSP-v1-0-0114 | 2 | ANT-RSP-v3-4-0288, ANT-RSP-v3-4-0289 | Note that because safeguards such as Reinforcement Learning from Human |
| many-to-one | ANT-RSP-v1-0-0127 | 2 | ANT-RSP-v3-4-0292, ANT-RSP-v3-4-0293 | We commit to an additional set of measures for producing ASL-3 model o |
| many-to-one | ANT-RSP-v1-0-0143 | 2 | ANT-RSP-v3-4-0298, ANT-RSP-v3-4-0300 | Tiered access: In limited cases, models with capabilities relevant to  |
| many-to-one | ANT-RSP-v1-0-0026 | 2 | ANT-RSP-v3-4-0309, ANT-RSP-v3-4-0311 | By iterative, we mean we will define ASL-2 (current system) and ASL-3  |
| alternates | ANT-RSP-v3-4-0060 | — | chose ANT-RSP-v1-0-0135, also considered ANT-RSP-v1-0-0128 | We will maintain or improve on our ASL-3 protections, which include cl |
| alternates | ANT-RSP-v3-4-0064 | — | chose ANT-RSP-v1-0-0089, also considered ANT-RSP-v1-0-0135 | Restrictions on model behavior, and/or measures for quickly detecting  |
| alternates | ANT-RSP-v3-4-0071 | — | chose ANT-RSP-v1-0-0104, also considered ANT-RSP-v1-0-0106 | Additionally, we will identify the most concerning specific threat pat |
| alternates | ANT-RSP-v3-4-0155 | — | chose ANT-RSP-v1-0-0033, also considered ANT-RSP-v1-0-0034 | Threat model specification: The relevant threat models (which will, at |
| alternates | ANT-RSP-v3-4-0288 | — | chose ANT-RSP-v1-0-0114, also considered ANT-RSP-v1-0-0169 | Less prescriptive evaluation methodology: We have replaced some specif |
| alternates | ANT-RSP-v3-4-0304 | — | chose ANT-RSP-v1-0-0163, also considered ANT-RSP-v1-0-0161,ANT-RSP-v1-0-0202 | These include expanding the duties of the Responsible Scaling Officer; |
| alternates | ANT-RSP-v3-4-0305 | — | chose ANT-RSP-v1-0-0158, also considered ANT-RSP-v1-0-0161 | new procedures related to internal governance; and maintaining a publi |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | ANT-RSP-v3-4-0035 | We use this term in its plain meaning rather than adopting any spe | ANT-RSP-v1-0-0010 | We have in mind events of the magnitude of thousands of deaths or  |
| 0.00 | ANT-RSP-v3-4-0048 | At this point in AI's rapid development, we cannot presently give  | ANT-RSP-v1-0-0024 | The ASL system thus has an unavoidable component of “building the  |
| 0.00 | ANT-RSP-v3-4-0053 | To the extent this takes the form of national regulation, differen | ANT-RSP-v1-0-0008 | Our commitments are designed in the spirit of the Responsible Scal |
| 0.00 | ANT-RSP-v3-4-0069 | That is, a well-resourced team could, using the model, accomplish  | ANT-RSP-v1-0-0206 | Critical catastrophic misuse risk: AI models have become the prima |
| 0.00 | ANT-RSP-v3-4-0090 | Monitoring and/or restricting AI behavior and usage internally. | ANT-RSP-v1-0-0142 | These logs are monitored for abnormal activity, including harmful  |
| 0.00 | ANT-RSP-v3-4-0113 | Even malicious employees and other insiders with maximal levels of | ANT-RSP-v1-0-0075 | We do not believe that merely possessing today’s models poses sign |
| 0.00 | ANT-RSP-v3-4-0152 | We should make a strong attempt to ensure that ongoing (as opposed | ANT-RSP-v1-0-0164 | Each quarter, they will share a report on implementation status to |
| 0.00 | ANT-RSP-v3-4-0155 | Threat model specification: The relevant threat models (which will | ANT-RSP-v1-0-0033 | Misuse: AI systems are dual-use technologies, and so as they becom |
| 0.00 | ANT-RSP-v3-4-0165 | Review of past Risk Reports and decisions. We will address: | ANT-RSP-v1-0-0164 | Each quarter, they will share a report on implementation status to |
| 0.00 | ANT-RSP-v3-4-0181 | The CEO and RSO will make the ultimate determination regarding the | ANT-RSP-v1-0-0163 | Responsible Scaling Officer. There is a designated member of staff |
| 0.00 | ANT-RSP-v3-4-0185 | We will publish a public version of our Risk Report. | ANT-RSP-v1-0-0161 | Publicly share evaluation results after model deployment where pos |
| 0.00 | ANT-RSP-v3-4-0204 | We will select external reviewers that: | ANT-RSP-v1-0-0111 | Our evaluations were developed in consultation with Paul Christian |
| 0.00 | ANT-RSP-v3-4-0235 | (1) as needed, proposing updates to this policy; (2) approving rel | ANT-RSP-v1-0-0163 | Responsible Scaling Officer. There is a designated member of staff |
| 0.00 | ANT-RSP-v3-4-0241 | Staff will have more than one option for who receives these report | ANT-RSP-v1-0-0166 | Implement a non-compliance reporting policy for our Responsible Sc |
| 0.00 | ANT-RSP-v3-4-0244 | If we determine that a report is (1) substantiated and (2) involve | ANT-RSP-v1-0-0166 | Implement a non-compliance reporting policy for our Responsible Sc |
| 0.00 | ANT-RSP-v3-4-0245 | Finally, we will protect reporters from retaliation, and where a r | ANT-RSP-v1-0-0166 | Implement a non-compliance reporting policy for our Responsible Sc |
| 0.00 | ANT-RSP-v3-4-0287 | We found that a three-month cadence forced teams to prioritize con | ANT-RSP-v1-0-0175 | Timing: During model training and fine-tuning, Anthropic will cond |
| 0.00 | ANT-RSP-v3-4-0288 | Less prescriptive evaluation methodology: We have replaced some sp | ANT-RSP-v1-0-0114 | Note that because safeguards such as Reinforcement Learning from H |
| 0.00 | ANT-RSP-v3-4-0293 | Rather than detailing specific operational and technical safeguard | ANT-RSP-v1-0-0127 | We commit to an additional set of measures for producing ASL-3 mod |
| 0.00 | ANT-RSP-v3-4-0296 | We also removed the commitment to protect against scaled attacks a | ANT-RSP-v1-0-0075 | We do not believe that merely possessing today’s models poses sign |
| 0.00 | ANT-RSP-v3-4-0323 | This update (1) revises our threshold for novel chemical/biologica | ANT-RSP-v1-0-0033 | Misuse: AI systems are dual-use technologies, and so as they becom |
| 0.02 | ANT-RSP-v3-4-0080 | AI systems that are highly relied on and have extensive access to  | ANT-RSP-v1-0-0034 | Autonomy and replication: As AI systems continue to scale, they ma |
| 0.02 | ANT-RSP-v3-4-0289 | to (a) match expected efforts of potential adversaries and (b) pro | ANT-RSP-v1-0-0114 | Note that because safeguards such as Reinforcement Learning from H |
| 0.02 | ANT-RSP-v3-4-0060 | We will maintain or improve on our ASL-3 protections, which includ | ANT-RSP-v1-0-0135 | Automated detection: As a "defense in depth" addition to harm refu |
| 0.02 | ANT-RSP-v3-4-0308 | We have also disaggregated our existing AI R&D capability threshol | ANT-RSP-v1-0-0210 | Autonomous AI research: A model for which the weights would be a m |
| 0.02 | ANT-RSP-v3-4-0298 | Clarified requirements for deployments with trusted users: We have | ANT-RSP-v1-0-0143 | Tiered access: In limited cases, models with capabilities relevant |
| 0.03 | ANT-RSP-v3-4-0297 | While distillation remains a concern for more capable models, mode | ANT-RSP-v1-0-0075 | We do not believe that merely possessing today’s models poses sign |
| 0.03 | ANT-RSP-v3-4-0307 | New Capability Thresholds: We have added a new capability threshol | ANT-RSP-v1-0-0033 | Misuse: AI systems are dual-use technologies, and so as they becom |
| 0.03 | ANT-RSP-v3-4-0156 | Evidence (including evaluations) about relevant model capabilities | ANT-RSP-v1-0-0044 | Evaluation protocol: A protocol for when and how to evaluate model |
| 0.03 | ANT-RSP-v3-4-0002 | It establishes how we identify and evaluate risks, how we make dec | ANT-RSP-v1-0-0002 | With this document we are making a public commitment to a concrete |
| 0.03 | ANT-RSP-v3-4-0011 | Our previous RSP committed to implementing mitigations that would  | ANT-RSP-v1-0-0021 | Anthropic’s commitment to follow the ASL scheme thus implies that  |
| 0.03 | ANT-RSP-v3-4-0252 | If we update the RSP, we will publicly share the updated version p | ANT-RSP-v1-0-0150 | Follow an "Update Process" for this document, including approval b |
| 0.03 | ANT-RSP-v3-4-0029 | Our RSP is only one part of our overall approach to safety. | ANT-RSP-v1-0-0005 | This work is complementary to our work on other areas of AI safety |
| 0.03 | ANT-RSP-v3-4-0028 | Finally, our governance commitments are intended to promote intern | ANT-RSP-v1-0-0148 | The ASLs specify what has to be true substantively of our models a |
| 0.03 | ANT-RSP-v3-4-0055 | We expect that the recommendations for industry-wide safety will e | ANT-RSP-v1-0-0025 | Rather than try to define all future ASLs and their safety measure |
| 0.03 | ANT-RSP-v3-4-0270 | and we instead prefer to focus on what sort of argument an AI deve | ANT-RSP-v1-0-0013 | Central to our plan is the concept of AI safety levels (ASL), whic |
| 0.03 | ANT-RSP-v3-4-0285 | Our most accurate tests change frequently enough that it is more p | ANT-RSP-v1-0-0150 | Follow an "Update Process" for this document, including approval b |
| 0.03 | ANT-RSP-v3-4-0071 | Additionally, we will identify the most concerning specific threat | ANT-RSP-v1-0-0104 | Our first area of effort is in evaluating bioweapons risks where w |
| 0.03 | ANT-RSP-v3-4-0332 | It requires us to publicly disclose, at a high level, when we make | ANT-RSP-v1-0-0161 | Publicly share evaluation results after model deployment where pos |
| 0.03 | ANT-RSP-v3-4-0089 | Capability assessments demonstrating that AI models lack the abili | ANT-RSP-v1-0-0108 | Autonomous replication in the lab: The model shows early signs of  |

_52 further alignments below 0.10 overlap not shown._

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

Nothing flagged.

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**288 of 355 prior units (81%).**

| prior section heading | orphaned units |
|---|---|
| ASL-2 and ASL-3 Security Commitments | 49 |
| Evaluation Protocol | 31 |
| ASL-2 Commitments | 19 |
| ASL-3 Commitments | 17 |
| Tasks | 17 |
| Early Thoughts on ASL-4 and Higher | 16 |
| ASL-3 Deployment Measures | 15 |
| 5. Implement a simple feature for flask | 14 |
| Table: AI Safety Level Framework Overview | 13 |
| ASL-3 Evaluations for Misuse Risks | 13 |
| Framework | 11 |
| 4. Basic SQL injection exploit | 10 |
| Initial Commitments | 9 |
| 3. Fine-tune an open source LM to add a backdoor | 9 |
| Procedural Commitments | 7 |
| ASL-3 Evaluations for Autonomous Capabilities | 6 |
| Anthropic's Responsible Scaling Policy | 5 |
| Evaluation details / Protocol | 5 |
| fn4 | 3 |
| fn5 | 3 |
