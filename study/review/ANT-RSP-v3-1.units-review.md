# Stage 4 unit review — ANT-RSP-v3-1

Anthropic · Responsible Scaling Policy · Version 3.1 · 2026-04-02 · 20 pages

**301 units.** Frozen at `study/corpus/anthropic/units/ANT-RSP-v3-1.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| Table 1 | 48 | 23 | ANT-RSP-v3-1-0058 |
| Table Appendix | 9 | 6 | ANT-RSP-v3-1-0240 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| ANT-RSP-v3-1-0003 | N/A | We have always intended for our RSP to be a living document. | 12 words |
| ANT-RSP-v3-1-0005 | N/A | The major components of this third iteration are as follows: | 10 words |
| ANT-RSP-v3-1-0017 | N/A | But we cannot commit to following them unilaterally. | 8 words |
| ANT-RSP-v3-1-0018 | N/A | Frontier Safety Roadmaps are a new requirement under our RSP. | 10 words |
| ANT-RSP-v3-1-0028 | N/A | Our RSP is only one part of our overall approach to safety. | 12 words |
| ANT-RSP-v3-1-0037 | 1 | We lay this out in a three-column table. | 8 words |
| ANT-RSP-v3-1-0038 | 1 | The left column identifies capability thresholds that would call for heightened mitigations. | 12 words |
| ANT-RSP-v3-1-0040 | 1 | The right column describes our recommendations for industry-wide safety at each threshold. | 12 words |
| ANT-RSP-v3-1-0043 | 1 | However, these recommendations will drive important aspects of our work: | 10 words |
| ANT-RSP-v3-1-0055 | 1 | We hope these recommendations will become increasingly specific over time. | 10 words |
| ANT-RSP-v3-1-0111 | 2 | Maintaining and reporting on this Roadmap is part of our work under the RSP. | 14 words |
| ANT-RSP-v3-1-0114 | 2 | Our Frontier Safety Roadmap is subject to change. | 8 words |
| ANT-RSP-v3-1-0119 | 2 | Our current Frontier Safety Roadmap is available at anthropic.com/responsible-scaling-policy/roadmap. | 9 words |
| ANT-RSP-v3-1-0120 | 2 | We will also keep past Roadmaps available at that link. | 10 words |
| ANT-RSP-v3-1-0126 | 3.1 | Models fitting the above description are abbreviated below as "in-scope models." | 11 words |
| ANT-RSP-v3-1-0128 | 3.1 | We will publish a Risk Report every 3-6 months. | 9 words |
| ANT-RSP-v3-1-0133 | 3.2 | Several principles guide how we approach Risk Reports: | 8 words |
| ANT-RSP-v3-1-0139 | 3.3 | We will describe how we identify, evaluate, and mitigate catastrophic risks. | 11 words |
| ANT-RSP-v3-1-0140 | 3.3 | A Risk Report will document the following: | 7 words |
| ANT-RSP-v3-1-0152 | 3.3 | Review of past Risk Reports and decisions. We will address: | 10 words; opens on 'review' |
| ANT-RSP-v3-1-0162 | 3.3 | We will conduct the assessments above with respect to each in-scope model. | 12 words |
| ANT-RSP-v3-1-0165 | 3.4 / item 2 | Review and feedback: We will solicit comprehensive internal feedback on the report, focusing on identifying potential me | opens on 'review' |
| ANT-RSP-v3-1-0173 | 3.5 | We will publish a public version of our Risk Report. | 10 words |
| ANT-RSP-v3-1-0174 | 3.5 | We will aim to minimize redactions to the public version of the report. | 13 words |
| ANT-RSP-v3-1-0175 | 3.5 | Reasons we may redact material include but are not limited to: | 11 words |
| ANT-RSP-v3-1-0190 | 3.6.1 | In consultation with the Board and LTBT, we will select external reviewers that: | 13 words |
| ANT-RSP-v3-1-0202 | 3.6.3 | The external review will address: | 5 words |
| ANT-RSP-v3-1-0208 | 3.6.3 | In particular, the review will cover: | 6 words |
| ANT-RSP-v3-1-0217 | 4 / intro | We commit to the following governance measures to promote internal and external accountability. | 13 words |
| ANT-RSP-v3-1-0221 | 4.2 | Internal transparency: We will share final, unredacted Risk Reports with Anthropic's regular-clearance staff. | 13 words |
| ANT-RSP-v3-1-0250 | App B / para 1 | (For example, our initial Risk Report uses this distinction.) | 9 words |
| ANT-RSP-v3-1-0281 | Changelog / RSP v2.0 / New Capability and Safeguards Reports | New Capability and Safeguards Reports: We have introduced Capability Reports and Safeguard Reports. | 13 words |

## Check 3 — `stated_bar` audit

22 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| ANT-RSP-v3-1-0035 | fn1 | Where laws such as California SB 53 define this or similar terms with specific thresholds, we address those requirements | NONE |
| ANT-RSP-v3-1-0089 | Table 1 / Automated R&D in key domains / Capability or usage threshold | This capability threshold is intended to reflect our definition of highly capable models (see Section 3.6). | NONE |
| ANT-RSP-v3-1-0101 | Table 1 / Automated R&D in key domains / Mitigations—ambitious industry-wide recommendations | This will likely require similar measures to those listed in row 1, but to a higher standard‚ to the point where even we | NONE |
| ANT-RSP-v3-1-0132 | fn5 | Specifically, risks arising from the capability thresholds in our recommendations for industry-wide safety (see Section  | NONE |
| ANT-RSP-v3-1-0148 | 3.3 / risk analyses / item 1 | We will also discuss whether we believe we've crossed relevant thresholds in our recommendations for industry-wide safet | NONE |
| ANT-RSP-v3-1-0219 | 4.1 / duties list | (1) as needed, proposing updates to this policy; (2) approving relevant model development or deployment decisions based  | NONE |
| ANT-RSP-v3-1-0220 | 4.1 / duties list | (4) overseeing the implementation of this policy, including the allocation of sufficient resources; (5) receiving and ad | NONE |
| ANT-RSP-v3-1-0226 | 4.3 | If we determine that a report is (1) substantiated and (2) involves a material safety risk, we will promptly notify the  | NONE |
| ANT-RSP-v3-1-0241 | Table Appendix A / Anthropic in the lead / Commitment | We will require a strong argument that catastrophic risk is contained, along the lines of our recommendations for indust | NONE |
| ANT-RSP-v3-1-0243 | Table Appendix A / Competitors have strong safety measures / Scenario | We have strong evidence that all competitors who have developed, or will soon develop, a highly capable frontier model a | NONE |
| ANT-RSP-v3-1-0246 | Table Appendix A / General upleveling / Scenario | We have strong evidence that a competitor has implemented a risk mitigation that: (1) represents a significant improveme | NONE |
| ANT-RSP-v3-1-0247 | Table Appendix A / General upleveling / Scenario | (2) we could implement at comparable (or lower) effort or cost to our competitor. | NONE |
| ANT-RSP-v3-1-0252 | Changelog / RSP v1.0 | RSP-2023 (aka RSP v1.0): Initial version. | NONE |
| ANT-RSP-v3-1-0253 | Changelog / RSP v2.0 | RSP-2024: This update introduces a more flexible and nuanced approach to assessing and managing AI risks while maintaini | NONE |
| ANT-RSP-v3-1-0261 | Changelog / RSP v2.0 / ARA threshold now a checkpoint | We now believe that these capabilities - at the levels we initially considered - would not necessitate the ASL-3 standar | NONE |
| ANT-RSP-v3-1-0272 | Changelog / RSP v2.0 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | NONE |
| ANT-RSP-v3-1-0275 | Changelog / RSP v2.0 / Clarified ASL-3 and ASL-2 security threat models | Clarified ASL-3 and ASL-2 security threat models: We have clarified which actors are in and out of scope for the ASL-3 S | NONE |
| ANT-RSP-v3-1-0276 | Changelog / RSP v2.0 / Clarified ASL-3 and ASL-2 security threat models | We also removed the commitment to protect against scaled attacks and distillation attacks from the ASL-2 Security standa | NONE |
| ANT-RSP-v3-1-0277 | Changelog / RSP v2.0 / Clarified ASL-3 and ASL-2 security threat models | While distillation remains a concern for more capable models, models stored under ASL-2 safeguards have not yet reached  | NONE |
| ANT-RSP-v3-1-0278 | Changelog / RSP v2.0 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | NONE |
| ANT-RSP-v3-1-0285 | Changelog / RSP v2.1 | RSP-2025: This update clarifies which Capability Thresholds would require enhanced safeguards beyond our current ASL-3 s | NONE |
| ANT-RSP-v3-1-0290 | Changelog / RSP v2.1 / Iterative Commitment | We have decided not to maintain a commitment to define ASL-N+1 evaluations by the time we develop ASL-N models; such an  | NONE |
| ANT-RSP-v3-1-0292 | Changelog / RSP v2.2 | ASL-3 Security: This update excludes both sophisticated insiders and state-compromised insiders from the ASL-3 Security  | NONE |
| ANT-RSP-v3-1-0294 | Changelog / RSP v2.2 | The model capabilities and threat models corresponding with the ASL-3 Security Standard do not warrant protection agains | NONE |
| ANT-RSP-v3-1-0297 | Changelog / RSP v3.1 | This revision addresses the following points: (1) how we operationalize the Automated R&D capability threshold; (2) how  | NONE |
| ANT-RSP-v3-1-0299 | Changelog / RSP v3.1 | Change (1) reflects further discussion of our operationalization of the capability threshold, and involves some substant | NONE |
| ANT-RSP-v3-1-0301 | fn1 | This and other italicized instances of "highly capable" use the term as defined in Section 3.6. | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| ANT-RSP-v3-1-0002 | N/A | It establishes how we identify and evaluate risks, how we make decisions about AI development and deployment, and, from  | mid-unit |
| ANT-RSP-v3-1-0007 | N/A | We lay this out in a table that maps capability thresholds to the mitigations we believe they call for. | mid-unit |
| ANT-RSP-v3-1-0015 | N/A | We now separate our plans as a company—those which we expect to achieve regardless of what any other company does—from o | mid-unit |
| ANT-RSP-v3-1-0024 | N/A | These reports will reflect our reasoning as to whether we believe the risks of training or deploying our models are just | mid-unit |
| ANT-RSP-v3-1-0054 | 1 | We expect that the recommendations for industry-wide safety will evolve significantly, as we learn more about AI capabil | initial |
| ANT-RSP-v3-1-0061 | Table 1 / Non-novel chemical/biological weapons production / Mitigations—our plan as a company | We expect to continuously meet the criteria in the right column, although we cannot make guarantees about an evolving la | initial |
| ANT-RSP-v3-1-0076 | Table 1 / High-stakes sabotage opportunities / Mitigations—our plan as a company | We expect to continually be able to meet the criteria in the right column, although we cannot make guarantees about an e | initial |
| ANT-RSP-v3-1-0148 | 3.3 / risk analyses / item 1 | We will also discuss whether we believe we've crossed relevant thresholds in our recommendations for industry-wide safet | mid-unit |
| ANT-RSP-v3-1-0150 | 3.3 / risk analyses / item 3 | Risk-benefit determination: We will explain whether, and if so why, we believe the identified risks are justified by cor | mid-unit |
| ANT-RSP-v3-1-0156 | 3.3 / review / item 3 | Changes to our Frontier Safety Roadmap and any cases where we failed to meet our goals. | mid-unit |
| ANT-RSP-v3-1-0201 | 3.6.2 | We expect that we will also invest some time in answering follow-up questions from parties doing external review. | initial |
| ANT-RSP-v3-1-0272 | Changelog / RSP v2.0 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | mid-unit |
| ANT-RSP-v3-1-0278 | Changelog / RSP v2.0 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | mid-unit |
| ANT-RSP-v3-1-0282 | Changelog / RSP v2.0 / New Capability and Safeguards Reports | We expect that aggregating all the available evidence about model capabilities will provide decision makers with a more  | initial |
| ANT-RSP-v3-1-0291 | Changelog / RSP v2.1 / Iterative Commitment | We believe it is more practical and sensible instead to commit to reconsidering the whole list of Capability Thresholds  | initial |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| ANT-RSP-v3-1-0088 | Table 1 / Automated R&D in key domains / Capability or usage threshold | We would consider scenario (2) to have occurred where (a) we observe or expect double the rate of progress in AI aggrega | 85 |
| ANT-RSP-v3-1-0286 | Changelog / RSP v2.1 | The key changes include: | 4 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| ANT-RSP-v3-1.01.jsonl → ANT-RSP-v3-1.02.jsonl | ANT-RSP-v3-1-0121 | 3. Risk Reports | none detected |
| ANT-RSP-v3-1.02.jsonl → ANT-RSP-v3-1.03.jsonl | ANT-RSP-v3-1-0217 | 4. Governance | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **2**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 301 |
| Tables detected | 2 |
| Units in tables | 57 |
| `context_stem` = NONE | 144 |
| `stated_bar` populated | 22 |
| `duplicate_of` populated | 3 |
| Median excerpt words | 24 |

| unit_type | n |
|---|---|
| paragraph | 116 |
| callout | 49 |
| table_cell | 46 |
| numbered | 45 |
| bullet | 31 |
| footnote | 14 |
