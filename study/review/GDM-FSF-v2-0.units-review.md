# Stage 4 unit review — GDM-FSF-v2-0

Google DeepMind · Frontier Safety Framework · Version 2.0 · 2025-02-04 · 9 pages

**138 units.** Frozen at `study/corpus/deepmind/units/GDM-FSF-v2-0.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| Table 1 | 24 | 10 | GDM-FSF-v2-0-0064 |
| Table 2 | 4 | 4 | GDM-FSF-v2-0-0103 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| GDM-FSF-v2-0-0003 | N/A | The Framework is informed by the broader conversation on Frontier AI Safety Frameworks. | 13 words |
| GDM-FSF-v2-0-0004 | N/A | The core components of Frontier AI Safety Frameworks are to: | 10 words |
| GDM-FSF-v2-0-0013 | N/A | The safety of frontier AI systems is a global public good. | 11 words |
| GDM-FSF-v2-0-0017 | N/A | The Framework is exploratory and based on early research. | 9 words |
| GDM-FSF-v2-0-0020 | fn1 | See https://www.gov.uk/government/publications/emerging-processes-for-frontier-ai-safety, https://metr.org/blog/2023-09- | 6 words |
| GDM-FSF-v2-0-0032 | N/A | This will inform the formulation and application of a response plan. | 11 words |
| GDM-FSF-v2-0-0045 | N/A | Security mitigations against exfiltration risk are important for models reaching CCLs. | 11 words |
| GDM-FSF-v2-0-0056 | numbered 3 | The safeguards for the model may be updated as well to ensure continued adequacy. | 14 words |
| GDM-FSF-v2-0-0058 | N/A | We expect these to evolve over time. | 7 words |
| GDM-FSF-v2-0-0060 | N/A | In practice, our overall security posture may commonly exceed the baseline levels recommended here. | 14 words |
| GDM-FSF-v2-0-0092 | fn11 | E.g. deletion or exfiltration of critical information, or destroying or disabling key systems. | 13 words |
| GDM-FSF-v2-0-0094 | fn13 | Relative to the counterfactual of using 2024 AI technology and tooling. | 11 words |
| GDM-FSF-v2-0-0095 | N/A | This section describes an initial approach for addressing risks of deceptive alignment. | 12 words |
| GDM-FSF-v2-0-0108 | N/A | For each deceptive alignment risk, AI developers should: | 8 words |
| GDM-FSF-v2-0-0112 | N/A | The approach above relies on two safety cases centering respectively on the claims that: | 14 words |
| GDM-FSF-v2-0-0117 | N/A | The Google DeepMind AGI Safety Council will periodically review the implementation of the Framework. | 14 words |
| GDM-FSF-v2-0-0124 | N/A | We will continue to review and evolve our disclosure process over time. | 12 words |
| GDM-FSF-v2-0-0126 | N/A | Issues that we aim to address in future versions of the Framework include: | 13 words |

## Check 3 — `stated_bar` audit

16 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| GDM-FSF-v2-0-0009 | N/A | In version 2.0 of the Framework, we specify protocols for the detection of capability levels at which models may pose se | NONE |
| GDM-FSF-v2-0-0020 | fn1 | See https://www.gov.uk/government/publications/emerging-processes-for-frontier-ai-safety, https://metr.org/blog/2023-09- | NONE |
| GDM-FSF-v2-0-0088 | fn9 | Note that we have removed the Autonomy risk domain, which was included in Frontier Safety Framework version 1.0. | NONE |
| GDM-FSF-v2-0-0094 | fn13 | Relative to the counterfactual of using 2024 AI technology and tooling. | NONE |
| GDM-FSF-v2-0-0127 | bullet 1 | Greater precision in risk modeling: While we have updated our CCLs and underlying threat models from version 1.0, there  | NONE |
| GDM-FSF-v2-0-0134 | N/A | Version 2.0 of the Frontier Safety Framework was developed by Lewis Ho, Celine Smith, Claudia van der Salm, Joslyn Barnh | NONE |
| GDM-FSF-v2-0-0137 | Past versions / bullet 1 | Version 1.0 (17 May 2024). | NONE |
| GDM-FSF-v2-0-0138 | Corrections and non-substantive changes / bullet 1 | Fixed an incorrect link to Google’s AI Principles webpage (21 March 2025). | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| GDM-FSF-v2-0-0019 | N/A | We will review the Framework periodically and we expect it to evolve substantially as our understanding of the risks and | mid-unit |
| GDM-FSF-v2-0-0049 | N/A | Because AI security is an area of active research, we expect the concrete measures implemented to reach each level of se | mid-unit |
| GDM-FSF-v2-0-0058 | N/A | We expect these to evolve over time. | initial |
| GDM-FSF-v2-0-0063 | N/A | Relatedly, we believe these recommendations will only be effective if the entire frontier AI field applies them, and of  | mid-unit |
| GDM-FSF-v2-0-0101 | N/A | When models reach this capability level, we believe applying an automated monitor to the model’s explicit reasoning (e.g | mid-unit |
| GDM-FSF-v2-0-0107 | N/A | Looking forward, we expect the approach to deceptive alignment risks to take a similar form as the deployment mitigation | mid-unit |
| GDM-FSF-v2-0-0118 | N/A | If we assess that a model has reached a CCL that poses an unmitigated and material risk to overall public safety, we aim | mid-unit |
| GDM-FSF-v2-0-0125 | N/A | We expect the Framework to evolve substantially as our understanding of the risks and benefits of frontier models improv | initial |
| GDM-FSF-v2-0-0126 | N/A | Issues that we aim to address in future versions of the Framework include: | mid-unit |
| GDM-FSF-v2-0-0127 | bullet 1 | Greater precision in risk modeling: While we have updated our CCLs and underlying threat models from version 1.0, there  | mid-unit |

## Check 5 — Suspicious units

Under five words, or over 75.

Nothing flagged.

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

Single chunk; no seam.

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **2**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 138 |
| Tables detected | 2 |
| Units in tables | 28 |
| `context_stem` = NONE | 87 |
| `stated_bar` populated | 16 |
| `duplicate_of` populated | 6 |
| Median excerpt words | 23 |

| unit_type | n |
|---|---|
| paragraph | 73 |
| table_cell | 28 |
| bullet | 19 |
| footnote | 10 |
| numbered | 8 |
