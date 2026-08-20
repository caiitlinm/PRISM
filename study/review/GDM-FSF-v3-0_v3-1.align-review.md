# Stage 6 alignment review — GDM-FSF-v3-0_v3-1

Prior **194** units · target **281** units · **283** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 281 | 100% |
| Aligned to a prior unit | 203 | 72% |
| `prior_unit_id: NONE` | 78 | 28% |
| Removal candidates | 2 | — |
| Prior units serving >1 target (many-to-one) | 22 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | GDM-FSF-v3-0-0074 | 4 | GDM-FSF-v3-1-0099, GDM-FSF-v3-1-0100, GDM-FSF-v3-1-0101, GDM-FSF-v3-1-0102 | Because the CCLs for misalignment risk are exploratory and intended fo |
| many-to-one | GDM-FSF-v3-0-0044-a | 3 | GDM-FSF-v3-1-0052, GDM-FSF-v3-1-0059, GDM-FSF-v3-1-0060 | Analysis: Central to our model evaluations are "early warning evaluati |
| many-to-one | GDM-FSF-v3-0-0063 | 3 | GDM-FSF-v3-1-0084, GDM-FSF-v3-1-0085, GDM-FSF-v3-1-0134 | These will form the basis of a safety case for models reaching CCLs, t |
| many-to-one | GDM-FSF-v3-0-0171 | 3 | GDM-FSF-v3-1-0191, GDM-FSF-v3-1-0192, GDM-FSF-v3-1-0193 | Automated monitoring: monitoring system to detect illicit use of instr |
| many-to-one | GDM-FSF-v3-0-0003 | 2 | GDM-FSF-v3-1-0003, GDM-FSF-v3-1-0004 | The Framework is informed by the broader conversation on Frontier AI S |
| many-to-one | GDM-FSF-v3-0-0009 | 2 | GDM-FSF-v3-1-0010, GDM-FSF-v3-1-0011 | The Framework addresses misuse risk, risks from machine learning resea |
| many-to-one | GDM-FSF-v3-0-0011 | 2 | GDM-FSF-v3-1-0014, GDM-FSF-v3-1-0015 | The safety and security of frontier AI models is a global public good. |
| many-to-one | GDM-FSF-v3-0-0014 | 2 | GDM-FSF-v3-1-0018, GDM-FSF-v3-1-0019 | The Framework is based on early and evolving research. We may change o |
| many-to-one | GDM-FSF-v3-0-0019 | 2 | GDM-FSF-v3-1-0024, GDM-FSF-v3-1-0025 | This section describes the central components of the Frontier Safety F |
| many-to-one | GDM-FSF-v3-0-0023 | 2 | GDM-FSF-v3-1-0029, GDM-FSF-v3-1-0030 | The Framework is built around capability thresholds called "Critical C |
| many-to-one | GDM-FSF-v3-0-0033 | 2 | GDM-FSF-v3-1-0032, GDM-FSF-v3-1-0041 | Most CCLs define one important component of our risk acceptance criter |
| many-to-one | GDM-FSF-v3-0-0054 | 2 | GDM-FSF-v3-1-0044, GDM-FSF-v3-1-0073 | When a model reaches an alert threshold for a CCL, we will assess the  |
| many-to-one | GDM-FSF-v3-0-0038 | 2 | GDM-FSF-v3-1-0047, GDM-FSF-v3-1-0055 | To identify meaningful new capabilities or material increases in perfo |
| many-to-one | GDM-FSF-v3-0-0043-a | 2 | GDM-FSF-v3-1-0048, GDM-FSF-v3-1-0049 | Identification: As explained above, we have identified risk domains wh |
| many-to-one | GDM-FSF-v3-0-0043-b | 2 | GDM-FSF-v3-1-0050, GDM-FSF-v3-1-0051 | As part of our broader research into frontier AI models, we continue t |
| many-to-one | GDM-FSF-v3-0-0044-d | 2 | GDM-FSF-v3-1-0063, GDM-FSF-v3-1-0064 | We conduct further analysis, including reviewing model independent inf |
| many-to-one | GDM-FSF-v3-0-0046 | 2 | GDM-FSF-v3-1-0065, GDM-FSF-v3-1-0066 | Our approach to model evaluations and risk assessments described above |
| many-to-one | GDM-FSF-v3-0-0075 | 2 | GDM-FSF-v3-1-0103, GDM-FSF-v3-1-0104 | Note: Assessing frontier AI capabilities and corresponding severe risk |
| many-to-one | GDM-FSF-v3-0-0089 | 2 | GDM-FSF-v3-1-0121, GDM-FSF-v3-1-0122 | In other words, "security level N" indicates security controls and det |
| many-to-one | GDM-FSF-v3-0-0132 | 2 | GDM-FSF-v3-1-0166, GDM-FSF-v3-1-0167 | Security mitigations against exfiltration risk are important for model |
| many-to-one | GDM-FSF-v3-0-0144 | 2 | GDM-FSF-v3-1-0182, GDM-FSF-v3-1-0183 | Post-deployment processes: our safety cases and mitigations may be upd |
| many-to-one | GDM-FSF-v3-0-0147 | 2 | GDM-FSF-v3-1-0188, GDM-FSF-v3-1-0195 | The table below details a set of ML R&D CCLs we have identified that m |
| alternates | GDM-FSF-v3-1-0085 | — | chose GDM-FSF-v3-0-0063, also considered GDM-FSF-v3-0-0065 | For models reaching CCLs, the residual risk assessment will be informe |
| alternates | GDM-FSF-v3-1-0137 | — | chose GDM-FSF-v3-0-0103, also considered GDM-FSF-v3-0-0104 | Post-deployment processes: our residual risk assessments, safety cases |
| alternates | GDM-FSF-v3-1-0145 | — | chose GDM-FSF-v3-0-0108, also considered GDM-FSF-v3-0-0109 | We recommend a security level for each CCL, which reflects our assessm |
| alternates | GDM-FSF-v3-1-0151 | — | chose GDM-FSF-v3-0-0115, also considered GDM-FSF-v3-0-0116 | Security level 2+ The difficulty of building defenses against certain  |
| alternates | GDM-FSF-v3-1-0158 | — | chose GDM-FSF-v3-0-0120, also considered GDM-FSF-v3-0-0121 | Security level 2+ Models able to greatly assist cyber attack might be  |
| alternates | GDM-FSF-v3-1-0163 | — | chose GDM-FSF-v3-0-0125, also considered GDM-FSF-v3-0-0129 | Security level 2+ The lower velocity of harm scenarios associated with |
| alternates | GDM-FSF-v3-1-0198 | — | chose GDM-FSF-v3-0-0152, also considered GDM-FSF-v3-0-0153 | Security level 3 Unrestricted access to models at this level of capabi |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | GDM-FSF-v3-1-0040 | This update to the Framework introduces "Tracked Capability Levels | GDM-FSF-v3-0-0032 | For misalignment risk, we outline an exploratory approach that foc |
| 0.00 | GDM-FSF-v3-1-0065 | Actionable insights from these processes allow us to enhance our t | GDM-FSF-v3-0-0046 | Our approach to model evaluations and risk assessments described a |
| 0.00 | GDM-FSF-v3-1-0189 | The Stealth and Situational Awareness TCL is defined as follows: | GDM-FSF-v3-0-0169 | Accordingly, we do not indicate security mitigations for models at |
| 0.03 | GDM-FSF-v3-1-0102 | We assess that the level of security applied is adequate, e.g. bas | GDM-FSF-v3-0-0074 | Because the CCLs for misalignment risk are exploratory and intende |
| 0.03 | GDM-FSF-v3-1-0192 | This assessment may take into account models' alignment propensiti | GDM-FSF-v3-0-0171 | Automated monitoring: monitoring system to detect illicit use of i |
| 0.04 | GDM-FSF-v3-1-0047 | We identify potential risks that could stem from our models and an | GDM-FSF-v3-0-0038 | To identify meaningful new capabilities or material increases in p |
| 0.05 | GDM-FSF-v3-1-0057 | To understand if such a change in capability in the subsequent ver | GDM-FSF-v3-0-0041 | Data from these evaluations are collected and analyzed to give us  |
| 0.05 | GDM-FSF-v3-1-0100 | We assess that the deployment mitigations have brought the residua | GDM-FSF-v3-0-0074 | Because the CCLs for misalignment risk are exploratory and intende |
| 0.06 | GDM-FSF-v3-1-0046 | The first part of our risk management process is risk identificati | GDM-FSF-v3-0-0042 | At a high level, our risk assessment involves the following steps  |
| 0.06 | GDM-FSF-v3-1-0052 | To understand whether a model may, without appropriate mitigations | GDM-FSF-v3-0-0044-a | Analysis: Central to our model evaluations are "early warning eval |
| 0.06 | GDM-FSF-v3-1-0191 | When a model has reached this TCL, we will carry out periodic resi | GDM-FSF-v3-0-0171 | Automated monitoring: monitoring system to detect illicit use of i |
| 0.07 | GDM-FSF-v3-1-0194 | If the risk assessment deems the residual risk from internal deplo | GDM-FSF-v3-0-0166 | When models reach this capability level, one possible mitigation i |
| 0.07 | GDM-FSF-v3-1-0187 | We set a Stealth and Situational Awareness TCL that indicates a ba | GDM-FSF-v3-0-0165 | Here we describe an approach for addressing misalignment risk that |
| 0.07 | GDM-FSF-v3-1-0099 | A model for which the inherent risk assessment indicates the TCL f | GDM-FSF-v3-0-0074 | Because the CCLs for misalignment risk are exploratory and intende |
| 0.08 | GDM-FSF-v3-1-0186 | We take a tiered approach to addressing ML R&D and misalignment ri | GDM-FSF-v3-0-0164 | Misalignment can pose a number of risks. In the context of the Fra |
| 0.10 | GDM-FSF-v3-1-0163 | Security level 2+ The lower velocity of harm scenarios associated  | GDM-FSF-v3-0-0125 | Security level 2 |
| 0.10 | GDM-FSF-v3-1-0041 | TCLs are meant to capture significant risks that may manifest at a | GDM-FSF-v3-0-0033 | Most CCLs define one important component of our risk acceptance cr |

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| GDM-FSF-v3-1-0013 | Overview | Please refer to the Glossary at the end of this document for definitions used in |
| GDM-FSF-v3-1-0114 | 2.1.1 Security Mitigations | Using Google's Secure AI Framework (SAIF) and Google's common security infrastru |
| GDM-FSF-v3-1-0115 | 2.1.1 Security Mitigations | SAIF is a defense-in-depth approach that embeds security into every layer of our |
| GDM-FSF-v3-1-0116 | 2.1.1 Security Mitigations | SAIF is premised on six core elements: strong security foundations, detection an |
| GDM-FSF-v3-1-0118 | 2.1.1 Security Mitigations | We also define and recommend "Security Level 2+," which uses RAND Security Level |
| GDM-FSF-v3-1-0119 | 2.1.1 Security Mitigations | These additional measures may include, for example: dedicated insider risk teams |
| GDM-FSF-v3-1-0141 | 2.1.2 Deployment Mitigations | See section 5 of https://arxiv.org/abs/2504.01849. |
| GDM-FSF-v3-1-0142 | 2.1.2 Deployment Mitigations | While we monitor for potential future risks related to insider misuse, our curre |
| GDM-FSF-v3-1-0143 | 2.1.2 Deployment Mitigations | At this stage, additional mitigations beyond these established safeguards are no |
| GDM-FSF-v3-1-0177 | 3.1.2 Deployment Mitigations | Where the model has reached a CCL, the residual risk assessment will be suppleme |
| GDM-FSF-v3-1-0178 | 3.1.2 Deployment Mitigations | While the RAND framework is not specifically designed to address this case, we i |
| GDM-FSF-v3-1-0179 | 3.1.2 Deployment Mitigations | See section 6 of https://arxiv.org/abs/2504.01849. |
| GDM-FSF-v3-1-0225 | 5.3 Past Updates and Changes | Introduced CBRN TCLs and outlined mitigation and risk acceptance process. |
| GDM-FSF-v3-1-0226 | 5.3 Past Updates and Changes | Incorporated the previous exploratory Misalignment risk domain into a combined M |
| GDM-FSF-v3-1-0227 | 5.3 Past Updates and Changes | Outlined enhanced level of security for CBRN, Cyber and Harmful Manipulation CCL |
| GDM-FSF-v3-1-0228 | 5.3 Past Updates and Changes | Included more detail on our risk management process. |
| GDM-FSF-v3-1-0229 | 5.3 Past Updates and Changes | Included description of our internal governance structure. |
| GDM-FSF-v3-1-0230 | 5.3 Past Updates and Changes | Introduced a glossary. |
| GDM-FSF-v3-1-0231 | 5.3 Past Updates and Changes | Version 3.0 (September 22, 2025) |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**16 of 194 prior units (8%).**

| prior section heading | orphaned units |
|---|---|
| 1.3 Outline of Our Risk Assessment Process | 3 |
| 3.2.1 Machine Learning R&D | 2 |
| Section 4: Misalignment (Exploratory Approach) | 2 |
| 1.3 Outline of Our Risk Assessment Process / fn4 | 1 |
| 1.3 Outline of Our Risk Assessment Process / Note on ML R&D CCLs | 1 |
| 1.5 Evaluating Mitigations / fn5 | 1 |
| 2.2 Misuse Critical Capability Levels | 1 |
| Table 2.2.1.a: CBRN CCLs and Security Mitigations | 1 |
| Table 2.2.2.a: Cyber CCLs and Security Mitigations | 1 |
| Footnotes | 1 |
| Table 2.2.3.a: Harmful Manipulation CCLs and Security Mitigations | 1 |
| Table 3.2.1.a: Machine Learning R&D CCLs and Security Mitigations | 1 |
