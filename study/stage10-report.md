# Stage 10 — front-matter removal

`.clean.txt` produced for all 19 documents from `.norm.txt`. **711 lines removed.**
`.norm.txt` and `.txt` are both untouched and remain alongside.

Removal used explicit per-document configuration, not a shared heuristic. The corpus
is not uniform: 7 of 19 documents have no separate cover page, one carries its table
of contents inline on a body page, and two encode the running footer on the same line
as footnote text. A single rule would have taken body text from several documents.

Hand-transcription spans are protected absolutely — no line between
`[TRANSCRIBED BY HAND …]` and `[END HAND TRANSCRIPTION]` was eligible for removal.
Cell counts confirm it: XAI-RMF-2025-02 20 cells before and after, OAI-PF-2023 13.

---

## 1. Summary

| Identifier | Stage 6 | Transcribed | Lines removed | norm → clean |
|---|---|---|---|---|
| ANT-RSP-v1-0 | transformed | — | 22 | 1032 → 1010 |
| ANT-RSP-v2-0 | copied | — | 47 | 1053 → 997 |
| ANT-RSP-v2-1 | transformed | — | 47 | 1069 → 1012 |
| ANT-RSP-v2-2 | transformed | — | 48 | 1086 → 1028 |
| ANT-RSP-v3-0 | transformed | — | 46 | 863 → 806 |
| ANT-RSP-v3-1 | transformed | — | 49 | 888 → 830 |
| ANT-RSP-v3-2 | transformed | — | 49 | 907 → 848 |
| ANT-RSP-v3-3 | transformed | — | 51 | 929 → 869 |
| ANT-RSP-v3-4 | transformed | — | 54 | 971 → 908 |
| GDM-FSF-v1-0 | copied | — | 15 | 343 → 328 |
| GDM-FSF-v2-0 | transformed | — | 51 | 468 → 408 |
| GDM-FSF-v3-0 | transformed | — | 54 | 740 → 672 |
| GDM-FSF-v3-1 | transformed | — | 75 | 961 → 873 |
| OAI-PF-2023 | transformed | p15 | 28 | 1621 → 1584 |
| OAI-PF-v2 | copied | — | 48 | 1049 → 990 |
| XAI-FAIF-2025 | transformed | — | **0** | 481 → 481 |
| XAI-FAIF-2026 | transformed | — | 10 | 411 → 401 |
| XAI-RMF-2025-02 | transformed | p3, p4, p5 | 8 | 515 → 507 |
| XAI-RMF-2025-08 | copied | — | 9 | 429 → 420 |

"copied" at Stage 6 = the file contained no invisible characters, so `.norm.txt` is
byte-identical to `.txt`.

## 2. What was removed, per document

| Identifier | Cover | TOC | Running header/footer | Bare page numbers |
|---|---|---|---|---|
| ANT-RSP-v1-0 | none — p1 is body | none in document | `Anthropic's Responsible Scaling Policy, Version 1.0  N` ×22 | in footer |
| ANT-RSP-v2-0 | p1 (4 lines) | p4 | `Responsible Scaling Policy, Anthropic  N` | in footer |
| ANT-RSP-v2-1 | p1 (5 lines) | p4 | same | in footer |
| ANT-RSP-v2-2 | p1 (5 lines) | p4 | same | in footer |
| ANT-RSP-v3-0 … v3-4 | p1 (5 lines) | p2 | same | in footer |
| GDM-FSF-v1-0 | none — p1 is body | **inline block on p1** (8 lines) | none | 7 bare |
| GDM-FSF-v2-0 | none — p1 is body | p2 | none | 8 bare |
| GDM-FSF-v3-0 | p1 (5 lines) | p3 | `Frontier Safety Framework` (header) + `Frontier Safety Framework \| N` (footer) | in footer |
| GDM-FSF-v3-1 | p1 (5 lines) | p3 | same | in footer |
| OAI-PF-2023 | p1 title block + date only — **see §3.1** | none in document | `Preparedness Framework (Beta)  N` | in footer |
| OAI-PF-v2 | p1 (2 lines) | p3 | none | 21 bare |
| XAI-FAIF-2025 | none — p1 is body | none | **none — see §3.3** | none |
| XAI-FAIF-2026 | none — p1 is body | none | `xAI Frontier Artificial Intelligence Framework` ×10 | none |
| XAI-RMF-2025-02 | none — p1 is body | none | none | 8 bare |
| XAI-RMF-2025-08 | none — p1 is body | none | none | 9 bare |

## 3. Flags

