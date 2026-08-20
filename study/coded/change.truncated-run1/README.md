# B-change run 1 — 22 batches truncated at the 21,333-token ceiling

Run 2026-08-14 with --max-tokens 21333, non-streaming. 89/89 calls returned and
none failed, but 22 stopped on max_tokens, leaving 70 of 1,316 change rows uncoded.

Cause: change records carry the prior-version unit inline (prior_counterpart_excerpt,
prior_stated_bar, prior_modal_register), so both input and output run larger than the
content pass. At 15 rows per batch the output crossed the 21,333-token non-streaming
ceiling that the SDK enforces (3600 * max_tokens / 128000 > 600).

Re-run with --stream --max-tokens 64000. Batch size stays 15, the pinned value: only
the transport changed. The 67 batches that completed on end_turn were never
constrained by the ceiling, so their output is unaffected and they were not re-run.

Retained, not deleted: JSONL runs are the primary record.
