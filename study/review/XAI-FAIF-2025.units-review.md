# Stage 4 unit review — XAI-FAIF-2025

xAI · xAI Frontier Artificial Intelligence Framework · NONE · 2025-12-30 · 11 pages

**159 units.** Frozen at `study/corpus/xai/units/XAI-FAIF-2025.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

No units carry a table locator.

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| XAI-FAIF-2025-0029 | N/A | This continues to be an accelerant for xAI's model risk identification and mitigation. | 13 words |
| XAI-FAIF-2025-0035 | N/A | In this FAIF, we particularly focus on requests that pose a Catastrophic Risk. | 13 words |
| XAI-FAIF-2025-0050 | 2 | Biological and Chemical Weapons: xAI approaches addressing risks using threat modeling. | 11 words |
| XAI-FAIF-2025-0052 | 2 | "build" consists of the protocols, reagents, and equipment necessary to create the threat; and "test" consists of measur | opens on 'build' |
| XAI-FAIF-2025-0076 | 2 | We plan to add additional thresholds tied to other benchmarks. | 10 words |
| XAI-FAIF-2025-0088 | N/A | xAI aims to accurately measure these propensities and reduce them through careful engineering. | 13 words |
| XAI-FAIF-2025-0102 | 2 | We plan to add additional thresholds tied to other benchmarks. | 10 words |
| XAI-FAIF-2025-0107 | 1 | xAI aims to keep the public informed about our risk management policies. | 12 words |
| XAI-FAIF-2025-0122 | 4 | Risk owners are also responsible for periodic audits to enforce framework implementation. | 12 words |
| XAI-FAIF-2025-0138 | 5 | We will also balance various factors when making deployment decisions. | 10 words |
| XAI-FAIF-2025-0140 | 5 | Pre-deployment reviews include assessing benchmark results (e.g., WMDP scores) and mitigation effectiveness. | 12 words |
| XAI-FAIF-2025-0141 | 5 | For internal use, we review catastrophic risks like oversight evasion before extensive rollout. | 13 words |
| XAI-FAIF-2025-0145 | N/A | This data disclosure is issued pursuant to California's AB-2013. | 9 words |
| XAI-FAIF-2025-0156 | N/A | Datasets were collected at various times since xAI was founded in March 2023. | 13 words |
| XAI-FAIF-2025-0157 | N/A | Data collection is ongoing. | 4 words |

## Check 3 — `stated_bar` audit

10 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| XAI-FAIF-2025-0004 | N/A | This FAIF complies with California's Transparency in Frontier Artificial Intelligence Act (the "TFAIA", California Busin | NONE |
| XAI-FAIF-2025-0019 | N/A | xAI references standards such as NIST's AI Risk Management Framework, ISO/IEC 42001 for AI management systems, and indus | NONE |
| XAI-FAIF-2025-0053 | 2 | By "learning" from these results and iterating after the test phase, the design can be revised until the threat is relea | NONE |
| XAI-FAIF-2025-0145 | N/A | This data disclosure is issued pursuant to California's AB-2013. | NONE |
| XAI-FAIF-2025-0146 | N/A | Grok is pretrained with a data recipe that includes publicly available Internet data, data produced by third parties for | NONE |
| XAI-FAIF-2025-0149 | N/A | Grok is pretrained with a data recipe that includes publicly available Internet data, data produced by third parties for | NONE |
| XAI-FAIF-2025-0156 | N/A | Datasets were collected at various times since xAI was founded in March 2023. | NONE |
| XAI-FAIF-2025-0158 | N/A | Grok 1 began training on or about August 2023; Grok 1.5 began training on or about August 2023; Grok 2 began training on | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| XAI-FAIF-2025-0031 | N/A | Without any safeguards, we recognize that advanced AI models could lower the barrier to entry for bad actors seeking to  | mid-unit |
| XAI-FAIF-2025-0106 | N/A | We believe that public transparency, third-party review, and information security are important methods that can be util | initial |
| XAI-FAIF-2025-0128 | 4 / item 1 | If we determine it is warranted, we may notify and cooperate with relevant law enforcement agencies, including any agenc | mid-unit |
| XAI-FAIF-2025-0142 | 5 | However, to ensure responsible deployment, this FAIF will be continually adapted and updated as circumstances change, be | mid-unit |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| XAI-FAIF-2025-0057 | 2 / bullet 2 / sub 1 | Restricted biological supplies | 3 |
| XAI-FAIF-2025-0124 | 4 / bullet 1 | Red-teaming and internal testing; | 4 |
| XAI-FAIF-2025-0157 | N/A | Data collection is ongoing. | 4 |
| XAI-FAIF-2025-0158 | N/A | Grok 1 began training on or about August 2023; Grok 1.5 began training on or about August 2023; Grok 2 began training on | 76 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| XAI-FAIF-2025.01.jsonl → XAI-FAIF-2025.02.jsonl | XAI-FAIF-2025-0134 | 5. Deployment Decisions | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **0**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 159 |
| Tables detected | 0 |
| Units in tables | 0 |
| `context_stem` = NONE | 117 |
| `stated_bar` populated | 10 |
| `duplicate_of` populated | 3 |
| Median excerpt words | 22 |

| unit_type | n |
|---|---|
| paragraph | 116 |
| bullet | 28 |
| numbered | 11 |
| footnote | 4 |
