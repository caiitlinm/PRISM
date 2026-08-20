# Stage 6 alignment review — GDM-FSF-v1-0_v3-1

Prior **116** units · target **281** units · **285** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 281 | 100% |
| Aligned to a prior unit | 118 | 42% |
| `prior_unit_id: NONE` | 163 | 58% |
| Removal candidates | 4 | — |
| Prior units serving >1 target (many-to-one) | 29 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | GDM-FSF-v1-0-0026 | 11 | GDM-FSF-v3-1-0072, GDM-FSF-v3-1-0073, GDM-FSF-v3-1-0074, GDM-FSF-v3-1-0075, GDM-FSF-v3-1-0110, GDM-FSF-v3-1-0125… | When a model reaches evaluation thresholds (i.e. passes a set of early |
| many-to-one | GDM-FSF-v1-0-0023 | 7 | GDM-FSF-v3-1-0044, GDM-FSF-v3-1-0059, GDM-FSF-v3-1-0060, GDM-FSF-v3-1-0247, GDM-FSF-v3-1-0248, GDM-FSF-v3-1-0253… | To do so, we will define a set of evaluations called "early warning ev |
| many-to-one | GDM-FSF-v1-0-0091 | 5 | GDM-FSF-v3-1-0038, GDM-FSF-v3-1-0164, GDM-FSF-v3-1-0188, GDM-FSF-v3-1-0195, GDM-FSF-v3-1-0241 | Machine Learning R&D: Risks of the misuse of models capable of acceler |
| many-to-one | GDM-FSF-v1-0-0028 | 5 | GDM-FSF-v3-1-0077, GDM-FSF-v3-1-0091, GDM-FSF-v3-1-0107, GDM-FSF-v3-1-0108, GDM-FSF-v3-1-0262 | The initial version of the Framework focuses on two categories of miti |
| many-to-one | GDM-FSF-v1-0-0029 | 5 | GDM-FSF-v3-1-0092, GDM-FSF-v3-1-0096, GDM-FSF-v3-1-0145, GDM-FSF-v3-1-0168, GDM-FSF-v3-1-0196 | We have developed frameworks for Security Levels and Deployment Levels |
| many-to-one | GDM-FSF-v1-0-0112 | 5 | GDM-FSF-v3-1-0218, GDM-FSF-v3-1-0219, GDM-FSF-v3-1-0220, GDM-FSF-v3-1-0221, GDM-FSF-v3-1-0222 | Involving external authorities and experts: We are exploring internal  |
| many-to-one | GDM-FSF-v1-0-0009 | 4 | GDM-FSF-v3-1-0019, GDM-FSF-v3-1-0020, GDM-FSF-v3-1-0212, GDM-FSF-v3-1-0213 | It will be reviewed periodically and we expect it to evolve substantia |
| many-to-one | GDM-FSF-v1-0-0018 | 4 | GDM-FSF-v3-1-0029, GDM-FSF-v3-1-0030, GDM-FSF-v3-1-0243, GDM-FSF-v3-1-0244 | The Framework is built around capability thresholds called "Critical C |
| many-to-one | GDM-FSF-v1-0-0002 | 3 | GDM-FSF-v3-1-0002, GDM-FSF-v3-1-0026, GDM-FSF-v3-1-0027 | In focusing on these risks at the model level, it is intended to compl |
| many-to-one | GDM-FSF-v1-0-0008 | 3 | GDM-FSF-v3-1-0014, GDM-FSF-v3-1-0017, GDM-FSF-v3-1-0025 | The Framework is exploratory and based on preliminary research, which  |
| many-to-one | GDM-FSF-v1-0-0019 | 3 | GDM-FSF-v3-1-0031, GDM-FSF-v3-1-0047, GDM-FSF-v3-1-0051 | We determine CCLs by analyzing several high-risk domains: we identify  |
| many-to-one | GDM-FSF-v1-0-0020 | 3 | GDM-FSF-v3-1-0034, GDM-FSF-v3-1-0048, GDM-FSF-v3-1-0049 | We have conducted preliminary analyses of the Autonomy, Biosecurity, C |
| many-to-one | GDM-FSF-v1-0-0078 | 3 | GDM-FSF-v3-1-0035, GDM-FSF-v3-1-0149, GDM-FSF-v3-1-0238 | Biosecurity: Risks of models assisting in the development, preparation |
| many-to-one | GDM-FSF-v1-0-0085 | 3 | GDM-FSF-v3-1-0036, GDM-FSF-v3-1-0156, GDM-FSF-v3-1-0239 | Cybersecurity: Risks of models assisting in the execution of a cyber a |
| many-to-one | GDM-FSF-v1-0-0022 | 3 | GDM-FSF-v3-1-0045, GDM-FSF-v3-1-0052, GDM-FSF-v3-1-0066 | The capabilities of frontier models are tested periodically to check w |
| many-to-one | GDM-FSF-v1-0-0027 | 3 | GDM-FSF-v3-1-0063, GDM-FSF-v3-1-0130, GDM-FSF-v3-1-0174 | We will also take into account considerations such as additional risks |
| many-to-one | GDM-FSF-v1-0-0041 | 3 | GDM-FSF-v3-1-0112, GDM-FSF-v3-1-0113, GDM-FSF-v3-1-0166 | This is an important measure because the release of model weights may  |
| many-to-one | GDM-FSF-v1-0-0050 | 3 | GDM-FSF-v3-1-0121, GDM-FSF-v3-1-0122, GDM-FSF-v3-1-0273 | See https://www.rand.org/pubs/working_papers/WRA2849-1.html. |
| many-to-one | GDM-FSF-v1-0-0010 | 2 | GDM-FSF-v3-1-0003, GDM-FSF-v3-1-0004 | The Framework is informed by the broader conversation on Responsible C |
| many-to-one | GDM-FSF-v1-0-0014 | 2 | GDM-FSF-v3-1-0008, GDM-FSF-v3-1-0067 | Where appropriate, involve external parties in the process to help inf |
| many-to-one | GDM-FSF-v1-0-0004 | 2 | GDM-FSF-v3-1-0010, GDM-FSF-v3-1-0033 | We are starting with an initial set of CCLs in the domains of Autonomy |
| many-to-one | GDM-FSF-v1-0-0006 | 2 | GDM-FSF-v3-1-0018, GDM-FSF-v3-1-0050 | We will be expanding our set of CCLs over time as we gain experience a |
| many-to-one | GDM-FSF-v1-0-0025 | 2 | GDM-FSF-v3-1-0062, GDM-FSF-v3-1-0249 | To account for the gap between rounds of evaluation, we will design ea |
| many-to-one | GDM-FSF-v1-0-0044 | 2 | GDM-FSF-v3-1-0117, GDM-FSF-v3-1-0272 | 1: Controlled access. Access Control List hygiene. Non-forgeable linea |
| many-to-one | GDM-FSF-v1-0-0059 | 2 | GDM-FSF-v3-1-0127, GDM-FSF-v3-1-0263 | Application, where appropriate, of the full suite of prevailing indust |
| many-to-one | GDM-FSF-v1-0-0060 | 2 | GDM-FSF-v3-1-0128, GDM-FSF-v3-1-0129 | Periodic red-teaming to assess the adequacy of mitigations. |
| many-to-one | GDM-FSF-v1-0-0093 | 2 | GDM-FSF-v3-1-0167, GDM-FSF-v3-1-0199 | The mismanagement of a model with these capabilities could enable the  |
| many-to-one | GDM-FSF-v1-0-0096 | 2 | GDM-FSF-v3-1-0203, GDM-FSF-v3-1-0204 | This could give any actor with adequate computational resources the ab |
| many-to-one | GDM-FSF-v1-0-0038 | 2 | GDM-FSF-v3-1-0269, GDM-FSF-v3-1-0270 | The Frontier Safety Framework proposes two kinds of mitigations to add |
| alternates | GDM-FSF-v3-1-0117 | — | chose GDM-FSF-v1-0-0044, also considered GDM-FSF-v1-0-0050 | We use security levels to indicate security goals/principles in line w |
| alternates | GDM-FSF-v3-1-0150 | — | chose GDM-FSF-v1-0-0079, also considered GDM-FSF-v1-0-0082 | CBRN uplift level 1: Provides low to medium resourced actors uplift in |
| alternates | GDM-FSF-v3-1-0157 | — | chose GDM-FSF-v1-0-0086, also considered GDM-FSF-v1-0-0088 | Cyber uplift level 1: Provides sufficient uplift with high impact cybe |
| alternates | GDM-FSF-v3-1-0195 | — | chose GDM-FSF-v1-0-0091, also considered GDM-FSF-v1-0-0092 | We define ML R&D CCLs at capability levels at which misalignment, misu |
| alternates | GDM-FSF-v3-1-0216 | — | chose GDM-FSF-v1-0-0105, also considered GDM-FSF-v1-0-0102 | Update our testing and mitigation approaches, where needed to ensure r |
| alternates | GDM-FSF-v3-1-0272 | — | chose GDM-FSF-v1-0-0044, also considered GDM-FSF-v1-0-0050 | RAND Security Levels: indicate security goals and principles relevant  |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | GDM-FSF-v3-1-0014 | The safety and security of frontier AI models is a global public g | GDM-FSF-v1-0-0008 | The Framework is exploratory and based on preliminary research, wh |
| 0.00 | GDM-FSF-v3-1-0017 | These mitigations are most effective when adopted by industry as a | GDM-FSF-v1-0-0008 | The Framework is exploratory and based on preliminary research, wh |
| 0.00 | GDM-FSF-v3-1-0018 | The Framework is based on early and evolving research. | GDM-FSF-v1-0-0006 | We will be expanding our set of CCLs over time as we gain experien |
| 0.00 | GDM-FSF-v3-1-0025 | These protocols represent our current understanding of and approac | GDM-FSF-v1-0-0008 | The Framework is exploratory and based on preliminary research, wh |
| 0.00 | GDM-FSF-v3-1-0045 | We conduct our risk management process as appropriate, throughout  | GDM-FSF-v1-0-0022 | The capabilities of frontier models are tested periodically to che |
| 0.00 | GDM-FSF-v3-1-0063 | We conduct further analysis, including reviewing model-independent | GDM-FSF-v1-0-0027 | We will also take into account considerations such as additional r |
| 0.00 | GDM-FSF-v3-1-0086 | See the deployment mitigations sections below regarding misuse and | GDM-FSF-v1-0-0032 | Figure 1 depicts the relationship between these components of the  |
| 0.00 | GDM-FSF-v3-1-0126 | Development and assessment of mitigations: safeguards and an accom | GDM-FSF-v1-0-0026 | When a model reaches evaluation thresholds (i.e. passes a set of e |
| 0.00 | GDM-FSF-v3-1-0130 | The likelihood and consequences of model misuse, capability improv | GDM-FSF-v1-0-0027 | We will also take into account considerations such as additional r |
| 0.00 | GDM-FSF-v3-1-0170 | Development and assessment of mitigations: safeguards and an accom | GDM-FSF-v1-0-0026 | When a model reaches evaluation thresholds (i.e. passes a set of e |
| 0.00 | GDM-FSF-v3-1-0174 | The likelihood and consequences of model misuse or misalignment, c | GDM-FSF-v1-0-0027 | We will also take into account considerations such as additional r |
| 0.00 | GDM-FSF-v3-1-0204 | This could be catastrophic if there is no effective way of defendi | GDM-FSF-v1-0-0096 | This could give any actor with adequate computational resources th |
| 0.00 | GDM-FSF-v3-1-0213 | The process will involve (i) an assessment of the Framework's appr | GDM-FSF-v1-0-0009 | It will be reviewed periodically and we expect it to evolve substa |
| 0.02 | GDM-FSF-v3-1-0107 | This section describes our mitigation approach for models that pos | GDM-FSF-v1-0-0028 | The initial version of the Framework focuses on two categories of  |
| 0.03 | GDM-FSF-v3-1-0110 | Regarding deployment mitigations for models reaching T/CCLs, we sp | GDM-FSF-v1-0-0026 | When a model reaches evaluation thresholds (i.e. passes a set of e |
| 0.03 | GDM-FSF-v3-1-0072 | We apply safety and security mitigations throughout the lifecycle  | GDM-FSF-v1-0-0026 | When a model reaches evaluation thresholds (i.e. passes a set of e |
| 0.03 | GDM-FSF-v3-1-0219 | Where appropriate, and subject to adequate confidentiality and sec | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.03 | GDM-FSF-v3-1-0125 | The following mitigation process for external deployments will be  | GDM-FSF-v1-0-0026 | When a model reaches evaluation thresholds (i.e. passes a set of e |
| 0.03 | GDM-FSF-v3-1-0216 | Update our testing and mitigation approaches, where needed to ensu | GDM-FSF-v1-0-0105 | Mitigation plans: Striking a balance between mitigating risks and  |
| 0.03 | GDM-FSF-v3-1-0091 | This is required only for external deployment, not internal deploy | GDM-FSF-v1-0-0028 | The initial version of the Framework focuses on two categories of  |
| 0.03 | GDM-FSF-v3-1-0199 | The exfiltration of such a model may therefore have a significant  | GDM-FSF-v1-0-0093 | The mismanagement of a model with these capabilities could enable  |
| 0.03 | GDM-FSF-v3-1-0272 | RAND Security Levels: indicate security goals and principles relev | GDM-FSF-v1-0-0044 | 1: Controlled access. Access Control List hygiene. Non-forgeable l |
| 0.03 | GDM-FSF-v3-1-0066 | Our approach to model evaluations and inherent risk assessments de | GDM-FSF-v1-0-0022 | The capabilities of frontier models are tested periodically to che |
| 0.03 | GDM-FSF-v3-1-0167 | In addition, exfiltration of highly capable models increases the l | GDM-FSF-v1-0-0093 | The mismanagement of a model with these capabilities could enable  |
| 0.03 | GDM-FSF-v3-1-0220 | Model information: characteristics of the AI model relevant to the | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.03 | GDM-FSF-v3-1-0221 | Evaluation results: such as details about the evaluation design, t | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.04 | GDM-FSF-v3-1-0166 | Security mitigations against exfiltration and unauthorized modific | GDM-FSF-v1-0-0041 | This is an important measure because the release of model weights  |
| 0.04 | GDM-FSF-v3-1-0129 | The effectiveness of the mitigations. For example, tests run on mi | GDM-FSF-v1-0-0060 | Periodic red-teaming to assess the adequacy of mitigations. |
| 0.04 | GDM-FSF-v3-1-0011 | For each type of risk, we define a set of CCLs (and TCLs where rel | GDM-FSF-v1-0-0005 | Risk assessment in these domains will necessarily involve evaluati |
| 0.04 | GDM-FSF-v3-1-0075 | Central to most response plans will be the application of the miti | GDM-FSF-v1-0-0026 | When a model reaches evaluation thresholds (i.e. passes a set of e |
| 0.04 | GDM-FSF-v3-1-0117 | We use security levels to indicate security goals/principles in li | GDM-FSF-v1-0-0044 | 1: Controlled access. Access Control List hygiene. Non-forgeable l |
| 0.04 | GDM-FSF-v3-1-0260 | Central to most response plans will be the application of the miti | GDM-FSF-v1-0-0026 | When a model reaches evaluation thresholds (i.e. passes a set of e |
| 0.05 | GDM-FSF-v3-1-0218 | If we assess that a model has reached a CCL that poses an unmitiga | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.05 | GDM-FSF-v3-1-0247 | Alert Thresholds: are thresholds which we set marginally earlier t | GDM-FSF-v1-0-0023 | To do so, we will define a set of evaluations called "early warnin |
| 0.05 | GDM-FSF-v3-1-0092 | Security mitigations have been applied to the model weights reachi | GDM-FSF-v1-0-0029 | We have developed frameworks for Security Levels and Deployment Le |
| 0.05 | GDM-FSF-v3-1-0096 | Security mitigations have been applied to the model weights reachi | GDM-FSF-v1-0-0029 | We have developed frameworks for Security Levels and Deployment Le |
| 0.05 | GDM-FSF-v3-1-0263 | They may include safety post-training, input/output/chain-of-thoug | GDM-FSF-v1-0-0059 | Application, where appropriate, of the full suite of prevailing in |
| 0.06 | GDM-FSF-v3-1-0121 | In other words, "security level N" indicates security controls and | GDM-FSF-v1-0-0050 | See https://www.rand.org/pubs/working_papers/WRA2849-1.html. |
| 0.06 | GDM-FSF-v3-1-0188 | We set ML R&D CCLs that indicate higher capability levels at which | GDM-FSF-v1-0-0091 | Machine Learning R&D: Risks of the misuse of models capable of acc |
| 0.06 | GDM-FSF-v3-1-0254 | They specifically target the threats and risk scenarios identified | GDM-FSF-v1-0-0023 | To do so, we will define a set of evaluations called "early warnin |

_21 further alignments below 0.10 overlap not shown._

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

Nothing flagged.

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**63 of 116 prior units (54%).**

| prior section heading | orphaned units |
|---|---|
| CCL Table | 13 |
| Future work | 12 |
| Deployment Mitigations Table | 10 |
| Security Mitigations Table | 9 |
| Footnotes | 3 |
| Deployment Mitigations | 3 |
| Critical Capability Levels | 3 |
| Acknowledgements | 3 |
| Frontier Safety Framework (intro) | 2 |
| 3 - Applying mitigations | 2 |
| 1 - Critical Capability Levels | 1 |
| 2 - Evaluating frontier models | 1 |
| Figure 1 caption | 1 |
