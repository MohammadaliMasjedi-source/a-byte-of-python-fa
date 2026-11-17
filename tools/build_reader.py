#!/usr/bin/env python3
"""Rebuild the chapter part of reading.html from translation/00..08 and check it.

Usage:
    python3 tools/build_reader.py          # rebuild reading.html
    python3 tools/build_reader.py --check  # compare reading.html with the Markdown

Only the standard library is used. The page shell (CSS, title page, table of
contents, footer) is not touched.
"""
import html
import os
import re
import sys
import unicodedata
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PAGE = os.path.join(ROOT, "reading.html")
CHAPTERS = [
    ("00-preface.md", "preface"),
    ("01-about-python.md", "about"),
    ("02-installation.md", "install"),
    ("03-first-steps.md", "first-steps"),
    ("04-basics.md", "basics"),
    ("05-operators-expressions.md", "op-exp"),
    ("06-control-flow.md", "control-flow"),
    ("07-functions.md", "functions"),
    ("08-modules.md", "modules"),
]
FILE_TO_ID = {f: i for f, i in CHAPTERS}
BEGIN = "<!-- chapters:begin -->"
END = "<!-- chapters:end -->"
ORDERED = re.compile(r"^\d+\. (.*)$")
BULLET = re.compile(r"^(\s*)[-*] (.*)$")
FOOTDEF = re.compile(r"^\[\^(\d+)\]: (.*)$")


def slug(text):
    text = re.sub(r"<[^>]*>", "", text.replace("`", "")).lower().strip()
    out = ""
    for c in text:
        cat = unicodedata.category(c)
        if c == " ":
            out += "-"
        elif c == "-" or c == "\u200c" or cat[0] in "LMN" or cat == "Pc":
            out += c
    return out


def inline(s):
    hold = []

    def keep(h):
        hold.append(h)
        return "\x00%d\x00" % (len(hold) - 1)

    s = re.sub(r"`([^`]+)`", lambda m: keep("<code>%s</code>" % html.escape(m.group(1), quote=False)), s)
    s = re.sub(r"<(https?://[^>\s]+)>",
               lambda m: keep('<a href="%s">%s</a>' % (html.escape(m.group(1)), html.escape(m.group(1), quote=False))), s)

    def link(m):
        label, url = m.group(1), m.group(2)
        if url.startswith("./"):
            name, _, _frag = url[2:].partition("#")
            if name in FILE_TO_ID:
                return keep('<a href="#%s">' % FILE_TO_ID[name]) + label + keep("</a>")
            return label
        if url.startswith("#"):
            return keep('<a href="#%s">' % html.escape(url[1:])) + label + keep("</a>")
        return keep('<a href="%s">' % html.escape(url)) + label + keep("</a>")

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    s = re.sub(r"\[\^(\d+)\]", lambda m: keep('<sup><a id="fnref-%s" href="#fn-%s">%s</a></sup>' % ((m.group(1),) * 3)), s)
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w])_(?=\S)(.+?)(?<=\S)_(?![\w])", r"<em>\1</em>", s)
    return re.sub(r"\x00(\d+)\x00", lambda m: hold[int(m.group(1))], s)


def is_block_start(line):
    return (line.startswith(("```", ">", "#")) or BULLET.match(line) or ORDERED.match(line)
            or line.strip() == "---" or FOOTDEF.match(line))


def render_list(items):
    """items: list of (indent, text); builds nested <ul>."""
    out, stack = [], []
    for indent, text in items:
        while stack and indent < stack[-1]:
            stack.pop()
            out.append("</li></ul>")
        if stack and indent == stack[-1]:
            out.append("</li>")
        elif not stack or indent > stack[-1]:
            out.append("<ul>")
            stack.append(indent)
        out.append("<li>" + inline(text))
    while stack:
        stack.pop()
        out.append("</li></ul>")
    return "".join(out)


