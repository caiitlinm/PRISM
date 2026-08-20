# Stage 4 unit review — GDM-FSF-v3-0

Google DeepMind · Frontier Safety Framework · Version 3.0 · 2025-09-22 · 16 pages

**194 units.** Frozen at `study/corpus/deepmind/units/GDM-FSF-v3-0.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| Table 2.2.1.a | 4 | 2 | GDM-FSF-v3-0-0114 |
| Table 2.2.2.a | 4 | 2 | GDM-FSF-v3-0-0119 |
| Table 2.2.3.a | 3 | 3 | GDM-FSF-v3-0-0125 |
| Table 3.2.1.a | 10 | 10 | GDM-FSF-v3-0-0151 |
| Table 4.a | 4 | 4 | GDM-FSF-v3-0-0170 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| GDM-FSF-v3-0-0016 | fn1 | See https://www.gov.uk/government/publications/emerging-processes-for-frontier-ai-safety, https://metr.org/faisc, https: | 6 words |
| GDM-FSF-v3-0-0048 | fn4 | We exclude misalignment risk from this list of domains because of its exploratory nature. | 14 words |
| GDM-FSF-v3-0-0055 | 1.4 | This will inform the formulation and application of a response plan. | 11 words |
| GDM-FSF-v3-0-0060 | 1.5 | We will use various processes to evaluate the effectiveness and limitations of mitigations: | 13 words |
| GDM-FSF-v3-0-0109 | 2.2 | In practice, our overall security posture may commonly exceed the baseline levels recommended here. | 14 words |
| GDM-FSF-v3-0-0156 | fn14 | The same caveats regarding security levels for misuse CCLs apply. | 10 words |
| GDM-FSF-v3-0-0176 | 5.1 / lead-in | Following this assessment, we may: | 5 words |
| GDM-FSF-v3-0-0186 | 5.2 / closing 2 | We will continue to review and evolve our disclosure process over time. | 12 words |

## Check 3 — `stated_bar` audit

16 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| GDM-FSF-v3-0-0065 | fn5 | A safety case is an assessable argument showing how severe risks associated with a model's CCLs have been reduced to an  | NONE |
| GDM-FSF-v3-0-0089 | fn8 | In other words, "security level N" indicates security controls and detections at a level generally aligned with RAND SL  | NONE |
| GDM-FSF-v3-0-0187 | 5.3 / bullet 1 | Version 2.0 (4 February 2025) | NONE |
| GDM-FSF-v3-0-0188 | 5.3 / bullet 2 | Version 1.0 (17 May 2024) | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| GDM-FSF-v3-0-0015 | N/A | We will review the Framework periodically and we expect it to evolve substantially as our understanding of the risks and | mid-unit |
| GDM-FSF-v3-0-0022 | 1.1 | The approaches and mitigations outlined in the Framework are not exclusive to models where we believe a severe risk coul | mid-unit |
| GDM-FSF-v3-0-0088 | 2.1.1 | Because AI security is an area of active research, we expect the concrete measures implemented to reach each level of se | mid-unit |
| GDM-FSF-v3-0-0106 | 2.1.2 | With iteration on safeguards and safety cases, we believe that we are able to make informed decisions about the level of | mid-unit |
| GDM-FSF-v3-0-0107 | 2.2 | The table below details a set of CCLs we have identified through ongoing analysis of the CBRN, cyber, and harmful manipu | mid-unit |
| GDM-FSF-v3-0-0112 | 2.2 | Relatedly, we believe these recommendations will only be effective if the entire frontier AI field applies them, and of  | mid-unit |
| GDM-FSF-v3-0-0146 | 3.1.2 / closing para 2 | With iteration on safeguards and safety cases, we believe that we are able to make informed decisions about the level of | mid-unit |
| GDM-FSF-v3-0-0147 | 3.2 | The table below details a set of ML R&D CCLs we have identified that may lead to heightened severe risk through ML R&D.  | mid-unit |
| GDM-FSF-v3-0-0155 | Table 3.2.1.a / ML R&D acceleration level 1 / Recommended security level and rationale (caveat) | However, we expect that acceleration will stem from systems of models integrated with workflows, rather than the model a | mid-unit |
| GDM-FSF-v3-0-0168 | Section 4 / para 2 | Given its nascency, we expect our approach to misalignment risk to evolve substantially. This section is therefore illus | mid-unit |
| GDM-FSF-v3-0-0180 | 5.2 | If we assess that a model has reached a CCL that poses an unmitigated and material risk to overall public safety, we aim | mid-unit |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| GDM-FSF-v3-0-0069-a | 1.6 / bullet 2 / sub-bullet 1 | We assess that the deployment mitigations have brought the risk of severe harm to an appropriate level proportionate to  | 85 |
| GDM-FSF-v3-0-0115 | Table 2.2.1.a / CBRN uplift level 1 / Recommended security level and rationale | Security level 2 | 3 |
| GDM-FSF-v3-0-0120 | Table 2.2.2.a / Cyber uplift level 1 / Recommended security level and rationale | Security level 2 | 3 |
| GDM-FSF-v3-0-0125 | Table 2.2.3.a / Harmful manipulation level / Recommended security level and rationale | Security level 2 | 3 |
| GDM-FSF-v3-0-0152 | Table 3.2.1.a / ML R&D acceleration level 1 / Recommended security level and rationale | Security level 3 | 3 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| GDM-FSF-v3-0.01.jsonl → GDM-FSF-v3-0.02.jsonl | GDM-FSF-v3-0-0123 | 2.2.3 Harmful Manipulation | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **5**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 194 |
| Tables detected | 5 |
| Units in tables | 25 |
| `context_stem` = NONE | 120 |
| `stated_bar` populated | 16 |
| `duplicate_of` populated | 4 |
| Median excerpt words | 28 |

| unit_type | n |
|---|---|
| paragraph | 97 |
| bullet | 41 |
| table_cell | 25 |
| footnote | 15 |
| numbered | 15 |
| callout | 1 |
