# Stage 6 alignment review — GDM-FSF-v1-0_v2-0

Prior **116** units · target **138** units · **144** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 138 | 100% |
| Aligned to a prior unit | 72 | 52% |
| `prior_unit_id: NONE` | 66 | 48% |
| Removal candidates | 6 | — |
| Prior units serving >1 target (many-to-one) | 7 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | GDM-FSF-v1-0-0112 | 6 | GDM-FSF-v2-0-0116, GDM-FSF-v2-0-0118, GDM-FSF-v2-0-0119, GDM-FSF-v2-0-0120, GDM-FSF-v2-0-0121, GDM-FSF-v2-0-0122 | Involving external authorities and experts: We are exploring internal  |
| many-to-one | GDM-FSF-v1-0-0026 | 3 | GDM-FSF-v2-0-0031, GDM-FSF-v2-0-0032, GDM-FSF-v2-0-0033 | When a model reaches evaluation thresholds (i.e. passes a set of early |
| many-to-one | GDM-FSF-v1-0-0010 | 2 | GDM-FSF-v2-0-0003, GDM-FSF-v2-0-0004 | The Framework is informed by the broader conversation on Responsible C |
| many-to-one | GDM-FSF-v1-0-0031 | 2 | GDM-FSF-v2-0-0038, GDM-FSF-v2-0-0039 | If this happens, we would put on hold further deployment or developmen |
| many-to-one | GDM-FSF-v1-0-0060 | 2 | GDM-FSF-v2-0-0055, GDM-FSF-v2-0-0056 | Periodic red-teaming to assess the adequacy of mitigations. |
| many-to-one | GDM-FSF-v1-0-0087 | 2 | GDM-FSF-v2-0-0070, GDM-FSF-v2-0-0071 | Harmful cyberattacks against organizations with limited security postu |
| many-to-one | GDM-FSF-v1-0-0093 | 2 | GDM-FSF-v2-0-0080, GDM-FSF-v2-0-0081 | The mismanagement of a model with these capabilities could enable the  |
| alternates | GDM-FSF-v2-0-0051 | — | chose GDM-FSF-v1-0-0058, also considered GDM-FSF-v1-0-0059 | Development and assessment of mitigations: safeguards and an accompany |
| alternates | GDM-FSF-v2-0-0064 | — | chose GDM-FSF-v1-0-0079, also considered GDM-FSF-v1-0-0082 | CBRN uplift 1: Can be used to significantly assist a low-resourced act |
| alternates | GDM-FSF-v2-0-0066 | — | chose GDM-FSF-v1-0-0083, also considered GDM-FSF-v1-0-0084 | The potential magnitude of harm these capabilities may enable means th |
| alternates | GDM-FSF-v2-0-0075 | — | chose GDM-FSF-v1-0-0089, also considered GDM-FSF-v1-0-0090 | A model at this capability level could help fairly well-resourced thre |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | GDM-FSF-v2-0-0131 | Deceptive alignment approach beyond automated monitoring: We are a | GDM-FSF-v1-0-0109 | Misaligned AI: protection against the risk of systems acting adver |
| 0.02 | GDM-FSF-v2-0-0118 | If we assess that a model has reached a CCL that poses an unmitiga | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.03 | GDM-FSF-v2-0-0119 | Where appropriate, and subject to adequate confidentiality and sec | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.03 | GDM-FSF-v2-0-0120 | Model information: characteristics of the AI model relevant to the | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.03 | GDM-FSF-v2-0-0121 | Evaluation results: such as details about the evaluation design, t | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.04 | GDM-FSF-v2-0-0086 | This could be catastrophic if there is no effective way of defendi | GDM-FSF-v1-0-0097 | The mismanagement of a model with these capabilities could result  |
| 0.04 | GDM-FSF-v2-0-0136 | We are grateful for input from Apollo Research, Carnegie Endowment | GDM-FSF-v1-0-0116 | We would like to thank METR for contributing their expertise on Re |
| 0.04 | GDM-FSF-v2-0-0080 | Unrestricted access to models at this level of capability could si | GDM-FSF-v1-0-0093 | The mismanagement of a model with these capabilities could enable  |
| 0.04 | GDM-FSF-v2-0-0033 | Central to most response plans will be the application of the miti | GDM-FSF-v1-0-0026 | When a model reaches evaluation thresholds (i.e. passes a set of e |
| 0.05 | GDM-FSF-v2-0-0116 | For Google models, when alert thresholds are reached, the response | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.05 | GDM-FSF-v2-0-0051 | Development and assessment of mitigations: safeguards and an accom | GDM-FSF-v1-0-0058 | 1: Mitigations targeting the critical capability. Use of the full  |
| 0.06 | GDM-FSF-v2-0-0047 | Here, we rely on the RAND framework to articulate the level of sec | GDM-FSF-v1-0-0050 | See https://www.rand.org/pubs/working_papers/WRA2849-1.html. |
| 0.06 | GDM-FSF-v2-0-0036 | Note that these mitigations reflect considerations from the perspe | GDM-FSF-v1-0-0027 | We will also take into account considerations such as additional r |
| 0.07 | GDM-FSF-v2-0-0122 | Mitigation plans: descriptions of our mitigation plans and how the | GDM-FSF-v1-0-0112 | Involving external authorities and experts: We are exploring inter |
| 0.07 | GDM-FSF-v2-0-0039 | Conversely, where model capabilities remain quite distant from a C | GDM-FSF-v1-0-0031 | If this happens, we would put on hold further deployment or develo |
| 0.07 | GDM-FSF-v2-0-0081 | The exfiltration of such a model may therefore have a significant  | GDM-FSF-v1-0-0093 | The mismanagement of a model with these capabilities could enable  |
| 0.08 | GDM-FSF-v2-0-0056 | The safeguards for the model may be updated as well to ensure cont | GDM-FSF-v1-0-0060 | Periodic red-teaming to assess the adequacy of mitigations. |
| 0.09 | GDM-FSF-v2-0-0059 | We recommend a security level to each of these CCLs, which reflect | GDM-FSF-v1-0-0029 | We have developed frameworks for Security Levels and Deployment Le |
| 0.09 | GDM-FSF-v2-0-0037 | A model flagged by an alert threshold may be assessed to pose risk | GDM-FSF-v1-0-0030 | A model may reach evaluation thresholds before mitigations at appr |

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

| target | target excerpt | named alternate | that unit's excerpt |
|---|---|---|---|
| GDM-FSF-v2-0-0011 | For each type of risk, we define here a set of CCLs and a mitiga | GDM-FSF-v1-0-0004 | We are starting with an initial set of CCLs in the domains of Au |
| GDM-FSF-v2-0-0016 | These mitigations should be understood as recommendations for th | GDM-FSF-v1-0-0014 | Where appropriate, involve external parties in the process to he |
| GDM-FSF-v2-0-0088 | Note that we have removed the Autonomy risk domain, which was in | GDM-FSF-v1-0-0073 | Autonomy: Risks of the misuse of AI models with significant capa |
| GDM-FSF-v2-0-0089 | Most of the advanced risk that was captured by this CCL is now c | GDM-FSF-v1-0-0074, GDM-FSF | Autonomy level 1: Capable of expanding its effective capacity in |
| GDM-FSF-v2-0-0090 | From the perspective of misuse risks, our threat models suggest  | GDM-FSF-v1-0-0075 | A model at this capability level could, if misused, pose difficu |

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| GDM-FSF-v2-0-0021 | Footnotes | As in, in the context of the Framework, risks of threat actors using critical ca |
| GDM-FSF-v2-0-0022 | Footnotes | As in, in the context of the Framework, risks of highly autonomous systems purpo |
| GDM-FSF-v2-0-0035 | 3 - Applying Mitigations | For deceptive alignment risk, automated monitoring may be applied to detect and  |
| GDM-FSF-v2-0-0040 | 3 - Applying Mitigations | The appropriateness and efficacy of applied mitigations should be reviewed perio |
| GDM-FSF-v2-0-0048 | Security Mitigations | When we reference RAND security levels, we are referring to the security princip |
| GDM-FSF-v2-0-0049 | Security Mitigations | Because AI security is an area of active research, we expect the concrete measur |
| GDM-FSF-v2-0-0088 | Footnotes | Note that we have removed the Autonomy risk domain, which was included in Fronti |
| GDM-FSF-v2-0-0089 | Footnotes | Most of the advanced risk that was captured by this CCL is now covered by our mi |
| GDM-FSF-v2-0-0090 | Footnotes | From the perspective of misuse risks, our threat models suggest that no heighten |
| GDM-FSF-v2-0-0091 | Footnotes | For example, through the use of a self-replicating CBRN agent. Compared to a cou |
| GDM-FSF-v2-0-0092 | Footnotes | E.g. deletion or exfiltration of critical information, or destroying or disablin |
| GDM-FSF-v2-0-0093 | Footnotes | E.g. deletion or exfiltration of sensitive information/disruption of key systems |
| GDM-FSF-v2-0-0094 | Footnotes | Relative to the counterfactual of using 2024 AI technology and tooling. |
| GDM-FSF-v2-0-0132 | Future Work | Broader approach to ML R&D risks: The risks posed by models reaching our ML R&D  |
| GDM-FSF-v2-0-0133 | Future Work | We are actively researching appropriate responses to these scenarios. |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**50 of 116 prior units (43%).**

| prior section heading | orphaned units |
|---|---|
| Security Mitigations Table | 10 |
| CCL Table | 9 |
| Deployment Mitigations Table | 7 |
| Future work | 7 |
| 1 - Critical Capability Levels | 4 |
| Frontier Safety Framework (intro) | 3 |
| Footnotes | 3 |
| Deployment Mitigations | 2 |
| Framework | 1 |
| 2 - Evaluating frontier models | 1 |
| 3 - Applying mitigations | 1 |
| Figure 1 caption | 1 |
| Critical Capability Levels | 1 |
