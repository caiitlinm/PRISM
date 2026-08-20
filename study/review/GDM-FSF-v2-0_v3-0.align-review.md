# Stage 6 alignment review — GDM-FSF-v2-0_v3-0

Prior **138** units · target **194** units · **225** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 194 | 100% |
| Aligned to a prior unit | 136 | 70% |
| `prior_unit_id: NONE` | 58 | 30% |
| Removal candidates | 31 | — |
| Prior units serving >1 target (many-to-one) | 28 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | GDM-FSF-v2-0-0057 | 6 | GDM-FSF-v3-0-0043-a, GDM-FSF-v3-0-0107, GDM-FSF-v3-0-0113, GDM-FSF-v3-0-0118, GDM-FSF-v3-0-0123, GDM-FSF-v3-0-0147 | The table below details a set of CCLs we have identified through ongoi |
| many-to-one | GDM-FSF-v2-0-0053 | 5 | GDM-FSF-v3-0-0063, GDM-FSF-v3-0-0095, GDM-FSF-v3-0-0096, GDM-FSF-v3-0-0097, GDM-FSF-v3-0-0137 | Assessing the robustness of these mitigations against the risk posed t |
| many-to-one | GDM-FSF-v2-0-0041 | 3 | GDM-FSF-v3-0-0026, GDM-FSF-v3-0-0080, GDM-FSF-v3-0-0130 | This section describes our mitigation approach for models that pose ri |
| many-to-one | GDM-FSF-v2-0-0054 | 3 | GDM-FSF-v3-0-0069-b, GDM-FSF-v3-0-0101, GDM-FSF-v3-0-0142 | Pre-deployment review of safety case: general availability deployment  |
| many-to-one | GDM-FSF-v2-0-0001 | 2 | GDM-FSF-v3-0-0001, GDM-FSF-v3-0-0020 | The Frontier Safety Framework is a set of protocols that aims to addre |
| many-to-one | GDM-FSF-v2-0-0002 | 2 | GDM-FSF-v3-0-0002, GDM-FSF-v3-0-0021 | It is intended to complement Google’s existing suite of AI responsibil |
| many-to-one | GDM-FSF-v2-0-0008 | 2 | GDM-FSF-v3-0-0007, GDM-FSF-v3-0-0047 | Where appropriate, involve external parties to help inform and guide o |
| many-to-one | GDM-FSF-v2-0-0009 | 2 | GDM-FSF-v3-0-0008, GDM-FSF-v3-0-0023 | In version 2.0 of the Framework, we specify protocols for the detectio |
| many-to-one | GDM-FSF-v2-0-0025 | 2 | GDM-FSF-v3-0-0025, GDM-FSF-v3-0-0036 | We also intend to evaluate any of these models that could indicate an  |
| many-to-one | GDM-FSF-v2-0-0064 | 2 | GDM-FSF-v3-0-0027, GDM-FSF-v3-0-0114 | CBRN uplift 1: Can be used to significantly assist a low-resourced act |
| many-to-one | GDM-FSF-v2-0-0068 | 2 | GDM-FSF-v3-0-0028, GDM-FSF-v3-0-0119 | Cyber autonomy level 1: Can be used to drastically reduce the cost (e. |
| many-to-one | GDM-FSF-v2-0-0078 | 2 | GDM-FSF-v3-0-0030, GDM-FSF-v3-0-0151 | Machine Learning R&D uplift level 1: Can or has been used to accelerat |
| many-to-one | GDM-FSF-v2-0-0080 | 2 | GDM-FSF-v3-0-0031, GDM-FSF-v3-0-0153 | Unrestricted access to models at this level of capability could signif |
| many-to-one | GDM-FSF-v2-0-0100 | 2 | GDM-FSF-v3-0-0032, GDM-FSF-v3-0-0165 | An initial mitigation approach focuses on detecting when models might  |
| many-to-one | GDM-FSF-v2-0-0024 | 2 | GDM-FSF-v3-0-0034, GDM-FSF-v3-0-0035 | We intend to evaluate our most powerful frontier models regularly to c |
| many-to-one | GDM-FSF-v2-0-0031 | 2 | GDM-FSF-v3-0-0045, GDM-FSF-v3-0-0054 | When a model reaches an alert threshold for a CCL, we will assess the  |
| many-to-one | GDM-FSF-v2-0-0040 | 2 | GDM-FSF-v3-0-0060, GDM-FSF-v3-0-0062 | The appropriateness and efficacy of applied mitigations should be revi |
| many-to-one | GDM-FSF-v2-0-0062 | 2 | GDM-FSF-v3-0-0070, GDM-FSF-v3-0-0111 | This may occur if, for example, a model does not possess capabilities  |
| many-to-one | GDM-FSF-v2-0-0042 | 2 | GDM-FSF-v3-0-0081, GDM-FSF-v3-0-0131 | There are two categories of mitigations to address models with misuse  |
| many-to-one | GDM-FSF-v2-0-0044 | 2 | GDM-FSF-v3-0-0083, GDM-FSF-v3-0-0084 | For deployment mitigations, we specify a standard process for applying |
| many-to-one | GDM-FSF-v2-0-0045 | 2 | GDM-FSF-v3-0-0085, GDM-FSF-v3-0-0132 | Security mitigations against exfiltration risk are important for model |
| many-to-one | GDM-FSF-v2-0-0047 | 2 | GDM-FSF-v3-0-0087, GDM-FSF-v3-0-0133 | Here, we rely on the RAND framework to articulate the level of securit |
| many-to-one | GDM-FSF-v2-0-0048 | 2 | GDM-FSF-v3-0-0089, GDM-FSF-v3-0-0090 | When we reference RAND security levels, we are referring to the securi |
| many-to-one | GDM-FSF-v2-0-0050 | 2 | GDM-FSF-v3-0-0092, GDM-FSF-v3-0-0134 | The following deployment mitigation process will be applied to models  |
| many-to-one | GDM-FSF-v2-0-0051 | 2 | GDM-FSF-v3-0-0093, GDM-FSF-v3-0-0135 | Development and assessment of mitigations: safeguards and an accompany |
| many-to-one | GDM-FSF-v2-0-0052 | 2 | GDM-FSF-v3-0-0094, GDM-FSF-v3-0-0136 | Developing and improving a suite of safeguards targeting the capabilit |
| many-to-one | GDM-FSF-v2-0-0055 | 2 | GDM-FSF-v3-0-0103, GDM-FSF-v3-0-0144 | Post-deployment review of safety case: the safety case will be updated |
| many-to-one | GDM-FSF-v2-0-0059 | 2 | GDM-FSF-v3-0-0108, GDM-FSF-v3-0-0148 | We recommend a security level to each of these CCLs, which reflect our |
| alternates | GDM-FSF-v3-0-0003 | — | chose GDM-FSF-v2-0-0003, also considered GDM-FSF-v2-0-0004 | The Framework is informed by the broader conversation on Frontier AI S |
| alternates | GDM-FSF-v3-0-0009 | — | chose GDM-FSF-v2-0-0010, also considered GDM-FSF-v2-0-0011 | The Framework addresses misuse risk, risks from machine learning resea |
| alternates | GDM-FSF-v3-0-0011 | — | chose GDM-FSF-v2-0-0013, also considered GDM-FSF-v2-0-0014 | The safety and security of frontier AI models is a global public good. |
| alternates | GDM-FSF-v3-0-0014 | — | chose GDM-FSF-v2-0-0017, also considered GDM-FSF-v2-0-0018 | The Framework is based on early and evolving research. We may change o |
| alternates | GDM-FSF-v3-0-0028 | — | chose GDM-FSF-v2-0-0068, also considered GDM-FSF-v2-0-0073 | Cyber: Risks of models assisting in the development, preparation, and/ |
| alternates | GDM-FSF-v3-0-0044-d | — | chose GDM-FSF-v2-0-0029, also considered GDM-FSF-v2-0-0030 | We conduct further analysis, including reviewing model independent inf |
| alternates | GDM-FSF-v3-0-0119 | — | chose GDM-FSF-v2-0-0068, also considered GDM-FSF-v2-0-0073 | Cyber uplift level 1: Provides sufficient uplift with high impact cybe |
| alternates | GDM-FSF-v3-0-0120 | — | chose GDM-FSF-v2-0-0069, also considered GDM-FSF-v2-0-0074 | Security level 2 |
| alternates | GDM-FSF-v3-0-0121 | — | chose GDM-FSF-v2-0-0075, also considered GDM-FSF-v2-0-0070 | Models able to greatly assist cyber attack might be of interest to wel |
| alternates | GDM-FSF-v3-0-0122 | — | chose GDM-FSF-v2-0-0071, also considered GDM-FSF-v2-0-0076 | However, the potential for automated cyber-defense and social adaptati |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | GDM-FSF-v3-0-0025 | We describe three sets of CCLs: misuse CCLs, machine learning R&D  | GDM-FSF-v2-0-0025 | We also intend to evaluate any of these models that could indicate |
| 0.00 | GDM-FSF-v3-0-0034 | For each risk domain, we conduct aspects of our risk assessment at | GDM-FSF-v2-0-0024 | We intend to evaluate our most powerful frontier models regularly  |
| 0.00 | GDM-FSF-v3-0-0053 | We apply safety and security mitigations throughout the lifecycle  | GDM-FSF-v2-0-0023 | delineating when such capability becomes present, and subsequently |
| 0.00 | GDM-FSF-v3-0-0127 | Mitigations at this level may include model access management, phy | GDM-FSF-v2-0-0091 | For example, through the use of a self-replicating CBRN agent. Com |
| 0.00 | GDM-FSF-v3-0-0169 | Accordingly, we do not indicate security mitigations for models at | GDM-FSF-v2-0-0097 | While we do not express any opinion here about how likely it is fo |
| 0.03 | GDM-FSF-v3-0-0175 | The process will involve (i) an assessment of the Framework's appr | GDM-FSF-v2-0-0117 | The Google DeepMind AGI Safety Council will periodically review th |
| 0.03 | GDM-FSF-v3-0-0027 | CBRN: Risks of models assisting in the development, preparation, a | GDM-FSF-v2-0-0064 | CBRN uplift 1: Can be used to significantly assist a low-resourced |
| 0.03 | GDM-FSF-v3-0-0123 | This risk domain focuses on risks of models with high manipulative | GDM-FSF-v2-0-0057 | The table below details a set of CCLs we have identified through o |
| 0.03 | GDM-FSF-v3-0-0178 | Update our testing and mitigation approaches, where needed to ensu | GDM-FSF-v2-0-0129 | Updated set of risks and mitigations: There may be additional risk |
| 0.04 | GDM-FSF-v3-0-0028 | Cyber: Risks of models assisting in the development, preparation,  | GDM-FSF-v2-0-0068 | Cyber autonomy level 1: Can be used to drastically reduce the cost |
| 0.04 | GDM-FSF-v3-0-0031 | Such capabilities may serve as a substantial cross-cutting risk fa | GDM-FSF-v2-0-0080 | Unrestricted access to models at this level of capability could si |
| 0.05 | GDM-FSF-v3-0-0035 | We conduct a risk assessment for the first external deployment of  | GDM-FSF-v2-0-0024 | We intend to evaluate our most powerful frontier models regularly  |
| 0.06 | GDM-FSF-v3-0-0060 | We will use various processes to evaluate the effectiveness and li | GDM-FSF-v2-0-0040 | The appropriateness and efficacy of applied mitigations should be  |
| 0.06 | GDM-FSF-v3-0-0089 | In other words, "security level N" indicates security controls and | GDM-FSF-v2-0-0048 | When we reference RAND security levels, we are referring to the se |
| 0.06 | GDM-FSF-v3-0-0105 | This process is designed to ensure that residual risk remains at a | GDM-FSF-v2-0-0056 | The safeguards for the model may be updated as well to ensure cont |
| 0.07 | GDM-FSF-v3-0-0036 | For subsequent versions of the model, we conduct a further risk as | GDM-FSF-v2-0-0025 | We also intend to evaluate any of these models that could indicate |
| 0.07 | GDM-FSF-v3-0-0119 | Cyber uplift level 1: Provides sufficient uplift with high impact  | GDM-FSF-v2-0-0068 | Cyber autonomy level 1: Can be used to drastically reduce the cost |
| 0.07 | GDM-FSF-v3-0-0164 | Misalignment can pose a number of risks. In the context of the Fra | GDM-FSF-v2-0-0096 | By "deceptive alignment," we mean the risk that AI systems purpose |
| 0.08 | GDM-FSF-v3-0-0030 | For machine learning R&D risk, we define CCLs that identify when M | GDM-FSF-v2-0-0078 | Machine Learning R&D uplift level 1: Can or has been used to accel |
| 0.08 | GDM-FSF-v3-0-0126 | Here, and in other misuse CCLs, we intend this to mean relative to | GDM-FSF-v2-0-0094 | Relative to the counterfactual of using 2024 AI technology and too |
| 0.08 | GDM-FSF-v3-0-0174 | The Frontier Safety Framework will be updated at least once a year | GDM-FSF-v2-0-0125 | We expect the Framework to evolve substantially as our understandi |
| 0.08 | GDM-FSF-v3-0-0069-b | This is required only for external deployment, not further develop | GDM-FSF-v2-0-0054 | Pre-deployment review of safety case: general availability deploym |
| 0.08 | GDM-FSF-v3-0-0113 | This risk domain focuses on risks of models assisting in the devel | GDM-FSF-v2-0-0057 | The table below details a set of CCLs we have identified through o |
| 0.08 | GDM-FSF-v3-0-0118 | This risk domain focuses on risks of models assisting in the devel | GDM-FSF-v2-0-0057 | The table below details a set of CCLs we have identified through o |
| 0.08 | GDM-FSF-v3-0-0150 | These capabilities may indicate a heightened ability to undermine  | GDM-FSF-v2-0-0081 | The exfiltration of such a model may therefore have a significant  |
| 0.09 | GDM-FSF-v3-0-0044-d | We conduct further analysis, including reviewing model independent | GDM-FSF-v2-0-0029 | Where necessary, early warning evaluations may be supplemented by  |
| 0.09 | GDM-FSF-v3-0-0096 | How much the risk has been reduced by mitigations. For example, wh | GDM-FSF-v2-0-0053 | Assessing the robustness of these mitigations against the risk pos |

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| GDM-FSF-v3-0-0156 | Footnotes | The same caveats regarding security levels for misuse CCLs apply. |
| GDM-FSF-v3-0-0157 | Footnotes | This level may include mitigations aligned with SL 2, plus additional mitigation |
| GDM-FSF-v3-0-0163 | Footnotes | This level may include mitigations aligned with SL 2 and 3, plus additional miti |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**8 of 138 prior units (6%).**

| prior section heading | orphaned units |
|---|---|
| Table 1: Misuse CCLs and Security Mitigations | 4 |
| Frontier Safety Framework | 2 |
| 2 - Assessing the Capabilities of Frontier Models | 1 |
| Misuse Critical Capability Levels | 1 |
