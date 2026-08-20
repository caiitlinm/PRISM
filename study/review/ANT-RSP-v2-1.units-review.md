# Stage 4 unit review — ANT-RSP-v2-1

Anthropic · Responsible Scaling Policy · Version 2.1 · 2025-03-31 · 22 pages

**322 units.** Frozen at `study/corpus/anthropic/units/ANT-RSP-v2-1.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| (unnumbered) 2. Capability Thresholds and Required Safeguards | 14 | 10 | ANT-RSP-v2-1-0066 |
| (unnumbered) Appendix A: Glossary | 12 | 12 | ANT-RSP-v2-1-0242 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| ANT-RSP-v2-1-0054 | 1 | These standards, which are summarized below, are available in full in Appendix B. | 13 words |
| ANT-RSP-v2-1-0089 | 2 | At present, we have identified one such capability: | 8 words |
| ANT-RSP-v2-1-0093 | fn1 | We hope to publish updates approximately every 6 months. | 9 words |
| ANT-RSP-v2-1-0100 | 3.1 | The term "notably more capable" is operationalized as at least one of the following: | 14 words |
| ANT-RSP-v2-1-0106 | 3.2 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-1-0117 | fn3 | This is, however, an open research question, and we will explore different possible methods. | 14 words |
| ANT-RSP-v2-1-0119 | fn4 | This is a broad category, including techniques like improved prompting and agent scaffolding. | 13 words |
| ANT-RSP-v2-1-0127 | 3.3 | The process for making such a determination is as follows: | 10 words |
| ANT-RSP-v2-1-0136 | 4 | As noted, the Required Safeguards for each Capability Threshold are specified in Section 2. | 14 words |
| ANT-RSP-v2-1-0137 | 4 | We will document our implementation of the Required Safeguards in a Safeguards Report. | 13 words |
| ANT-RSP-v2-1-0143 | 4.1 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-1-0161 | 4.2 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-1-0207 | fn13 | "Comparable or greater capabilities" is operationalized as 1x or more in Effective Compute. | 13 words |
| ANT-RSP-v2-1-0212 | 7.1 / bullet 2 | We will run exercises to ensure our readiness for incident scenarios. | 11 words |
| ANT-RSP-v2-1-0260 | App B / ASL-2 Security Standard / intro | ASL-2 Security Standard: A security system that can likely thwart most opportunistic attackers. | 13 words |
| ANT-RSP-v2-1-0271 | App C / intro | This appendix contains detailed definitions for each Capability Threshold in Section 2. | 12 words |
| ANT-RSP-v2-1-0285 | fn22 | Combined, these have an effective rate of scaling of 35 x/year. | 11 words |
| ANT-RSP-v2-1-0286 | Changelog / September 19, 2023 (RSP v1.0) | September 19, 2023 (RSP v1.0) RSP-2023 (aka RSP v1.0): Initial version. | 11 words |
| ANT-RSP-v2-1-0313 | Changelog / October 15, 2024 / New Capability and Safeguards Reports | New Capability and Safeguards Reports: We have introduced Capability Reports and Safeguard Reports. | 13 words |

## Check 3 — `stated_bar` audit

53 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| ANT-RSP-v2-1-0001 | N/A | In September 2023, we released our Responsible Scaling Policy (RSP), a public commitment not to train or deploy models c | NONE |
| ANT-RSP-v2-1-0008 | N/A | Capability assessment. We will routinely test models to determine whether their capabilities fall sufficiently far below | NONE |
| ANT-RSP-v2-1-0010 | N/A | If, after the comprehensive testing, we determine that the model is sufficiently below the relevant Capability Threshold | NONE |
| ANT-RSP-v2-1-0023 | N/A | In September 2023, we released our Responsible Scaling Policy (RSP), a first-of-its-kind public commitment not to train  | NONE |
| ANT-RSP-v2-1-0042 | fn (unnumbered) | This policy also helps satisfy our Voluntary White House Commitments (2023) and Frontier AI Safety Commitments (2024). | NONE |
| ANT-RSP-v2-1-0057 | 1 | Although the ASL-2 Standard is appropriate for all of our current models, that may not hold true in the future as our mo | NONE |
| ANT-RSP-v2-1-0060 | 1 | A Capability Threshold is a prespecified level of AI capability that, if reached, signals (1) a meaningful increase in t | NONE |
| ANT-RSP-v2-1-0061 | 1 | In other words, a Capability Threshold serves as a trigger for shifting from an ASL-N Standard to an ASL-N+1 Standard (o | NONE |
| ANT-RSP-v2-1-0065 | 2 | We will conduct assessments to inform when to implement the Required Safeguards (see Section 4). The Capability Threshol | NONE |
| ANT-RSP-v2-1-0076 | Table (untitled) / AI R&D / Required Safeguards / AI R&D-5 | As with AI R&D-4, we also expect an affirmative case will be required. | NONE |
| ANT-RSP-v2-1-0092 | Table (untitled) / Cyber Operations / Ongoing Assessment | We will conduct either pre- or post-deployment testing, including specialized evaluations. We will document any salient  | NONE |
| ANT-RSP-v2-1-0097 | 3.1 | We will routinely test models to determine whether their capabilities fall sufficiently far below the Capability Thresho | NONE |
| ANT-RSP-v2-1-0126 | 3.3 | If, after the comprehensive testing, we determine that the model is sufficiently below the relevant Capability Threshold | NONE |
| ANT-RSP-v2-1-0129 | 3.3 / list item 2 | The report will be escalated to the CEO and the Responsible Scaling Officer, who will (1) make the ultimate determinatio | NONE |
| ANT-RSP-v2-1-0130 | 3.3 / list item 3 | In general, as noted in Sections 7.1.4 and 7.2.2, we will solicit both internal and external expert feedback on the repo | NONE |
| ANT-RSP-v2-1-0135 | 4 | To determine whether the measures we have adopted satisfy the ASL-3 Required Safeguards, we will conduct a safeguards as | NONE |
| ANT-RSP-v2-1-0136 | 4 | As noted, the Required Safeguards for each Capability Threshold are specified in Section 2. | NONE |
| ANT-RSP-v2-1-0138 | fn7 | Currently, these will be informal estimates of (1) the extent to which widely available elicitation techniques may impro | NONE |
| ANT-RSP-v2-1-0142 | 4.1 | When a model must meet the ASL-3 Deployment Standard, we will evaluate whether the measures we have implemented make us  | NONE |
| ANT-RSP-v2-1-0155 | 4.2 | When a model must meet the ASL-3 Security Standard, we will evaluate whether the measures we have implemented make us hi | NONE |
| ANT-RSP-v2-1-0159 | 4.2 | The following groups are out of scope for the ASL-3 Security Standard because further testing (as discussed below) shoul | NONE |
| ANT-RSP-v2-1-0174 | 4.2 / bullet 2e | Existing guidance: Aligning where appropriate with existing guidance on securing model weights, including Securing AI Mo | NONE |
| ANT-RSP-v2-1-0175 | fn11 | We will implement robust insider risk controls to mitigate most insider risk, but consider mitigating risks from highly  | NONE |
| ANT-RSP-v2-1-0176 | fn11 | We are committed to further enhancing these protections as a part of our ASL-4 preparations. | NONE |
| ANT-RSP-v2-1-0177 | 4.2 / bullet 3 | Audits: Develop plans to (1) audit and assess the design and implementation of the security program and (2) share these  | NONE |
| ANT-RSP-v2-1-0180 | 4.3 | If, after the evaluations above, we determine that we have met the ASL-3 Required Safeguards, then we may proceed with d | NONE |
| ANT-RSP-v2-1-0181 | 4.3 | The process for determining whether we have met the ASL-3 Required Safeguards is as follows: | NONE |
| ANT-RSP-v2-1-0183 | 4.3 / bullet 2 | The Safeguards Report(s) will be escalated to the CEO and the Responsible Scaling Officer, who will (1) make the ultimat | NONE |
| ANT-RSP-v2-1-0184 | 4.3 / bullet 3 | In general, as noted in Sections 7.1.4 and 7.2.2, we will solicit both internal and external expert feedback on the repo | NONE |
| ANT-RSP-v2-1-0189 | 5 | In parallel with upgrading a model to the Required Safeguards, we will (1) update this policy to include any additional  | NONE |
| ANT-RSP-v2-1-0190 | 6.1 | To summarize the commitments and procedures outlined above, we may deploy or store a model if either of the following cr | NONE |
| ANT-RSP-v2-1-0191 | 6.1 | or (2) the model's capabilities have surpassed the existing Capabilities Threshold, but we have implemented the ASL-3 Re | NONE |
| ANT-RSP-v2-1-0193 | 6.2 | In any scenario where we determine that a model requires ASL-3 Required Safeguards but we are unable to implement them i | NONE |
| ANT-RSP-v2-1-0194 | 6.2 / bullet 1 | Interim measures: The CEO and Responsible Scaling Officer may approve the use of interim measures that provide the same  | NONE |
| ANT-RSP-v2-1-0196 | 6.2 / bullet 1 | In the security context, an example of such a measure would be storing the model weights in a single-purpose, isolated n | NONE |
| ANT-RSP-v2-1-0199 | 6.2 / bullet 2 | In the deployment context, we will de-deploy the model and replace it with a model that falls below the Capability Thres | NONE |
| ANT-RSP-v2-1-0201 | 6.2 / bullet 3 | Monitoring pretraining: We will not train models with comparable or greater capabilities to the one that requires the AS | NONE |
| ANT-RSP-v2-1-0203 | 6.2 / bullet 3 | If the pretraining model's capabilities are comparable or greater, we will pause training until we have implemented the  | NONE |
| ANT-RSP-v2-1-0206 | fn13 | We consider implementation of the ASL-3 Security Standard alone sufficient to continue training, regardless of whether t | NONE |
| ANT-RSP-v2-1-0209 | 7.1 / bullet 1 | (1) as needed, proposing updates to this policy to the Board of Directors; (2) approving relevant model training or depl | NONE |
| ANT-RSP-v2-1-0210 | 7.1 / bullet 1 | (4) overseeing implementation of this policy, including the allocation of sufficient resources; (5) receiving and addres | NONE |
| ANT-RSP-v2-1-0211 | 7.1 / bullet 2 | We will develop internal safety procedures for incident scenarios. Such scenarios include (1) pausing training in respon | NONE |
| ANT-RSP-v2-1-0217 | 7.1 / bullet 5 | We will also establish a policy governing noncompliance reporting, which will (1) protect reporters from retaliation and | NONE |
| ANT-RSP-v2-1-0220 | fn14 | In addition to noncompliance processes, we will (1) establish pathways for Anthropic staff to raise any issues related t | NONE |
| ANT-RSP-v2-1-0244 | App A / ASL-3 Standard | A higher level of safeguards required when a model cannot be certified as ASL-2 appropriate. It includes more stringent  | NONE |
| ANT-RSP-v2-1-0260 | App B / ASL-2 Security Standard / intro | ASL-2 Security Standard: A security system that can likely thwart most opportunistic attackers. | NONE |
| ANT-RSP-v2-1-0269 | App B / ASL-2 Security Standard / item 5 | External validation like SOC 2 compliance and continuous vulnerability management must ensure adaptations match infosec  | NONE |
| ANT-RSP-v2-1-0271 | App C / intro | This appendix contains detailed definitions for each Capability Threshold in Section 2. | NONE |
| ANT-RSP-v2-1-0283 | fn21 | This comparison is hard to make in practice; this note is to clarify the meaning of the conceptual threshold and the fac | NONE |
| ANT-RSP-v2-1-0286 | Changelog / September 19, 2023 (RSP v1.0) | September 19, 2023 (RSP v1.0) RSP-2023 (aka RSP v1.0): Initial version. | NONE |
| ANT-RSP-v2-1-0287 | Changelog / October 15, 2024 (RSP v2.0) / intro | RSP-2024: This update introduces a more flexible and nuanced approach to assessing and managing AI risks while maintaini | NONE |
| ANT-RSP-v2-1-0305 | Changelog / October 15, 2024 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | NONE |
| ANT-RSP-v2-1-0308 | Changelog / October 15, 2024 / Clarified ASL-3 and ASL-2 security threat models | Clarified ASL-3 and ASL-2 security threat models: We have clarified which actors are in and out of scope for the ASL-3 S | NONE |
| ANT-RSP-v2-1-0309 | Changelog / October 15, 2024 / Clarified ASL-3 and ASL-2 security threat models | We also removed the commitment to protect against scaled attacks and distillation attacks from the ASL-2 Security standa | NONE |
| ANT-RSP-v2-1-0310 | Changelog / October 15, 2024 / Clarified ASL-3 and ASL-2 security threat models | While distillation remains a concern for more capable models, models stored under ASL-2 safeguards have not yet reached  | NONE |
| ANT-RSP-v2-1-0311 | Changelog / October 15, 2024 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | NONE |
| ANT-RSP-v2-1-0321 | Changelog / March 31, 2025 / Iterative Commitment | We have decided not to maintain a commitment to define ASL-N+1 evaluations by the time we develop ASL-N models; such an  | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| ANT-RSP-v2-1-0021 | N/A | As frontier AI models advance, we believe they will bring about transformative benefits for our society and economy. AI  | mid-unit |
| ANT-RSP-v2-1-0034 | N/A | By sharing our approach externally, we aim to set a new industry standard that encourages widespread adoption of similar | mid-unit |
| ANT-RSP-v2-1-0052 | 1 | We expect to continue refining our framework in response to future risks (for example, the risk that an AI system attemp | initial |
| ANT-RSP-v2-1-0064 | 2 | In developing these standards, we have weighed the risks and benefits of frontier model development. We believe these sa | mid-unit |
| ANT-RSP-v2-1-0070 | Table (untitled) / CBRN / Required Safeguards / CBRN-4 | We expect this threshold will require the ASL-4 Deployment and Security Standards. We plan to add more information about | initial |
| ANT-RSP-v2-1-0075 | Table (untitled) / AI R&D / Required Safeguards / AI R&D-5 | At minimum, the ASL-4 Security Standard (which would protect against model-weight theft by state-level adversaries) is r | mid-unit |
| ANT-RSP-v2-1-0094 | fn2 | We recognize the potential risks of highly persuasive AI models. While we are actively consulting experts, we believe th | initial |
| ANT-RSP-v2-1-0167 | 4.2 / bullet 2a | We expect this will include a combination of physical security, encryption, cloud security, infrastructure policy, acces | initial |
| ANT-RSP-v2-1-0169 | 4.2 / bullet 2b | We expect this will include a combination of software inventory, supply chain security, artifact integrity, binary autho | initial |
| ANT-RSP-v2-1-0171 | 4.2 / bullet 2c | We expect this will include a combination of endpoint patching, product security testing, log management, asset monitori | initial |
| ANT-RSP-v2-1-0173 | 4.2 / bullet 2d | We expect meeting this standard of security to require roughly 5-10% of employees being dedicated to security and securi | initial |
| ANT-RSP-v2-1-0178 | 4.2 / bullet 3 | We expect this to include independent validation of threat modeling and risk assessment results; a sampling-based audit  | initial |
| ANT-RSP-v2-1-0211 | 7.1 / bullet 2 | We will develop internal safety procedures for incident scenarios. Such scenarios include (1) pausing training in respon | mid-unit |
| ANT-RSP-v2-1-0236 | 7.2 / bullet 4 | On approximately an annual basis, we will commission a third-party review that assesses whether we adhered to this polic | mid-unit |
| ANT-RSP-v2-1-0240 | fn19 | Where possible, we will include descriptions of the empirical evaluation results we believe would indicate that a model  | mid-unit |
| ANT-RSP-v2-1-0305 | Changelog / October 15, 2024 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | mid-unit |
| ANT-RSP-v2-1-0311 | Changelog / October 15, 2024 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | mid-unit |
| ANT-RSP-v2-1-0314 | Changelog / October 15, 2024 / New Capability and Safeguards Reports | We expect that aggregating all the available evidence about model capabilities will provide decision makers with a more  | initial |
| ANT-RSP-v2-1-0322 | Changelog / March 31, 2025 / Iterative Commitment | We believe it is more practical and sensible instead to commit to reconsidering the whole list of Capability Thresholds  | initial |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| ANT-RSP-v2-1-0165 | 4.2 / bullet 2 | This includes: | 2 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| ANT-RSP-v2-1.01.jsonl → ANT-RSP-v2-1.02.jsonl | ANT-RSP-v2-1-0135 | 4. Safeguards Assessment | none detected |
| ANT-RSP-v2-1.02.jsonl → ANT-RSP-v2-1.03.jsonl | ANT-RSP-v2-1-0208 | 7. Governance and Transparency / 7.1. Internal Governance | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **2**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 322 |
| Tables detected | 2 |
| Units in tables | 26 |
| `context_stem` = NONE | 202 |
| `stated_bar` populated | 53 |
| `duplicate_of` populated | 13 |
| Median excerpt words | 27 |

| unit_type | n |
|---|---|
| paragraph | 170 |
| numbered | 59 |
| footnote | 41 |
| bullet | 26 |
| table_cell | 26 |
