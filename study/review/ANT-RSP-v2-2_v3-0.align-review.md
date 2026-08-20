# Stage 6 alignment review — ANT-RSP-v2-2_v3-0

Prior **348** units · target **278** units · **287** crosswalk rows.

Alignment decides which units are eligible for change codes at all. A prior unit that is neither aligned nor flagged as a removal is invisible to every later step.

## Check 1 — Counts

| Measure | n | % of target rows |
|---|---|---|
| Target rows | 278 | 100% |
| Aligned to a prior unit | 117 | 42% |
| `prior_unit_id: NONE` | 161 | 58% |
| Removal candidates | 9 | — |
| Prior units serving >1 target (many-to-one) | 21 | — |
| Target units with >1 prior (one-to-many) | 0 | — |

## Check 2 — Many-to-one groups, and targets with alternates

A prior unit serving several targets means the later version split it.

**One-to-many cannot occur and is not reported.** A2-align.md emits one row per target unit with a single `prior_unit_id`, so a target can never carry two priors; where more than one could be the counterpart, the alternates go in `alignment_note`. Those rows are listed below instead — they are the schema's actual representation of a merge.

| kind | unit | n | counterparts | excerpt |
|---|---|---|---|---|
| many-to-one | ANT-RSP-v2-2-0078 | 3 | ANT-RSP-v3-0-0026, ANT-RSP-v3-0-0115, ANT-RSP-v3-0-0124 | Below, we specify the Capability Thresholds and their corresponding Re |
| many-to-one | ANT-RSP-v2-2-0093 | 3 | ANT-RSP-v3-0-0080, ANT-RSP-v3-0-0082, ANT-RSP-v3-0-0083 | At minimum, the ASL-4 Security Standard (which would protect against m |
| many-to-one | ANT-RSP-v2-2-0147 | 3 | ANT-RSP-v3-0-0097, ANT-RSP-v3-0-0122, ANT-RSP-v3-0-0141 | First, we will compile a Capability Report that documents the findings |
| many-to-one | ANT-RSP-v2-2-0229 | 3 | ANT-RSP-v3-0-0199, ANT-RSP-v3-0-0200, ANT-RSP-v3-0-0201 | (3) reviewing major contracts (i.e., deployment partnerships) for cons |
| many-to-one | ANT-RSP-v2-2-0082 | 2 | ANT-RSP-v3-0-0005, ANT-RSP-v3-0-0027 | The Capability Thresholds summarized below are available in full in Ap |
| many-to-one | ANT-RSP-v2-2-0250 | 2 | ANT-RSP-v3-0-0019, ANT-RSP-v3-0-0156 | Expert input: We will solicit input from external experts in relevant  |
| many-to-one | ANT-RSP-v2-2-0085 | 2 | ANT-RSP-v3-0-0043, ANT-RSP-v3-0-0046 | The ASL-3 Deployment Standard and the ASL-3 Security Standard, which p |
| many-to-one | ANT-RSP-v2-2-0087 | 2 | ANT-RSP-v3-0-0051, ANT-RSP-v3-0-0053 | We expect this threshold will require the ASL-4 Deployment and Securit |
| many-to-one | ANT-RSP-v2-2-0067 | 2 | ANT-RSP-v3-0-0056, ANT-RSP-v3-0-0059 | We expect to continue refining our framework in response to future ris |
| many-to-one | ANT-RSP-v2-2-0092 | 2 | ANT-RSP-v3-0-0071, ANT-RSP-v3-0-0072 | AI R&D-5: The ability to cause dramatic acceleration in the rate of ef |
| many-to-one | ANT-RSP-v2-2-0149 | 2 | ANT-RSP-v3-0-0142, ANT-RSP-v3-0-0143 | In general, as noted in Sections 7.1.4 and 7.2.2, we will solicit both |
| many-to-one | ANT-RSP-v2-2-0148 | 2 | ANT-RSP-v3-0-0144, ANT-RSP-v3-0-0145 | The report will be escalated to the CEO and the Responsible Scaling Of |
| many-to-one | ANT-RSP-v2-2-0228 | 2 | ANT-RSP-v3-0-0197, ANT-RSP-v3-0-0198 | The Responsible Scaling Officer's duties will include (but are not lim |
| many-to-one | ANT-RSP-v2-2-0237 | 2 | ANT-RSP-v3-0-0205, ANT-RSP-v3-0-0209 | We will also establish a policy governing noncompliance reporting, whi |
| many-to-one | ANT-RSP-v2-2-0240 | 2 | ANT-RSP-v3-0-0207, ANT-RSP-v3-0-0208 | The Responsible Scaling Officer will regularly update the Board of Dir |
| many-to-one | ANT-RSP-v2-2-0247 | 2 | ANT-RSP-v3-0-0216, ANT-RSP-v3-0-0217 | The current version of the RSP is accessible at www.anthropic.com/rsp. |
| many-to-one | ANT-RSP-v2-2-0255 | 2 | ANT-RSP-v3-0-0218, ANT-RSP-v3-0-0220 | It is possible at some point in the future that another actor in the f |
| many-to-one | ANT-RSP-v2-2-0257 | 2 | ANT-RSP-v3-0-0219, ANT-RSP-v3-0-0221 | If we take this measure, however, we will also acknowledge the overall |
| many-to-one | ANT-RSP-v2-2-0256 | 2 | ANT-RSP-v3-0-0223, ANT-RSP-v3-0-0224 | In such a scenario, because the incremental increase in risk attributa |
| many-to-one | ANT-RSP-v2-2-0310 | 2 | ANT-RSP-v3-0-0231, ANT-RSP-v3-0-0237 | ASL definition changed: The term "ASL" now refers to groups of technic |
| many-to-one | ANT-RSP-v2-2-0345 | 2 | ANT-RSP-v3-0-0273, ANT-RSP-v3-0-0274 | ASL-3 Security: This update excludes both sophisticated insiders and s |
| alternates | ANT-RSP-v3-0-0001 | — | chose ANT-RSP-v2-2-0001, also considered ANT-RSP-v2-2-0031 | Our Responsible Scaling Policy (RSP) is our voluntary framework for ma |
| alternates | ANT-RSP-v3-0-0002 | — | chose ANT-RSP-v2-2-0002, also considered ANT-RSP-v2-2-0034 | We have always intended for our RSP to be a living document. We will c |
| alternates | ANT-RSP-v3-0-0004 | — | chose ANT-RSP-v2-2-0008, also considered ANT-RSP-v2-2-0011 | Our recommendations for industry-wide safety outline what it would tak |
| alternates | ANT-RSP-v3-0-0015 | — | chose ANT-RSP-v2-2-0265, also considered ANT-RSP-v2-2-0273 | Risk Reports are another new requirement. Risk Reports will provide de |
| alternates | ANT-RSP-v3-0-0042 | — | chose ANT-RSP-v2-2-0083, also considered ANT-RSP-v2-2-0293 | AI systems with the ability to significantly help individuals or group |
| alternates | ANT-RSP-v3-0-0050 | — | chose ANT-RSP-v2-2-0086, also considered ANT-RSP-v2-2-0295 | AI systems with the ability to significantly help threat actors (for e |
| alternates | ANT-RSP-v3-0-0068 | — | chose ANT-RSP-v2-2-0088, also considered ANT-RSP-v2-2-0092 | AI systems that can fully automate, or otherwise dramatically accelera |
| alternates | ANT-RSP-v3-0-0071 | — | chose ANT-RSP-v2-2-0092, also considered ANT-RSP-v2-2-0298 | Our working operationalization is to trigger this risk threshold at th |
| alternates | ANT-RSP-v3-0-0072 | — | chose ANT-RSP-v2-2-0092, also considered ANT-RSP-v2-2-0298 | This capability threshold is intended to reflect our definition of hig |
| alternates | ANT-RSP-v3-0-0075 | — | chose ANT-RSP-v2-2-0089, also considered ANT-RSP-v2-2-0090 | Achieve an "eyes on everything" state for our internal AI development. |
| alternates | ANT-RSP-v3-0-0097 | — | chose ANT-RSP-v2-2-0147, also considered ANT-RSP-v2-2-0156;ANT-RSP-v2-2-0265;ANT-RSP- | We will publish Risk Reports discussing the risks of our systems and h |
| alternates | ANT-RSP-v3-0-0120 | — | chose ANT-RSP-v2-2-0156, also considered ANT-RSP-v2-2-0161;ANT-RSP-v2-2-0174 | Risk mitigations: For each in-scope model, the mitigations we are impl |
| alternates | ANT-RSP-v3-0-0124 | — | chose ANT-RSP-v2-2-0078, also considered ANT-RSP-v2-2-0116 | Threat-specific risk assessment: For each threat model, we will analyz |
| alternates | ANT-RSP-v3-0-0141 | — | chose ANT-RSP-v2-2-0147, also considered ANT-RSP-v2-2-0201 | Initial assessment and drafting: Our internal subject matter experts w |
| alternates | ANT-RSP-v3-0-0142 | — | chose ANT-RSP-v2-2-0149, also considered ANT-RSP-v2-2-0203 | Review and feedback: Separate internal reviewers will provide comprehe |
| alternates | ANT-RSP-v3-0-0143 | — | chose ANT-RSP-v2-2-0149, also considered ANT-RSP-v2-2-0203 | We will usually also seek feedback from trusted external parties with  |
| alternates | ANT-RSP-v3-0-0144 | — | chose ANT-RSP-v2-2-0148, also considered ANT-RSP-v2-2-0202 | Executive approval: The Risk Report, along with the internal feedback  |
| alternates | ANT-RSP-v3-0-0145 | — | chose ANT-RSP-v2-2-0148, also considered ANT-RSP-v2-2-0202 | The CEO and RSO will make the ultimate determination regarding the ade |
| alternates | ANT-RSP-v3-0-0146 | — | chose ANT-RSP-v2-2-0151, also considered ANT-RSP-v2-2-0205 | Governance notification: Following approval of a Risk Report, the CEO  |
| alternates | ANT-RSP-v3-0-0203 | — | chose ANT-RSP-v2-2-0233, also considered ANT-RSP-v2-2-0234 | Internal transparency: We will share final, unredacted Risk Reports wi |
| alternates | ANT-RSP-v3-0-0206 | — | chose ANT-RSP-v2-2-0238, also considered ANT-RSP-v2-2-0239 | When we receive a report, we will promptly investigate, take appropria |
| alternates | ANT-RSP-v3-0-0207 | — | chose ANT-RSP-v2-2-0240, also considered ANT-RSP-v2-2-0242 | We will provide quarterly updates to the Board regarding reports of po |
| alternates | ANT-RSP-v3-0-0229 | — | chose ANT-RSP-v2-2-0262, also considered ANT-RSP-v2-2-0310 | Earlier editions of our RSP defined "AI Safety Levels" with specific l |
| alternates | ANT-RSP-v3-0-0231 | — | chose ANT-RSP-v2-2-0310, also considered ANT-RSP-v2-2-0327 | However, when defining the risk mitigations needed for future levels o |
| alternates | ANT-RSP-v3-0-0275 | — | chose ANT-RSP-v2-2-0346, also considered ANT-RSP-v2-2-0347 | The model capabilities and threat models corresponding with the ASL-3  |

## Check 3 — Alignments sharing almost no vocabulary

Either the most valuable alignments in the study — a renamed mechanism, a threshold restated in different units, an architecture replaced by a structurally different one — or the most wrong. Read every one.

| overlap | target | target excerpt | prior | prior excerpt |
|---|---|---|---|---|
| 0.00 | ANT-RSP-v3-0-0004 | Our recommendations for industry-wide safety outline what it would | ANT-RSP-v2-2-0008 | To determine when a model has become sufficiently advanced such th |
| 0.00 | ANT-RSP-v3-0-0053 | A frontier developer should make a strong argument that threat act | ANT-RSP-v2-2-0087 | We expect this threshold will require the ASL-4 Deployment and Sec |
| 0.00 | ANT-RSP-v3-0-0056 | AI systems that are highly relied on and have extensive access to  | ANT-RSP-v2-2-0067 | We expect to continue refining our framework in response to future |
| 0.00 | ANT-RSP-v3-0-0071 | Our working operationalization is to trigger this risk threshold a | ANT-RSP-v2-2-0092 | AI R&D-5: The ability to cause dramatic acceleration in the rate o |
| 0.00 | ANT-RSP-v3-0-0072 | This capability threshold is intended to reflect our definition of | ANT-RSP-v2-2-0092 | AI R&D-5: The ability to cause dramatic acceleration in the rate o |
| 0.00 | ANT-RSP-v3-0-0118 | Threat model specification: The relevant threat models (which will | ANT-RSP-v2-2-0011 | This update to our RSP provides specifications for Capabilities Th |
| 0.00 | ANT-RSP-v3-0-0122 | Risk analyses. We will provide our reasoning and conclusions regar | ANT-RSP-v2-2-0147 | First, we will compile a Capability Report that documents the find |
| 0.00 | ANT-RSP-v3-0-0130 | Changes in risk mitigation practices—noteworthy cases in which our | ANT-RSP-v2-2-0249 | We will also periodically release information on internal reports  |
| 0.00 | ANT-RSP-v3-0-0218 | These commitments are necessarily high-level and limited. In many  | ANT-RSP-v2-2-0255 | It is possible at some point in the future that another actor in t |
| 0.02 | ANT-RSP-v3-0-0231 | However, when defining the risk mitigations needed for future leve | ANT-RSP-v2-2-0310 | ASL definition changed: The term "ASL" now refers to groups of tec |
| 0.03 | ANT-RSP-v3-0-0075 | Achieve an "eyes on everything" state for our internal AI developm | ANT-RSP-v2-2-0089 | The ASL-3 Security Standard is required. |
| 0.03 | ANT-RSP-v3-0-0219 | But to the extent that other relevant AI developers prioritize saf | ANT-RSP-v2-2-0257 | If we take this measure, however, we will also acknowledge the ove |
| 0.03 | ANT-RSP-v3-0-0026 | This section outlines our recommendations for what it would take,  | ANT-RSP-v2-2-0078 | Below, we specify the Capability Thresholds and their correspondin |
| 0.03 | ANT-RSP-v3-0-0220 | Anthropic in the lead. We have developed or will imminently develo | ANT-RSP-v2-2-0255 | It is possible at some point in the future that another actor in t |
| 0.03 | ANT-RSP-v3-0-0221 | We will require a strong argument that catastrophic risk is contai | ANT-RSP-v2-2-0257 | If we take this measure, however, we will also acknowledge the ove |
| 0.03 | ANT-RSP-v3-0-0223 | Competitors have strong safety measures. We have strong evidence t | ANT-RSP-v2-2-0256 | In such a scenario, because the incremental increase in risk attri |
| 0.03 | ANT-RSP-v3-0-0015 | Risk Reports are another new requirement. Risk Reports will provid | ANT-RSP-v2-2-0265 | A document attesting that a model is sufficiently far from each of |
| 0.03 | ANT-RSP-v3-0-0097 | We will publish Risk Reports discussing the risks of our systems a | ANT-RSP-v2-2-0147 | First, we will compile a Capability Report that documents the find |
| 0.03 | ANT-RSP-v3-0-0002 | We have always intended for our RSP to be a living document. We wi | ANT-RSP-v2-2-0002 | We are now updating our RSP to account for the lessons we've learn |
| 0.03 | ANT-RSP-v3-0-0149 | We will publish a public version of our Risk Report. | ANT-RSP-v2-2-0248 | Public disclosures: We will publicly release key information relat |
| 0.03 | ANT-RSP-v3-0-0051 | We will apply protections at least as strong as our ASL-3 protecti | ANT-RSP-v2-2-0087 | We expect this threshold will require the ASL-4 Deployment and Sec |
| 0.04 | ANT-RSP-v3-0-0033 | At this point in AI's rapid development, we cannot presently give  | ANT-RSP-v2-2-0079 | In developing these standards, we have weighed the risks and benef |
| 0.04 | ANT-RSP-v3-0-0224 | For our highly capable frontier models, we will meet or exceed the | ANT-RSP-v2-2-0256 | In such a scenario, because the incremental increase in risk attri |
| 0.04 | ANT-RSP-v3-0-0208 | If we determine that a report is (1) substantiated and (2) involve | ANT-RSP-v2-2-0240 | The Responsible Scaling Officer will regularly update the Board of |
| 0.04 | ANT-RSP-v3-0-0019 | As detailed below, we also aim to subject Risk Reports to review b | ANT-RSP-v2-2-0250 | Expert input: We will solicit input from external experts in relev |
| 0.04 | ANT-RSP-v3-0-0059 | We will detail the state of our AI systems' capabilities and prope | ANT-RSP-v2-2-0067 | We expect to continue refining our framework in response to future |
| 0.04 | ANT-RSP-v3-0-0083 | Actors subject to such a regime would not need to be treated as th | ANT-RSP-v2-2-0093 | At minimum, the ASL-4 Security Standard (which would protect again |
| 0.04 | ANT-RSP-v3-0-0115 | Factual information. We will describe how we identify, evaluate, a | ANT-RSP-v2-2-0078 | Below, we specify the Capability Thresholds and their correspondin |
| 0.05 | ANT-RSP-v3-0-0156 | We will work toward a practice of seeking comprehensive, public ex | ANT-RSP-v2-2-0250 | Expert input: We will solicit input from external experts in relev |
| 0.05 | ANT-RSP-v3-0-0020 | Finally, our governance commitments are intended to promote intern | ANT-RSP-v2-2-0026 | Governance and transparency. To facilitate the effective implement |
| 0.05 | ANT-RSP-v3-0-0206 | When we receive a report, we will promptly investigate, take appro | ANT-RSP-v2-2-0238 | Further, we will track and investigate any reported or otherwise i |
| 0.05 | ANT-RSP-v3-0-0080 | A frontier developer should make a strong argument that: No user o | ANT-RSP-v2-2-0093 | At minimum, the ASL-4 Security Standard (which would protect again |
| 0.05 | ANT-RSP-v3-0-0043 | We will maintain or improve on our ASL-3 protections, which includ | ANT-RSP-v2-2-0085 | The ASL-3 Deployment Standard and the ASL-3 Security Standard, whi |
| 0.05 | ANT-RSP-v3-0-0120 | Risk mitigations: For each in-scope model, the mitigations we are  | ANT-RSP-v2-2-0156 | We will document our implementation of the Required Safeguards in  |
| 0.05 | ANT-RSP-v3-0-0046 | A frontier developer should make a strong argument that individual | ANT-RSP-v2-2-0085 | The ASL-3 Deployment Standard and the ASL-3 Security Standard, whi |
| 0.06 | ANT-RSP-v3-0-0082 | Accomplishing this would likely mean security roughly in line with | ANT-RSP-v2-2-0093 | At minimum, the ASL-4 Security Standard (which would protect again |
| 0.07 | ANT-RSP-v3-0-0141 | Initial assessment and drafting: Our internal subject matter exper | ANT-RSP-v2-2-0147 | First, we will compile a Capability Report that documents the find |
| 0.08 | ANT-RSP-v3-0-0086 | AI models have not been deliberately or inadvertently trained with | ANT-RSP-v2-2-0090 | In addition, we will develop an affirmative case that (1) identifi |
| 0.08 | ANT-RSP-v3-0-0124 | Threat-specific risk assessment: For each threat model, we will an | ANT-RSP-v2-2-0078 | Below, we specify the Capability Thresholds and their correspondin |
| 0.08 | ANT-RSP-v3-0-0068 | AI systems that can fully automate, or otherwise dramatically acce | ANT-RSP-v2-2-0088 | AI R&D-4: The ability to fully automate the work of an entry-level |

_6 further alignments below 0.10 overlap not shown._

## Check 4a — NONE with an alternate named

`prior_unit_id` is NONE, yet `alignment_note` names a candidate. The row asserts that nothing in the prior version addresses this object while naming something that might. **These are the most likely missed alignments in the transition.**

Nothing flagged.

## Check 4 — `prior_unit_id: NONE` where the section exists in the prior version

A target unit under a heading the prior version also has, yet aligned to nothing. Likely a missed alignment rather than genuinely new material.

| target | section heading (present in prior) | excerpt |
|---|---|---|
| ANT-RSP-v3-0-0003 | Introduction | The major components of this third iteration are as follows: |
| ANT-RSP-v3-0-0006 | Introduction | This approach represents a change from our previous RSP, driven by a collective  |
| ANT-RSP-v3-0-0007 | Introduction | Our previous RSP committed to implementing mitigations that would reduce our mod |
| ANT-RSP-v3-0-0008 | Introduction | But from a societal perspective, what matters is the risk to the ecosystem as a  |
| ANT-RSP-v3-0-0009 | Introduction | Although this situation has not yet arisen, it looks likely enough that we want  |
| ANT-RSP-v3-0-0010 | Introduction | We now separate our plans as a company—those which we expect to achieve regardle |
| ANT-RSP-v3-0-0011 | Introduction | We aspire to advance the latter through a mixture of example-setting, addressing |
| ANT-RSP-v3-0-0012 | Introduction | Frontier Safety Roadmaps are a new requirement under our RSP. These will describ |
| ANT-RSP-v3-0-0013 | Introduction | Goals described in the Roadmaps are intended to be ambitious, yet achievable—pro |
| ANT-RSP-v3-0-0014 | Introduction | These are not hard commitments but rather public goals against which we will ope |
| ANT-RSP-v3-0-0016 | Introduction | They will go beyond describing model capabilities, addressing our thinking on ho |
| ANT-RSP-v3-0-0017 | Introduction | These reports will reflect our reasoning as to whether we believe the risks of t |
| ANT-RSP-v3-0-0018 | Introduction | They will be published online, with some redactions to protect sensitive details |
| ANT-RSP-v3-0-0022 | Introduction | Further, the RSP may serve some regulatory requirements, but it is not designed  |
| ANT-RSP-v3-0-0023 | Introduction | Where regulatory requirements exceed or differ from what the RSP covers, we will |
| ANT-RSP-v3-0-0024 | Introduction | "Catastrophic risk" as used in our RSP refers generally to risks of the most sev |
| ANT-RSP-v3-0-0025 | Introduction | Where laws such as California SB 53 define this or similar terms with specific t |
| ANT-RSP-v3-0-0236 | Changelog | We describe the most notable changes below. |
| ANT-RSP-v3-0-0267 | Changelog | The key changes include: |
| ANT-RSP-v3-0-0277 | Changelog | This update is a comprehensive rewrite of our RSP. |
| ANT-RSP-v3-0-0278 | Changelog | For a summary of changes and the thinking behind them, see here. |

## Orphaned prior units

Neither aligned to a target nor flagged as a removal, so absent from the change pass entirely. Most are ordinary rewording or dropped rationale, which Step A3 excludes by design. **Scan for anything category-, threshold-, governance- or architecture-level.**

**247 of 348 prior units (71%).**

| prior section heading | orphaned units |
|---|---|
| Introduction | 25 |
| 4.2. ASL-3 Security Standard | 24 |
| Executive Summary | 22 |
| 1. Background | 18 |
| 2. Capability Thresholds and Required Safeguards | 18 |
| 3. Capability Assessment / 3.2 Comprehensive Assessment | 18 |
| Appendix B: ASL-2 Standard | 16 |
| 6.2. Restrict Deployment and Further Scaling | 15 |
| Appendix C: Detailed Capability Thresholds | 14 |
| 4.1. ASL-3 Deployment Standard | 12 |
| Appendix A: Glossary | 10 |
| 4.3. Safeguards Decision | 9 |
| 3. Capability Assessment / 3.1 Preliminary Assessment | 8 |
| 7. Governance and Transparency / 7.1. Internal Governance | 7 |
| 4. Safeguards Assessment | 6 |
| 7.2. Transparency and External Input | 6 |
| Introduction (footnote-style note) | 5 |
| 3. Capability Assessment / 3.3 Capability Decision | 5 |
| Table: Capability Thresholds and Required Safeguards | 3 |
| Table: Ongoing Assessment Capabilities | 3 |
