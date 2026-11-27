# Adding a puzzle

The bilingual app and its English and Persian companion pages build from `cards.json`. This is original supplementary material, separate from the translated chapters. Keep the first eight IDs intact: their Persian Markdown cards already have shared links.

1. Pick one small surprise. Include a short, deterministic Python snippet with visible output, two distinct choices, and a plain explanation in each language. Use the same input and output in both languages. Use a new permanent ID and a link to the relevant Python documentation.
2. Run your snippet in Python and compare its exact output with the choice at `answer` (0 or 1). Another learner should be able to explain why the other choice is plausible.
3. From the repo root run `python3 tools/build_pocket_lab.py`, then `python3 tools/build_pocket_lab.py --check` and `python3 -m doctest labs/README.md`. Commit the source and generated outputs together.
4. Download/open `labs/python-pocket-lab.html`, disconnect, switch languages mid-round, and check the explanation and final score. Previews of HTML source on github.com do not execute it; the two Markdown editions work directly on GitHub.

Bug reports are useful even without a code change: include the question ID, selected language, expected/observed output, and browser or Python version. Do not include personal details or browser storage dumps.


For an illustrated puzzle, add a relative `diagram` under `labs/diagrams/`, a bilingual text alternative (`alt`), a common wrong prediction (`misconception`), and a second executable snippet (`variant`) whose result is the other choice (`variant_answer`). The four illustrated puzzles in `cards.json` are worked examples. The SVG is embedded in the offline game; no image host is required. Original Persian feedback for the first eight cards lives in `classic.fa.md`.

Run `python3 -m unittest discover -s tests` to compare every snippet and alternate with its advertised output. Only run contributor code after reviewing it.