### 3.1 OAI-PF-2023 — cover-page rationale prose *(RESOLVED — restored)*

Two rules collided here: "remove the cover page" against "keep… any rationale or
explanatory prose. Some of these carry codes in the downstream scheme, so removing
them would cause silent data loss."

The cover page reads, in full:

```
Preparedness                                                    <- removed
Framework                                                       <- removed
(Beta)                                                          <- removed
We believe the scientific study of catastrophic risks from AI has        <- KEPT
fallen far short of where we need to be.                                 <- KEPT
To help address this gap, we are introducing our Preparedness            <- KEPT
Framework, a living document describing OpenAI’s processes to            <- KEPT
track, evaluate, forecast, and protect against catastrophic risks        <- KEPT
posed by increasingly powerful models.                                   <- KEPT
December 18, 2023                                               <- removed
```

**Resolved by analyst decision, 2026-08-13: the six prose lines are restored.** They
are a motivational statement of why the framework exists — prime C08
`[A-motivation]` material, the code the runbook warns is easiest to lose — and appear
nowhere else in the document. Only the title block and the date are removed.

The restored text forms page 1 of `.clean.txt`, with the page break preserved, so the
page structure and any page-based locator still line up with `.norm.txt`. The
paragraph break between the two sentences is retained.

This is implemented as a `COVER_KEEP` line range in the Stage 10 config rather than a
hand edit, so the file remains reproducible from `.norm.txt`.

No other document needs this: the Anthropic, GDM and OAI-PF-v2 covers are title,
version, date and a URL only.

### 3.2 OAI-PF-2023 — two running footers share a line with footnote text

Two footers could not be removed as whole lines:

```
line  87: Development in this case refers to the spectrum of activities to enhance the technology.   Preparedness Framework (Beta)  2
line 675: of capability gains could outstrip our ability to anticipate and react to them.            Preparedness Framework (Beta)  9
```

In both, footnote text and the running footer were extracted onto one line. Removing
the line would delete footnote text; removing only the trailing fragment would mean
editing a line of content mid-string. **I did neither** — both lines are retained
whole, so two footer strings survive in this file. Flagging rather than trimming.
There are also truncated footer variants in this document (`ramework (Beta)  9`),
which the extraction report already noted; the matched ones were removed.

### 3.3 XAI-FAIF-2025 — nothing removed at all

The only document where Stage 10 removed zero lines. Verified rather than assumed:
it has no cover page, no table of contents, no running header, no running footer and
no page numbers. Its page 1 opens with the document title, which appears **once** and
is therefore the title of the body text, not furniture — the other 11 pages open with
ordinary prose. Retained deliberately.

### 3.4 Seven documents have no separate cover page

`ANT-RSP-v1-0`, `GDM-FSF-v1-0`, `GDM-FSF-v2-0`, `XAI-FAIF-2025`, `XAI-FAIF-2026`,
`XAI-RMF-2025-02`, `XAI-RMF-2025-08` all open with title, version and/or date
followed immediately by body text on the same page. Removing page 1 would have
deleted body prose, so nothing was removed for them under "cover page".

**Consequence for the corpus:** the title/version/date block is absent from the 12
documents that had a real cover page and present at the top of these 7. If a
downstream coder treats that block as codeable text, the two groups are not
comparable. Worth a decision before A1, though it does not block anything.

### 3.5 Bare numbers retained are footnote markers, not page numbers

`.clean.txt` still contains bare-number lines — 23 in ANT-RSP-v2-0, 16 in
GDM-FSF-v3-0, 11 in XAI-FAIF-2025 and so on. These are **footnote markers**, each
immediately followed by its footnote text, and removing them would sever the marker
from the note. A page number was removed only where the line was the first or last
non-blank line of its page *and* its value equalled the page index; across all 19
documents that test produced 53 removals and **zero mismatches**, so the two classes
separate cleanly.

## 4. Verified after cleaning

- Anthropic v3.4 `Changelog` section: present. `Appendix A`: present (3 references).
- ANT-RSP-v2-1 appendices: present (6 references).
- OAI-PF-2023 page 6 rationale prose ("Our rationale for grouping…"): present.
- GDM-FSF-v3-1 `Section 1: Framework` body heading: present once — the TOC entry went
  with the TOC page, the heading itself survived. The bare running header
  `Frontier Safety Framework` was confirmed never to appear away from a page edge in
  either v3.0 or v3.1 before it was used as a removal pattern.
- Hand-transcribed cells: 20 and 13, unchanged.
- No residual page numbers in any file.
