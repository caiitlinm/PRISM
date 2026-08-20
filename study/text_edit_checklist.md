Checkpoint 2. Stages 2–4 complete. extraction-report.md is the deliverable to review.

Built: study/corpus/ with 4 lab directories × 5 subdirs, 19 PDFs copied (SHA-256 verified identical to originals), 19 text files, 19-line manifest.jsonl. Source folder still holds all 20 PDFs, unmodified.

Three things need hand transcription before coding:

XAI-RMF-2025-02 pages 3–5 — both tables genuinely scrambled. The DRAFT watermark's letters extract as fragments that land inside cells. The WMDP-Cyber reference score is detached from its row and displaced below a stray T; on page 5 a watermark D has fused into the Model Alignment (MASK) cell and the threshold <X% lying on MASK sits against the wrong row. This is the only true cell-level corruption in the corpus, and it reads plausibly — a coder would attribute the wrong threshold to the wrong benchmark with nothing looking wrong.

OAI-PF-2023 page 15 — the Illustrative Scorecard. Header row split, and the word "Illustrative" is a background watermark whose letters (e, i v, t, ra, st) land between rows. This one carries disproportionate weight: your runbook §2.4 names the 2023 Scorecard as the alignment counterpart for the 2025 per-category thresholds, so C03's architecture_replaced depends on it.

OAI-PF-2023 page 6 — a 3102×3435 raster image with no text-layer contribution. The page extracts one paragraph plus footer. I can't tell what the image depicts without viewing it; if it's content, it's silently absent.

Two findings worth flagging beyond the defects:

Three of four xAI documents contain no tables at all — thresholds are stated in prose. That's a real structural difference from the other labs, not an extraction failure, so don't read a low table-derived unit count for xAI as missing data.

Five files carry invisible Unicode (U+202D/U+202C in ANT-RSP-v2-2 and XAI-RMF-2025-02; U+200B running to ~2,500 instances in ANT-RSP-v3-1/3-3/3-4). Invisible in any editor, but they'll break the verbatim-evidence check in your validator (§2.7). The same encoding produces ~29 visible intra-word splits (b ecome, w ww.anthropic.com). I haven't touched any of it — Stage 5 as specified doesn't mention normalisation. This is a decision I need for Stage 5: I'd strip the control characters (pure invisible noise, nothing can be lost) but leave the intra-word splits alone, since repairing those mechanically means editing words.

The remaining 16 documents need no table repair. OAI-PF-v2 Table 1 is sound but has its row-label column offset onto each row's second line — the exact context_stem hazard your runbook §2.2 item 2 describes, so worth care at A1 rather than repair now.

Full ranked hand-inspection list is §5 of the report; per-document verdicts in §7.