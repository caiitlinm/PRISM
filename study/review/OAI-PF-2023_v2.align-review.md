# Stage 6 alignment review — OAI-PF-2023_v2

Prior **250** units · target **372** units · **379** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 372 | 100% |
| Aligned to a prior unit | 160 | 43% |
| `prior_unit_id: NONE` | 212 | 57% |
| Removal candidates | 7 | — |
| Prior units serving >1 target (many-to-one) | 35 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | OAI-PF-2023-0011 | 15 | OAI-PF-v2-0009, OAI-PF-v2-0024, OAI-PF-v2-0025, OAI-PF-v2-0026, OAI-PF-v2-0058, OAI-PF-v2-0060… | Establishing safety baselines. Only models with a post-mitigation scor |
| many-to-one | OAI-PF-2023-0132 | 7 | OAI-PF-v2-0123, OAI-PF-v2-0160, OAI-PF-v2-0164, OAI-PF-v2-0167, OAI-PF-v2-0184, OAI-PF-v2-0268… | As a result, these mitigations might span increasing compartmentalizat |
| many-to-one | OAI-PF-2023-0021 | 5 | OAI-PF-v2-0028, OAI-PF-v2-0220, OAI-PF-v2-0221, OAI-PF-v2-0223, OAI-PF-v2-0249 | Creating a cross-functional advisory body. We are creating a Safety Ad |
| many-to-one | OAI-PF-2023-0031 | 4 | OAI-PF-v2-0012, OAI-PF-v2-0018, OAI-PF-v2-0021, OAI-PF-v2-0053 | In this section, we identify the categories of risks that we will be t |
| many-to-one | OAI-PF-2023-0108 | 4 | OAI-PF-v2-0052, OAI-PF-v2-0097, OAI-PF-v2-0098, OAI-PF-v2-0102 | Therefore, as a part of our Governance process (described later in thi |
| many-to-one | OAI-PF-2023-0225 | 4 | OAI-PF-v2-0137, OAI-PF-v2-0190, OAI-PF-v2-0218, OAI-PF-v2-0219 | Audits: Scorecard evaluations (and corresponding mitigations) will be  |
| many-to-one | OAI-PF-2023-0038 | 3 | OAI-PF-v2-0005, OAI-PF-v2-0112, OAI-PF-v2-0118 | Chemical, Biological, Nuclear, and Radiological (CBRN) threats |
| many-to-one | OAI-PF-2023-0033 | 3 | OAI-PF-v2-0008, OAI-PF-v2-0054, OAI-PF-v2-0056 | Each of the Tracked Risk Categories comes with a gradation scale. |
| many-to-one | OAI-PF-2023-0121 | 3 | OAI-PF-v2-0023, OAI-PF-v2-0130, OAI-PF-v2-0143 | We will be running these evaluations continually, i.e., as often as ne |
| many-to-one | OAI-PF-2023-0017 | 3 | OAI-PF-v2-0055, OAI-PF-v2-0174, OAI-PF-v2-0222 | This includes conducting research, evaluations, monitoring, and foreca |
| many-to-one | OAI-PF-2023-0012 | 3 | OAI-PF-v2-0068, OAI-PF-v2-0079, OAI-PF-v2-0090 | In addition, we will ensure Security is appropriately tailored to any  |
| many-to-one | OAI-PF-2023-0100 | 3 | OAI-PF-v2-0091, OAI-PF-v2-0103, OAI-PF-v2-0108 | Model can profitably survive and replicate in the wild given minimal h |
| many-to-one | OAI-PF-2023-0217 | 3 | OAI-PF-v2-0151, OAI-PF-v2-0172, OAI-PF-v2-0188 | The SAG will be responsible for assessing the merits of each case subm |
| many-to-one | OAI-PF-2023-0181 | 3 | OAI-PF-v2-0159, OAI-PF-v2-0340, OAI-PF-v2-0345 | If we reach (or are forecasted to reach) at least “high” pre-mitigatio |
| many-to-one | OAI-PF-2023-0182 | 3 | OAI-PF-v2-0163, OAI-PF-v2-0205, OAI-PF-v2-0341 | This is defined as establishing network and compute security controls  |
| many-to-one | OAI-PF-2023-0194 | 3 | OAI-PF-v2-0207, OAI-PF-v2-0208, OAI-PF-v2-0248 | We also establish an operational structure to oversee our procedural c |
| many-to-one | OAI-PF-2023-0188 | 3 | OAI-PF-v2-0278, OAI-PF-v2-0296, OAI-PF-v2-0303 | (Note that a potentially effective mitigation in this context could be |
| many-to-one | OAI-PF-2023-0005 | 2 | OAI-PF-v2-0002, OAI-PF-v2-0263 | This Preparedness Framework is a living document that distills our lat |
| many-to-one | OAI-PF-2023-0008 | 2 | OAI-PF-v2-0004, OAI-PF-v2-0022 | Tracking catastrophic risk level via evaluations. We will be building  |
| many-to-one | OAI-PF-2023-0226 | 2 | OAI-PF-v2-0027, OAI-PF-v2-0217 | External access: We will also continue to enable external research and |
| many-to-one | OAI-PF-2023-0204 | 2 | OAI-PF-v2-0029, OAI-PF-v2-0261 | The OpenAI Board of Directors (BoD), as the ultimate governing body of |
| many-to-one | OAI-PF-2023-0109 | 2 | OAI-PF-v2-0099, OAI-PF-v2-0101 | In addition, we will invest in staying abreast of relevant research de |
| many-to-one | OAI-PF-2023-0091 | 2 | OAI-PF-v2-0114, OAI-PF-v2-0304 | Model autonomy enables actors to run scaled misuse that can adapt to e |
| many-to-one | OAI-PF-2023-0126 | 2 | OAI-PF-v2-0134, OAI-PF-v2-0157 | For this reason, we will be investing in efforts that help create an i |
| many-to-one | OAI-PF-2023-0122 | 2 | OAI-PF-v2-0145, OAI-PF-v2-0146 | This would include whenever there is a >2x effective compute increase  |
| many-to-one | OAI-PF-2023-0022 | 2 | OAI-PF-v2-0148, OAI-PF-v2-0250 | SAG responsibilities will thus include overseeing the assessment of th |
| many-to-one | OAI-PF-2023-0112 | 2 | OAI-PF-v2-0149, OAI-PF-v2-0173 | As a part of our Preparedness Framework, we will maintain a dynamic (i |
| many-to-one | OAI-PF-2023-0130 | 2 | OAI-PF-v2-0156, OAI-PF-v2-0274 | A central part of meeting our safety baselines is implementing mitigat |
| many-to-one | OAI-PF-2023-0131 | 2 | OAI-PF-v2-0158, OAI-PF-v2-0273 | Our mitigation strategy will involve both containment measures, which  |
| many-to-one | OAI-PF-2023-0018 | 2 | OAI-PF-v2-0166, OAI-PF-v2-0252 | These reports will include a summary of the latest evidence and make r |
| many-to-one | OAI-PF-2023-0026 | 2 | OAI-PF-v2-0185, OAI-PF-v2-0196 | We recognize other organizations for contributing to action in this sp |
| many-to-one | OAI-PF-2023-0219 | 2 | OAI-PF-v2-0189, OAI-PF-v2-0193 | The OpenAI Leadership will make the final decision and be responsible  |
| many-to-one | OAI-PF-2023-0215 | 2 | OAI-PF-v2-0206, OAI-PF-v2-0266 | Fast-track: In the rare case that a severe risk rapidly develops (e.g. |
| many-to-one | OAI-PF-2023-0223 | 2 | OAI-PF-v2-0209, OAI-PF-v2-0216 | Internal visibility: The Preparedness Framework, reports and decisions |
| many-to-one | OAI-PF-2023-0201 | 2 | OAI-PF-v2-0256, OAI-PF-v2-0257 | SAG membership will rotate yearly. OpenAI leadership might choose to r |
| alternates | OAI-PF-v2-0004 | — | chose OAI-PF-2023-0008, also considered OAI-PF-2023-0036 | We currently focus this work on three areas of frontier capability, wh |
| alternates | OAI-PF-v2-0008 | — | chose OAI-PF-2023-0033, also considered OAI-PF-2023-0051 | In each area, we develop and maintain a threat model that identifies t |
| alternates | OAI-PF-v2-0021 | — | chose OAI-PF-2023-0031, also considered OAI-PF-2023-0008 | Decide where to focus – we use a holistic risk assessment to decide wh |
| alternates | OAI-PF-v2-0025 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0186 | We do not deploy models that reach a High capability threshold until t |
| alternates | OAI-PF-v2-0026 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0189 | If a model under development reaches a Critical capability threshold,  |
| alternates | OAI-PF-v2-0045 | — | chose OAI-PF-2023-0028, also considered OAI-PF-2023-0029 | Tracked Categories are those capabilities which we track most closely, |
| alternates | OAI-PF-v2-0053 | — | chose OAI-PF-2023-0031, also considered OAI-PF-2023-0106 | Research Categories are capabilities that, while they do not meet the  |
| alternates | OAI-PF-v2-0056 | — | chose OAI-PF-2023-0033, also considered OAI-PF-2023-0035 | Capability thresholds concretely describe things an AI system might be |
| alternates | OAI-PF-v2-0058 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0012 | Covered systems that cross this capability threshold are required to h |
| alternates | OAI-PF-v2-0060 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0190 | Critical capabilities require safeguards even during the development o |
| alternates | OAI-PF-v2-0067 | — | chose OAI-PF-2023-0073, also considered OAI-PF-2023-0074 | Significantly increased likelihood and frequency of biological or chem |
| alternates | OAI-PF-v2-0072 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0190 | Until we have specified safeguards and security controls that would me |
| alternates | OAI-PF-v2-0077 | — | chose OAI-PF-2023-0061, also considered OAI-PF-2023-0062 | Removing bottlenecks limiting malicious cyber activity may upset the c |
| alternates | OAI-PF-v2-0086 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0190 | Until we have specified safeguards and security controls standards tha |
| alternates | OAI-PF-v2-0092 | — | chose OAI-PF-2023-0103, also considered OAI-PF-2023-0101 | A major acceleration in the rate of AI R&D could rapidly increase the  |
| alternates | OAI-PF-v2-0093 | — | chose OAI-PF-2023-0101, also considered OAI-PF-2023-0104 | including risks to maintaining human control of the AI system itself. |
| alternates | OAI-PF-v2-0094 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0190 | Until we have specified safeguards and security controls that would me |
| alternates | OAI-PF-v2-0097 | — | chose OAI-PF-2023-0108, also considered OAI-PF-2023-0109 | We call these Research Categories, and in these areas we will take the |
| alternates | OAI-PF-v2-0103 | — | chose OAI-PF-2023-0100, also considered OAI-PF-2023-0097 | ability for a model to execute a long-horizon sequence of actions suff |
| alternates | OAI-PF-v2-0131 | — | chose OAI-PF-2023-0119, also considered OAI-PF-2023-0120 | Our evaluations are intended to approximate the full capability that t |
| alternates | OAI-PF-v2-0149 | — | chose OAI-PF-2023-0112, also considered OAI-PF-2023-0113 | Prior to deployment, every covered model undergoes the suite of Scalab |
| alternates | OAI-PF-v2-0151 | — | chose OAI-PF-2023-0217, also considered OAI-PF-2023-0022 | The SAG reviews the Capabilities Report and decides on next steps. The |
| alternates | OAI-PF-v2-0159 | — | chose OAI-PF-2023-0181, also considered OAI-PF-2023-0132 | We first identify the plausible ways in which the associated risk of s |
| alternates | OAI-PF-v2-0172 | — | chose OAI-PF-2023-0217, also considered OAI-PF-2023-0198 | SAG is responsible for assessing whether the safeguards associated wit |
| alternates | OAI-PF-v2-0187 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0190 | Systems that reach Critical capability also require safeguards that su |
| alternates | OAI-PF-v2-0189 | — | chose OAI-PF-2023-0219, also considered OAI-PF-2023-0237 | SAG can find that it is confident that the safeguards sufficiently min |
| alternates | OAI-PF-v2-0202 | — | chose OAI-PF-2023-0193, also considered OAI-PF-2023-0026 | Models that have reached or are forecasted to reach Critical capabilit |
| alternates | OAI-PF-v2-0203 | — | chose OAI-PF-2023-0190, also considered OAI-PF-2023-0011 | Such models require additional safeguards (safety and security control |
| alternates | OAI-PF-v2-0207 | — | chose OAI-PF-2023-0194, also considered OAI-PF-2023-0177 | Effective implementation of the Preparedness Framework requires intern |
| alternates | OAI-PF-v2-0217 | — | chose OAI-PF-2023-0226, also considered OAI-PF-2023-0020 | Third-party evaluation of tracked model capabilities: If we deem that  |
| alternates | OAI-PF-v2-0220 | — | chose OAI-PF-2023-0021, also considered OAI-PF-2023-0225 | Independent expert opinions for evidence produced to SAG: The SAG may  |
| alternates | OAI-PF-v2-0249 | — | chose OAI-PF-2023-0021, also considered OAI-PF-2023-0022 | Overseeing the effective design, implementation, and adherence to the  |
| alternates | OAI-PF-v2-0250 | — | chose OAI-PF-2023-0022, also considered OAI-PF-2023-0217 | For each deployment in scope under the Preparedness Framework, reviewi |
| alternates | OAI-PF-v2-0259 | — | chose OAI-PF-2023-0203, also considered OAI-PF-2023-0219 | Making all final decisions, including accepting any residual risks and |
| alternates | OAI-PF-v2-0261 | — | chose OAI-PF-2023-0204, also considered OAI-PF-2023-0205 | The Safety and Security Committee (SSC) of the OpenAI Board of Directo |
| alternates | OAI-PF-v2-0264 | — | chose OAI-PF-2023-0213, also considered OAI-PF-2023-0214 | The SAG reviews proposed changes to the Preparedness Framework and mak |
| alternates | OAI-PF-v2-0272 | — | chose OAI-PF-2023-0011, also considered OAI-PF-2023-0190 | Systems that reach Critical capability also require sufficient safegua |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | OAI-PF-v2-0007 | AI Self-improvement capabilities that, in addition to unlocking he | OAI-PF-2023-0040 | Model autonomy |
| 0.00 | OAI-PF-v2-0008 | In each area, we develop and maintain a threat model that identifi | OAI-PF-2023-0033 | Each of the Tracked Risk Categories comes with a gradation scale. |
| 0.00 | OAI-PF-v2-0026 | If a model under development reaches a Critical capability thresho | OAI-PF-2023-0011 | Establishing safety baselines. Only models with a post-mitigation  |
| 0.00 | OAI-PF-v2-0027 | Build trust – we engage with subject–matter experts across and bey | OAI-PF-2023-0226 | External access: We will also continue to enable external research |
| 0.00 | OAI-PF-v2-0052 | We review and update Tracked Categories periodically or when we le | OAI-PF-2023-0108 | Therefore, as a part of our Governance process (described later in |
| 0.00 | OAI-PF-v2-0055 | SAG reviews and approves these threat models. | OAI-PF-2023-0017 | This includes conducting research, evaluations, monitoring, and fo |
| 0.00 | OAI-PF-v2-0060 | Critical capabilities require safeguards even during the developme | OAI-PF-2023-0011 | Establishing safety baselines. Only models with a post-mitigation  |
| 0.00 | OAI-PF-v2-0077 | Removing bottlenecks limiting malicious cyber activity may upset t | OAI-PF-2023-0061 | High-value exploits are generally against hardened platforms, scar |
| 0.00 | OAI-PF-v2-0088 | This milestone suggests AI self-improvement may be beginning to ac | OAI-PF-2023-0098 | Solving open-ended tasks offers an immediate speedup for AI resear |
| 0.00 | OAI-PF-v2-0089 | To meet the large-scale safety research, operations, and security  | OAI-PF-2023-0099 | However, this does not yet demonstrate the ability to orchestrate  |
| 0.00 | OAI-PF-v2-0092 | A major acceleration in the rate of AI R&D could rapidly increase  | OAI-PF-2023-0103 | If the model is able to conduct AI research fully autonomously, it |
| 0.00 | OAI-PF-v2-0093 | including risks to maintaining human control of the AI system itse | OAI-PF-2023-0101 | If the model is able to successfully replicate and survive or self |
| 0.00 | OAI-PF-v2-0097 | We call these Research Categories, and in these areas we will take | OAI-PF-2023-0108 | Therefore, as a part of our Governance process (described later in |
| 0.00 | OAI-PF-v2-0098 | Further developing the threat models for the area, | OAI-PF-2023-0108 | Therefore, as a part of our Governance process (described later in |
| 0.00 | OAI-PF-v2-0099 | Advancing the science of capability measurement in the area and in | OAI-PF-2023-0109 | In addition, we will invest in staying abreast of relevant researc |
| 0.00 | OAI-PF-v2-0123 | We build safeguards to prevent our models from assisting with high | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartmental |
| 0.00 | OAI-PF-v2-0134 | We incorporate this uncertainty into our assessments. We monitor t | OAI-PF-2023-0126 | For this reason, we will be investing in efforts that help create  |
| 0.00 | OAI-PF-v2-0141 | The Preparedness Framework applies to any new or updated deploymen | OAI-PF-2023-0044 | Our procedural commitments are triggered when any of the tracked r |
| 0.00 | OAI-PF-v2-0143 | every frontier model (e.g., OpenAI o1 or OpenAI o3) that we plan t | OAI-PF-2023-0121 | We will be running these evaluations continually, i.e., as often a |
| 0.00 | OAI-PF-v2-0145 | any significant change in the deployment conditions of an existing | OAI-PF-2023-0122 | This would include whenever there is a >2x effective compute incre |
| 0.00 | OAI-PF-v2-0146 | incremental updates or distilled models with unexpectedly signific | OAI-PF-2023-0122 | This would include whenever there is a >2x effective compute incre |
| 0.00 | OAI-PF-v2-0152 | Determine that the capability threshold has been crossed, and ther | OAI-PF-2023-0233 | The SAG Chair accepts the evidence supporting this new risk level, |
| 0.00 | OAI-PF-v2-0160 | For each of those, we then identify specific safeguards that eithe | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartmental |
| 0.00 | OAI-PF-v2-0164 | Appendix C provides illustrative examples of potential safeguards  | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartmental |
| 0.00 | OAI-PF-v2-0173 | The level of capability in the Tracked Category based on the Capab | OAI-PF-2023-0112 | As a part of our Preparedness Framework, we will maintain a dynami |
| 0.00 | OAI-PF-v2-0184 | The safeguards in place and their effectiveness based on the Safeg | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartmental |
| 0.00 | OAI-PF-v2-0185 | The baseline risk from other deployments, based on a review of any | OAI-PF-2023-0026 | We recognize other organizations for contributing to action in thi |
| 0.00 | OAI-PF-v2-0187 | Systems that reach Critical capability also require safeguards tha | OAI-PF-2023-0011 | Establishing safety baselines. Only models with a post-mitigation  |
| 0.00 | OAI-PF-v2-0205 | Our approach to Critical capabilities will need to be robust to bo | OAI-PF-2023-0182 | This is defined as establishing network and compute security contr |
| 0.00 | OAI-PF-v2-0207 | Effective implementation of the Preparedness Framework requires in | OAI-PF-2023-0194 | We also establish an operational structure to oversee our procedur |
| 0.00 | OAI-PF-v2-0208 | Clear internal decision-making practices. We have clear roles and  | OAI-PF-2023-0194 | We also establish an operational structure to oversee our procedur |
| 0.00 | OAI-PF-v2-0216 | Such disclosures about results and safeguards may be redacted or s | OAI-PF-2023-0223 | Internal visibility: The Preparedness Framework, reports and decis |
| 0.00 | OAI-PF-v2-0219 | We may seek this out in particular for models that are over a High | OAI-PF-2023-0225 | Audits: Scorecard evaluations (and corresponding mitigations) will |
| 0.00 | OAI-PF-v2-0250 | For each deployment in scope under the Preparedness Framework, rev | OAI-PF-2023-0022 | SAG responsibilities will thus include overseeing the assessment o |
| 0.00 | OAI-PF-v2-0268 | This Appendix provides illustrative examples of potential safeguar | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartmental |
| 0.00 | OAI-PF-v2-0272 | Systems that reach Critical capability also require sufficient saf | OAI-PF-2023-0011 | Establishing safety baselines. Only models with a post-mitigation  |
| 0.00 | OAI-PF-v2-0278 | Trust-based Access: The actors who gain access to the model will n | OAI-PF-2023-0188 | (Note that a potentially effective mitigation in this context coul |
| 0.02 | OAI-PF-v2-0138 | To assess the degree to which a covered system can reduce the barr | OAI-PF-2023-0154 | GPT vs search eval: Post-PhD professionals trained in biology (spe |
| 0.02 | OAI-PF-v2-0131 | Our evaluations are intended to approximate the full capability th | OAI-PF-2023-0119 | We want to ensure our understanding of pre-mitigation risk takes i |
| 0.02 | OAI-PF-v2-0022 | Measure capabilities associated with risks of severe harms – we ru | OAI-PF-2023-0008 | Tracking catastrophic risk level via evaluations. We will be build |

_87 further alignments below 0.10 overlap not shown._

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

| target | target excerpt | named alternate | that unit's excerpt |
|---|---|---|---|
| OAI-PF-v2-0001 | OpenAI’s mission is to ensure that AGI (artificial general intel | OAI-PF-2023-0023 | Finally, OpenAI’s primary fiduciary duty is to humanity, and we  |
| OAI-PF-v2-0011 | In this updated version of the Framework we also introduce a set | OAI-PF-2023-0031 | In this section, we identify the categories of risks that we wil |
| OAI-PF-v2-0017 | In choosing to set a high bar here, we aim to ensure that the mo | OAI-PF-2023-0007 | The central thesis behind our Preparedness Framework is that a r |
| OAI-PF-v2-0043 | This process draws on our own internal research and signals, and | OAI-PF-2023-0226 | External access: We will also continue to enable external resear |
| OAI-PF-v2-0044 | Where we determine that a capability presents a real risk of sev | OAI-PF-2023-0031 | In this section, we identify the categories of risks that we wil |
| OAI-PF-v2-0057 | High capability thresholds mean capabilities that significantly  | OAI-PF-2023-0035 | In general, “low” on this gradation scale is meant to indicate t |
| OAI-PF-v2-0059 | Critical capability thresholds mean capabilities that present a  | OAI-PF-2023-0035 | In general, “low” on this gradation scale is meant to indicate t |
| OAI-PF-v2-0062 | Threat models are informed both by our broader risk assessment p | OAI-PF-2023-0031 | In this section, we identify the categories of risks that we wil |
| OAI-PF-v2-0113 | Heighten safeguards (and consider further actions) in consultati | OAI-PF-2023-0012 | In addition, we will ensure Security is appropriately tailored t |
| OAI-PF-v2-0115 | We have separated self-improvement because it presents a distinc | OAI-PF-2023-0091 | Model autonomy enables actors to run scaled misuse that can adap |
| OAI-PF-v2-0126 | Persuasion: OpenAI prohibits the use of our products to manipula | OAI-PF-2023-0079 | Persuasion is focused on risks related to convincing people to c |
| OAI-PF-v2-0127 | We also continue to study the persuasive and relational capabili | OAI-PF-2023-0079 | Persuasion is focused on risks related to convincing people to c |
| OAI-PF-v2-0129 | Within our wider safety stack, our Preparedness Framework is spe | OAI-PF-2023-0079 | Persuasion is focused on risks related to convincing people to c |
| OAI-PF-v2-0155 | Recommend deep dive research: This is appropriate if SAG needs a | OAI-PF-2023-0225 | Audits: Scorecard evaluations (and corresponding mitigations) wi |
| OAI-PF-v2-0175 | Robustness: Malicious users cannot use the model to cause the se | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartment |
| OAI-PF-v2-0176 | Usage Monitoring: If a model does not refuse and provides assist | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartment |
| OAI-PF-v2-0177 | Trust-based Access: The actors who gain access to the model are  | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartment |
| OAI-PF-v2-0178 | Lack of Autonomous Capability: The model is not capable of carry | OAI-PF-2023-0093 | Model can take discrete actions if explicitly instructed to do s |
| OAI-PF-v2-0182 | System Architecture: The model can't take actions that cause har | OAI-PF-2023-0093 | Model can take discrete actions if explicitly instructed to do s |
| OAI-PF-v2-0213 | Public disclosures: We will release information about our Prepar | OAI-PF-2023-0226 | External access: We will also continue to enable external resear |
| OAI-PF-v2-0230 | Also, we are removing terms "low" and "medium" from the Framewor | OAI-PF-2023-0051 | Our current estimates of levels and thresholds for “medium” thro |
| OAI-PF-v2-0233 | Going forward we will handle risks related to persuasion outside | OAI-PF-2023-0079 | Persuasion is focused on risks related to convincing people to c |
| OAI-PF-v2-0234 | We are moving Nuclear and Radiological capabilities into Researc | OAI-PF-2023-0118 | In the end, coupling capabilities growth with robust safety solu |
| OAI-PF-v2-0244 | Deprioritize safety drills, as we are shifting our attention to  | OAI-PF-2023-0227 | Safety drills: A critical part of this process is to be prepared |
| OAI-PF-v2-0245 | Clarify our focus on marginal risk, including the context of oth | OAI-PF-2023-0026 | We recognize other organizations for contributing to action in t |
| OAI-PF-v2-0247 | For covered launches, SAG assesses residual risk in tracked area | OAI-PF-2023-0022 | SAG responsibilities will thus include overseeing the assessment |
| OAI-PF-v2-0260 | Resourcing the implementation of the Preparedness Framework (e.g | OAI-PF-2023-0219 | The OpenAI Leadership will make the final decision and be respon |
| OAI-PF-v2-0265 | We will review and potentially update the Preparedness Framework | OAI-PF-2023-0212 | If the Preparedness or any other team determines that any change |
| OAI-PF-v2-0276 | Robustness: Users cannot use the model to cause the harm because | OAI-PF-2023-0132 | As a result, these mitigations might span increasing compartment |
| OAI-PF-v2-0346 | Comprehensive Security Threat Models: Ensure OpenAI employs secu | OAI-PF-2023-0182 | This is defined as establishing network and compute security con |
| OAI-PF-v2-0350 | Continuous Monitoring and Validation: Ensure security threat mod | OAI-PF-2023-0182 | This is defined as establishing network and compute security con |
| OAI-PF-v2-0352 | Layered Security Architecture: Adopt a layered security strategy | OAI-PF-2023-0182 | This is defined as establishing network and compute security con |
| OAI-PF-v2-0355 | Principle of Least Privilege: Ensure access to systems and data  | OAI-PF-2023-0183 | increasing compartmentalization, including immediately restricti |
| OAI-PF-v2-0368 | Adversarial Testing and Red-Teaming: Conduct adversarial testing | OAI-PF-2023-0020 | In addition, Preparedness will also manage safety drills and coo |
| OAI-PF-v2-0370 | Independent Security Audits: Ensure security controls and practi | OAI-PF-2023-0225 | Audits: Scorecard evaluations (and corresponding mitigations) wi |

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

Nothing flagged.

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**156 of 250 prior units (62%).**

| prior section heading | orphaned units |
|---|---|
| Persuasion | 18 |
| Cybersecurity | 14 |
| CBRN | 14 |
| Model autonomy | 12 |
| Illustrative Scorecard (p15) | 12 |
| Tracked Risk Categories | 11 |
| Example scenario 1: “High” risk in persuasion | 9 |
| Example scenario 2: Forecasted “critical” risk in cybersecurity with fast-track process | 9 |
| Process | 8 |
| Introduction | 5 |
| Our Preparedness Framework contains five key elements | 5 |
| Pre-mitigation versus post-mitigation risk | 4 |
| Footnotes | 3 |
| How to read this document | 3 |
| Forecasting, "early warnings," and monitoring | 3 |
| Asset Protection | 3 |
| Restricting development | 3 |
| Parties in the Preparedness Framework operationalization process | 3 |
| Accountability | 3 |
| Unknown unknowns | 2 |

## Check 5 — Scorecard to per-category thresholds

**This check stands** (the p6 aggregation-rule graphic was excluded from the corpus; the p15 Scorecard is in). C03 `architecture_replaced` on this transition rests on this alignment alone.

| prior (scorecard) | prior excerpt | target | target excerpt |
|---|---|---|---|
| OAI-PF-2023-0112 | As a part of our Preparedness Framework, we will maintain a  | OAI-PF-v2-0149 | Prior to deployment, every covered model undergoes the suite |
| OAI-PF-2023-0112 | As a part of our Preparedness Framework, we will maintain a  | OAI-PF-v2-0173 | The level of capability in the Tracked Category based on the |
| OAI-PF-2023-0133 | Note: Below is only an illustrative template version of what | REMOVAL |  |

_16 scorecard units in the prior version; 2 appear in the crosswalk. Units 0133–0145 are an explicitly illustrative template carrying placeholder values, and should not align; 0112–0114 carry the architecture claim._
