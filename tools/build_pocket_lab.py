"""Build and check the portable FA/EN game and visual reading editions (Python 3)."""
import argparse
import base64
import json
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
SRC = LABS / "studio"
REPO = "https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa"
THREAD = REPO + "/issues/6"
DOWNLOAD = REPO + "/raw/refs/heads/main/labs/python-pocket-lab.html"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--check", action="store_true")
CHECK = parser.parse_args().check
cards = json.loads((SRC / "cards.json").read_text(encoding="utf-8"))
ids = [c["id"] for c in cards]
assert ids and len(set(ids)) == len(ids)
visual = [c for c in cards if "diagram" in c]
encore = [c for c in cards if c["id"] in ("music", "pitch", "qa", "meter")]
classic = [c for c in cards if c not in visual]
def emit(name, body):
    file = LABS / name
    if CHECK:
        if not file.exists() or file.read_text(encoding="utf-8") != body:
            raise SystemExit("Rebuild: " + str(file))
    else:
        file.write_text(body, encoding="utf-8")
deck = []
for card in visual + classic:
    assert len(card["options"]) == len(set(card["options"])) == 2
    assert card["answer"] in (0, 1)
    assert all(len(card[k]) == 2 and all(card[k]) for k in ("title", "topic", "why"))
    assert card["ref"].startswith("https://docs.python.org/3/")
    c = dict(card)
    if "diagram" in c:
        assert all(len(c[k]) == 2 for k in ("alt","experiment","misconception"))
        assert c["variant_answer"] != c["answer"]
        image = (LABS / c["diagram"]).read_bytes()
        assert ET.fromstring(image).tag.endswith("}svg")
        c["image"] = "data:image/svg+xml;base64," + base64.b64encode(image).decode()
    deck.append(c)
template = (SRC / "template.html").read_text(encoding="utf-8")
assert template.count("__CARDS__") == 1
emit("python-pocket-lab.html",template.replace("__CARDS__",json.dumps(deck,ensure_ascii=False,separators=(",",":")).replace("<",r"\u003c")))
def entries(items, i):
    s = []
    for c in items:
        s += [f'<a name="{c["id"]}"></a>', '## ' + c['title'][i], '```python\n' + c['code'] + '\n```',
              '　/　'.join('`' + x + '`' for x in c['options'])]
        lines = ['<details><summary>' + ['حدست را زدی؟ پاسخ و دلیل','Made a prediction? Reveal the explanation'][i] + '</summary>','**'+['خروجی: ','Output: '][i]+'`'+c['options'][c['answer']]+'`**',c['why'][i]]
        if 'diagram' in c:
            lines += ['![' + c['alt'][i] + '](' + c['diagram'] + ')', '**'+['چرا گزینهٔ دیگر وسوسه‌کننده است؟','Why the other answer is tempting'][i]+'**　'+c['misconception'][i]]
        s += ['\n\n'.join(lines + ['</details>'])]
        if 'variant' in c:
            s += ['**' + ['بار دوم: یک تغییر','Round two: change one thing'][i] + '**　' + c['experiment'][i],
                  '<details><summary>'+['نسخهٔ تغییریافته و نتیجه','See the modified example and its output'][i]+'</summary>\n\n```python\n'+c['variant']+'\n```\n\n`'+c['options'][c['variant_answer']]+'`\n\n</details>']
        s += ['['+c.get('source_label',['مرجع پایتون','Python reference'])[i]+']('+c['ref']+')']
    return '\n\n'.join(s)+'\n'
nav = f'[فارسی](PLAY.md) · [English](PLAY.en.md) · [Offline HTML]({DOWNLOAD}) · [اتاق معماها / Puzzle desk]({THREAD})'
emit('PLAY.en.md','# Python Pocket Lab · 16 predictions\n\n![Visual field notes: predict, trace, change one line](diagrams/cover.svg)\n\nStart with the four illustrated puzzles. Commit to an output, follow the diagram, then change one line to make the other output true. The remaining twelve are quick rounds in text, music, tests and measurement.\n\n'+nav+'\n\n'+entries(visual+classic,1))
emit('ENCORE.fa.md','# چهار حدس دیگر: ریتم، گیتار، تست و اندازه‌گیری\n\n'+nav+'\n\n'+entries(encore,0))
classic_fa = (SRC/'classic.fa.md').read_text(encoding="utf-8").rstrip()
emit('PLAY.md','# آزمایشگاه مصور پایتون\n\n![جلد دفتر آزمایش: حدس بزن، رد اجرا را بگیر، یک خط را تغییر بده](diagrams/cover.svg)\n\nوقتی سه ردیفِ یک جدول را می‌سازی، ممکن است پایتون فقط **یک** ردیف در حافظه داشته باشد؟ اول حدس بزن. بعد پیکان‌های شکل را دنبال کن؛ آخر سر یک خط را عوض کن تا جواب دیگر درست شود.\n\n**مسیرت را انتخاب کن:** [جدول و حافظه](#shared-rows) · [ملودی و پیمایشگر](#one-way-stream) · [دکمه‌ها و زمان اجرا](#late-buttons) · [رتبه‌بندی و تساوی](#stable-ties)\n\nاگر تازه شروع کرده‌ای، از [۸ معمای پایه](#q1) برو. [۴ معمای موسیقی، تست و اندازه‌گیری](ENCORE.fa.md) هم یک مسیر مستقل‌اند. برای امتیاز و مرور خطاها، [نسخهٔ آفلاین]('+DOWNLOAD+') را ذخیره کن و در مرورگر باز کن.\n\n'+nav+'\n\n'+entries(visual,0)+'\n---\n\n# هشت حدس کوتاه\n\n'+classic_fa+'\n')
