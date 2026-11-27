"""Build one portable HTML page. --check compares output without writing it."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
src = ROOT / 'labs/studio'
target = ROOT / 'labs/python-pocket-lab.html'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
cards = json.loads((src / 'cards.json').read_text(encoding='utf-8'))
ids = [card['id'] for card in cards]
assert len(ids) == len(set(ids)) and ids
for card in cards:
    assert len(card['options']) == len(set(card['options'])) == 2
    assert card['answer'] in (0, 1)
    assert all(len(card[k]) == 2 and all(card[k]) for k in ('title', 'topic', 'why'))
    assert card['ref'].startswith('https://docs.python.org/3/')
template = (src / 'template.html').read_text(encoding='utf-8')
assert template.count('__CARDS__') == 1
payload = json.dumps(cards, ensure_ascii=False, separators=(',', ':')).replace('<', r'\u003c')
result = template.replace('__CARDS__', payload)
if args.check:
    if not target.exists() or target.read_text(encoding='utf-8') != result:
        raise SystemExit('Stale portable page: run python3 tools/build_pocket_lab.py')
else:
    target.write_text(result, encoding='utf-8')

def reading_cards(selected, language):
    english = language == 1
    body = [
        '# Twelve Python predictions' if english else '# چهار حدس دیگر: ریتم، گیتار، تست و اندازه‌گیری',
        'Pick an output before you open the explanation. No installation needed.'
        if english else 'پیش از بازکردن پاسخ، یکی از دو خروجی را انتخاب کن.',
        '[فارسی](PLAY.md) · [English](PLAY.en.md) · [Download the offline game](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/raw/refs/heads/main/labs/python-pocket-lab.html)',
    ]
    for card in selected:
        body.extend([f'<a name="{card["id"]}"></a>', '## ' + card['title'][language],
                     '```python\n' + card['code'] + '\n```',
                     ' / '.join('`' + v + '`' for v in card['options']),
                     '<details>\n<summary>' + ('Reveal the answer' if english else 'دیدن پاسخ') + '</summary>\n\n'
                     + '`' + card['options'][card['answer']] + '` — ' + card['why'][language] + '\n\n</details>',
                     '[Python reference](' + card['ref'] + ')'])
    body.append('[Run a camera experiment](https://github.com/MohammadaliMasjedi-source/rpi-camera-af/blob/main/examples/focus_scores.py) · [Suggest a puzzle](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa/issues) · [Text license](../LICENSE) · [Code license](../LICENSE-CODE)')
    return '\n\n'.join(body) + '\n'

for filename, selected, language in [('PLAY.en.md', cards, 1), ('ENCORE.fa.md', cards[8:], 0)]:
    path = ROOT / 'labs' / filename
    document = reading_cards(selected, language)
    if args.check:
        if not path.exists() or path.read_text(encoding='utf-8') != document:
            raise SystemExit('Stale reading cards: ' + filename)
    else:
        path.write_text(document, encoding='utf-8')
