# Stage 4 unit review — XAI-FAIF-2026

xAI · xAI Frontier Artificial Intelligence Framework · NONE · 2026-06-30 · 9 pages

**123 units.** Frozen at `study/corpus/xai/units/XAI-FAIF-2026.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

No units carry a table locator.

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| XAI-FAIF-2026-0003 | 1 | Managing the risks related to advanced AI models presents unique challenges. | 11 words |
| XAI-FAIF-2026-0009 | 1 | Within our risk management framework, we may identify and assess other risks. | 12 words |
| XAI-FAIF-2026-0010 | 1 | Absent mitigation, high-risk scenarios become more likely as model capabilities increase. | 11 words |
| XAI-FAIF-2026-0016 | 1 | We evaluate these during annual reviews and integrate them into benchmarks and safeguards. | 13 words |
| XAI-FAIF-2026-0027 | 2 | Results of our systemic risk assessment and mitigation processes and measures will be documented. | 14 words |
| XAI-FAIF-2026-0031 | 2.1 | These risk domains describe principal pathways through which severe or systemic harm may arise. | 14 words |
| XAI-FAIF-2026-0059 | 2.1(c) | xAI treats AI-accelerated malicious cyber offense as a core risk domain. | 11 words |
| XAI-FAIF-2026-0078 | 2.3 | These results help determine whether the threshold has been reached. | 10 words |
| XAI-FAIF-2026-0102 | 2.4 | The Security Goal will be reviewed at least every year. | 10 words |
| XAI-FAIF-2026-0106 | fn3 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | 9 words |
| XAI-FAIF-2026-0108 | 2.4 | Access is tightly managed through least-privilege principles, role-based authorization, and regular reviews. | 12 words |

## Check 3 — `stated_bar` audit

4 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| XAI-FAIF-2026-0015 | 1 | xAI references standards such as NIST's AI Risk Management Framework and ISO/IEC 42001 for AI management systems. | NONE |
| XAI-FAIF-2026-0106 | fn3 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| XAI-FAIF-2026-0044 | 2.1(a) | Without any safeguards, we recognize that advanced AI models could lower the barrier to entry for malicious actors seeki | mid-unit |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| XAI-FAIF-2026-0111 | 3 / channel 1 | Red-teaming and internal testing; | 4 |
| XAI-FAIF-2026-0114 | 3 / channel 4 | Employee escalation; | 2 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

Single chunk; no seam.

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **0**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 123 |
| Tables detected | 0 |
| Units in tables | 0 |
| `context_stem` = NONE | 87 |
| `stated_bar` populated | 4 |
| `duplicate_of` populated | 3 |
| Median excerpt words | 23 |

| unit_type | n |
|---|---|
| paragraph | 90 |
| numbered | 18 |
| bullet | 12 |
| footnote | 3 |
