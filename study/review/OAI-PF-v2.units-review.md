# Stage 4 unit review — OAI-PF-v2

OpenAI · Preparedness Framework · Version 2 · 2025-04-15 · 22 pages

**372 units.** Frozen at `study/corpus/openai/units/OAI-PF-v2.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| Table 1 | 29 | 27 | OAI-PF-v2-0066 |
| Table 2 | 11 | 11 | OAI-PF-v2-0103 |
| Table 3 | 9 | 9 | OAI-PF-v2-0175 |
| Table 4 | 24 | 24 | OAI-PF-v2-0280 |
| Table 5 | 26 | 25 | OAI-PF-v2-0314 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| OAI-PF-v2-0020 | 1 | To do this, we: | 4 words |
| OAI-PF-v2-0030 | 1.1 | Our environment is changing in four key ways: | 8 words |
| OAI-PF-v2-0041 | fn2 | For example, our adoption of Capability Reports and Safeguards Reports parallels Anthropic’s updated RSP. | 14 words |
| OAI-PF-v2-0052 | 2.1 | We review and update Tracked Categories periodically or when we learn significant new information. | 14 words |
| OAI-PF-v2-0055 | 2.2 | SAG reviews and approves these threat models. | 7 words |
| OAI-PF-v2-0057 | 2.2 | High capability thresholds mean capabilities that significantly increase existing risk vectors for severe harm. | 14 words |
| OAI-PF-v2-0061 | fn3 | These criteria were informed in part by Meta’s recent Frontier AI Framework. | 12 words |
| OAI-PF-v2-0074 | fn5 | We will build safeguards against both biological and chemical threats. | 10 words |
| OAI-PF-v2-0101 | 2.3 | We will periodically review the latest research and findings for each Research Category. | 13 words |
| OAI-PF-v2-0118 | callout 2 | Nuclear and Radiological capabilities are now a Research Category. | 9 words |
| OAI-PF-v2-0135 | 3.1 | Capability evaluations come in two different forms: | 7 words |
| OAI-PF-v2-0142 | 3.2 | Examples of such covered deployments are: | 6 words |
| OAI-PF-v2-0151 | 3.3 | The SAG reviews the Capabilities Report and decides on next steps. These can include: | 14 words |
| OAI-PF-v2-0183 | Table 3 / caption | Table 3: Types of safeguards. See Appendix C.1 and C.2 for additional details. | 13 words |
| OAI-PF-v2-0188 | 4.2 | Based on this evidence, SAG then has the following decision points: | 11 words |
| OAI-PF-v2-0194 | 4.2 | We expect to continuously improve our safeguards over time. | 9 words |
| OAI-PF-v2-0248 | B / intro | We establish an operational structure to oversee our procedural commitments within the Preparedness Framework. | 14 words |
| OAI-PF-v2-0272 | C / reminder | Systems that reach Critical capability also require sufficient safeguards during development. | 11 words |
| OAI-PF-v2-0345 | C.3 / intro to list | We will require the following practices for High capability models: | 10 words |

## Check 3 — `stated_bar` audit

58 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| OAI-PF-v2-0065 | 2.2 | We further break down the specific capability thresholds, associated risks, and safeguards for those thresholds in Table | NONE |
| OAI-PF-v2-0078 | Table 1 / Cybersecurity / Associated risk / High / part 2 | In conjunction with a Long-range Autonomy capability (Section 2.3), models that could bypass OpenAI’s technical safeguar | NONE |
| OAI-PF-v2-0128 | callout 3 | We believe many of the challenges around AI persuasion risks require solutions at a systemic or societal level, and we a | NONE |
| OAI-PF-v2-0140 | callout / para 3 | You can learn more about our Tracked Category capability evaluations in past system cards, such as those for OpenAI o1 a | NONE |
| OAI-PF-v2-0143 | 3.2 / bullet 1 | every frontier model (e.g., OpenAI o1 or OpenAI o3) that we plan to deploy externally | NONE |
| OAI-PF-v2-0162 | 4.1 | We consider separate safeguards for two of the main ways in which risks can be realized: a malicious user, who can lever | NONE |
| OAI-PF-v2-0183 | Table 3 / caption | Table 3: Types of safeguards. See Appendix C.1 and C.2 for additional details. | NONE |
| OAI-PF-v2-0217 | 5.2 / bullet 2 | Third-party evaluation of tracked model capabilities: If we deem that a deployment warrants deeper testing of Tracked Ca | NONE |
| OAI-PF-v2-0243 | A / item 9 | Clarify approach to establishing safeguard efficacy, moving beyond the flawed approach of re-running capability evaluati | NONE |
| OAI-PF-v2-0315 | Table 5 / Lack of Autonomous Capability / Efficacy | Long-range Autonomy capability evaluations show the model cannot act autonomously as described in the threat model (Sect | NONE |
| OAI-PF-v2-0342 | C.3 / para 2 | Our security practices are designed to protect against external and internal adversaries and align with established fram | NONE |
| OAI-PF-v2-0344 | C.3 / para 2 | This may include efforts emerging from the Cloud Security Alliance's AI Safety Initiative or the NIST SP 800-218 AI upda | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| OAI-PF-v2-0010 | N/A | This Framework lays out the kinds of safeguards we expect to need, and how we’ll confirm internally and show externally  | mid-unit |
| OAI-PF-v2-0014 | N/A | This revision of the Preparedness Framework focuses on the safeguards we expect will be needed for future models more ca | mid-unit |
| OAI-PF-v2-0017 | fn1 | In choosing to set a high bar here, we aim to ensure that the most severe risks receive attention commensurate with thei | mid-unit |
| OAI-PF-v2-0018 | 1 | We believe there are a limited number of AI capabilities that could pose new risks of severe harm. | initial |
| OAI-PF-v2-0095 | 2.3 | There are also some areas of frontier capability that do not meet the criteria to be Tracked Categories, but where we be | mid-unit |
| OAI-PF-v2-0117 | callout 1 | Meanwhile, while these latter risks’ threat models are not yet sufficiently mature to receive the scrutiny of Tracked Ca | mid-unit |
| OAI-PF-v2-0128 | callout 3 | We believe many of the challenges around AI persuasion risks require solutions at a systemic or societal level, and we a | initial |
| OAI-PF-v2-0194 | 4.2 | We expect to continuously improve our safeguards over time. | initial |
| OAI-PF-v2-0196 | 4.3 | We recognize that another frontier AI model developer might develop or release a system with High or Critical capability | initial |
| OAI-PF-v2-0204 | 4.4 | We do not currently possess any models that have Critical levels of capability, and we expect to further update this Pre | mid-unit |
| OAI-PF-v2-0235 | A / item 5 | Introduce Research Categories, areas of capability that do not meet the criteria to be Tracked Categories, but where we  | mid-unit |
| OAI-PF-v2-0240 | A / item 7 | Provide risk-specific safeguard guidelines. This information gives more detail on how we expect to safely develop and de | mid-unit |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| OAI-PF-v2-0020 | 1 | To do this, we: | 4 |
| OAI-PF-v2-0298 | Table 4 / Trust-based Access / Safeguards / sub-bullet Trusted customer relationships | Trusted customer relationships | 3 |
| OAI-PF-v2-0335 | Table 5 / System Architecture / Safeguards / bullet 2 | Limiting credentials | 2 |
| OAI-PF-v2-0337 | Table 5 / System Architecture / Safeguards / bullet 4 | Limiting persistence or state | 4 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| OAI-PF-v2.01.jsonl → OAI-PF-v2.02.jsonl | OAI-PF-v2-0130 | 3.1 Evaluation approach | none detected |
| OAI-PF-v2.02.jsonl → OAI-PF-v2.03.jsonl | OAI-PF-v2-0207 | 5 Building trust | none detected |

## Check 8 — OAI-PF-v2 Table 1 `context_stem`

Table 1 has its row labels offset onto each row's second line in the extraction. It is the most code-dense table in the corpus, and a stem failure here is invisible until it surfaces as unexplained zeros on C09 and C13. **Check every row.**

| unit_id | locator | excerpt | context_stem |
|---|---|---|---|
| OAI-PF-v2-0066 | Table 1 / Biological and Chemical / Capability threshold / High | The model can provide meaningful counterfactual assistance (relative to unlimited access to baseline of tools available  | Tracked Category: Biological and Chemical — Capability threshold that could lead to the risk — High |
| OAI-PF-v2-0067 | Table 1 / Biological and Chemical / Associated risk / High | Significantly increased likelihood and frequency of biological or chemical terror events by non-state actors using known | Tracked Category: Biological and Chemical — Associated risk of severe harm — High |
| OAI-PF-v2-0068 | Table 1 / Biological and Chemical / Safeguard guidelines / High / bullet 1 | Require security controls meeting High standard (Appendix C.3) | Tracked Category: Biological and Chemical — Risk-specific safeguard guidelines — High |
| OAI-PF-v2-0069 | Table 1 / Biological and Chemical / Safeguard guidelines / High / bullet 2 | Require safeguards against misuse meeting High standard (Appendix C.1) before external deployment | Tracked Category: Biological and Chemical — Risk-specific safeguard guidelines — High |
| OAI-PF-v2-0070 | Table 1 / Biological and Chemical / Capability threshold / Critical | The model can enable an expert to develop a highly dangerous novel threat vector (e.g., comparable to a novel CDC Class  | Tracked Category: Biological and Chemical — Capability threshold that could lead to the risk — Critical |
| OAI-PF-v2-0071 | Table 1 / Biological and Chemical / Associated risk / Critical | Proliferating the ability to create a novel threat vector of the severity of a CDC Class A biological agent (i.e., high  | Tracked Category: Biological and Chemical — Associated risk of severe harm — Critical |
| OAI-PF-v2-0072 | Table 1 / Biological and Chemical / Safeguard guidelines / Critical / bullet 1 | Until we have specified safeguards and security controls that would meet a Critical standard, halt further development | Tracked Category: Biological and Chemical — Risk-specific safeguard guidelines — Critical |
| OAI-PF-v2-0073 | Table 1 / Biological and Chemical / Safeguard guidelines / Critical / bullet 2 | Contribute towards improved public policy and pandemic preparedness | Tracked Category: Biological and Chemical — Risk-specific safeguard guidelines — Critical |
| OAI-PF-v2-0074 | fn5 | We will build safeguards against both biological and chemical threats. | NONE |
| OAI-PF-v2-0075 | fn5 | Given the higher potential severity of biological threats relative to chemical ones, we will prioritize Biological capab | NONE |
| OAI-PF-v2-0076 | Table 1 / Cybersecurity / Capability threshold / High | The model removes existing bottlenecks to scaling cyber operations including by automating end-to-end cyber operations a | Tracked Category: Cybersecurity — Capability threshold that could lead to the risk — High |
| OAI-PF-v2-0077 | Table 1 / Cybersecurity / Associated risk / High / part 1 | Removing bottlenecks limiting malicious cyber activity may upset the current cyberoffense-cyberdefense balance by signif | Tracked Category: Cybersecurity — Associated risk of severe harm — High |
| OAI-PF-v2-0078 | Table 1 / Cybersecurity / Associated risk / High / part 2 | In conjunction with a Long-range Autonomy capability (Section 2.3), models that could bypass OpenAI’s technical safeguar | Tracked Category: Cybersecurity — Associated risk of severe harm — High |
| OAI-PF-v2-0079 | Table 1 / Cybersecurity / Safeguard guidelines / High / bullet 1 | Require security controls meeting High standard (Appendix C.3) | Tracked Category: Cybersecurity — Risk-specific safeguard guidelines — High |
| OAI-PF-v2-0080 | Table 1 / Cybersecurity / Safeguard guidelines / High / bullet 2 | Require safeguards against misuse meeting High standard (Appendix C.1) for external deployment | Tracked Category: Cybersecurity — Risk-specific safeguard guidelines — High |
| OAI-PF-v2-0081 | Table 1 / Cybersecurity / Safeguard guidelines / High / bullet 3 | Require safeguards meeting High standard against misalignment (Appendix C.2) for large-scale internal deployment | Tracked Category: Cybersecurity — Risk-specific safeguard guidelines — High |
| OAI-PF-v2-0082 | Table 1 / Cybersecurity / Safeguard guidelines / High / bullet 4 | Contribute towards improved cyberdefense policies and tools for cyberdefense | Tracked Category: Cybersecurity — Risk-specific safeguard guidelines — High |
| OAI-PF-v2-0083 | Table 1 / Cybersecurity / Capability threshold / Critical | A tool-augmented model can identify and develop functional zero-day exploits of all severity levels in many hardened rea | Tracked Category: Cybersecurity — Capability threshold that could lead to the risk — Critical |
| OAI-PF-v2-0084 | Table 1 / Cybersecurity / Associated risk / Critical | Finding and executing end-to-end exploits for all software could lead to catastrophe from unilateral actors, hacking mil | Tracked Category: Cybersecurity — Associated risk of severe harm — Critical |
| OAI-PF-v2-0085 | Table 1 / Cybersecurity / Associated risk / Critical | Novel cyber operations, e.g., those involving novel zero-days or novel methods of command-and-control, generally pose th | Tracked Category: Cybersecurity — Associated risk of severe harm — Critical |
| OAI-PF-v2-0086 | Table 1 / Cybersecurity / Safeguard guidelines / Critical / bullet 1 | Until we have specified safeguards and security controls standards that would meet a Critical standard, halt further dev | Tracked Category: Cybersecurity — Risk-specific safeguard guidelines — Critical |
| OAI-PF-v2-0087 | Table 1 / AI Self-improvement / Capability threshold / High | The model’s impact is equivalent to giving every OpenAI researcher a highly performant mid-career research engineer assi | Tracked Category: AI Self-improvement — Capability threshold that could lead to the risk — High |
| OAI-PF-v2-0088 | Table 1 / AI Self-improvement / Associated risk / High / part 1 | This milestone suggests AI self-improvement may be beginning to accelerate. | Tracked Category: AI Self-improvement — Associated risk of severe harm — High |
| OAI-PF-v2-0089 | Table 1 / AI Self-improvement / Associated risk / High / part 2 | To meet the large-scale safety research, operations, and security investments that need to be in place when we reach Cri | Tracked Category: AI Self-improvement — Associated risk of severe harm — High |
| OAI-PF-v2-0090 | Table 1 / AI Self-improvement / Safeguard guidelines / High | Require security controls meeting High standard (Appendix C.3) | Tracked Category: AI Self-improvement — Risk-specific safeguard guidelines — High |
| OAI-PF-v2-0091 | Table 1 / AI Self-improvement / Capability threshold / Critical | The model is capable of recursively self improving (i.e., fully automated AI R&D), defined as either (leading indicator) | Tracked Category: AI Self-improvement — Capability threshold that could lead to the risk — Critical |
| OAI-PF-v2-0092 | Table 1 / AI Self-improvement / Associated risk / Critical / part 1 | A major acceleration in the rate of AI R&D could rapidly increase the rate at which new capabilities and risks emerge, t | Tracked Category: AI Self-improvement — Associated risk of severe harm — Critical |
| OAI-PF-v2-0093 | Table 1 / AI Self-improvement / Associated risk / Critical / part 2 | including risks to maintaining human control of the AI system itself. | Tracked Category: AI Self-improvement — Associated risk of severe harm — Critical |
| OAI-PF-v2-0094 | Table 1 / AI Self-improvement / Safeguard guidelines / Critical | Until we have specified safeguards and security controls that would meet a Critical standard, halt further development | Tracked Category: AI Self-improvement — Risk-specific safeguard guidelines — Critical |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **5**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 372 |
| Tables detected | 5 |
| Units in tables | 99 |
| `context_stem` = NONE | 147 |
| `stated_bar` populated | 58 |
| `duplicate_of` populated | 7 |
| Median excerpt words | 23 |

| unit_type | n |
|---|---|
| bullet | 122 |
| paragraph | 107 |
| table_cell | 82 |
| numbered | 31 |
| callout | 20 |
| footnote | 10 |
