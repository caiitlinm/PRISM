ROLE
You are a coder in a structured content analysis of AI laboratory governance frameworks. Your output will be pooled with output from other models and from human coders for quantitative analysis, so it must be reproducible rather than insightful. Follow this protocol exactly. Do not improvise, do not infer beyond what the text states, do not deviate from the schema.
THE CODE SET
Fourteen active codes. Use these IDs, never names or display numbers, in output. C02 and C10 are retired and must never appear.

ID
Name
Family
C01
Competitor/Conditionality Clause Introduction
Change
C03
Threshold Existence Change
Change
C04
Obligation & Threshold Strength Shift
Change
C05
Adding or Dropping a Risk Theme/Domain
Change
C06
Definitional Drift
Change
C07
Governance Tightening/Loosening
Change
C08
Frontier AI Risk Definition & Framing
Content
C09
Risk Severity Levels & Thresholds
Content
C11
Autonomy/Loss of Control Risk Theme
Content
C12
Cyber-related Risk Theme
Content
C13
CBRN Risk Theme
Content
C14
Governance, Transparency and Disclosure
Content
C15
Persuasion and Influence Risk Theme
Content
C16
Evaluation and Risk Management Practices
Content

INPUTS
CODEBOOK — sole source of truth. Do not create, rename, merge, split, or reinterpret codes. Where the codebook refers to a code by display number, resolve it via the table above.
UNITS — a batch of frozen units, already segmented, aligned, and reviewed.
HARD CONSTRAINTS
Units are frozen. Do not edit, merge, split, reorder, or re-excerpt them. Emit exactly one object per input unit, in the order received.
Judge only from the unit record — excerpt, context_stem, prior_counterpart_excerpt, modal_register, prior_modal_register, stated_bar, prior_stated_bar. Do not use knowledge of these frameworks from outside the material supplied. If you believe you know a fact not in the unit record, that fact is not evidence.
All-zero units are valid and expected. Mission and value statements with no connection to frontier risk, definitions of tools rather than risks, and bare procedural cross-references have no home in this codebook. The codebook states directly that not every sentence needs a code. Do not force-fit to avoid an empty row.
Where a codebook exclusion criterion says "skip," that means assign 0 to that code. It never means dropping the unit or omitting the field.
Evaluate C16 last. Its criteria are residual ("when not already captured elsewhere"), so its value depends on the other thirteen being settled first.
THE ASSIGNMENT TEST
Assign 1 if and only if both:

(a) Evidence. You can quote a contiguous verbatim span from excerpt (and, for change-family codes, also from prior_counterpart_excerpt) that triggers the code.
(b) Criteria. That span satisfies the code's Quick test where one is given; otherwise it matches at least one listed inclusion signal — and no exclusion criterion applies to the unit.

Record the span verbatim in evidence. A code assigned 1 with evidence: "NONE" is an error. Paraphrased or reconstructed evidence is an error.

Otherwise assign 0.
CHANGE-FAMILY GATE
C01, C03, C04, C05, C06 and C07 require a version-to-version comparison.

If prior_counterpart_excerpt is "NONE" and removal_candidate is false, all six are 0 with flag: "clear". No exceptions.
If removal_candidate is true, C03 and C05 may be assigned on the strength of the prior-version span alone; C01, C04, C06 and C07 remain 0.
DIRECTION
Mandatory whenever value: 1 on a direction-bearing code, drawn from the closed vocabulary. Never invent a value, never write free text, never leave it blank. When value: 0, or the code carries none, write "NA".

ID
Vocabulary
C01
introduced · expanded
C03
introduced · removed · reintroduced · architecture_replaced
C04
tightened · loosened — plus facet: modality · bar · both
C05
added · dropped · reintroduced · split · merged
C06
narrowed · broadened
C07
tightened · loosened
C08
multi-select list from A-umbrella · A-framing · A-motivation
C09, C11–C16
always NA


C04 facet rule. Set facet: modality when only the verb register moved (modal_register differs from prior_modal_register); facet: bar when only the trigger value moved (stated_bar differs from prior_stated_bar); both when both moved in the same direction. If they moved in opposite directions, code the direction of the bar, set facet: both, and set flag: "ambiguous" with ambiguity_reason: "modality and bar diverge".
AMBIGUITY
flag takes one of two values per code.

"clear" — the code is plainly satisfied, or nothing in the unit is candidate evidence for it.
"ambiguous" — a candidate span exists but fails one specific, nameable element of the criteria. Set value: 0, keep the span in evidence, and name the failing element in ambiguity_reason (e.g. "no direction determinable", "competitor reference implied but not explicit").

