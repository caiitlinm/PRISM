# Stage 4 unit review — ANT-RSP-v3-0

Anthropic · Responsible Scaling Policy · Version 3.0 · 2026-02-24 · 19 pages

**278 units.** Frozen at `study/corpus/anthropic/units/ANT-RSP-v3-0.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| Table 1 | 46 | 23 | ANT-RSP-v3-0-0042 |
| Table Appendix | 9 | 6 | ANT-RSP-v3-0-0220 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| ANT-RSP-v3-0-0003 | Introduction / para 2 | The major components of this third iteration are as follows: | 10 words |
| ANT-RSP-v3-0-0028 | 1 / para 1 | The right column describes our recommendations for industry-wide safety at each threshold. | 12 words |
| ANT-RSP-v3-0-0102 | 3.1 | Models fitting the above description are abbreviated below as "in-scope models." | 11 words |
| ANT-RSP-v3-0-0104 | 3.1 | Timing. We will publish a Risk Report every 3-6 months. | 10 words |
| ANT-RSP-v3-0-0109 | 3.2 | Several principles guide how we approach Risk Reports: | 8 words |
| ANT-RSP-v3-0-0115 | 3.3 | Factual information. We will describe how we identify, evaluate, and mitigate catastrophic risks. | 13 words |
| ANT-RSP-v3-0-0116 | 3.3 | A Risk Report will document the following: | 7 words |
| ANT-RSP-v3-0-0123 | 3.3 | Our analyses will include: | 4 words |
| ANT-RSP-v3-0-0129 | 3.3 | Review of past Risk Reports and decisions. We will address: | 10 words; opens on 'review' |
| ANT-RSP-v3-0-0139 | 3.3 | We will conduct the assessments above with respect to each in-scope model. | 12 words |
| ANT-RSP-v3-0-0142 | 3.4 / item 2 | Review and feedback: Separate internal reviewers will provide comprehensive feedback on the report, focusing on identify | opens on 'review' |
| ANT-RSP-v3-0-0143 | 3.4 / item 2 | We will usually also seek feedback from trusted external parties with relevant expertise. | 13 words |
| ANT-RSP-v3-0-0149 | 3.5 | We will publish a public version of our Risk Report. | 10 words |
| ANT-RSP-v3-0-0150 | 3.5 | We will aim to minimize redactions to the public version of the report. | 13 words |
| ANT-RSP-v3-0-0151 | 3.5 | Reasons we may redact material include but are not limited to: | 11 words |
| ANT-RSP-v3-0-0168 | 3.6.1 | In consultation with the Board and LTBT, we will select external reviewers that: | 13 words |
| ANT-RSP-v3-0-0180 | 3.6.3 | The external review will address: | 5 words |
| ANT-RSP-v3-0-0186 | 3.6.3 | In particular, the review will cover: | 6 words |
| ANT-RSP-v3-0-0195 | 4 / intro | We commit to the following governance measures to promote internal and external accountability. | 13 words |
| ANT-RSP-v3-0-0203 | 4.2 | Internal transparency: We will share final, unredacted Risk Reports with Anthropic's regular-clearance staff. | 13 words |
| ANT-RSP-v3-0-0214 | 4.6 | This review will focus on procedural compliance, not substantive outcomes. | 10 words |
| ANT-RSP-v3-0-0217 | 4.7 | We will maintain the current version of the RSP on our website. | 12 words |
| ANT-RSP-v3-0-0230 | App B | (For example, our initial Risk Report uses this distinction.) | 9 words |
| ANT-RSP-v3-0-0260 | Changelog / RSP v2.0 / Clarified requirements for deployments with trusted users | For any general access systems, we still require passing intensive red-teaming. | 11 words |
| ANT-RSP-v3-0-0262 | Changelog / RSP v2.0 / New Capability and Safeguards Reports | New Capability and Safeguards Reports: We have introduced Capability Reports and Safeguard Reports. | 13 words |
| ANT-RSP-v3-0-0274 | Changelog / RSP v2.2 / ASL-3 Security | Previously, only "highly sophisticated state-compromised insiders" were explicitly excluded. | 9 words |

## Check 3 — `stated_bar` audit

30 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| ANT-RSP-v3-0-0025 | fn1 | Where laws such as California SB 53 define this or similar terms with specific thresholds, we address those requirements | NONE |
| ANT-RSP-v3-0-0072 | Table 1 / Automated R&D in key domains / Capability or usage threshold | This capability threshold is intended to reflect our definition of highly capable models (see Section 3.6). It may be se | NONE |
| ANT-RSP-v3-0-0081 | Table 1 / Automated R&D in key domains / Mitigations-ambitious industry-wide recommendations | This will likely require similar measures to those listed in row 1, but to a higher standard‚ to the point where even we | NONE |
| ANT-RSP-v3-0-0108 | fn4 | Specifically, risks arising from the capability thresholds in our recommendations for industry-wide safety (see Section  | NONE |
| ANT-RSP-v3-0-0125 | 3.3 / item 1 | We will also discuss whether we believe we've crossed relevant thresholds in our recommendations for industry-wide safet | NONE |
| ANT-RSP-v3-0-0164 | 3.6 / bullet 1-c | We hope to develop additional metrics for other domains over time. (The recommendations for industry-wide safety (see Se | NONE |
| ANT-RSP-v3-0-0202 | 4.1 / duty 6 | and (6) making judgment calls on policy interpretation and application. | NONE |
| ANT-RSP-v3-0-0208 | 4.3 | If we determine that a report is (1) substantiated and (2) involves a material safety risk, we will promptly notify the  | NONE |
| ANT-RSP-v3-0-0221 | Table Appendix A / Anthropic in the lead / Commitment | We will require a strong argument that catastrophic risk is contained, along the lines of our recommendations for indust | NONE |
| ANT-RSP-v3-0-0223 | Table Appendix A / Competitors have strong safety measures / Scenario | Competitors have strong safety measures. We have strong evidence that all competitors who have developed, or will soon d | NONE |
| ANT-RSP-v3-0-0226 | Table Appendix A / General upleveling / Scenario | General upleveling. We have strong evidence that a competitor has implemented a risk mitigation that: (1) represents a s | NONE |
| ANT-RSP-v3-0-0227 | Table Appendix A / General upleveling / Scenario | (2) we could implement at comparable (or lower) effort or cost to our competitor. | NONE |
| ANT-RSP-v3-0-0232 | fn7 | This and other italicized instances of "highly capable" use the term as defined in Section 3.6. | NONE |
| ANT-RSP-v3-0-0233 | Changelog / RSP v1.0 | RSP-2023 (aka RSP v1.0): Initial version. | NONE |
| ANT-RSP-v3-0-0234 | Changelog / RSP v2.0 / intro | RSP-2024: This update introduces a more flexible and nuanced approach to assessing and managing AI risks while maintaini | NONE |
| ANT-RSP-v3-0-0271 | Changelog / RSP v2.1 / Iterative Commitment | We have decided not to maintain a commitment to define ASL-N+1 evaluations by the time we develop ASL-N models; such an  | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| ANT-RSP-v3-0-0001 | Introduction / para 1 | Our Responsible Scaling Policy (RSP) is our voluntary framework for managing catastrophic risks from advanced AI systems | mid-unit |
| ANT-RSP-v3-0-0005 | Introduction / para 3 | We lay this out in a table that maps capability thresholds to the mitigations we believe they call for. We also include  | mid-unit |
| ANT-RSP-v3-0-0010 | Introduction / para 5 | We now separate our plans as a company—those which we expect to achieve regardless of what any other company does—from o | mid-unit |
| ANT-RSP-v3-0-0017 | Introduction / para 7 | These reports will reflect our reasoning as to whether we believe the risks of training or deploying our models are just | mid-unit |
| ANT-RSP-v3-0-0039 | 1 / para 5 | We expect that the recommendations for industry-wide safety will evolve significantly, as we learn more about AI capabil | initial |
| ANT-RSP-v3-0-0045 | Table 1 / Non-novel chem/bio weapons production / Mitigations-our plan as a company | We expect to continuously meet the criteria in the right column, although we cannot make guarantees about an evolving la | initial |
| ANT-RSP-v3-0-0060 | Table 1 / High-stakes sabotage opportunities / Mitigations-our plan as a company | We expect to continually be able to meet the criteria in the right column, although we cannot make guarantees about an e | initial |
| ANT-RSP-v3-0-0125 | 3.3 / item 1 | We will also discuss whether we believe we've crossed relevant thresholds in our recommendations for industry-wide safet | mid-unit |
| ANT-RSP-v3-0-0127 | 3.3 / item 3 | Risk-benefit determination: We will explain whether, and if so why, we believe the identified risks are justified by cor | mid-unit |
| ANT-RSP-v3-0-0133 | 3.3 / item 3 | Changes to our Frontier Safety Roadmap and any cases where we failed to meet our goals. | mid-unit |
| ANT-RSP-v3-0-0179 | 3.6.2 | We expect that we will also invest some time in answering follow-up questions from parties doing external review. | initial |
| ANT-RSP-v3-0-0253 | Changelog / RSP v2.0 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | mid-unit |
| ANT-RSP-v3-0-0259 | Changelog / RSP v2.0 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | mid-unit |
| ANT-RSP-v3-0-0263 | Changelog / RSP v2.0 / New Capability and Safeguards Reports | We expect that aggregating all the available evidence about model capabilities will provide decision makers with a more  | initial |
| ANT-RSP-v3-0-0272 | Changelog / RSP v2.1 / Iterative Commitment | We believe it is more practical and sensible instead to commit to reconsidering the whole list of Capability Thresholds  | initial |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| ANT-RSP-v3-0-0073 | Table 1 / Automated R&D in key domains / Mitigations-our plan as a company | We will: | 2 |
| ANT-RSP-v3-0-0123 | 3.3 | Our analyses will include: | 4 |
| ANT-RSP-v3-0-0267 | Changelog / RSP v2.1 / intro | The key changes include: | 4 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| ANT-RSP-v3-0.01.jsonl → ANT-RSP-v3-0.02.jsonl | ANT-RSP-v3-0-0097 | 3. Risk Reports | none detected |
| ANT-RSP-v3-0.02.jsonl → ANT-RSP-v3-0.03.jsonl | ANT-RSP-v3-0-0195 | 4. Governance | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **2**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 278 |
| Tables detected | 2 |
| Units in tables | 55 |
| `context_stem` = NONE | 163 |
| `stated_bar` populated | 30 |
| `duplicate_of` populated | 2 |
| Median excerpt words | 25 |

| unit_type | n |
|---|---|
| paragraph | 142 |
| numbered | 50 |
| table_cell | 44 |
| bullet | 32 |
| footnote | 10 |
