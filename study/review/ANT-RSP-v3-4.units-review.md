# Stage 4 unit review — ANT-RSP-v3-4

Anthropic · Responsible Scaling Policy · Version 3.4 · 2026-07-08 · 21 pages

**334 units.** Frozen at `study/corpus/anthropic/units/ANT-RSP-v3-4.units.jsonl`.

Units freeze at Checkpoint C and cannot be corrected afterwards. Every section below lists units to read, not verdicts.

## Check 1 — Table coverage

Units per table. **Count these against the cell count in the PDF.** A shortfall is the most common failure and the hardest to see, because the unit list looks complete on its own.

| Table | Units | Distinct row/col locators | First unit |
|---|---|---|---|
| (unnumbered) Capability/Mitigations Table | 38 | 36 | ANT-RSP-v3-4-0059 |
| Table Appendix | 9 | 6 | ANT-RSP-v3-4-0258 |

## Check 2 — `context_stem` = NONE on units that look dependent

Downstream coders see only the unit record. A short unit, or one opening on a bare verb, usually depends on a parent stem that must be carried here.

| unit_id | locator | excerpt | why |
|---|---|---|---|
| ANT-RSP-v3-4-0003 | Introduction / para 1 | We have always intended for our RSP to be a living document. | 12 words |
| ANT-RSP-v3-4-0005 | Introduction / major components | The major components of this third iteration are as follows: | 10 words |
| ANT-RSP-v3-4-0017 | Introduction / para on separation | But we cannot commit to following them unilaterally. | 8 words |
| ANT-RSP-v3-4-0018 | Introduction / Frontier Safety Roadmaps | Frontier Safety Roadmaps are a new requirement under our RSP. | 10 words |
| ANT-RSP-v3-4-0022 | Introduction / Risk Reports | Risk Reports are another new requirement. | 6 words |
| ANT-RSP-v3-4-0029 | Introduction / scope para | Our RSP is only one part of our overall approach to safety. | 12 words |
| ANT-RSP-v3-4-0038 | 1 / para 1 | We lay this out in a three-column table. | 8 words |
| ANT-RSP-v3-4-0039 | 1 / para 1 | The left column identifies capability thresholds that would call for heightened mitigations. | 12 words |
| ANT-RSP-v3-4-0041 | 1 / para 1 | The right column describes our recommendations for industry-wide safety at each threshold. | 12 words |
| ANT-RSP-v3-4-0044 | 1 / para 2 | However, these recommendations will drive important aspects of our work: | 10 words |
| ANT-RSP-v3-4-0056 | 1 / para 5 | We hope these recommendations will become increasingly specific over time. | 10 words |
| ANT-RSP-v3-4-0066 | fn3 | This column summarizes commitments drawn from other sections of this policy and associated artifacts. | 14 words |
| ANT-RSP-v3-4-0079 | fn7 | E.g., hundreds. | 2 words |
| ANT-RSP-v3-4-0122 | fn9 | Over at least three model generations. | 6 words |
| ANT-RSP-v3-4-0124 | 2 / para 1 | Maintaining and reporting on this Roadmap is part of our work under the RSP. | 14 words |
| ANT-RSP-v3-4-0127 | 2 / para 2 | Our Frontier Safety Roadmap is subject to change. | 8 words |
| ANT-RSP-v3-4-0132 | 2 / para 3 | Our current Frontier Safety Roadmap is available at anthropic.com/responsible-scaling-policy/roadmap. | 9 words |
| ANT-RSP-v3-4-0133 | 2 / para 3 | We will also keep past Roadmaps available at that link. | 10 words |
| ANT-RSP-v3-4-0139 | 3.1 | Models fitting the above description are abbreviated below as "in-scope models." | 11 words |
| ANT-RSP-v3-4-0141 | 3.1 | We will publish a Risk Report every 3-6 months. | 9 words |
| ANT-RSP-v3-4-0147 | 3.2 | Several principles guide how we approach Risk Reports: | 8 words |
| ANT-RSP-v3-4-0165 | 3.3 | Review of past Risk Reports and decisions. We will address: | 10 words; opens on 'review' |
| ANT-RSP-v3-4-0175 | 3.3 | We will conduct the assessments above with respect to each in-scope model. | 12 words |
| ANT-RSP-v3-4-0178 | 3.4 / item 2 | Review and feedback: We will solicit comprehensive internal feedback on the report, focusing on identifying potential me | opens on 'review' |
| ANT-RSP-v3-4-0185 | 3.5 | We will publish a public version of our Risk Report. | 10 words |
| ANT-RSP-v3-4-0187 | 3.5 | Reasons we may redact material include but are not limited to: | 11 words |
| ANT-RSP-v3-4-0204 | 3.6.1 | We will select external reviewers that: | 6 words |
| ANT-RSP-v3-4-0220 | 3.6.3 | The external review will address: | 5 words |
| ANT-RSP-v3-4-0226 | 3.6.3 | In particular, the review will cover: | 6 words |
| ANT-RSP-v3-4-0233 | 4 / intro | We commit to the following governance measures to promote internal and external accountability. | 13 words |
| ANT-RSP-v3-4-0239 | 4.3 | We will share minimally-redacted Risk Reports with all of Anthropic's regular-clearance staff. | 12 words |
| ANT-RSP-v3-4-0271 | Changelog / Sept 19, 2023 | September 19, 2023 (RSP v1.0) RSP-2023 (aka RSP v1.0): Initial version. | 11 words |
| ANT-RSP-v3-4-0274 | Changelog / Oct 15, 2024 | We describe the most notable changes below. | 7 words |
| ANT-RSP-v3-4-0299 | Changelog / Oct 15, 2024 / Clarified requirements for deployments with trusted users | For any general access systems, we still require passing intensive red-teaming. | 11 words |
| ANT-RSP-v3-4-0301 | Changelog / Oct 15, 2024 / New Capability and Safeguards Reports | New Capability and Safeguards Reports: We have introduced Capability Reports and Safeguard Reports. | 13 words |
| ANT-RSP-v3-4-0313 | Changelog / May 14, 2025 | Previously, only "highly sophisticated state-compromised insiders" were explicitly excluded. | 9 words |
| ANT-RSP-v3-4-0321 | Changelog / April 2, 2026 | This update also includes minor edits for style or clarity. | 10 words |
| ANT-RSP-v3-4-0324 | Changelog / July 8, 2026 | This update makes five changes: | 5 words |
| ANT-RSP-v3-4-0334 | Changelog / July 8, 2026 | It also contains minor typo and formatting corrections. | 8 words |