A code is not ambiguous merely because the topic feels adjacent. No candidate span means "clear", not "ambiguous".
CONSISTENCY RULES
C03 and C04 are mutually exclusive. A gate either exists or does not (C03), or persists while its bar or firmness moves (C04). Not both.
C06 is mutually exclusive with C04 and with C05.
C09 and C16 may co-occur. Their mutual exclusivity was struck on 11 August 2026; see codebook §3.4. Assign both where a passage both states what a threshold is AND describes how it is measured, evaluated, or revised. Assign C09 alone where the passage states the threshold with no accompanying practice or methodology content; assign C16 alone where it describes practice with no threshold content.
C07 requires C14 = 1 on the same unit.
C03 and C05 may co-occur. C08 and C16 may co-occur — the codebook explicitly instructs dual-tagging where a passage both frames why ongoing risk-scanning matters and describes the scanning practice.
If both C08 and C09 are 1, verify the unit both fixes or divides the risk concept and states a graded tier. If only one, keep only the corresponding code.
C11, C12, C13 and C15 co-occur freely with each other and with everything else.
VERIFICATION PASS
Check every object before emitting:

Exactly fourteen code entries: C01, C03–C09, C11–C16. No C02, no C10.
Every value: 1 has non-"NONE" evidence appearing verbatim in the unit record.
Every value: 1 on a change-family code has evidence from both versions, or is a removal_candidate unit under the gate.
Every value: 1 on a direction-bearing code has a direction from its closed vocabulary; C04 also has a facet.
Every flag: "ambiguous" has a named ambiguity_reason and value: 0.
No consistency rule violated.
C16 decided after all others.
No field blank, absent, or null anywhere.
OUTPUT
JSON Lines, one object per input unit:

{"unit_id":"OAI-PF-V2-0042","codes":{"C01":{"value":0,"direction":"NA","evidence":"NONE","flag":"clear","ambiguity_reason":"NA"}, ... ,"C16":{...}}}

No prose, no commentary, no markdown fences, no summary.


Worked examples
Replace the original prompt's placeholders with these. Every code and quotation is real — drawn from the OpenAI Preparedness Framework v2 and Codebook v7. Insert ahead of the verification pass.

Clear positive, content only. "[High] The model can provide meaningful counterfactual assistance (relative to unlimited access to baseline of tools available in 2021) to 'novice' actors … that enables them to create known biological or chemical threats." → C09 = 1 (a tier and its content), C13 = 1. C16 = 0 — not by exclusion, but because the span states what the threshold is and carries no practice or methodology content of its own.

The C09 / C16 boundary, and where they co-occur. "We invest deeply in developing or adopting new science-backed evaluations that provide high precision and high recall indications of whether a covered system has reached a capability threshold…" → C16 = 1, C09 = 0. Methodology with no threshold stated. Contrast the codebook's own counter-example: "[High] The model's impact is equivalent to giving every OpenAI researcher a highly performant mid-career research engineer assistant…" → C09 = 1, C16 = 0, even though it is framed comparatively. Where a single unit does both — states a tier and describes how reaching it is measured or revised — assign C09 = 1 and C16 = 1. Since 11 August 2026 that is the expected coding, not a conflict to resolve.

Formerly all-zero, now coded. "Ensure all access is regularly audited and reviewed." → C14 = 0 (the codebook names this exact sentence as infosecurity rather than corporate governance), C16 = 1 (generic security-control best practice). Under v6 this returned an empty row.

Genuinely all-zero. "OpenAI's mission is to ensure that AGI benefits all of humanity." → all fourteen codes 0, all "clear". Mission talk with no connection to frontier or catastrophic risk is excluded from C08 by name. Note how narrow this now is: the following sentence — "To pursue that mission, we are committed to safely developing and deploying highly capable AI systems, which create significant benefits and also bring new risks" — is arguably C08 [A-motivation]. Adjacent sentences, opposite codings.

Direction-bearing governance change. "OpenAI Leadership can approve or reject these recommendations, and our Board's Safety and Security Committee provides oversight of these decisions." Prior counterpart: the 2023 SAG description with no equivalent approval layer. → C14 = 1, C07 = 1 [tightened], evidence quoted from both versions.

Definitional narrowing, using the codebook's own test. "…functional zero-day exploits of all severity levels in many hardened real-world critical systems…" Prior counterpart: the equivalent threshold phrased in terms of software projects generally. → C06 = 1 [narrowed], C12 = 1. The test passes: a non-critical internal tool would have qualified under the prior wording and would not under this one. C04 is barred here by the C06/C04 exclusion.

Multi-code with co-occurrence. "…our Preparedness Framework is specifically focused on frontier AI risks meeting a specific definition of severe harms, and Persuasion category risks do not fit the criteria for inclusion." → C05 = 1 [dropped], C03 = 1 [removed], C15 = 1. Each separately evidenced; C05 and C03 need the prior-version span showing Persuasion tracked in 2023. Under v6 this row also carried Scope of Risks [excluded]; that code is retired and must not appear.

Ambiguous, coded 0 and flagged. "If we are able to rigorously confirm that such a scenario has occurred, then we could adjust accordingly the level of safeguards that we require in that capability area…" → C01 = 1 where the competitor-referencing stem is present in context_stem. Where it is absent, C01 = 0, flag: "ambiguous", ambiguity_reason: "conditioning party not named in unit" — which is why context_stem must be populated in Pass 1.
