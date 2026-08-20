# Stage 4 unit review — GDM-FSF-v3-1

Google DeepMind · Frontier Safety Framework · Version 3.1 · 2026-04-17 · 20 pages

**281 units.** Frozen at `study/corpus/deepmind/units/GDM-FSF-v3-1.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| Table 2.2.1.a | 3 | 2 | GDM-FSF-v3-1-0150 |
| Table 2.2.2.a | 3 | 2 | GDM-FSF-v3-1-0157 |
| Table 2.2.3.a | 2 | 2 | GDM-FSF-v3-1-0162 |
| Table 3.2.2.a | 9 | 4 | GDM-FSF-v3-1-0197 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| GDM-FSF-v3-1-0004 | N/A | The core components of such Frameworks are to: | 8 words |
| GDM-FSF-v3-1-0014 | N/A | The safety and security of frontier AI models is a global public good. | 13 words |
| GDM-FSF-v3-1-0018 | N/A | The Framework is based on early and evolving research. | 9 words |
| GDM-FSF-v3-1-0021 | fn1 | See https://www.gov.uk/government/publications/emerging-processes-for-frontier-ai-safety, https://metr.org/faisc, https: | 7 words |
| GDM-FSF-v3-1-0024 | N/A | This section describes the central components of the Frontier Safety Framework. | 11 words |
| GDM-FSF-v3-1-0029 | 1.2 | The Framework is built primarily around capability thresholds called "Critical Capability Levels (CCLs)." | 13 words |
| GDM-FSF-v3-1-0032 | 1.2 | CCLs are one important component of our risk acceptance determination. | 10 words |
| GDM-FSF-v3-1-0040 | 1.2 | This update to the Framework introduces "Tracked Capability Levels (TCLs)." | 10 words |
| GDM-FSF-v3-1-0042 | 1.2 | We identify TCLs for CBRN risk, as well as ML R&D and misalignment risks. | 14 words |
| GDM-FSF-v3-1-0046 | 1.3.1 | The first part of our risk management process is risk identification. | 11 words |
| GDM-FSF-v3-1-0074 | 1.3.3 | This will inform the formulation and application of a response plan. | 11 words |
| GDM-FSF-v3-1-0081 | 1.3.4 | We will use various processes to evaluate the effectiveness and limitations of mitigations: | 13 words |
| GDM-FSF-v3-1-0122 | fn6 | See https://www.rand.org/pubs/research_reports/RRA2849-1.html, pp 21-22. | 4 words |
| GDM-FSF-v3-1-0141 | fn7 | See section 5 of https://arxiv.org/abs/2504.01849. | 5 words |
| GDM-FSF-v3-1-0143 | N/A | At this stage, additional mitigations beyond these established safeguards are not required. | 12 words |
| GDM-FSF-v3-1-0153 | 2.2.1 / CBRN TCL | The CBRN TCL is defined as follows: | 7 words |
| GDM-FSF-v3-1-0179 | fn10 | See section 6 of https://arxiv.org/abs/2504.01849. | 5 words |
| GDM-FSF-v3-1-0186 | 3.2 | We take a tiered approach to addressing ML R&D and misalignment risks: | 12 words |
| GDM-FSF-v3-1-0189 | 3.2.1 | The Stealth and Situational Awareness TCL is defined as follows: | 10 words |
| GDM-FSF-v3-1-0206 | fn11 | The same caveats regarding security levels for misuse CCLs apply. | 10 words |
| GDM-FSF-v3-1-0211 | 4.1 | This includes legal, compliance, and safety reviews with escalation procedures to ensure appropriate oversight. | 14 words |
| GDM-FSF-v3-1-0214 | 5.1 | Following this assessment, we may: | 5 words |
| GDM-FSF-v3-1-0224 | 5.2 | We will continue to review and evolve our disclosure process over time. | 12 words |
| GDM-FSF-v3-1-0247 | Glossary / Thresholds / Alert Thresholds | Alert Thresholds: are thresholds which we set marginally earlier than our CCLs. | 12 words |
| GDM-FSF-v3-1-0253 | Glossary / Inherent Risk Assessment / Early Warning Evaluations | Early Warning Evaluations: are evaluations which measure the dangerous capabilities of a model. | 13 words |
| GDM-FSF-v3-1-0255 | Glossary / Inherent Risk Assessment / Material Capability Change Assessments | Material Capability Change Assessments: indicate whether a critical capability assessment is required. | 12 words |
| GDM-FSF-v3-1-0264 | Glossary / Risk Mitigation / External Deployments | External Deployments: represent model releases to entities outside of Google. | 10 words |
| GDM-FSF-v3-1-0267 | Glossary / Risk Mitigation / Internal Deployments | Internal Deployments: represent model releases restricted to Google employees for internal use. | 12 words |

## Check 3 — `stated_bar` audit

25 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| GDM-FSF-v3-1-0021 | fn1 | See https://www.gov.uk/government/publications/emerging-processes-for-frontier-ai-safety, https://metr.org/faisc, https: | NONE |
| GDM-FSF-v3-1-0054 | 1.3.2 | For external deployment of subsequent versions of the model, we determine whether a substantial modification has been ma | NONE |
| GDM-FSF-v3-1-0122 | fn6 | See https://www.rand.org/pubs/research_reports/RRA2849-1.html, pp 21-22. | NONE |
| GDM-FSF-v3-1-0141 | fn7 | See section 5 of https://arxiv.org/abs/2504.01849. | NONE |
| GDM-FSF-v3-1-0179 | fn10 | See section 6 of https://arxiv.org/abs/2504.01849. | NONE |
| GDM-FSF-v3-1-0231 | Versions list / item 2 | Version 3.0 (September 22, 2025) | NONE |
| GDM-FSF-v3-1-0232 | Versions list / item 3 | Version 2.0 (February 4, 2025) | NONE |
| GDM-FSF-v3-1-0233 | Versions list / item 4 | Version 1.0 (May 17, 2024) | NONE |
| GDM-FSF-v3-1-0236 | Glossary / Model | There may be many different checkpoints and versions of the same model along the entire model lifecycle: we consider che | NONE |
| GDM-FSF-v3-1-0273 | fn14 | See https://www.rand.org/pubs/research_reports/RRA2849-1.html. | NONE |
| GDM-FSF-v3-1-0281 | fn15 | See also, for reference, https://arxiv.org/abs/2505.01420. | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| GDM-FSF-v3-1-0020 | N/A | We will review the Framework periodically and we expect it to evolve substantially as our understanding of the risks and | mid-unit |
| GDM-FSF-v3-1-0028 | 1.1 | The approaches and mitigations outlined in the Framework are not exclusive to models where we believe a severe risk coul | mid-unit |
| GDM-FSF-v3-1-0054 | 1.3.2 | For external deployment of subsequent versions of the model, we determine whether a substantial modification has been ma | mid-unit |
| GDM-FSF-v3-1-0120 | 2.1.1 | Because AI security is an area of active research, we expect the concrete measures implemented to reach each level of se | mid-unit |
| GDM-FSF-v3-1-0140 | 2.1.2 | With iteration on mitigations and residual risk assessments, we believe that we are able to make informed decisions abou | mid-unit |
| GDM-FSF-v3-1-0144 | 2.2 | We set out below a set of CBRN, cyber, and harmful manipulation CCLs as well as the CBRN TCL that we have identified thr | mid-unit |
| GDM-FSF-v3-1-0148 | 2.2 | Relatedly, we believe these recommendations will only be effective if the entire frontier AI field applies them, and of  | mid-unit |
| GDM-FSF-v3-1-0185 | 3.1.2 | With iteration on mitigations and residual risk assessments, we believe that we are able to make informed decisions abou | mid-unit |
| GDM-FSF-v3-1-0195 | 3.2.2 | We define ML R&D CCLs at capability levels at which misalignment, misuse and structural risks may reach a severe scale.  | mid-unit |
| GDM-FSF-v3-1-0200 | Table 3.2.2.a / ML R&D acceleration level 1 / Recommended security level and rationale | However, we expect that acceleration will stem from systems of models integrated with workflows, rather than the model a | mid-unit |
| GDM-FSF-v3-1-0218 | 5.2 | If we assess that a model has reached a CCL that poses an unmitigated and material risk to overall public safety, we aim | mid-unit |
| GDM-FSF-v3-1-0258 | Glossary / Inherent Risk Assessment / Material Capability Increases | Material Capability Increases: are meaningful new capabilities or material increases in model performance that we believ | mid-unit |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| GDM-FSF-v3-1-0122 | fn6 | See https://www.rand.org/pubs/research_reports/RRA2849-1.html, pp 21-22. | 4 |
| GDM-FSF-v3-1-0230 | Version 3.1 / bullet 6 | Introduced a glossary. | 3 |
| GDM-FSF-v3-1-0273 | fn14 | See https://www.rand.org/pubs/research_reports/RRA2849-1.html. | 2 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| GDM-FSF-v3-1.01.jsonl → GDM-FSF-v3-1.02.jsonl | GDM-FSF-v3-1-0125 | 2.1.2 Deployment Mitigations | none detected |
| GDM-FSF-v3-1.02.jsonl → GDM-FSF-v3-1.03.jsonl | GDM-FSF-v3-1-0225 | 5.3 Past Updates and Changes | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **4**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 281 |
| Tables detected | 4 |
| Units in tables | 17 |
| `context_stem` = NONE | 182 |
| `stated_bar` populated | 25 |
| `duplicate_of` populated | 11 |
| Median excerpt words | 23 |

| unit_type | n |
|---|---|
| paragraph | 166 |
| bullet | 62 |
| footnote | 19 |
| table_cell | 17 |
| numbered | 10 |
| callout | 7 |