def convert(md, h1_id, used):
    lines = md.split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith("```"):
            body, i = [], i + 1
            while not lines[i].startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1
            out.append("  <pre><code>%s</code></pre>" % html.escape("\n".join(body), quote=False))
        elif re.match(r"#{1,3} ", line):
            level = len(line.split()[0])
            text = line[level + 1:]
            if level == 1:
                hid = h1_id
            else:
                hid = base = slug(text)
                n = 1
                while hid in used:
                    hid = "%s-%d" % (base, n)
                    n += 1
            used.add(hid)
            out.append("  <h%d id=\"%s\">%s</h%d>" % (level, hid, inline(text), level))
            i += 1
        elif line.strip() == "---":
            out.append("  <hr>")
            i += 1
        elif FOOTDEF.match(line):
            m = FOOTDEF.match(line)
            out.append('  <p class="footnote" id="fn-%s"><sup>%s</sup> %s</p>' % (m.group(1), m.group(1), inline(m.group(2))))
            i += 1
        elif line.startswith(">"):
            paras, cur = [], []
            while i < len(lines) and lines[i].startswith(">"):
                t = lines[i][1:].strip()
                if t:
                    cur.append(t)
                elif cur:
                    paras.append(cur)
                    cur = []
                i += 1
            if cur:
                paras.append(cur)
            out.append("  <blockquote>" + "".join("<p>%s</p>" % inline(" ".join(p)) for p in paras) + "</blockquote>")
        elif ORDERED.match(line):
            out.append("  <ol>")
            while i < len(lines) and ORDERED.match(lines[i]):
                item = "<li>" + inline(ORDERED.match(lines[i]).group(1))
                i += 1
                sub = []
                while i < len(lines) and BULLET.match(lines[i]) and BULLET.match(lines[i]).group(1):
                    m = BULLET.match(lines[i])
                    sub.append((len(m.group(1)), m.group(2)))
                    i += 1
                out.append("    " + item + (render_list(sub) if sub else "") + "</li>")
            out.append("  </ol>")
        elif BULLET.match(line):
            items = []
            while i < len(lines) and BULLET.match(lines[i]):
                m = BULLET.match(lines[i])
                items.append((len(m.group(1)), m.group(2)))
                i += 1
            out.append("  " + render_list(items))
        else:
            para = [line.strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not is_block_start(lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append("  <p>%s</p>" % inline(" ".join(para)))
    return "\n".join(out)


def build():
    used = set()
    parts = [BEGIN]
    for n, (fname, hid) in enumerate(CHAPTERS):
        with open(os.path.join(ROOT, "translation", fname), encoding="utf-8") as f:
            md = f.read()
        parts.append("\n  <!-- ===================== %d. %s ===================== -->" % (n, fname))
        parts.append(convert(md, hid, used))
    parts.append("\n" + END + "\n")
    with open(PAGE, encoding="utf-8") as f:
        page = f.read()
    new = "\n".join(parts)
    s, e = page.index(BEGIN), page.index(END) + len(END) + 1
    page = page[:s] + new + page[e:]
    with open(PAGE, "w", encoding="utf-8") as f:
        f.write(page)


# ---------------------------------------------------------------- check
class Counter(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.c, self.pre, self.text, self.in_pre, self.ids, self.hrefs = {}, [], [], False, set(), []
        self.cur = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"):
            self.hrefs.append(a["href"][1:])
        if tag in ("h1", "h2", "h3", "p", "li", "blockquote", "hr", "pre", "ol"):
            self.c[tag] = self.c.get(tag, 0) + 1
        if tag == "pre":
            self.in_pre, self.cur = True, ""

    def handle_endtag(self, tag):
        if tag == "pre":
            self.in_pre = False
            self.pre.append(self.cur)

    def handle_data(self, d):
        if self.in_pre:
            self.cur += d
        else:
            self.text.append(d)


def md_counts_and_text(md):
    lines, c, code, text, inb = md.split("\n"), {}, [], [], False
    blk = []

    def bump(k):
        c[k] = c.get(k, 0) + 1

    prev_para = False
    prev_item = False
    for l in lines:
        if not ORDERED.match(l) and not BULLET.match(l):
            prev_item = False
        if l.startswith("```"):
            if inb:
                code.append("\n".join(blk))
                blk = []
            else:
                bump("pre")
            inb, prev_para = not inb, False
            continue
        if inb:
            blk.append(l)
            continue
        if not l.strip() or l.strip() == ">":
            prev_para = False
            continue
        if l.strip() == "---":
            bump("hr")
            prev_para = False
            continue
        m = re.match(r"(#{1,3}) (.*)", l)
        if m:
            bump("h%d" % len(m.group(1)))
            text.append(m.group(2))
            prev_para = False
            continue
        if l.startswith(">"):
            if not prev_para:
                bump("p")
            prev_para = True
            text.append(l[1:])
            continue
        if ORDERED.match(l):
            bump("li")
            if not prev_item:
                bump("ol")
            text.append(ORDERED.match(l).group(1))
            prev_para, prev_item = False, True
            continue
        if BULLET.match(l):
            bump("li")
            text.append(BULLET.match(l).group(2))
            prev_para = False
            continue
        if FOOTDEF.match(l) or not prev_para:
            bump("p")
        prev_para = True
        text.append(l)
    return c, code, text


def norm_md(chunks):
    t = "\n".join(chunks)
    t = re.sub(r"<(https?://[^>\s]+)>", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\((?:[^)]+)\)", r"\1", t)
    t = re.sub(r"\[\^(\d+)\]:?", r" \1 ", t)
    t = t.replace("`", "")
    return re.sub(r"[\W_]+", "", t)


def check():
    with open(PAGE, encoding="utf-8") as f:
        page = f.read()
    sec = page[page.index(BEGIN):page.index(END)]
    chapters = re.split(r"\n  <!-- ={5,} \d+\. [^\n]* =+ -->\n", sec)[1:]
    ok, ids, hrefs = True, set(), []
    print("%-28s %5s %5s %5s %5s %5s %5s  %s" % ("chapter", "h", "p", "li", "ol", "code", "hr", "result"))
    for (fname, _), chunk in zip(CHAPTERS, chapters):
        with open(os.path.join(ROOT, "translation", fname), encoding="utf-8") as f:
            md = f.read()
        mc, mcode, mtext = md_counts_and_text(md)
        p = Counter()
        p.feed(chunk)
        hc = {k: p.c.get(k, 0) for k in ("h1", "h2", "h3", "li", "hr", "pre", "ol")}
        # paragraphs: <p> inside blockquote count once each, like the Markdown paragraphs
        pc = p.c.get("p", 0)
        problems = []
        for k in ("h1", "h2", "h3", "li", "hr", "pre", "ol"):
            if mc.get(k, 0) != hc[k]:
                problems.append("%s md=%d html=%d" % (k, mc.get(k, 0), hc[k]))
        if mc.get("p", 0) != pc:
            problems.append("p md=%d html=%d" % (mc.get("p", 0), pc))
        if mcode != p.pre:
            problems.append("code text differs")
        if norm_md(mtext) != re.sub(r"[\W_]+", "", "\n".join(p.text)):
            problems.append("prose text differs")
        ids |= p.ids
        hrefs += p.hrefs
        ok &= not problems
        print("%-28s %5d %5d %5d %5d %5d %5d  %s" % (
            fname, hc["h1"] + hc["h2"] + hc["h3"], pc, hc["li"], hc["ol"], hc["pre"], hc["hr"],
            "ok" if not problems else "; ".join(problems)))
    missing = sorted(set(h for h in hrefs if h not in ids and h not in
                         {i for i in re.findall(r'id="([^"]+)"', page)}))
    if missing:
        ok = False
        print("unresolved anchors:", missing)
    print("ALL OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    build()
