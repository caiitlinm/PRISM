# A1 run 1 — failed validation, retained as primary record

Run 2026-08-14T19:10Z. 12/12 calls returned, 0 truncated, 0 429s, 513,312 output
tokens, 15.2 min at concurrency 8. Cost ~$5.35.

Validation: 4 pass, 8 fail. Two independent classes:

* **Class A, 7/12** — a prose preamble ("Looking at this document, I'll segment it
  …") ahead of the first record, on 4 of them followed by an opening ```json
  fence. Head-only in every file; no interior junk. strip_fence() removed the
  closing fence but could not reach the opening one, because it only strips a
  fence sitting on the first or last non-blank line.
* **Class B, 209/209 units of GDM-FSF-v3-0, both chunks** — unit_id emitted as
  GDM-FSF-v3-0001 rather than GDM-FSF-v3-0-0001. The identifier's trailing "-0"
  was consumed as the first digit of the four-digit sequence. Not repairable by
  stripping; an ambiguous unit_id corrupts the A2 crosswalk and the change pass.

Neither rate is transient noise, so the batches were not re-run unchanged. The
remedy was a prompt fix (A1-segment.md OUTPUT), a preamble stripper in
run_pass.py, and a full 12-batch re-run. Analyst approved 2026-08-14.

Not deleted: JSONL runs are the primary record. Superseded by study/raw/a1/.
