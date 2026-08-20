Part 0 — Decisions to make before you run anything

These four are cheap now and expensive later. Write each one down in a decisions.md alongside the corpus; you will need them for the methods section.

0.1 Freeze the codebook. --> ``[Codebook](<Codebook_Canonical_11_August_v8_final - with Quick Tests 12Aug2026.docx.pdf>)``
0.2 Decide what counts as a version. --> all published updates from METER database.

0.3 Decide your coder panel. This is the one that most often goes wrong.

Three repeats of one model at temperature 0 will produce near-identical output. The resulting agreement figure is not a measure of whether your codebook is clear — it is a measure of sampling noise, and it will look excellent regardless. A codebook entry that is ambiguous in the same direction every time yields α ≈ 1.0.

Use at least three different model families (e.g. Claude, GPT, Gemini), plus a human-coded subsample of 40–60 units per lab. Between-model agreement tells you whether the codebook is specific enough. Human-versus-ensemble agreement is the only thing that tells you whether the codebook is measuring what you think.

0.4 Decide your normalization now. Change-code counts scale with the number of transitions, not with how much changed — a lab with six frameworks mechanically out-scores a lab with two. Choose per transition, per unit, or per elapsed year before you look at any results.
--> per transition

0.5 Corpus scope (recorded 13 August 2026).

Decision 0.2 above reads "all published updates from METER database". That is
narrowed here, deliberately, and 0.2 should be read subject to this entry.

--> Four labs only: Anthropic, OpenAI, Google DeepMind, xAI. 19 documents,
    15 adjacent transitions. METR (https://metr.org/fsp) additionally lists
    Meta, Microsoft, Amazon, Nvidia, Magic, NAVER, G42 and Cohere; these are
    out of scope for this study and no documents from them are collected.

--> Anthropic's Frontier Compliance Framework (METR: Jun 2026) is out of scope.
    It is not treated as part of the RSP chain, and the Anthropic chain runs
    RSP v1.0 → v2.0 → v2.1 → v2.2 → v3.0 → v3.1 → v3.2 → v3.3 → v3.4 unbroken.

    Note for the methods section: this framework falls inside the window the
    RSP chain covers, under the same lab, and was excluded by scoping decision
    rather than because its relationship to the RSP was established. If a
    reviewer asks whether it supersedes or splits from the RSP, that question
    has not been investigated.

--> Cross-lab comparison (runbook Part 6) is therefore across four labs, not
    the full METR set.
