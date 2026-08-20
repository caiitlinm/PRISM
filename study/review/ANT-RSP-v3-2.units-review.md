# Stage 4 unit review — ANT-RSP-v3-2

Anthropic · Responsible Scaling Policy · Version 3.2 · 2026-04-29 · 20 pages

**313 units.** Frozen at `study/corpus/anthropic/units/ANT-RSP-v3-2.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| (unnumbered) Appendix A: Commitments Related to Competitors | 9 | 6 | ANT-RSP-v3-2-0252 |
| (unnumbered) Table: Capability/usage thresholds and mitigations | 29 | 12 | ANT-RSP-v3-2-0059 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| ANT-RSP-v3-2-0003 | N/A | We have always intended for our RSP to be a living document. | 12 words |
| ANT-RSP-v3-2-0005 | N/A | The major components of this third iteration are as follows: | 10 words |
| ANT-RSP-v3-2-0017 | N/A | But we cannot commit to following them unilaterally. | 8 words |
| ANT-RSP-v3-2-0018 | N/A | Frontier Safety Roadmaps are a new requirement under our RSP. | 10 words |
| ANT-RSP-v3-2-0022 | N/A | Risk Reports are another new requirement. | 6 words |
| ANT-RSP-v3-2-0029 | N/A | Our RSP is only one part of our overall approach to safety. | 12 words |
| ANT-RSP-v3-2-0038 | 1 | We lay this out in a three-column table. | 8 words |
| ANT-RSP-v3-2-0039 | 1 | The left column identifies capability thresholds that would call for heightened mitigations. | 12 words |
| ANT-RSP-v3-2-0041 | 1 | The right column describes our recommendations for industry-wide safety at each threshold. | 12 words |
| ANT-RSP-v3-2-0044 | 1 | However, these recommendations will drive important aspects of our work: | 10 words |
| ANT-RSP-v3-2-0058 | 1 | We hope these recommendations will become increasingly specific over time. | 10 words |
| ANT-RSP-v3-2-0115 | 2 | Maintaining and reporting on this Roadmap is part of our work under the RSP. | 14 words |
| ANT-RSP-v3-2-0118 | 2 | Our Frontier Safety Roadmap is subject to change. | 8 words |
| ANT-RSP-v3-2-0123 | 2 | Our current Frontier Safety Roadmap is available at anthropic.com/responsible-scaling-policy/roadmap. | 9 words |
| ANT-RSP-v3-2-0124 | 2 | We will also keep past Roadmaps available at that link. | 10 words |
| ANT-RSP-v3-2-0130 | 3.1 | Models fitting the above description are abbreviated below as "in-scope models." | 11 words |
| ANT-RSP-v3-2-0132 | 3.1 | Timing. We will publish a Risk Report every 3-6 months. | 10 words |
| ANT-RSP-v3-2-0137 | 3.2 | Several principles guide how we approach Risk Reports: | 8 words |
| ANT-RSP-v3-2-0143 | 3.3 | Factual information. We will describe how we identify, evaluate, and mitigate catastrophic risks. | 13 words |
| ANT-RSP-v3-2-0144 | 3.3 | A Risk Report will document the following: | 7 words |
| ANT-RSP-v3-2-0151 | 3.3 | Our analyses will include: | 4 words |
| ANT-RSP-v3-2-0157 | 3.3 | Review of past Risk Reports and decisions. We will address: | 10 words; opens on 'review' |
| ANT-RSP-v3-2-0167 | 3.3 | We will conduct the assessments above with respect to each in-scope model. | 12 words |
| ANT-RSP-v3-2-0170 | 3.4 / item 2 | Review and feedback: We will solicit comprehensive internal feedback on the report, focusing on identifying potential me | opens on 'review' |
| ANT-RSP-v3-2-0178 | 3.5 | We will publish a public version of our Risk Report. | 10 words |
| ANT-RSP-v3-2-0179 | 3.5 | We will aim to minimize redactions to the public version of the report. | 13 words |
| ANT-RSP-v3-2-0180 | 3.5 | Reasons we may redact material include but are not limited to: | 11 words |
| ANT-RSP-v3-2-0196 | 3.6.1 | We will select external reviewers that: | 6 words |
| ANT-RSP-v3-2-0209 | 3.6.3 | The external review will address: | 5 words |
| ANT-RSP-v3-2-0215 | 3.6.3 | In particular, the review will cover: | 6 words |
| ANT-RSP-v3-2-0224 | 4 / intro | We commit to the following governance measures to promote internal and external accountability. | 13 words |
| ANT-RSP-v3-2-0233 | 4.3 | Internal transparency: We will share final, unredacted Risk Reports with Anthropic's regular-clearance staff. | 13 words |
| ANT-RSP-v3-2-0262 | App B | (For example, our initial Risk Report uses this distinction.) | 9 words |
| ANT-RSP-v3-2-0265 | Changelog / September 19, 2023 (RSP v1.0) | RSP-2023 (aka RSP v1.0): Initial version. | 6 words |
| ANT-RSP-v3-2-0268 | Changelog / October 15, 2024 (RSP v2.0) | We describe the most notable changes below. | 7 words |
| ANT-RSP-v3-2-0294 | Changelog / v2.0 / New Capability and Safeguards Reports | New Capability and Safeguards Reports: We have introduced Capability Reports and Safeguard Reports. | 13 words |
| ANT-RSP-v3-2-0305 | Changelog / v2.2 | Previously, only "highly sophisticated state-compromised insiders" were explicitly excluded. | 9 words |
| ANT-RSP-v3-2-0312 | Changelog / v3.1 | This update also includes minor edits for style or clarity. | 10 words |

## Check 3 — `stated_bar` audit

32 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| ANT-RSP-v3-2-0036 | fn1 | Where laws such as California SB 53 define this or similar terms with specific thresholds, we address those requirements | NONE |
| ANT-RSP-v3-2-0090 | Table / Automated R&D in key domains / Capability or usage threshold | This capability threshold is intended to reflect our definition of highly capable models (see Section 3.6). | NONE |
| ANT-RSP-v3-2-0105 | Table / Automated R&D in key domains / Mitigations—ambitious industry-wide recommendations / bullet 1 | This will likely require similar measures to those listed in row 1, but to a higher standard‚ to the point where even we | NONE |
| ANT-RSP-v3-2-0128 | 3.1 | It will also cover internally deployed models when we determine that these models could pose significant risks5 beyond t | NONE |
| ANT-RSP-v3-2-0136 | fn5 | Specifically, risks arising from the capability thresholds in our recommendations for industry-wide safety (see Section  | NONE |
| ANT-RSP-v3-2-0153 | 3.3 / item 1 | We will also discuss whether we believe we've crossed relevant thresholds in our recommendations for industry-wide safet | NONE |
| ANT-RSP-v3-2-0162 | 3.3 | Marginal risk and ecosystem analysis. If we determine that the absolute level of risk being imposed industry-wide by AI  | NONE |
| ANT-RSP-v3-2-0207 | 3.6.2 | For purposes of external review, the only redactions to the Risk Report will be those necessary to comply with legal pro | NONE |
| ANT-RSP-v3-2-0238 | 4.4 | If we determine that a report is (1) substantiated and (2) involves a material safety risk, we will promptly notify the  | NONE |
| ANT-RSP-v3-2-0253 | Table / Anthropic in the lead / Commitment | We will require a strong argument that catastrophic risk is contained, along the lines of our recommendations for indust | NONE |
| ANT-RSP-v3-2-0255 | Table / Competitors have strong safety measures / Scenario | We have strong evidence that all competitors who have developed, or will soon develop, a highly capable frontier model a | NONE |
| ANT-RSP-v3-2-0258 | Table / General upleveling / Scenario | We have strong evidence that a competitor has implemented a risk mitigation that: (1) represents a significant improveme | NONE |
| ANT-RSP-v3-2-0259 | Table / General upleveling / Scenario | (2) we could implement at comparable (or lower) effort or cost to our competitor. | NONE |
| ANT-RSP-v3-2-0264 | fn8 | This and other italicized instances of "highly capable" use the term as defined in Section 3.6. | NONE |
| ANT-RSP-v3-2-0265 | Changelog / September 19, 2023 (RSP v1.0) | RSP-2023 (aka RSP v1.0): Initial version. | NONE |
| ANT-RSP-v3-2-0266 | Changelog / October 15, 2024 (RSP v2.0) | RSP-2024: This update introduces a more flexible and nuanced approach to assessing and managing AI risks while maintaini | NONE |
| ANT-RSP-v3-2-0309 | Changelog / April 2, 2026 (RSP v3.1) | This revision addresses the following points: (1) how we operationalize the Automated R&D capability threshold; (2) how  | NONE |
| ANT-RSP-v3-2-0311 | Changelog / v3.1 | Change (1) reflects further discussion of our operationalization of the capability threshold, and involves some substant | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| ANT-RSP-v3-2-0002 | N/A | It establishes how we identify and evaluate risks, how we make decisions about AI development and deployment, and, from  | mid-unit |
| ANT-RSP-v3-2-0007 | N/A | We lay this out in a table that maps capability thresholds to the mitigations we believe they call for. | mid-unit |
| ANT-RSP-v3-2-0015 | N/A | We now separate our plans as a company—those which we expect to achieve regardless of what any other company does—from o | mid-unit |
| ANT-RSP-v3-2-0025 | N/A | These reports will reflect our reasoning as to whether we believe the risks of training or deploying our models are just | mid-unit |
| ANT-RSP-v3-2-0057 | 1 | We expect that the recommendations for industry-wide safety will evolve significantly, as we learn more about AI capabil | initial |
| ANT-RSP-v3-2-0062 | Table / Non-novel chemical/biological weapons production / Mitigations—our plan as a company | We expect to continuously meet the criteria in the right column, although we cannot make guarantees about an evolving la | initial |
| ANT-RSP-v3-2-0077 | Table / High-stakes sabotage opportunities / Mitigations—our plan as a company | We expect to continually be able to meet the criteria in the right column, although we cannot make guarantees about an e | initial |
| ANT-RSP-v3-2-0153 | 3.3 / item 1 | We will also discuss whether we believe we've crossed relevant thresholds in our recommendations for industry-wide safet | mid-unit |
| ANT-RSP-v3-2-0155 | 3.3 / item 3 | Risk-benefit determination: We will explain whether, and if so why, we believe the identified risks are justified by cor | mid-unit |
| ANT-RSP-v3-2-0161 | 3.3 / item 3 | Changes to our Frontier Safety Roadmap and any cases where we failed to meet our goals. | mid-unit |
| ANT-RSP-v3-2-0208 | 3.6.2 | We expect that we will also invest some time in answering follow-up questions from parties doing external review. | initial |
| ANT-RSP-v3-2-0285 | Changelog / v2.0 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | mid-unit |
| ANT-RSP-v3-2-0291 | Changelog / v2.0 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | mid-unit |
| ANT-RSP-v3-2-0295 | Changelog / v2.0 / New Capability and Safeguards Reports | We expect that aggregating all the available evidence about model capabilities will provide decision makers with a more  | initial |
| ANT-RSP-v3-2-0303 | Changelog / v2.1 / Iterative Commitment | We believe it is more practical and sensible instead to commit to reconsidering the whole list of Capability Thresholds  | initial |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| ANT-RSP-v3-2-0089 | Table / Automated R&D in key domains / Capability or usage threshold | We would consider scenario (2) to have occurred where (a) we observe or expect double the rate of progress in AI aggrega | 85 |
| ANT-RSP-v3-2-0095 | Table / Automated R&D in key domains / Mitigations—our plan as a company | We will: | 2 |
| ANT-RSP-v3-2-0151 | 3.3 | Our analyses will include: | 4 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| ANT-RSP-v3-2.01.jsonl → ANT-RSP-v3-2.02.jsonl | ANT-RSP-v3-2-0125 | 3. Risk Reports | none detected |
| ANT-RSP-v3-2.02.jsonl → ANT-RSP-v3-2.03.jsonl | ANT-RSP-v3-2-0224 | 4. Governance | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **2**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 313 |
| Tables detected | 2 |
| Units in tables | 38 |
| `context_stem` = NONE | 164 |
| `stated_bar` populated | 32 |
| `duplicate_of` populated | 4 |
| Median excerpt words | 23 |

| unit_type | n |
|---|---|
| paragraph | 167 |
| numbered | 52 |
| bullet | 42 |
| table_cell | 38 |
| footnote | 14 |
