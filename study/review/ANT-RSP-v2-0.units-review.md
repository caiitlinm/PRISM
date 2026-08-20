# Stage 4 unit review — ANT-RSP-v2-0

Anthropic · Responsible Scaling Policy · NONE · 2024-10-15 · 22 pages

**338 units.** Frozen at `study/corpus/anthropic/units/ANT-RSP-v2-0.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| (unnumbered) 2. Capability Thresholds and Required Safeguards | 11 | 6 | ANT-RSP-v2-0-0088 |
| (unnumbered) Appendix A: Glossary | 13 | 12 | ANT-RSP-v2-0-0264 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| ANT-RSP-v2-0-0006 | Executive Summary / Background | At present, all of our models must meet the ASL-2 Deployment and Security Standards. | 14 words |
| ANT-RSP-v2-0-0035 | Introduction / para 3 | First, our approach to risk should be proportional. | 8 words |
| ANT-RSP-v2-0-0039 | Introduction / para 4 | Second, our approach to risk should be iterative. | 8 words |
| ANT-RSP-v2-0-0042 | Introduction / para 4 | Further, we will continue to research potential risks and next-generation mitigation techniques. | 12 words |
| ANT-RSP-v2-0-0044 | Introduction / para 5 | Third, our approach to risk should be exportable. | 8 words |
| ANT-RSP-v2-0-0048 | Introduction / para 5 | In the meantime, we will continue to share our findings with policymakers. | 12 words |
| ANT-RSP-v2-0-0051 | Introduction / para 6 | Further, we conduct research to understand the broader societal impacts of our models. | 13 words |
| ANT-RSP-v2-0-0053 | Introduction / para 7 | At Anthropic, we are committed to developing AI responsibly and transparently. | 11 words |
| ANT-RSP-v2-0-0060 | Introduction / para 8 | To submit your feedback or suggestions, please contact us at rsp@anthropic.com. | 11 words |
| ANT-RSP-v2-0-0061 | 1 | AI Safety Level Standards (ASL Standards) are core to our risk mitigation strategy. | 13 words |
| ANT-RSP-v2-0-0064 | 1 | Definitions of ASL Standards and other key terms are available in Appendix A. | 13 words |
| ANT-RSP-v2-0-0071 | 1 | At present, all of our models must meet the ASL-2 Deployment and Security Standards. | 14 words |
| ANT-RSP-v2-0-0073 | 1 | These standards, which are summarized below, are available in full in Appendix B. | 13 words |
| ANT-RSP-v2-0-0082 | 2 | Below, we specify the Capability Thresholds and their corresponding Required Safeguards. | 11 words |
| ANT-RSP-v2-0-0087 | 2 | The Capability Thresholds summarized below are available in full in Appendix C. | 12 words |
| ANT-RSP-v2-0-0105 | 2 | At present, we have identified one such capability: | 8 words |
| ANT-RSP-v2-0-0110 | fn2 | We hope to publish updates approximately every 6 months. | 9 words |
| ANT-RSP-v2-0-0113 | fn3 | We recognize the potential risks of highly persuasive AI models. | 10 words |
| ANT-RSP-v2-0-0118 | 3.1 | The term “notably more capable” is operationalized as at least one of the following: | 14 words |
| ANT-RSP-v2-0-0124 | 3.2 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-0-0127 | fn4 | “Effective Compute” is a scaling-trend-based metric that accounts for both FLOPs and algorithmic improvements. | 14 words |
| ANT-RSP-v2-0-0130 | fn4 | This is, however, an open research question, and we will explore different possible methods. | 14 words |
| ANT-RSP-v2-0-0132 | fn5 | This is a broad category, including techniques like improved prompting and agent scaffolding. | 13 words |
| ANT-RSP-v2-0-0148 | 3.3 | The process for making such a determination is as follows: | 10 words |
| ANT-RSP-v2-0-0158 | 4 | As noted, the Required Safeguards for each Capability Threshold are specified in Section 2. | 14 words |
| ANT-RSP-v2-0-0159 | 4 | We will document our implementation of the Required Safeguards in a Safeguards Report. | 13 words |
| ANT-RSP-v2-0-0161 | 4.1 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-0-0180 | 4.2 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-0-0208 | 5 | We will update this policy with the Capability Thresholds for the ASL-4 Required Safeguards. | 14 words |
| ANT-RSP-v2-0-0212 | 5 | We will follow the procedures outlined in Section 3. | 9 words |
| ANT-RSP-v2-0-0228 | fn14 | 14 | 1 words |
| ANT-RSP-v2-0-0238 | 7.1 / bullet 2 | We will run exercises to ensure our readiness for incident scenarios. | 11 words |
| ANT-RSP-v2-0-0283 | App B / ASL-2 Security Standard | ASL-2 Security Standard: A security system that can likely thwart most opportunistic attackers. | 13 words |
| ANT-RSP-v2-0-0295 | App C / intro | This appendix contains detailed definitions for each Capability Threshold in Section 2. | 12 words |
| ANT-RSP-v2-0-0307 | fn23 | Combined, these have an effective rate of scaling of 35 x/year. | 11 words |
| ANT-RSP-v2-0-0308 | Changelog / September 19, 2023 | September 19, 2023 RSP-2023 (aka RSP v1.0): Initial version. | 9 words |
| ANT-RSP-v2-0-0311 | Changelog / October 15, 2024 | We describe the most notable changes below. | 7 words |
| ANT-RSP-v2-0-0335 | Changelog / New Capability and Safeguards Reports | New Capability and Safeguards Reports: We have introduced Capability Reports and Safeguard Reports. | 13 words |

## Check 3 — `stated_bar` audit

59 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| ANT-RSP-v2-0-0001 | Executive Summary / para 1 | In September 2023, we released our Responsible Scaling Policy (RSP), a public commitment not to train or deploy models c | NONE |
| ANT-RSP-v2-0-0011 | Executive Summary / Capability assessment | We will routinely test models to determine whether their capabilities fall sufficiently far below the Capability Thresho | NONE |
| ANT-RSP-v2-0-0014 | Executive Summary / Capability assessment | If, after the comprehensive testing, we determine that the model is sufficiently below the relevant Capability Threshold | NONE |
| ANT-RSP-v2-0-0030 | Introduction / para 1 | In September 2023, we released our Responsible Scaling Policy (RSP), a first-of-its-kind public commitment not to train  | NONE |
| ANT-RSP-v2-0-0057 | Introduction / para 8 | This policy also helps satisfy our Voluntary White House Commitments (2023) and Frontier AI Safety Commitments (2024). | NONE |
| ANT-RSP-v2-0-0079 | 1 | A Capability Threshold is a prespecified level of AI capability that, if reached, signals (1) a meaningful increase in t | NONE |
| ANT-RSP-v2-0-0080 | 1 | In other words, a Capability Threshold serves as a trigger for shifting from an ASL-N Standard to an ASL-N+1 Standard (o | NONE |
| ANT-RSP-v2-0-0086 | 2 | We will conduct assessments to inform when to implement the Required Safeguards (see Section 4). | NONE |
| ANT-RSP-v2-0-0109 | Table: Capabilities / Cyber Operations / Ongoing Assessment | We will document any salient results alongside our Capability Reports (see Section 3). | NONE |
| ANT-RSP-v2-0-0115 | 3.1 | We will routinely test models to determine whether their capabilities fall sufficiently far below the Capability Thresho | NONE |
| ANT-RSP-v2-0-0144 | fn8 | Currently, these will be informal estimates of (1) the extent to which widely available elicitation techniques may impro | NONE |
| ANT-RSP-v2-0-0147 | 3.3 | If, after the comprehensive testing, we determine that the model is sufficiently below the relevant Capability Threshold | NONE |
| ANT-RSP-v2-0-0150 | 3.3 / bullet 2 | The report will be escalated to the CEO and the Responsible Scaling Officer, who will (1) make the ultimate determinatio | NONE |
| ANT-RSP-v2-0-0151 | 3.3 / bullet 3 | In general, as noted in Sections 7.1.4 and 7.2.2, we will solicit both internal and external expert feedback on the repo | NONE |
| ANT-RSP-v2-0-0157 | 4 | To determine whether the measures we have adopted satisfy the ASL-3 Required Safeguards, we will conduct a safeguards as | NONE |
| ANT-RSP-v2-0-0158 | 4 | As noted, the Required Safeguards for each Capability Threshold are specified in Section 2. | NONE |
| ANT-RSP-v2-0-0188 | fn12 | We will implement robust insider risk controls to mitigate most insider risk, but consider mitigating risks from highly  | NONE |
| ANT-RSP-v2-0-0194 | 4.2 / bullet 2e | Existing guidance: Aligning where appropriate with existing guidance on securing model weights, including Securing AI Mo | NONE |
| ANT-RSP-v2-0-0195 | 4.2 / bullet 3 | Audits: Develop plans to (1) audit and assess the design and implementation of the security program and (2) share these  | NONE |
| ANT-RSP-v2-0-0198 | 4.3 | If, after the evaluations above, we determine that we have met the ASL-3 Required Safeguards, then we may proceed with d | NONE |
| ANT-RSP-v2-0-0199 | 4.3 | The process for determining whether we have met the ASL-3 Required Safeguards is as follows: | NONE |
| ANT-RSP-v2-0-0201 | 4.3 / bullet 2 | The Safeguards Report(s) will be escalated to the CEO and the Responsible Scaling Officer, who will (1) make the ultimat | NONE |
| ANT-RSP-v2-0-0202 | 4.3 / bullet 3 | In general, as noted in Sections 7.1.4 and 7.2.2, we will solicit both internal and external expert feedback on the repo | NONE |
| ANT-RSP-v2-0-0212 | 5 | We will follow the procedures outlined in Section 3. | NONE |
| ANT-RSP-v2-0-0215 | 6.2 | In any scenario where we determine that a model requires ASL-3 Required Safeguards but we are unable to implement them i | NONE |
| ANT-RSP-v2-0-0216 | 6.2 / bullet 1 | Interim measures: The CEO and Responsible Scaling Officer may approve the use of interim measures that provide the same  | NONE |
| ANT-RSP-v2-0-0222 | 6.2 / bullet 2 | In the deployment context, we will de-deploy the model and replace it with a model that falls below the Capability Thres | NONE |
| ANT-RSP-v2-0-0228 | fn14 | 14 | NONE |
| ANT-RSP-v2-0-0231 | 7.1 / bullet 1 | (1) as needed, proposing updates to this policy to the Board of Directors; (2) approving relevant model training or depl | NONE |
| ANT-RSP-v2-0-0232 | 7.1 / bullet 1 | (4) overseeing implementation of this policy, including the allocation of sufficient resources; (5) receiving and addres | NONE |
| ANT-RSP-v2-0-0234 | fn15 | In addition to noncompliance processes, we will (1) establish pathways for Anthropic staff to raise any issues related t | NONE |
| ANT-RSP-v2-0-0237 | 7.1 / bullet 2 | Readiness: We will develop internal safety procedures for incident scenarios. Such scenarios include (1) pausing trainin | NONE |
| ANT-RSP-v2-0-0242 | 7.1 / bullet 5 | We will also establish a policy governing noncompliance reporting, which will (1) protect reporters from retaliation and | NONE |
| ANT-RSP-v2-0-0262 | fn20 | Where possible, we will include descriptions of the empirical evaluation results we believe would indicate that a model  | NONE |
| ANT-RSP-v2-0-0266 | App A / ASL-3 Standard | A higher level of safeguards required when a model cannot be certified as ASL-2 appropriate. It includes more stringent  | NONE |
| ANT-RSP-v2-0-0283 | App B / ASL-2 Security Standard | ASL-2 Security Standard: A security system that can likely thwart most opportunistic attackers. | NONE |
| ANT-RSP-v2-0-0293 | App B / ASL-2 Security Standard / bullet 5 | External validation like SOC 2 compliance and continuous vulnerability management must ensure adaptations match infosec  | NONE |
| ANT-RSP-v2-0-0295 | App C / intro | This appendix contains detailed definitions for each Capability Threshold in Section 2. | NONE |
| ANT-RSP-v2-0-0301 | App C / Autonomous AI R&D | Autonomous AI Research and Development: The ability to either: (1) Fully automate the work of an entry-level remote-only | NONE |
| ANT-RSP-v2-0-0308 | Changelog / September 19, 2023 | September 19, 2023 RSP-2023 (aka RSP v1.0): Initial version. | NONE |
| ANT-RSP-v2-0-0309 | Changelog / October 15, 2024 | October 15, 2024 RSP-2024: This update introduces a more flexible and nuanced approach to assessing and managing AI risk | NONE |
| ANT-RSP-v2-0-0317 | Changelog / ARA threshold now a checkpoint | We now believe that these capabilities - at the levels we initially considered - would not necessitate the ASL-3 standar | NONE |
| ANT-RSP-v2-0-0328 | Changelog / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | NONE |
| ANT-RSP-v2-0-0330 | Changelog / Clarified ASL-3 and ASL-2 security threat models | Clarified ASL-3 and ASL-2 security threat models: We have clarified which actors are in and out of scope for the ASL-3 S | NONE |
| ANT-RSP-v2-0-0331 | Changelog / Clarified ASL-3 and ASL-2 security threat models | We also removed the commitment to protect against scaled attacks and distillation attacks from the ASL-2 Security standa | NONE |
| ANT-RSP-v2-0-0332 | Changelog / Clarified ASL-3 and ASL-2 security threat models | While distillation remains a concern for more capable models, models stored under ASL-2 safeguards have not yet reached  | NONE |
| ANT-RSP-v2-0-0333 | Changelog / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| ANT-RSP-v2-0-0027 | Introduction / para 1 | As frontier AI models advance, we believe they will bring about transformative benefits for our society and economy. | mid-unit |
| ANT-RSP-v2-0-0046 | Introduction / para 5 | By sharing our approach externally, we aim to set a new industry standard that encourages widespread adoption of similar | mid-unit |
| ANT-RSP-v2-0-0070 | 1 | We expect to continue refining our framework in response to future risks (for example, the risk that an AI system attemp | initial |
| ANT-RSP-v2-0-0085 | 2 | We believe these safeguards are achievable with sufficient investment and advance planning into research and development | initial |
| ANT-RSP-v2-0-0093 | Table: Capability Thresholds / AI R&D / Required Safeguards | At minimum, the ASL-3 Security Standard is required, although we expect a higher security standard (which would protect  | mid-unit |
| ANT-RSP-v2-0-0098 | 2 | We will test for this checkpoint and, by the time we reach it, we aim to have met (or be close to meeting) the ASL-3 Sec | mid-unit |
| ANT-RSP-v2-0-0113 | fn3 | We recognize the potential risks of highly persuasive AI models. | initial |
| ANT-RSP-v2-0-0114 | fn3 | While we are actively consulting experts, we believe this capability is not yet sufficiently understood to include in ou | mid-unit |
| ANT-RSP-v2-0-0185 | 4.2 / bullet 2a | We expect this will include a combination of physical security, encryption, cloud security, infrastructure policy, acces | initial |
| ANT-RSP-v2-0-0187 | 4.2 / bullet 2b | We expect this will include a combination of software inventory, supply chain security, artifact integrity, binary autho | initial |
| ANT-RSP-v2-0-0191 | 4.2 / bullet 2c | We expect this will include a combination of endpoint patching, product security testing, log management, asset monitori | initial |
| ANT-RSP-v2-0-0193 | 4.2 / bullet 2d | We expect meeting this standard of security to require roughly 5-10% of employees being dedicated to security and securi | initial |
| ANT-RSP-v2-0-0196 | 4.2 / bullet 3 | We expect this to include independent validation of threat modeling and risk assessment results; a sampling-based audit  | initial |
| ANT-RSP-v2-0-0237 | 7.1 / bullet 2 | Readiness: We will develop internal safety procedures for incident scenarios. Such scenarios include (1) pausing trainin | mid-unit |
| ANT-RSP-v2-0-0259 | 7.2 / bullet 4 | Procedural compliance review: On approximately an annual basis, we will commission a third-party review that assesses wh | mid-unit |
| ANT-RSP-v2-0-0262 | fn20 | Where possible, we will include descriptions of the empirical evaluation results we believe would indicate that a model  | mid-unit |
| ANT-RSP-v2-0-0328 | Changelog / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | mid-unit |
| ANT-RSP-v2-0-0333 | Changelog / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | mid-unit |
| ANT-RSP-v2-0-0336 | Changelog / New Capability and Safeguards Reports | We expect that aggregating all the available evidence about model capabilities will provide decision makers with a more  | initial |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| ANT-RSP-v2-0-0213 | 6.1 | To summarize the commitments and procedures outlined above, we may deploy or store a model if either of the following cr | 85 |
| ANT-RSP-v2-0-0228 | fn14 | 14 | 1 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| ANT-RSP-v2-0.01.jsonl → ANT-RSP-v2-0.02.jsonl | ANT-RSP-v2-0-0157 | 4. Safeguards Assessment | none detected |
| ANT-RSP-v2-0.02.jsonl → ANT-RSP-v2-0.03.jsonl | ANT-RSP-v2-0-0229 | 7. Governance and Transparency / 7.1. Internal Governance | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **2**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 338 |
| Tables detected | 2 |
| Units in tables | 24 |
| `context_stem` = NONE | 234 |
| `stated_bar` populated | 59 |
| `duplicate_of` populated | 15 |
| Median excerpt words | 25 |

| unit_type | n |
|---|---|
| paragraph | 168 |
| bullet | 67 |
| footnote | 42 |
| numbered | 37 |
| table_cell | 24 |
