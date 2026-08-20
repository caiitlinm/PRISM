# Stage 4 unit review — GDM-FSF-v1-0

Google DeepMind · Frontier Safety Framework · Version 1.0 · 2024-05-17 · 7 pages

**116 units.** Frozen at `study/corpus/deepmind/units/GDM-FSF-v1-0.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| (unnumbered) CCL Table | 25 | 18 | GDM-FSF-v1-0-0073 |
| (unnumbered) Deployment Mitigations Table | 12 | 8 | GDM-FSF-v1-0-0056 |
| (unnumbered) Security Mitigations Table | 10 | 10 | GDM-FSF-v1-0-0042 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| GDM-FSF-v1-0-0016 | fn1 | See https://www.gov.uk/government/publications/emerging-processes-for-frontier-ai-safety, https://metr.org/blog/2023-09- | 5 words |
| GDM-FSF-v1-0-0017 | Framework intro | This section describes the central components of the Frontier Safety Framework. | 11 words |
| GDM-FSF-v1-0-0021 | 1 | The CCLs we have identified are described below. | 8 words |
| GDM-FSF-v1-0-0030 | 3 | A model may reach evaluation thresholds before mitigations at appropriate levels are ready. | 13 words |
| GDM-FSF-v1-0-0032 | 3 | Figure 1 depicts the relationship between these components of the Framework. | 11 words |
| GDM-FSF-v1-0-0037 | Figure 1 | Figure 1: the relationship between different components of the Framework. | 10 words |
| GDM-FSF-v1-0-0050 | fn5 | See https://www.rand.org/pubs/working_papers/WRA2849-1.html. | 2 words |
| GDM-FSF-v1-0-0099 | Future work para 2 | The Framework is exploratory and based on preliminary research. | 9 words |
| GDM-FSF-v1-0-0101 | Future work para 2 | Issues that we aim to address in future versions of the Framework include: | 13 words |
| GDM-FSF-v1-0-0116 | Acknowledgements para 2 | We would like to thank METR for contributing their expertise on Responsible Capability Scaling. | 14 words |

## Check 3 — `stated_bar` audit

20 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| GDM-FSF-v1-0-0016 | fn1 | See https://www.gov.uk/government/publications/emerging-processes-for-frontier-ai-safety, https://metr.org/blog/2023-09- | NONE |
| GDM-FSF-v1-0-0032 | 3 | Figure 1 depicts the relationship between these components of the Framework. | NONE |
| GDM-FSF-v1-0-0037 | Figure 1 | Figure 1: the relationship between different components of the Framework. | NONE |
| GDM-FSF-v1-0-0050 | fn5 | See https://www.rand.org/pubs/working_papers/WRA2849-1.html. | NONE |
| GDM-FSF-v1-0-0058 | Deployment Table / Level 1 / Level and capabilities | 1: Mitigations targeting the critical capability. Use of the full suite of mitigations to prevent the inappropriate acce | NONE |
| GDM-FSF-v1-0-0061 | Deployment Table / Level 2 / Level and capabilities | 2: Safety case with red team validation. Targeted safeguards, aimed at keeping numbers of incidents below a prespecified | NONE |
| GDM-FSF-v1-0-0063 | Deployment Table / Level 2 / Measures | Afterwards, similar mitigations as Level 1 are applied, but deployment takes place only after the robustness of safeguar | NONE |
| GDM-FSF-v1-0-0065 | Deployment Table / Level 3 / Level and capabilities | 3: Prevention of access. Mitigations that allow for high levels of confidence that capabilities cannot be accessed at al | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| GDM-FSF-v1-0-0007 | Intro para 3 | We aim to have this initial framework implemented by early 2025, which we anticipate should be well before these risks m | initial |
| GDM-FSF-v1-0-0009 | Intro para 3 | It will be reviewed periodically and we expect it to evolve substantially as our understanding of the risks and benefits | mid-unit |
| GDM-FSF-v1-0-0072 | CCL intro para 2 | As we conduct further research into these and other risk domains, we expect these CCLs to evolve and for several CCLs at | mid-unit |
| GDM-FSF-v1-0-0098 | Future work para 1 | We aim to have this initial framework implemented by early 2025, which we anticipate should be well before these risks m | initial |
| GDM-FSF-v1-0-0100 | Future work para 2 | We expect it to evolve substantially as our understanding of the risks and benefits of frontier models improves, and we  | initial |
| GDM-FSF-v1-0-0101 | Future work para 2 | Issues that we aim to address in future versions of the Framework include: | mid-unit |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| GDM-FSF-v1-0-0042 | Security Table / Level 0 / Level and capabilities | 0: Status quo | 3 |
| GDM-FSF-v1-0-0050 | fn5 | See https://www.rand.org/pubs/working_papers/WRA2849-1.html. | 2 |
| GDM-FSF-v1-0-0056 | Deployment Table / Level 0 / Level and capabilities | 0: Status quo | 3 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

Single chunk; no seam.

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **3**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 116 |
| Tables detected | 3 |
| Units in tables | 47 |
| `context_stem` = NONE | 53 |
| `stated_bar` populated | 20 |
| `duplicate_of` populated | 4 |
| Median excerpt words | 24 |

| unit_type | n |
|---|---|
| table_cell | 47 |
| paragraph | 46 |
| bullet | 16 |
| footnote | 7 |
