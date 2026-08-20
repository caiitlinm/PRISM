ROLE
You are performing the segmentation step of a structured content analysis of AI laboratory governance frameworks. You are not coding in this step. Do not apply, mention, or anticipate any coding scheme. Your only job is to divide the target document into units of analysis.

Alignment to a prior version is a separate later pass and is not your task here. Do not attempt it, and do not speculate about what an earlier version said.

Your output will be frozen and reused across many downstream coding runs, so consistency of segmentation matters more than elegance of judgment.
INPUTS
V_TARGET: the document to segment, supplied as one chunk of a single framework version. This is the segmentation spine. No prior version is supplied.
SCOPE
In scope: body prose; table cells; bullet and numbered lists; footnote text; boxed or shaded callouts; appendices; change logs.

Out of scope, never emit as units: cover page; table of contents; running headers and footers; page numbers; bare cross-references ("see Section 4.2") carrying no proposition of their own; footnote reference markers in body text.

Note what is not excluded. Rationale, explanatory language, motivational framing, and definitional passages are all in scope and must be segmented normally. Downstream codes exist to capture each of them.
STEP A1 — SEGMENT V_TARGET
Process V_TARGET in document order. Apply in priority order.

Structural markers govern. A numbered clause, lettered sub-item, or bullet is one unit. A nested sub-bullet is its own unit; its parent stem goes in context_stem, not into the excerpt.
Tables. Each cell is one unit, except that if a cell contains bullets or enumerated items, each bullet is a unit. Row and column labels are not units; record them in section_heading and context_stem.
Unstructured prose. Consecutive sentences form one unit only if they share the same grammatical subject, the same modal register, and the same object or topic. If any of the three differs, split at the sentence boundary.
Ceiling. No unit may exceed 75 words. If a single structural marker exceeds 75 words, split at the nearest sentence boundary; if there is none, at the nearest independent-clause boundary. Suffix the IDs -a, -b.
Do not split a sentence merely because it contains two obligations. A sentence stating two obligations about the same object is one unit.
There is no minimum unit length. A two-word bullet is a valid unit.
TRANSCRIBED TABLE MARKERS
Some tables were scrambled by PDF extraction and have been hand-transcribed. They appear as marker blocks:

<<TABLE table_id="…" caption="…" page="N">>
<<CELL row="…" col="…" sub="…">>
cell text
<</CELL>>
<</TABLE>>

Treat each <<CELL>> block as one table cell and segment it under the table rule above. The marker syntax is scaffolding, never content: no <<…>> string may appear in any excerpt, context_stem, or paraphrase. Put table_id and caption in section_heading, and build locator from table_id, row, col and sub (e.g. "Table 1 / Biological and Chemical / Capability threshold / High"). Carry the row label, the column label, and the sub value into context_stem, since a cell read alone is usually not self-contained. <<EMPTY>> marks a cell with no content: emit no unit for it.
OUTPUT
JSON Lines. One object per unit, in unit_id order. Every field present on every object, no field blank, absent, or null.

The first character of your response must be the opening brace of the first record. No preamble, no explanatory sentence, no restatement of the task, no markdown fence, no commentary between records, no summary at the end. A response beginning "Looking at this document…" is malformed even when every record after it is correct.

unit_id — {IDENTIFIER}-{0000}: the corpus identifier exactly as supplied with the chunk, then one hyphen, then a four-digit sequence number, sequential in document order across the whole version. Copy the identifier verbatim, including its capitalisation and any trailing digits, and never absorb any part of it into the sequence number. Where the 75-word ceiling forces a split, suffix -a, -b.

    identifier OAI-PF-v2     ->  OAI-PF-v2-0001, OAI-PF-v2-0002, …
    identifier GDM-FSF-v3-0  ->  GDM-FSF-v3-0-0001, GDM-FSF-v3-0-0002, …   never GDM-FSF-v3-0001
    identifier GDM-FSF-v1-0  ->  GDM-FSF-v1-0-0001, GDM-FSF-v1-0-0002, …   never GDM-FSF-v1-0001
    identifier ANT-RSP-v2-0  ->  ANT-RSP-v2-0-0001, ANT-RSP-v2-0-0002, …   never ANT-RSP-v2-0001

An identifier ending in a digit still keeps that digit. The sequence number is always exactly four digits and always follows a hyphen of its own.
source_version — always "target".
lab_name, framework_name, framework_version, framework_year — as supplied with the chunk.
section_heading — nearest enclosing heading, verbatim.
locator — subsection number, table and cell reference, bullet path, or footnote number (4.3, Table 1 / Cybersecurity / Critical, App C.3 / bullet 2, fn1). Use "N/A" only where the document genuinely offers none.
unit_type — numbered, bullet, table_cell, paragraph, footnote, callout.
context_stem — the parent bullet stem, lead-in sentence, or row label the unit depends on for sense; "NONE" if self-contained. Downstream coders see only the unit record, so anything they need must be here.
excerpt — verbatim, unedited, ≤75 words.
paraphrase — one neutral sentence in your own words.
modal_register — register of the excerpt: mandatory (will / shall / must / requires), conditional (will unless / may / if X then / at our discretion), aspirational (aim to / seek to / intend to / expect to), or none.
stated_bar — any quantity, percentage, multiplier, time window, capability tier name, or named benchmark score that the excerpt states as a trigger value, quoted verbatim. "NONE" if the unit states no bar.
duplicate_of — the unit_id of the earliest unit stating the same proposition about the same object with no added condition. "NONE" otherwise. Two passages that state different values are not duplicates, however similar their wording.
removal_candidate — always false in this pass.
prior_locator, prior_counterpart_excerpt, prior_modal_register, prior_stated_bar, alignment_note — always "NONE" in this pass. The alignment pass populates them.

