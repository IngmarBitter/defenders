# Adds NKJV quotes (blockquote lines) under each item of the "## Key Scripture" section.
# Items that already have quotes are skipped. The verse cache (tools/nkjv_cache.json) is gitignored.
# usage: python tools/nkjv-keyscripture.py <folder> [--dry]
import re, sys, os, json, glob, html, urllib.request

BOOKS = [("Genesis","gen"),("Exodus","exo"),("Leviticus","lev"),("Numbers","num"),("Deuteronomy","deu"),
("Joshua","jos"),("Judges","jdg"),("Ruth","rut"),("1 Samuel","1sa"),("2 Samuel","2sa"),("1 Kings","1ki"),("2 Kings","2ki"),
("1 Chronicles","1ch"),("2 Chronicles","2ch"),("Ezra","ezr"),("Nehemiah","neh"),("Esther","est"),("Job","job"),
("Psalms","psa"),("Psalm","psa"),("Proverbs","pro"),("Ecclesiastes","ecc"),("Song of Solomon","sng"),("Song of Songs","sng"),
("Isaiah","isa"),("Jeremiah","jer"),("Lamentations","lam"),("Ezekiel","eze"),("Daniel","dan"),("Hosea","hos"),("Joel","joe"),
("Amos","amo"),("Obadiah","oba"),("Jonah","jon"),("Micah","mic"),("Nahum","nah"),("Habakkuk","hab"),("Zephaniah","zep"),
("Haggai","hag"),("Zechariah","zec"),("Malachi","mal"),("Matthew","mat"),("Mark","mar"),("Luke","luk"),("John","jhn"),
("Acts","act"),("Romans","rom"),("1 Corinthians","1co"),("2 Corinthians","2co"),("Galatians","gal"),("Ephesians","eph"),
("Philippians","phl"),("Colossians","col"),("1 Thessalonians","1th"),("2 Thessalonians","2th"),("1 Timothy","1ti"),
("2 Timothy","2ti"),("Titus","tit"),("Philemon","phm"),("Hebrews","heb"),("James","jas"),("1 Peter","1pe"),("2 Peter","2pe"),
("1 John","1jo"),("2 John","2jo"),("3 John","3jo"),("Jude","jde"),("Revelation","rev")]
CODE = dict(BOOKS)
DISPLAY = {"Psalms":"Psalm"}
ONECH = {"oba","phm","2jo","3jo","jde"}
MAXV = 8
names = sorted(CODE, key=len, reverse=True)
TOK = re.compile(r"(?P<book>" + "|".join(re.escape(n) for n in names) + r")\b"
                 r"|(?P<cv>\d+:\d+(?:[–-]\d+(?::\d+)?)?)"
                 r"|(?P<num>\d+(?:[–-]\d+)?)"
                 r"|(?P<sep>[,;]|\band\b|\bwith\b|\bcf\.)"
                 r"|(?P<ws>\s+)"
                 r"|(?P<other>.)", re.S)

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nkjv_cache.json")
cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

def chapter(code, ch):
    k = f"{code}:{ch}"
    if k not in cache:
        u = f"https://www.blueletterbible.org/nkjv/{code}/{ch}/1/"
        s = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf8")
        out = {}
        for m in re.finditer(r'<div class="EngBibleText scriptureText"[^>]*data-print-verse-prefix="(\d+)">(.*?)</div>', s, re.S):
            t = m.group(2)
            t = re.sub(r'<a[^>]*class="hide-for-tablet">.*?</a>', '', t, flags=re.S)
            t = re.sub(r'<span class="hide-for-tablet"> - </span>', '', t)
            t = re.sub(r'<sup.*?</sup>', '', t, flags=re.S)
            t = re.sub(r'<[^>]+>', '', t); t = html.unescape(re.sub(r'\s+', ' ', t)).strip()
            t = re.sub('[“”‘’]', "'", t.replace('[fn]', ''))
            out[m.group(1)] = t
        if not out: raise RuntimeError("no verses for " + k)
        cache[k] = out
        json.dump(cache, open(CACHE, "w", encoding="utf-8"))
    return cache[k]

def parse(line):
    """Return list of (book, ch, v1, v2) ; v1=None means whole chapter(s) ch..v2."""
    refs = []; book = None; ch = None; last = None; prev_sep = None
    for m in TOK.finditer(line):
        g = m.lastgroup; t = m.group()
        if g == "book": book = t; ch = None; last = "book"
        elif g == "ws": continue
        elif g == "sep": last = "sep"; prev_sep = ";" if t == ";" else ","
        elif g == "cv" and book:
            c, rest = t.split(":", 1); r = re.split("[–-]", rest)
            if len(r) == 2 and ":" in r[1]:
                refs.append((book, int(c), int(r[0]), None, "x" + t)); ch = None
            else:
                refs.append((book, int(c), int(r[0]), int(r[-1]), None)); ch = int(c)
            last = "cv"
        elif g == "num" and book:
            r = [int(x) for x in re.split("[–-]", t)]
            if CODE[book] in ONECH: refs.append((book, 1, r[0], r[-1], None)); ch = 1
            elif ch is not None and last == "sep" and prev_sep == ",": refs.append((book, ch, r[0], r[-1], None))
            else: refs.append((book, r[0], None, r[-1], None)); ch = None
            last = "num"
        else:
            if g == "other" and t in "(" : book = None
            elif g == "other" and t not in ".)": book = None
            last = g
    return refs

prev_sep = None
def label(b, c, v1, v2, x):
    n = DISPLAY.get(b, b)
    if x: return f"{n} {x[1:]}"
    if CODE[b] in ONECH: return f"{n} {v1}" + (f"–{v2}" if v2 != v1 else "")
    if v1 is None: return f"{n} {c}" + (f"–{v2}" if v2 != c else "")
    return f"{n} {c}:{v1}" + (f"–{v2}" if v2 != v1 else "")

def quote(r):
    b, c, v1, v2, x = r
    lab = label(*r)
    if x or v1 is None or v2 - v1 + 1 > MAXV:
        return f"> *{lab}* – longer passage, read in full", 0
    d = chapter(CODE[b], c)
    txt = " ".join(d[str(i)] for i in range(v1, v2 + 1))
    return f'> *{lab} (NKJV)*: "{txt}"', v2 - v1 + 1

total = 0
dry = "--dry" in sys.argv
for p in sorted(glob.glob(os.path.join(sys.argv[1], "*.md"))):
    lines = open(p, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    out = []; inks = False; i = 0
    while i < len(lines):
        L = lines[i]; out.append(L)
        if L.startswith("## "): inks = L.strip() == "## Key Scripture"
        if inks and re.match(r"^\d+\. ", L):
            # take continuation lines of the item
            while i + 1 < len(lines) and lines[i+1].startswith("   ") and not lines[i+1].lstrip().startswith(">"):
                i += 1; out.append(lines[i]); L += " " + lines[i]
            j = i + 1
            while j < len(lines) and lines[j].strip() == "": j += 1
            if j < len(lines) and lines[j].lstrip().startswith(">"):
                i += 1; continue  # already done
            seen = set(); qs = []
            prev_sep = None
            for r in parse(L):
                k = label(*r)
                if k in seen: continue
                seen.add(k); q, n = quote(r); total += n; qs.append("   " + q)
            if qs:
                out.append("")
                for q in qs: out.append(q); out.append("")
                if out[-1] == "" and i + 1 < len(lines) and lines[i+1] == "": out.pop()
        i += 1
    if not dry:
        open(p, "wb").write("\r\n".join(out).encode("utf-8"))
    print(os.path.basename(p))
print("verses quoted:", total)
