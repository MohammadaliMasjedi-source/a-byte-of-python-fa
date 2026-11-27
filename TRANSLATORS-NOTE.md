# Translator's note

Persian translation of *A Byte of Python* by Swaroop C H, draft. AI-assisted draft, human review pending.

## Upstream version followed

The translation follows the upstream repository https://github.com/swaroopch/byte-of-python at
commit `84f4dd8d` (HEAD on 2026-10-07, "docs: clarify Python 3 version guidance").
Basis for this statement: between 2026-07-22 and that commit, upstream changed only these
translated files, and each change is in the translation:
`about_python.md` (the "Python 3 versus 2" section), `basics.md` (the Coding Horror link),
`control_flow.md` (headings with backticks, `[enter]` instead of `kbd:[enter]`), `op_exp.md`
(`print` in backticks) and `programs/function_varargs.txt` (output order).
`preface.md` already points to the paper-book page in its current form.

## Checks done

- On 2026-11-10 automated checks compared the translation with upstream: the structure (sections,
  paragraphs, code blocks), all code and program output, inline code, and links. Code blocks and
  program outputs of chapters 02 to 09 are identical to upstream apart from the language tag of the
  fence (see below). The prose was sampled, not proofread by a human. Human review is pending.
- `reading.html` is generated from the Markdown chapters 00 to 09 by `tools/build_reader.py`.
  `python3 tools/build_reader.py --check` compares headings, paragraphs, list items and code blocks
  of every chapter, the code text, and the prose text with the Markdown, and checks that internal
  anchors resolve. It also checks that every translated draft is registered and reachable
  once from the table of contents, in chapter order.

## Adaptations

### Chapter 02 (`translation/02-installation.md`)

1. Dropped: the sentence "At the time of this writing, it was Python 3.5.1" (it is out of date).
2. Dropped: the PATH steps for Windows 2000, XP and 2003, for older Windows versions
   (`AUTOEXEC.BAT` and `AUTOEXEC.NT`) and for Windows Vista.
   Kept: the steps for Windows 7 and 8 and for Windows 10, and the note that pre-Vista Windows
   needs Python 3.4.
3. Version numbers in installer options and paths are written without a minor version, because
   upstream mixes 3.5 and 3.6 in them:
   - Upstream `Add Python 3.5 to PATH`, `Add Python 3.5 Path` and `Add Python 3.5 PATH` are written `Add Python 3 to PATH`.
   - Upstream `C:\python35`, `C:\Python35` and `C:\Python36` are written `C:\python3` and `C:\Python3`.
4. Kept: "equal to or greater than version 3.6.0", the "(or another appropriate location)" hint
   and the `%SystemRoot%\system32` example bullet (with `C:\Python3`).
5. In "Running Python prompt on Windows" the two upstream paragraphs (open a terminal with `cmd`;
   then type `python`) are one paragraph.

### Images

6. The screenshots of chapter 03 (eight PyCharm screenshots and the terminal screenshot) are replaced
   by placeholders of the form "[تصویر: ...]", with a translator's note at the top of the chapter.
   The PyCharm screenshot after the command line arguments note in chapter 04 is replaced the same way.

### Other

7. Code blocks stay in English and are not changed. The REPL blocks and the error block are fenced
   as `pycon` and `text` for syntax highlighting; the content is the same.
8. Chapter files are numbered `00` to `09` and named in English. Links between chapters point to
   these files; links to chapters that are not translated yet (object oriented programming,
   standard library) are plain text. The `{#id}` heading markers of the upstream build are not used;
   in-page links use the automatic heading anchors.
9. `translation/00-preface.md`: the first person of the original ("I") is written as "the author"
   in the paragraph about the official website and the paper book.
10. Dead upstream links, kept as they are in upstream: the Google jobs page (`01-about-python.md`)
   and the Docker on Windows page (`02-installation.md`).
11. Chapter 9 (data structures) is included in `reading.html` from
    `translation/09-data-structures.md`. The reader covers chapters 00 to 09, all still drafts.

## Glossary (one Persian term per concept)

| English | Persian |
|---|---|
| list | فهرست |
| tuple | چندتایی |
| file | فایل |
| underscore | زیرخط |
| index | اندیس |
| indexing | اندیس‌گذاری |
| subscription | زیرنویس‌گذاری |
| comment | توضیح |
| comma | ویرگول (semicolon: نقطه‌ویرگول) |
| set (Python `set`) | مجموعه |
| collection (general word) | گردایه |
| "Note for … programmers" | نکته‌ای برای برنامه‌نویسانِ … |

### Known inconsistencies

- "مجموعه" is also used for the plain English "set of" (for example "a set of statements" in
  `04-basics.md` and "a set of packages and modules" in `08-modules.md`), not only for Python's `set`.

## Status

- Chapters 00 to 09 are translated as a draft (the Dedication is not translated).
- Not translated yet: problem solving, object oriented programming, input and output, exceptions,
  standard library, more, what next.
