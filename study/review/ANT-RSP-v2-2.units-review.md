# Stage 4 unit review — ANT-RSP-v2-2

Anthropic · Responsible Scaling Policy · Version 2.2 · 2025-05-14 · 23 pages

**348 units.** Frozen at `study/corpus/anthropic/units/ANT-RSP-v2-2.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| (unnumbered) Appendix A: Glossary | 12 | 12 | ANT-RSP-v2-2-0262 |
| Table 1 | 12 | 8 | ANT-RSP-v2-2-0083 |
| Table 2 | 4 | 2 | ANT-RSP-v2-2-0108 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| ANT-RSP-v2-2-0005 | N/A | These currently fall into two categories: Deployment Standards and Security Standards. | 11 words |
| ANT-RSP-v2-2-0007 | N/A | At present, all of our models must meet the ASL-2 Deployment and Security Standards. | 14 words |
| ANT-RSP-v2-2-0041 | N/A | Further, we will continue to research potential risks and next-generation mitigation techniques. | 12 words |
| ANT-RSP-v2-2-0046 | N/A | In the meantime, we will continue to share our findings with policymakers. | 12 words |
| ANT-RSP-v2-2-0049 | N/A | Further, we conduct research to understand the broader societal impacts of our models. | 13 words |
| ANT-RSP-v2-2-0051 | N/A | At Anthropic, we are committed to developing AI responsibly and transparently. | 11 words |
| ANT-RSP-v2-2-0058 | N/A | To submit your feedback or suggestions, please contact us at rsp@anthropic.com. | 11 words |
| ANT-RSP-v2-2-0061 | 1 | Definitions of ASL Standards and other key terms are available in Appendix A. | 13 words |
| ANT-RSP-v2-2-0069 | 1 | These standards, which are summarized below, are available in full in Appendix B. | 13 words |
| ANT-RSP-v2-2-0082 | 2 | The Capability Thresholds summarized below are available in full in Appendix C. | 12 words |
| ANT-RSP-v2-2-0095 | 2 | These Capability Thresholds represent our current understanding of the most pressing catastrophic risks. | 13 words |
| ANT-RSP-v2-2-0096 | 2 | As our understanding evolves, we may identify additional thresholds. | 9 words |
| ANT-RSP-v2-2-0107 | 2 | At present, we have identified one such capability: | 8 words |
| ANT-RSP-v2-2-0112 | fn1 | We hope to publish updates approximately every 6 months. | 9 words |
| ANT-RSP-v2-2-0119 | 3.1 | The term "notably more capable" is operationalized as at least one of the following: | 14 words |
| ANT-RSP-v2-2-0125 | 3.2 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-2-0136 | fn3 | This is, however, an open research question, and we will explore different possible methods. | 14 words |
| ANT-RSP-v2-2-0138 | fn4 | This is a broad category, including techniques like improved prompting and agent scaffolding. | 13 words |
| ANT-RSP-v2-2-0146 | 3.3 | The process for making such a determination is as follows: | 10 words |
| ANT-RSP-v2-2-0155 | 4 | As noted, the Required Safeguards for each Capability Threshold are specified in Section 2. | 14 words |
| ANT-RSP-v2-2-0156 | 4 | We will document our implementation of the Required Safeguards in a Safeguards Report. | 13 words |
| ANT-RSP-v2-2-0162 | 4.1 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-2-0179 | 4.2 | To make the required showing, we will need to satisfy the following criteria: | 13 words |
| ANT-RSP-v2-2-0226 | fn13 | "Comparable or greater capabilities" is operationalized as 1x or more in Effective Compute. | 13 words |
| ANT-RSP-v2-2-0232 | 7.1 / item 2 | We will run exercises to ensure our readiness for incident scenarios. | 11 words |
| ANT-RSP-v2-2-0280 | App B / Security intro | ASL-2 Security Standard: A security system that can likely thwart most opportunistic attackers. | 13 words |
| ANT-RSP-v2-2-0292 | App C / intro | This appendix contains detailed definitions for each Capability Threshold in Section 2. | 12 words |
| ANT-RSP-v2-2-0306 | fn22 | Combined, these have an effective rate of scaling of 35x/year. | 10 words |
| ANT-RSP-v2-2-0307 | Changelog / Sept 19 2023 (v1.0) | September 19, 2023 (RSP v1.0) RSP-2023 (aka RSP v1.0): Initial version. | 11 words |
| ANT-RSP-v2-2-0333 | Changelog / v2.0 / Clarified requirements for deployments with trusted users | For any general access systems, we still require passing intensive red-teaming. | 11 words |
| ANT-RSP-v2-2-0335 | Changelog / v2.0 / New Capability and Safeguards Reports | New Capability and Safeguards Reports: We have introduced Capability Reports and Safeguard Reports. | 13 words |

## Check 3 — `stated_bar` audit

47 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| ANT-RSP-v2-2-0001 | N/A | In September 2023, we released our Responsible Scaling Policy (RSP), a public commitment not to train or deploy models c | NONE |
| ANT-RSP-v2-2-0012 | N/A | Capability assessment. We will routinely test models to determine whether their capabilities fall sufficiently far below | NONE |
| ANT-RSP-v2-2-0015 | N/A | If, after the comprehensive testing, we determine that the model is sufficiently below the relevant Capability Threshold | NONE |
| ANT-RSP-v2-2-0017 | N/A | This means that we will both upgrade to the ASL-3 Required Safeguards and conduct a follow-up capability assessment to c | NONE |
| ANT-RSP-v2-2-0019 | N/A | For the ASL-3 Deployment Standard, we will evaluate whether it is robust to persistent attempts to misuse the capability | NONE |
| ANT-RSP-v2-2-0020 | N/A | For the ASL-3 Security Standard, we will evaluate whether it is highly protected against non-state attackers attempting  | NONE |
| ANT-RSP-v2-2-0021 | N/A | If we determine that we have met the ASL-3 Required Safeguards, then we will proceed to deployment, provided we have als | NONE |
| ANT-RSP-v2-2-0022 | N/A | Follow-up capability assessment. In parallel with upgrading a model to the ASL-3 Required Safeguards, we will conduct a  | NONE |
| ANT-RSP-v2-2-0023 | N/A | Deployment and scaling outcomes. We may deploy or store a model if either of the following criteria are met: (1) the mod | NONE |
| ANT-RSP-v2-2-0024 | N/A | or (2) the model's capabilities have surpassed the existing Capabilities Threshold, but we have implemented the ASL-3 Re | NONE |
| ANT-RSP-v2-2-0025 | N/A | In any scenario where we determine that a model requires ASL-3 Required Safeguards but we are unable to implement them i | NONE |
| ANT-RSP-v2-2-0031 | N/A | In September 2023, we released our Responsible Scaling Policy (RSP), a first-of-its-kind public commitment not to train  | NONE |
| ANT-RSP-v2-2-0055 | N/A | This policy also helps satisfy our Voluntary White House Commitments (2023) and Frontier AI Safety Commitments (2024). | NONE |
| ANT-RSP-v2-2-0075 | 1 | A Capability Threshold is a prespecified level of AI capability that, if reached, signals (1) a meaningful increase in t | NONE |
| ANT-RSP-v2-2-0076 | 1 | In other words, a Capability Threshold serves as a trigger for shifting from an ASL-N Standard to an ASL-N+1 Standard (o | NONE |
| ANT-RSP-v2-2-0081 | 2 | We will conduct assessments to inform when to implement the Required Safeguards (see Section 4). | NONE |
| ANT-RSP-v2-2-0100 | 2 | We will test for this checkpoint and, by the time we reach it, we will (1) aim to have met (or be close to meeting) the  | NONE |
| ANT-RSP-v2-2-0101 | 2 | (2) share an update on our progress around that time; and (3) begin testing for the full Autonomous AI R&D Capability Th | NONE |
| ANT-RSP-v2-2-0102 | 2 | We will also maintain a list of capabilities that we think require significant investigation and may require stronger sa | NONE |
| ANT-RSP-v2-2-0104 | 2 | These capabilities may warrant a higher standard of safeguards, such as the ASL-3 Security or Deployment Standard. | NONE |
| ANT-RSP-v2-2-0111 | Table 2 / Cyber Operations / Ongoing Assessment | We will document any salient results alongside our Capability Reports (see Section 3). | NONE |
| ANT-RSP-v2-2-0116 | 3.1 | We will routinely test models to determine whether their capabilities fall sufficiently far below the Capability Thresho | NONE |
| ANT-RSP-v2-2-0145 | 3.3 | If, after the comprehensive testing, we determine that the model is sufficiently below the relevant Capability Threshold | NONE |
| ANT-RSP-v2-2-0148 | 3.3 / step 2 | The report will be escalated to the CEO and the Responsible Scaling Officer, who will (1) make the ultimate determinatio | NONE |
| ANT-RSP-v2-2-0149 | 3.3 / step 3 | In general, as noted in Sections 7.1.4 and 7.2.2, we will solicit both internal and external expert feedback on the repo | NONE |
| ANT-RSP-v2-2-0153 | 3.3 | This means that we will (1) upgrade to the ASL-3 Required Safeguards (see Section 4) and (2) conduct follow-up a capabil | NONE |
| ANT-RSP-v2-2-0154 | 4 | To determine whether the measures we have adopted satisfy the ASL-3 Required Safeguards, we will conduct a safeguards as | NONE |
| ANT-RSP-v2-2-0155 | 4 | As noted, the Required Safeguards for each Capability Threshold are specified in Section 2. | NONE |
| ANT-RSP-v2-2-0157 | fn7 | Currently, these will be informal estimates of (1) the extent to which widely available elicitation techniques may impro | NONE |
| ANT-RSP-v2-2-0161 | 4.1 | When a model must meet the ASL-3 Deployment Standard, we will evaluate whether the measures we have implemented make us  | NONE |
| ANT-RSP-v2-2-0174 | 4.2 | When a model must meet the ASL-3 Security Standard, we will evaluate whether the measures we have implemented make us hi | NONE |
| ANT-RSP-v2-2-0191 | 4.2 / bullet 2 / sub e | Existing guidance: Aligning where appropriate with existing guidance on securing model weights, including Securing AI Mo | NONE |
| ANT-RSP-v2-2-0192 | fn11 | We will implement robust controls to mitigate basic insider risk, but consider mitigating risks from sophisticated or st | NONE |
| ANT-RSP-v2-2-0196 | 4.2 / bullet 3 | Audits: Develop plans to (1) audit and assess the design and implementation of the security program and (2) share these  | NONE |
| ANT-RSP-v2-2-0199 | 4.3 | If, after the evaluations above, we determine that we have met the ASL-3 Required Safeguards, then we may proceed with d | NONE |
| ANT-RSP-v2-2-0200 | 4.3 | The process for determining whether we have met the ASL-3 Required Safeguards is as follows: | NONE |
| ANT-RSP-v2-2-0202 | 4.3 / step 2 | The Safeguards Report(s) will be escalated to the CEO and the Responsible Scaling Officer, who will (1) make the ultimat | NONE |
| ANT-RSP-v2-2-0203 | 4.3 / step 3 | In general, as noted in Sections 7.1.4 and 7.2.2, we will solicit both internal and external expert feedback on the repo | NONE |
| ANT-RSP-v2-2-0208 | 5 | In parallel with upgrading a model to the Required Safeguards, we will (1) update this policy to include any additional  | NONE |
| ANT-RSP-v2-2-0209 | 6.1 | To summarize the commitments and procedures outlined above, we may deploy or store a model if either of the following cr | NONE |
| ANT-RSP-v2-2-0210 | 6.1 | or (2) the model's capabilities have surpassed the existing Capabilities Threshold, but we have implemented the ASL-3 Re | NONE |
| ANT-RSP-v2-2-0212 | 6.2 | In any scenario where we determine that a model requires ASL-3 Required Safeguards but we are unable to implement them i | NONE |
| ANT-RSP-v2-2-0213 | 6.2 / bullet 1 | Interim measures: The CEO and Responsible Scaling Officer may approve the use of interim measures that provide the same  | NONE |
| ANT-RSP-v2-2-0215 | 6.2 / bullet 1 | In the security context, an example of such a measure would be storing the model weights in a single-purpose, isolated n | NONE |
| ANT-RSP-v2-2-0218 | 6.2 / bullet 2 | In the deployment context, we will de-deploy the model and replace it with a model that falls below the Capability Thres | NONE |
| ANT-RSP-v2-2-0220 | 6.2 / bullet 3 | Monitoring pretraining: We will not train models with comparable or greater capabilities to the one that requires the AS | NONE |
| ANT-RSP-v2-2-0222 | 6.2 / bullet 3 | If the pretraining model's capabilities are comparable or greater, we will pause training until we have implemented the  | NONE |
| ANT-RSP-v2-2-0225 | fn13 | We consider implementation of the ASL-3 Security Standard alone sufficient to continue training, regardless of whether t | NONE |
| ANT-RSP-v2-2-0228 | 7.1 / item 1 | The Responsible Scaling Officer's duties will include (but are not limited to): (1) as needed, proposing updates to this | NONE |
| ANT-RSP-v2-2-0229 | 7.1 / item 1 | (3) reviewing major contracts (i.e., deployment partnerships) for consistency with this policy; (4) overseeing implement | NONE |
| ANT-RSP-v2-2-0230 | 7.1 / item 1 | (6) promptly notifying the Board of Directors of any cases of noncompliance that pose material risk; and (7) making judg | NONE |
| ANT-RSP-v2-2-0231 | 7.1 / item 2 | Readiness: We will develop internal safety procedures for incident scenarios. Such scenarios include (1) pausing trainin | NONE |
| ANT-RSP-v2-2-0237 | 7.1 / item 5 | We will also establish a policy governing noncompliance reporting, which will (1) protect reporters from retaliation and | NONE |
| ANT-RSP-v2-2-0241 | fn14 | In addition to noncompliance processes, we will (1) establish pathways for Anthropic staff to raise any issues related t | NONE |
| ANT-RSP-v2-2-0264 | App A / ASL-3 Standard | A higher level of safeguards required when a model cannot be certified as ASL-2 appropriate. It includes more stringent  | NONE |
| ANT-RSP-v2-2-0280 | App B / Security intro | ASL-2 Security Standard: A security system that can likely thwart most opportunistic attackers. | NONE |
| ANT-RSP-v2-2-0289 | App B / Security / item 5 | Process elements like incident reporting procedures, lost/stolen device protocols and Detection and Response should supp | NONE |
| ANT-RSP-v2-2-0292 | App C / intro | This appendix contains detailed definitions for each Capability Threshold in Section 2. | NONE |
| ANT-RSP-v2-2-0304 | fn21 | This comparison is hard to make in practice; this note is to clarify the meaning of the conceptual threshold and the fac | NONE |
| ANT-RSP-v2-2-0307 | Changelog / Sept 19 2023 (v1.0) | September 19, 2023 (RSP v1.0) RSP-2023 (aka RSP v1.0): Initial version. | NONE |
| ANT-RSP-v2-2-0308 | Changelog / Oct 15 2024 (v2.0) intro | RSP-2024: This update introduces a more flexible and nuanced approach to assessing and managing AI risks while maintaini | NONE |
| ANT-RSP-v2-2-0315 | Changelog / v2.0 / ARA threshold now a checkpoint | We now believe that these capabilities - at the levels we initially considered - would not necessitate the ASL-3 standar | NONE |
| ANT-RSP-v2-2-0326 | Changelog / v2.0 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | NONE |
| ANT-RSP-v2-2-0329 | Changelog / v2.0 / Clarified ASL-3 and ASL-2 security threat models | Clarified ASL-3 and ASL-2 security threat models: We have clarified which actors are in and out of scope for the ASL-3 S | NONE |
| ANT-RSP-v2-2-0330 | Changelog / v2.0 / Clarified ASL-3 and ASL-2 security threat models | We also removed the commitment to protect against scaled attacks and distillation attacks from the ASL-2 Security standa | NONE |
| ANT-RSP-v2-2-0331 | Changelog / v2.0 / Clarified ASL-3 and ASL-2 security threat models | While distillation remains a concern for more capable models, models stored under ASL-2 safeguards have not yet reached  | NONE |
| ANT-RSP-v2-2-0332 | Changelog / v2.0 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | NONE |
| ANT-RSP-v2-2-0339 | Changelog / March 31 2025 (v2.1) intro | RSP-2025: This update clarifies which Capability Thresholds would require enhanced safeguards beyond our current ASL-3 s | NONE |
| ANT-RSP-v2-2-0343 | Changelog / v2.1 / Iterative Commitment | We have decided not to maintain a commitment to define ASL-N+1 evaluations by the time we develop ASL-N models; such an  | NONE |
| ANT-RSP-v2-2-0345 | Changelog / May 14 2025 (v2.2) / ASL-3 Security | ASL-3 Security: This update excludes both sophisticated insiders and state-compromised insiders from the ASL-3 Security  | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| ANT-RSP-v2-2-0028 | N/A | As frontier AI models advance, we believe they will bring about transformative benefits for our society and economy. | mid-unit |
| ANT-RSP-v2-2-0044 | N/A | By sharing our approach externally, we aim to set a new industry standard that encourages widespread adoption of similar | mid-unit |
| ANT-RSP-v2-2-0067 | 1 | We expect to continue refining our framework in response to future risks (for example, the risk that an AI system attemp | initial |
| ANT-RSP-v2-2-0080 | 2 | We believe these safeguards are achievable with sufficient investment and advance planning into research and development | initial |
| ANT-RSP-v2-2-0087 | Table 1 / CBRN / CBRN-4 / Required Safeguards | We expect this threshold will require the ASL-4 Deployment and Security Standards. We plan to add more information about | initial |
| ANT-RSP-v2-2-0093 | Table 1 / AI R&D / AI R&D-5 / Required Safeguards | At minimum, the ASL-4 Security Standard (which would protect against model-weight theft by state-level adversaries) is r | mid-unit |
| ANT-RSP-v2-2-0115 | fn2 | We recognize the potential risks of highly persuasive AI models. While we are actively consulting experts, we believe th | initial |
| ANT-RSP-v2-2-0184 | 4.2 / bullet 2 / sub a | We expect this will include a combination of physical security, encryption, cloud security, infrastructure policy, acces | initial |
| ANT-RSP-v2-2-0186 | 4.2 / bullet 2 / sub b | We expect this will include a combination of software inventory, supply chain security, artifact integrity, binary autho | initial |
| ANT-RSP-v2-2-0188 | 4.2 / bullet 2 / sub c | We expect this will include a combination of endpoint patching, product security testing, log management, asset monitori | initial |
| ANT-RSP-v2-2-0190 | 4.2 / bullet 2 / sub d | We expect meeting this standard of security to require roughly 5-10% of employees being dedicated to security and securi | initial |
| ANT-RSP-v2-2-0197 | 4.2 / bullet 3 | We expect this to include independent validation of threat modeling and risk assessment results; a sampling-based audit  | initial |
| ANT-RSP-v2-2-0231 | 7.1 / item 2 | Readiness: We will develop internal safety procedures for incident scenarios. Such scenarios include (1) pausing trainin | mid-unit |
| ANT-RSP-v2-2-0253 | 7.2 / item 4 | Procedural compliance review: On approximately an annual basis, we will commission a third-party review that assesses wh | mid-unit |
| ANT-RSP-v2-2-0260 | fn19 | Where possible, we will include descriptions of the empirical evaluation results we believe would indicate that a model  | mid-unit |
| ANT-RSP-v2-2-0326 | Changelog / v2.0 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | mid-unit |
| ANT-RSP-v2-2-0332 | Changelog / v2.0 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | mid-unit |
| ANT-RSP-v2-2-0336 | Changelog / v2.0 / New Capability and Safeguards Reports | We expect that aggregating all the available evidence about model capabilities will provide decision makers with a more  | initial |
| ANT-RSP-v2-2-0344 | Changelog / v2.1 / Iterative Commitment | We believe it is more practical and sensible instead to commit to reconsidering the whole list of Capability Thresholds  | initial |

## Check 5 — Suspicious units

Under five words, or over 75.

Nothing flagged.

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| ANT-RSP-v2-2.01.jsonl → ANT-RSP-v2-2.02.jsonl | ANT-RSP-v2-2-0154 | 4. Safeguards Assessment | none detected |
| ANT-RSP-v2-2.02.jsonl → ANT-RSP-v2-2.03.jsonl | ANT-RSP-v2-2-0227 | 7. Governance and Transparency / 7.1. Internal Governance | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **3**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 348 |
| Tables detected | 3 |
| Units in tables | 28 |
| `context_stem` = NONE | 226 |
| `stated_bar` populated | 47 |
| `duplicate_of` populated | 13 |
| Median excerpt words | 25 |

| unit_type | n |
|---|---|
| paragraph | 192 |
| numbered | 74 |
| footnote | 40 |
| table_cell | 28 |
| bullet | 14 |
