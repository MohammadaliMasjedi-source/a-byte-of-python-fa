"""Check the answers shown to learners against an isolated Python interpreter."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
CARDS = json.loads((ROOT / "labs/studio/cards.json").read_text(encoding="utf-8"))


class PocketLabAnswers(unittest.TestCase):
    def test_examples_and_alternates_print_the_advertised_result(self):
        for card in CARDS:
            cases = [("code", "answer")]
            if "variant" in card:
                cases.append(("variant", "variant_answer"))
            for snippet, answer in cases:
                with self.subTest(puzzle=card["id"], snippet=snippet):
                    result = subprocess.run(
                        [sys.executable, "-I", "-c", card[snippet]],
                        input="", capture_output=True, text=True, timeout=5, check=True,
                    )
                    self.assertEqual(result.stdout.splitlines(), [card["options"][card[answer]]])
