#!/usr/bin/env python3
"""
strip_invisibles.py — remove invisible Unicode from extracted text, verifiably.

    python strip_invisibles.py corpus/*/text/*.txt --check     # report only
    python strip_invisibles.py corpus/*/text/*.txt --apply     # write .norm.txt

Removes format-category (Cf) characters — zero-width spaces, bidi controls, BOM,
soft hyphens — and converts non-breaking spaces to ordinary ones. These are
invisible in any editor but will break the verbatim-evidence check: a model asked
to quote an excerpt will silently normalise them away, and the mismatch then looks
like fabrication.

Does NOT repair intra-word splits ('b ecome'). Those are reported for awareness
only — repairing them mechanically means editing words, and no rule distinguishes
them from legitimate spacing.

--apply asserts that the visible text is unchanged before writing. If that
assertion fails the file is left alone and reported, because it means something
other than an invisible character was about to be removed.
"""

import argparse, re, sys, unicodedata
from pathlib import Path
from collections import Counter

# Zs-category spaces that should become an ordinary space rather than vanish
SPACE_LIKE = {
    "\u00a0": " ",   # no-break space
    "\u2007": " ",   # figure space
    "\u202f": " ",   # narrow no-break space
    "\u2060": "",    # word joiner (Cf, listed here for clarity)
}

# Intra-word split: single letter, space, lowercase run — 'b ecome', 'w ww'
SPLIT_RE = re.compile(r"\b([A-Za-z])\s([a-z]{2,})\b")


def classify(text):
    """Counter of {codepoint label: count} for every character to be removed."""
    c = Counter()
    for ch in text:
        if ch in SPACE_LIKE:
            c[f"U+{ord(ch):04X} {unicodedata.name(ch, '?')} -> space"] += 1
        elif unicodedata.category(ch) == "Cf":
            c[f"U+{ord(ch):04X} {unicodedata.name(ch, '?')} -> removed"] += 1
    return c


def transform(text):
    out = []
    for ch in text:
        if ch in SPACE_LIKE:
            out.append(SPACE_LIKE[ch])
        elif unicodedata.category(ch) == "Cf":
            continue
        else:
            out.append(ch)
    return "".join(out)


def visible(text):
    """Everything a human can see, with all spacing collapsed away."""
    keep = [c for c in text if unicodedata.category(c) not in ("Cf", "Zs", "Cc")]
    return re.sub(r"\s+", "", "".join(keep))


def splits(text):
    """(line_no, matched_text) for suspected intra-word splits."""
    found = []
    for i, line in enumerate(text.splitlines(), 1):
        for m in SPLIT_RE.finditer(line):
            frag = m.group(0)
            # 'a lot', 'I think' are legitimate — 'a' and 'I' are real words
            if m.group(1) in ("a", "A", "I"):
                continue
            found.append((i, frag))
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--suffix", default=".norm.txt")
    a = ap.parse_args()

    if not (a.check or a.apply):
        raise SystemExit("pass --check or --apply")

    total_removed = 0
    failures = 0

    for f in a.files:
        p = Path(f)
        text = p.read_text(encoding="utf-8")
        counts = classify(text)
        n = sum(counts.values())
        sp = splits(text)

        if n == 0 and not sp:
            print(f"  clean   {p.name}")
            continue

        print(f"\n  {p.name}")
        for label, c in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"      {c:>6}  {label}")
        if sp:
            shown = sp[:8]
            print(f"      {len(sp):>6}  suspected intra-word splits (NOT repaired)")
            for line_no, frag in shown:
                print(f"              line {line_no}: {frag!r}")
            if len(sp) > len(shown):
                print(f"              … {len(sp) - len(shown)} more")

        total_removed += n

        if a.apply:
            new = transform(text)
            if visible(new) != visible(text):
                print("      ABORTED — visible text would change. File untouched.")
                failures += 1
                continue
            out = p.with_name(p.stem + a.suffix)
            out.write_text(new, encoding="utf-8")
            print(f"      wrote {out.name}  ({n} char(s) removed, visible text identical)")

    print(f"\n{total_removed} invisible character(s) across {len(a.files)} file(s).")
    if a.check:
        print("Dry run. Re-run with --apply to write .norm.txt files.")
    if failures:
        print(f"{failures} file(s) aborted — inspect before proceeding.")
        sys.exit(1)


if __name__ == "__main__":
    main()
