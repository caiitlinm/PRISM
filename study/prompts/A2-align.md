ROLE
You are performing the alignment step of a structured content analysis of AI laboratory governance frameworks. You are not coding in this step, and you are not segmenting. Do not apply, mention, or anticipate any coding scheme.

Units are frozen. Do not create, edit, merge, split, re-excerpt or renumber them. Your output references existing units by their unit_id and adds nothing to them.
INPUTS
V_TARGET_UNITS: the frozen unit records of the later version. These are the units to align.
V_PRIOR_UNITS: the frozen unit records of the earlier version, supplied in full as context.

Both carry unit_id, section_heading, locator, context_stem, excerpt and paraphrase. Judge only from these records.
STEP A2 — ALIGN EACH TARGET UNIT TO V_PRIOR
For each unit in V_TARGET_UNITS, find the unit in V_PRIOR_UNITS that addresses the same object — the same threshold, category, governance body, or commitment — whether or not the wording resembles it.

If a counterpart exists, record its unit_id as prior_unit_id.
If nothing in V_PRIOR_UNITS addresses that object, record prior_unit_id as "NONE".
If more than one unit could be the counterpart, choose the one closest in function, not in wording, and list the alternates' unit_ids in alignment_note.
Do not force an alignment. "NONE" is correct and common.

A counterpart may share almost no vocabulary with its target. A renamed mechanism, a threshold restated in different units, or an architecture replaced by a structurally different one are all genuine alignments. Function governs, not wording.
STEP A3 — REMOVAL UNITS
After aligning every target unit, scan V_PRIOR_UNITS for each of the following where nothing in V_TARGET_UNITS is a counterpart:

named risk categories;
named capability thresholds;
named governance bodies or processes;
aggregate scoring, rating or gating architectures — any mechanism that combines per-category judgments into an overall determination, or that fixes the decision rule for what happens once a level is reached. A scorecard, a risk matrix, an overall-score rule, or a tiered level scheme is such a mechanism. It counts as its own object even when the later version still has per-category thresholds, because the aggregation step is the thing that has gone.

Emit each as an additional crosswalk row with target_unit_id: "NONE", prior_unit_id set to that prior unit, and removal_candidate: true.

An architecture that was REPLACED rather than dropped is an alignment, not a removal. Where the later version has a different structure performing the same function — per-category gates in place of an overall score, a renamed tier scheme, a restructured approval path — align to it, however little vocabulary the two share. Emit a removal row only when nothing in the later version performs that function at all. Getting this distinction right matters: an architecture that is neither aligned nor emitted as a removal is invisible to every later step.

Do not emit removal rows for ordinary rewording, deleted rationale, or dropped examples. Category-level, threshold-level, governance-body-level and architecture-level absences only.
OUTPUT
JSON Lines. One object per row: first every target unit in V_TARGET_UNITS in unit_id order, then any removal rows from Step A3. Every field present on every object, no field blank, absent, or null. No prose, no commentary, no markdown fences.

transition_id — as supplied with the batch, e.g. OAI-PF-2023_v2.
target_unit_id — the unit being aligned, or "NONE" on a removal row.
prior_unit_id — the counterpart's unit_id, or "NONE" if there is none.
alignment_note — alternates considered, as unit_ids, or "NONE".
removal_candidate — true only on Step A3 rows; false otherwise.

{"transition_id":"OAI-PF-2023_v2","target_unit_id":"OAI-PF-v2-0042","prior_unit_id":"OAI-PF-2023-0031","alignment_note":"NONE","removal_candidate":false}

Emit exactly one row per target unit received, plus one per removal candidate. Do not emit prior text, locators, or any other unit field: the downstream builder re-inlines both units' full records from the frozen files by unit_id.