## Check 3 — `stated_bar` audit

36 units carry a bar. Listed below are units whose excerpt contains a number, percentage, multiplier or tier name but returned NONE.

| unit_id | locator | excerpt | stated_bar |
|---|---|---|---|
| ANT-RSP-v3-4-0036 | fn1 | Where laws such as California SB 53 define this or similar terms with specific thresholds, we address those requirements | NONE |
| ANT-RSP-v3-4-0098 | Table / Automated R&D / Capability threshold-g | This capability threshold is intended to reflect our definition of highly capable models (see Section 3.6). | NONE |
| ANT-RSP-v3-4-0110 | Table / Automated R&D / Mitigations-industry-wide / para after bullet1-a | This will likely require similar measures to those listed in row 1, but to a higher standard‚ to the point where even we | NONE |
| ANT-RSP-v3-4-0137 | 3.1 | It will cover all publicly deployed models as of the coverage date, as well as any internally deployed models as of the  | NONE |
| ANT-RSP-v3-4-0144 | 3.1 / off-cycle updates / bullet 1 | When we publicly deploy a model that we determine is (1) significantly more capable than (2) all models for which we hav | NONE |
| ANT-RSP-v3-4-0161 | 3.3 / risk analyses / item 1 | We will also discuss whether we believe we've crossed relevant thresholds in our recommendations for industry-wide safet | NONE |
| ANT-RSP-v3-4-0199 | 3.6 / bullet 1 | A model is "highly capable" if we conclude that it crosses the threshold for automated AI R&D described in Section 1. | NONE |
| ANT-RSP-v3-4-0235 | 4.1 | (1) as needed, proposing updates to this policy; (2) approving relevant model development or deployment decisions based  | NONE |
| ANT-RSP-v3-4-0236 | 4.1 | (4) overseeing the implementation of this policy, including the allocation of sufficient resources; (5) receiving and ad | NONE |
| ANT-RSP-v3-4-0244 | 4.4 | If we determine that a report is (1) substantiated and (2) involves a material safety risk, we will promptly notify the  | NONE |
| ANT-RSP-v3-4-0259 | Table Appendix A / Anthropic in the lead / Commitment | We will require a strong argument that catastrophic risk is contained, along the lines of our recommendations for indust | NONE |
| ANT-RSP-v3-4-0264 | Table Appendix A / General upleveling / Scenario | We have strong evidence that a competitor has implemented a risk mitigation that: (1) represents a significant improveme | NONE |
| ANT-RSP-v3-4-0265 | Table Appendix A / General upleveling / Scenario | (2) we could implement at comparable (or lower) effort or cost to our competitor. | NONE |
| ANT-RSP-v3-4-0268 | fn13 | This and other italicized instances of "highly capable" use the term as defined in Section 3.6. | NONE |
| ANT-RSP-v3-4-0271 | Changelog / Sept 19, 2023 | September 19, 2023 (RSP v1.0) RSP-2023 (aka RSP v1.0): Initial version. | NONE |
| ANT-RSP-v3-4-0272 | Changelog / Oct 15, 2024 | RSP-2024: This update introduces a more flexible and nuanced approach to assessing and managing AI risks while maintaini | NONE |
| ANT-RSP-v3-4-0280 | Changelog / Oct 15, 2024 / ARA threshold now a checkpoint | We now believe that these capabilities - at the levels we initially considered - would not necessitate the ASL-3 standar | NONE |
| ANT-RSP-v3-4-0292 | Changelog / Oct 15, 2024 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | NONE |
| ANT-RSP-v3-4-0295 | Changelog / Oct 15, 2024 / Clarified ASL-3 and ASL-2 security threat models | Clarified ASL-3 and ASL-2 security threat models: We have clarified which actors are in and out of scope for the ASL-3 S | NONE |
| ANT-RSP-v3-4-0296 | Changelog / Oct 15, 2024 / Clarified ASL-3 and ASL-2 security threat models | We also removed the commitment to protect against scaled attacks and distillation attacks from the ASL-2 Security standa | NONE |
| ANT-RSP-v3-4-0297 | Changelog / Oct 15, 2024 / Clarified ASL-3 and ASL-2 security threat models | While distillation remains a concern for more capable models, models stored under ASL-2 safeguards have not yet reached  | NONE |
| ANT-RSP-v3-4-0298 | Changelog / Oct 15, 2024 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | NONE |
| ANT-RSP-v3-4-0306 | Changelog / March 31, 2025 | RSP-2025: This update clarifies which Capability Thresholds would require enhanced safeguards beyond our current ASL-3 s | NONE |
| ANT-RSP-v3-4-0310 | Changelog / March 31, 2025 / Iterative Commitment | We have decided not to maintain a commitment to define ASL-N+1 evaluations by the time we develop ASL-N models; such an  | NONE |
| ANT-RSP-v3-4-0312 | Changelog / May 14, 2025 | ASL-3 Security: This update excludes both sophisticated insiders and state-compromised insiders from the ASL-3 Security  | NONE |
| ANT-RSP-v3-4-0314 | Changelog / May 14, 2025 | The model capabilities and threat models corresponding with the ASL-3 Security Standard do not warrant protection agains | NONE |
| ANT-RSP-v3-4-0315 | Changelog / May 14, 2025 | the CBRN-3 threat models entail large numbers of users having access to unguarded models (which is more likely to occur  | NONE |
| ANT-RSP-v3-4-0318 | Changelog / April 2, 2026 | This revision addresses the following points: (1) how we operationalize the Automated R&D capability threshold; (2) how  | NONE |
| ANT-RSP-v3-4-0320 | Changelog / April 2, 2026 | Change (1) reflects further discussion of our operationalization of the capability threshold, and involves some substant | NONE |
| ANT-RSP-v3-4-0323 | Changelog / May 26, 2026 | This update (1) revises our threshold for novel chemical/biological weapons production to better track the threat model  | NONE |

## Check 4 — Rationale and framing retention

The codebook codes explanatory and motivational language, so these must survive segmentation. Their **absence** is the finding: if this table is empty and the document argues for its own choices, the segmenter dropped them as preamble.

| unit_id | locator | excerpt | position |
|---|---|---|---|
| ANT-RSP-v3-4-0002 | Introduction / para 1 | It establishes how we identify and evaluate risks, how we make decisions about AI development and deployment, and, from  | mid-unit |
| ANT-RSP-v3-4-0007 | Introduction / component 1 | We lay this out in a table that maps capability thresholds to the mitigations we believe they call for. | mid-unit |
| ANT-RSP-v3-4-0015 | Introduction / para on separation | We now separate our plans as a company—those which we expect to achieve regardless of what any other company does—from o | mid-unit |
| ANT-RSP-v3-4-0025 | Introduction / Risk Reports | These reports will reflect our reasoning as to whether we believe the risks of training or deploying our models are just | mid-unit |
| ANT-RSP-v3-4-0055 | 1 / para 5 | We expect that the recommendations for industry-wide safety will evolve significantly, as we learn more about AI capabil | initial |
| ANT-RSP-v3-4-0062 | Table / Non-novel chem/bio / Mitigations-our plan | We expect to continuously meet the criteria in the right column, although we cannot make guarantees about an evolving la | initial |
| ANT-RSP-v3-4-0084 | Table / Misaligned AI systems / Mitigations-our plan-b | We expect to continually be able to meet the criteria in the right column, although we cannot make guarantees about an e | initial |
| ANT-RSP-v3-4-0161 | 3.3 / risk analyses / item 1 | We will also discuss whether we believe we've crossed relevant thresholds in our recommendations for industry-wide safet | mid-unit |
| ANT-RSP-v3-4-0163 | 3.3 / risk analyses / item 3 | Risk-benefit determination: We will explain whether, and if so why, we believe the identified risks are justified by cor | mid-unit |
| ANT-RSP-v3-4-0169 | 3.3 / review / item 3 | Changes to our Frontier Safety Roadmap and any cases where we failed to meet our goals. | mid-unit |
| ANT-RSP-v3-4-0217 | 3.6.2 | We expect that we will also invest some time in answering follow-up questions from parties doing external review. | initial |
| ANT-RSP-v3-4-0292 | Changelog / Oct 15, 2024 / More outcome-focused safeguard requirements | More outcome-focused safeguard requirements: We have updated our ASL-3 safeguards requirements to be less prescriptive a | mid-unit |
| ANT-RSP-v3-4-0298 | Changelog / Oct 15, 2024 / Clarified requirements for deployments with trusted users | Clarified requirements for deployments with trusted users: We have updated the ASL-3 Deployment Standard to allow for di | mid-unit |
| ANT-RSP-v3-4-0302 | Changelog / Oct 15, 2024 / New Capability and Safeguards Reports | We expect that aggregating all the available evidence about model capabilities will provide decision makers with a more  | initial |
| ANT-RSP-v3-4-0311 | Changelog / March 31, 2025 / Iterative Commitment | We believe it is more practical and sensible instead to commit to reconsidering the whole list of Capability Thresholds  | initial |
| ANT-RSP-v3-4-0331 | Changelog / July 8, 2026 / item 3 | We aim to hold our Risk Reports to a higher standard of thoroughness and coverage than our system cards while operating  | initial |

## Check 5 — Suspicious units

Under five words, or over 75.

| unit_id | locator | excerpt | words |
|---|---|---|---|
| ANT-RSP-v3-4-0079 | fn7 | E.g., hundreds. | 2 |
| ANT-RSP-v3-4-0100 | Table / Automated R&D / Mitigations-our plan / lead-in | We will: | 2 |

## Check 6 — Hand-transcribed tables

Transcribed pages in this document: none.

Marker syntax leaking into a unit field:

No `<<…>>` marker syntax in any unit field.

## Check 7 — Chunk seams

A model resuming mid-document sometimes re-emits the last unit of the prior chunk. Read the units either side of each seam.

| Between | First unit after seam | Section | Re-emitted |
|---|---|---|---|
| ANT-RSP-v3-4.01.jsonl → ANT-RSP-v3-4.02.jsonl | ANT-RSP-v3-4-0134 | 3. Risk Reports | none detected |
| ANT-RSP-v3-4.02.jsonl → ANT-RSP-v3-4.03.jsonl | ANT-RSP-v3-4-0233 | 4. Governance | none detected |

## Untagged tables

Only OAI-PF-2023 p15 and XAI-RMF-2025-02 pp3–5 were hand-transcribed. Every other table in the corpus reaches A1 as pdftotext column layout with no `<<TABLE>>` markers, so Check 1 is the only thing standing between a mangled multi-column table and units that look plausible one at a time.

Tables detected here: **2**. Transcribed pages: **none — all layout-derived**.

## Counts

| Measure | Value |
|---|---|
| Units | 334 |
| Tables detected | 2 |
| Units in tables | 47 |
| `context_stem` = NONE | 200 |
| `stated_bar` populated | 36 |
| `duplicate_of` populated | 1 |
| Median excerpt words | 24 |

| unit_type | n |
|---|---|
| paragraph | 165 |
| numbered | 66 |
| table_cell | 47 |
| bullet | 35 |
| footnote | 21 |
