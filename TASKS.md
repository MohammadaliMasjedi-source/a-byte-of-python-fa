# TASKS.md — Mo-ByteOfPython-FA

Live backlog. This is the task list for contributors. Claiming a task = opening a **draft PR** titled
`T-BOP-xx: <title>`. One task per PR. Status: `OPEN` → `CLAIMED` (draft PR link) → `DONE` (merge).

The book so far: chapters 0–9 translated as DRAFTS in `translation/` (see `TODO.md`'s honest
status). Chapters translate IN ORDER — don't skip ahead. Source text: *A Byte of Python* by
Swaroop C H, CC BY-SA 4.0 (this translation carries the same license; attribution stays intact
in every file).

**The quality gate (applies to every translation card):** your PR stays a DRAFT until a
translation review approves it — natural Persian for self-taught Iranian programmers, NOT stiff
machine-فارسی. Read the glossary in `TRANSLATORS-NOTE.md` and `translation/06-control-flow.md` first and
match their register, terminology, and formatting exactly. Every chapter keeps the header label
«پیش‌نویس — نیازمندِ بازخوانیِ نهاییِ مترجم». Code blocks, commands, and identifiers stay in English.
In the PR body, list any term you were unsure about — that honesty speeds the review.

---

### T-BOP-01 · Translate chapter 9: Data Structures [phase: translate · size: M · status: DONE]
**Done:** `translation/09-data-structures.md` exists and its `TODO.md` line is ticked. Kept for reference.

### T-BOP-02 · Translate chapter 10: Problem Solving [phase: translate · size: M · status: CLAIMED]
**Draft PR:** [#2](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/pull/2)
— AI-assisted chapter draft and source-parity checks prepared on 20 November 2026.
Human Persian/teaching review and merge remain open; this task is not DONE.
**Context:** read `translation/06-control-flow.md` and `translation/07-functions.md`, the glossary in
`TRANSLATORS-NOTE.md`, `TODO.md`, and the original `problem_solving` chapter (the backup-script worked
example) of *A Byte of Python* (python.swaroopch.com). Chapters go in order; chapter 9 is done.
**Do:** create `translation/10-problem-solving.md` in the structure of chapters 06 to 09 (same heading
style, draft label, code-block conventions, attribution footer) and tick the `problem_solving` line in `TODO.md`.
**DoD:** all sections of the original chapter are present; every code example and output is identical to
the original; draft label and CC BY-SA attribution present. PR body: your unsure-terms list.
**Don't:** touch earlier chapters or the licence files. Don't merge yourself.

### T-BOP-03 · Add chapter 9 and later chapters to reading.html [phase: publish · size: S · status: OPEN]
**Context:** `reading.html` is generated from the Markdown chapters by `tools/build_reader.py`
(chapters 00 to 08 so far). `TODO.md` lists extending it to all chapters as an open item.
**Do:** add every chapter file in `translation/` that is missing (chapter 09 and later ones) to the
`CHAPTERS` list and to the table of contents of `reading.html`, then rebuild. Keep it fully offline
(no external requests, no CDN), same styling and RTL handling as the existing entries.
**DoD:** `python3 tools/build_reader.py --check` passes; open `reading.html` in a browser from a
plain file path: every translated chapter is reachable from the table of contents, Persian renders
RTL correctly, zero console errors, zero network requests (verify in devtools and say so in the PR body).
**Don't:** add frameworks or fonts fetched from the network.
