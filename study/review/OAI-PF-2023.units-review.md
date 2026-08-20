# Stage 4 unit review — OAI-PF-2023

OpenAI · Preparedness Framework · NONE · 2023-12-18 · 27 pages

**250 units.** Frozen at `study/corpus/openai/units/OAI-PF-2023.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| (unnumbered) CBRN | 12 | 8 | OAI-PF-2023-0067 |
| (unnumbered) Cybersecurity | 12 | 8 | OAI-PF-2023-0054 |
| (unnumbered) Model autonomy | 11 | 8 | OAI-PF-2023-0093 |
| (unnumbered) Persuasion | 9 | 8 | OAI-PF-2023-0082 |
| Table Illustrative | 12 | 12 | OAI-PF-2023-0134 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| OAI-PF-2023-0027 | N/A | This living document has three sections: | 6 words |
| OAI-PF-2023-0033 | N/A | Each of the Tracked Risk Categories comes with a gradation scale. | 11 words |
| OAI-PF-2023-0036 | N/A | Specifically, below, we lay out details for the following Tracked Risk Categories | 12 words |
| OAI-PF-2023-0050 | N/A | As mentioned, the empirical study of catastrophic risk from frontier AI models is nascent. | 14 words |
| OAI-PF-2023-0092 | N/A | Autonomy is also a prerequisite for self-exfiltration, self-improvement, and resource acquisition. | 11 words |
| OAI-PF-2023-0106 | N/A | The list of Tracked Risk Categories above is almost certainly not exhaustive. | 12 words |
| OAI-PF-2023-0146 | N/A | Cybersecurity: Low (pre-mitigation), Low (post-mitigation) | 5 words |
| OAI-PF-2023-0152 | N/A | CBRN: Low (pre-mitigation), Low (post-mitigation) | 5 words |
| OAI-PF-2023-0159 | N/A | Persuasion: Medium (pre-mitigation), Low (post-mitigation) | 5 words |
| OAI-PF-2023-0170 | N/A | Model autonomy: Medium (pre-mitigation), Low (post-mitigation) | 6 words |
| OAI-PF-2023-0174 | bullet 3 | Reward hacking eval: Model cannot reward hack in a structured environment (0% success rate) | 14 words |
| OAI-PF-2023-0180 | N/A | We now augment these processes with three safety baselines. | 9 words |
| OAI-PF-2023-0186 | N/A | Only models with a post-mitigation score of "medium" or below can be deployed. | 13 words |
| OAI-PF-2023-0189 | N/A | Only models with a post-mitigation score of "high" or below can be developed further. | 14 words |
| OAI-PF-2023-0191 | N/A | Note that this should not preclude safety-enhancing development. | 8 words |
| OAI-PF-2023-0194 | N/A | We also establish an operational structure to oversee our procedural commitments. | 11 words |
| OAI-PF-2023-0206 | N/A | The Preparedness team is responsible for: | 6 words |
| OAI-PF-2023-0224 | N/A | This also includes any audit trails created from the below. | 10 words |
| OAI-PF-2023-0229 | N/A | Therefore, the SAG will call for safety drills at a recommended minimum yearly basis | 14 words |
| OAI-PF-2023-0232 | N/A | This report includes a case with evidence from evaluations. | 9 words |
| OAI-PF-2023-0235 | N/A | The SAG Chair escalates to OpenAI leadership for a final decision. | 11 words |
| OAI-PF-2023-0238 | N/A | The BoD does not overrule the decision. | 7 words |
| OAI-PF-2023-0242 | N/A | The Preparedness team discovers a new, much more effective prompting technique. | 11 words |
| OAI-PF-2023-0248 | N/A | The BoD also does not overrule the decision. | 8 words |

## Check 3 — `stated_bar` audit

62 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| OAI-PF-2023-0025 | N/A | This is also one more way in which we are meeting our voluntary commitments to safety, security and trust in AI that we  | NONE |
| OAI-PF-2023-0081 | N/A | Typically, strong persuasion is rare and requires significant human effort (e.g., a 1:1 grassroots conversation, or a hi | NONE |
| OAI-PF-2023-0084 | Table / Persuasion / Medium / Definition | Model can create (potentially interactive) content with comparable persuasive effectiveness to typical human-written con | NONE |
| OAI-PF-2023-0160 | N/A | Model can create (potentially interactive) content with comparable persuasive effectiveness to typical human-written con | NONE |
| OAI-PF-2023-0195 | N/A | These commitments aim to make sure that: (1) there is a dedicated team “on the ground” focused on preparedness research  | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| OAI-PF-2023-0001 | N/A | We believe the scientific study of catastrophic risks from AI has fallen far short of where we need to be. | initial |
| OAI-PF-2023-0026 | N/A | We recognize other organizations for contributing to action in this space too, for example, via publishing Responsible S | initial |
| OAI-PF-2023-0034 | N/A | We believe monitoring gradations of risk will enable us to get in front of escalating threats and be able to apply more  | initial |
| OAI-PF-2023-0199 | N/A | In particular, we recognize that pausing deployment or development would be the last resort (but potentially necessary)  | mid-unit |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| OAI-PF-2023-0037 | bullet 1 | Cybersecurity | 1 |
| OAI-PF-2023-0039 | bullet 3 | Persuasion | 1 |
| OAI-PF-2023-0040 | bullet 4 | Model autonomy | 2 |
| OAI-PF-2023-0136 | Table Illustrative Scorecard (p15) / Cybersecurity / Pre-mitigation risk level | Low | 1 |
| OAI-PF-2023-0137 | Table Illustrative Scorecard (p15) / Cybersecurity / Post-mitigation risk level | Low | 1 |
| OAI-PF-2023-0138 | Table Illustrative Scorecard (p15) / CBRN / Pre-mitigation risk level | Low | 1 |
| OAI-PF-2023-0139 | Table Illustrative Scorecard (p15) / CBRN / Post-mitigation risk level | Low | 1 |
| OAI-PF-2023-0140 | Table Illustrative Scorecard (p15) / Persuasion / Pre-mitigation risk level | Medium | 1 |
| OAI-PF-2023-0141 | Table Illustrative Scorecard (p15) / Persuasion / Post-mitigation risk level | Low | 1 |
| OAI-PF-2023-0142 | Table Illustrative Scorecard (p15) / Model Autonomy / Pre-mitigation risk level | Medium | 1 |
| OAI-PF-2023-0143 | Table Illustrative Scorecard (p15) / Model Autonomy / Post-mitigation risk level | Low | 1 |
| OAI-PF-2023-0144 | Table Illustrative Scorecard (p15) / Unknown Unknowns / Pre-mitigation risk level | Low | 1 |
| OAI-PF-2023-0145 | Table Illustrative Scorecard (p15) / Unknown Unknowns / Post-mitigation risk level | Low | 1 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: p15.

| Table | Units | First unit |
|---|---|---|
| (unnumbered) CBRN | 12 | OAI-PF-2023-0067 |
| (unnumbered) Cybersecurity | 12 | OAI-PF-2023-0054 |
| (unnumbered) Model autonomy | 11 | OAI-PF-2023-0093 |
| (unnumbered) Persuasion | 9 | OAI-PF-2023-0082 |
| Table Illustrative | 12 | OAI-PF-2023-0134 |

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| OAI-PF-2023.01.jsonl → OAI-PF-2023.02.jsonl | OAI-PF-2023-0130 | Mitigations | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **5**. Transcribed pages: p15.

## Counts

| Measure | Value |
|---|---|
| Units | 250 |
| Tables detected | 5 |
| Units in tables | 56 |
| `context_stem` = NONE | 169 |
| `stated_bar` populated | 62 |
| `duplicate_of` populated | 2 |
| Median excerpt words | 24 |

| unit_type | n |
|---|---|
| paragraph | 131 |
| table_cell | 56 |
| bullet | 54 |
| callout | 5 |
| footnote | 4 |
