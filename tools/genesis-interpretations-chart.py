"""Generates docs/Creation/pics/GenesisInterpretations.svg (text outlined) on a strict grid.
All text one size, all boxes one line width, each box one main HuBiSa hue (standard saturation),
parallel lines G apart, text P away from every line."""
from PIL import ImageFont

FS = 30                      # font size (px) for all text
SUP = 1.0                    # superscript markers: same size as the text, only raised
LW = 3                       # box line width
G = 14                       # distance between adjacent parallel box lines
P = 14                       # distance between text and box lines
RAISE = round(FS * 0.3)      # how far superscript markers sit above the baseline
LH = round(FS * 1.2) + RAISE # line height, with room for a raised marker
FONT = ImageFont.truetype(r'C:\Windows\Fonts\calibrib.ttf', FS)
SYM = ImageFont.truetype(r'C:\Windows\Fonts\seguisym.ttf', FS)

# HuBiSa standard-saturation base colors (ColorHuBiSa.cs, RgbGridInit, [hue][3*BiS][2])
C = dict(Red='#DD2222', Orange='#B4731D', Yellow='#A9A902', Green='#02B302',
         Cyan='#0297A4', Blue='#2057DD', Purple='#8016E9', Magenta='#BC07BC', Gray='#808080')

def tw(s):
  """Width of a label; markers after '^' are superscript."""
  base, _, sup = s.partition('^')
  return FONT.getlength(base) + SUP * sum((SYM if ch in '✓✗' else FONT).getlength(ch) for ch in sup)

def block_w(lines): return max(tw(l) for l in lines)
def block_h(lines): return len(lines) * LH

# ---- rows: (items in day=24h column, items in day!=24h column) ----
rows = [
  (['YEC^†'], []),
  (['Verse 1-2 Gap^*', 'Day-Gap^*'], ['Day-Age^+']),
  (['Literal Naive^*‡'], []),
  ([], ['Mytho-History^*']),
  (['Revelation-Day^*‡'], ['Creation Myth^*‡', 'Functional Creation^*']),
]
framework = ['Literary Framework^*?']
ROWS_MIN = 2 * LH             # every band row tall enough for a two-line label

# horizontal box lines at each row boundary, outer to inner does not matter, just count
# boundary k is above row k (k = 0..len(rows)), then boundary 'col_bottom' above framework, then F bottom
bnd = {
  0: ['L_top', 'AS_top', 'YE_top'],
  1: ['YE_bot', 'OE_top'],
  2: ['AS_bot', 'OS_top'],
  3: ['OS_bot', 'F_top'],
  4: ['L_bot', 'OE_bot'],
  5: ['COL_bot'],
}

# ---- x layout ----
labL = block_w(['Literal', 'Figurative'])
labS = block_w(['Accurate', 'Science', 'Obsolete'])
colA = max(block_w(r[0]) for r in rows if r[0])
colB = max(block_w(r[1]) for r in rows if r[1])
colA = max(colA, tw('day = 24h ✓'))
colB = max(colB, tw('day ≠ 24h ✗'))
labR = block_w(['Young', 'Earth', 'Old'])

x = {}
x['L_l'] = 0
x['F_l'] = G
x['S_l'] = x['F_l'] + P + labL + P          # AS and OS share the left edge (no vertical overlap)
x['E_l'] = x['S_l'] + P + labS + P          # YE and OE share the left edge
x['A_l'] = x['E_l'] + G                     # day=24h column
x['A_r'] = x['A_l'] + P + colA + P
x['OS_r'] = x['A_r'] + G
x['B_l'] = x['OS_r'] + G                    # day!=24h column
x['B_r'] = x['B_l'] + P + colB + P
x['AS_r'] = x['B_r'] + G
x['L_r'] = x['AS_r'] + G
x['F_r'] = x['L_r'] + G
x['E_r'] = x['F_r'] + P + labR + P          # YE and OE share the right edge

# ---- y layout ----
y = {}
cur = 0
y['COL_top'] = cur
cur += P
y['collab'] = cur                           # column label baseline area top
cur += LH + P
row_top = []
for k, r in enumerate(rows):
  lines = bnd[k]
  for i, name in enumerate(lines):
    y[name] = cur + i * G
  cur += (len(lines) - 1) * G + P
  h = max(ROWS_MIN, block_h(r[0]), block_h(r[1]))
  row_top.append((cur, h))
  cur += h + P
y['COL_bot'] = cur
fw_top = cur + P
cur = fw_top + block_h(framework) + P
y['F_bot'] = cur
H = cur

# ---- svg ----
out = []
def rect(x1, y1, x2, y2, col):
  out.append(f'<rect x="{x1:.1f}" y="{y1:.1f}" width="{x2-x1:.1f}" height="{y2-y1:.1f}" '
             f'fill="none" stroke="{C[col]}" stroke-width="{LW}"/>')
def text(lines, cx, ty, col, anchor='middle'):
  for i, l in enumerate(lines):
    base, _, sup = l.partition('^')
    bl = ty + i * LH + RAISE + FS * 0.85
    s = base.replace('&', '&amp;')
    if sup:
      s += f'<tspan font-size="{FS*SUP:.1f}" dy="{-RAISE}">{sup}</tspan>'
    out.append(f'<text x="{cx:.1f}" y="{bl:.1f}" text-anchor="{anchor}" fill="{C[col]}">{s}</text>')

# boxes
rect(x['A_l'], y['COL_top'], x['A_r'], y['COL_bot'], 'Green')
rect(x['B_l'], y['COL_top'], x['B_r'], y['COL_bot'], 'Red')
rect(x['L_l'], y['L_top'], x['L_r'], y['L_bot'], 'Magenta')
rect(x['F_l'], y['F_top'], x['F_r'], y['F_bot'], 'Purple')
rect(x['S_l'], y['AS_top'], x['AS_r'], y['AS_bot'], 'Blue')
rect(x['S_l'], y['OS_top'], x['OS_r'], y['OS_bot'], 'Cyan')
rect(x['E_l'], y['YE_top'], x['E_r'], y['YE_bot'], 'Yellow')
rect(x['E_l'], y['OE_top'], x['E_r'], y['OE_bot'], 'Orange')

# column labels
text(['day = 24h ✓'], (x['A_l'] + x['A_r']) / 2, y['collab'], 'Green')
text(['day ≠ 24h ✗'], (x['B_l'] + x['B_r']) / 2, y['collab'], 'Red')

# region labels (left-aligned in their strips, vertically centered on the box span not shared)
def vc(y1, y2, lines): return (y1 + y2) / 2 - block_h(lines) / 2
text(['Literal'], x['F_l'] + P, vc(y['L_top'], y['F_top'], ['Literal']), 'Magenta', 'start')
text(['Figurative'], x['F_l'] + P, vc(y['L_bot'], y['F_bot'], ['Figurative']), 'Purple', 'start')
text(['Accurate', 'Science'], x['S_l'] + P, vc(y['AS_top'], y['AS_bot'], ['a', 'b']), 'Blue', 'start')
text(['Obsolete', 'Science'], x['S_l'] + P, vc(y['OS_top'], y['OS_bot'], ['a', 'b']), 'Cyan', 'start')
text(['Young', 'Earth'], x['F_r'] + P, vc(y['YE_top'], y['YE_bot'], ['a', 'b']), 'Yellow', 'start')
text(['Old', 'Earth'], x['F_r'] + P, vc(y['OE_top'], y['OE_bot'], ['a', 'b']), 'Orange', 'start')

# items
for (top, h), (a, b) in zip(row_top, rows):
  if a: text(a, (x['A_l'] + x['A_r']) / 2, top + (h - block_h(a)) / 2, 'Gray')
  if b: text(b, (x['B_l'] + x['B_r']) / 2, top + (h - block_h(b)) / 2, 'Gray')
text(framework, (x['A_l'] + x['B_r']) / 2, fw_top, 'Gray')

# title and legend
# title: two lines, larger, top-left in the space left of the day columns and above the Literal box
TFS = round(FS * 1.5)
TLH = round(TFS * 1.15)
title_top = y['L_top'] - P - 2 * TLH
TITLE_H = max(0, -title_top)
LEG = ['^*Compatible with evolution and old age fossils', '^+Compatible with old age fossils',
       '^†No death before the fall', '^‡Historical Adam not affirmed', '^?Day length left open']
leg_top = H + P
for i, l in enumerate(['Genesis', 'Interpretations']):
  out.append(f'<text x="0" y="{title_top + i*TLH + TFS*0.85:.1f}" font-size="{TFS}" fill="{C["Gray"]}">{l}</text>')
assert FONT.font_variant(size=TFS).getlength('Interpretations') <= x['A_l'] - P, 'title too wide for the space left of the columns'
for i, l in enumerate(LEG):
  sym, rest = l[1], l[2:]
  text([rest], max(FONT.getlength(c) for c in '*+†‡?') * SUP + 8, leg_top + i * LH, 'Gray', 'start')
  out.append(f'<text x="0" y="{leg_top + i*LH + FS*0.85:.1f}" font-size="{FS*SUP:.1f}" fill="{C["Gray"]}">{sym}</text>')
bottom = leg_top + len(LEG) * LH + P

M = 4
W = x['E_r']
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W+2*M:.0f}" height="{bottom+TITLE_H+2*M:.0f}" '
       f'viewBox="{-M} {-TITLE_H-M} {W+2*M:.0f} {bottom+TITLE_H+2*M:.0f}" '
       f'font-family="Calibri, sans-serif" font-weight="bold" font-size="{FS}">\n  ' + '\n  '.join(out) + '\n</svg>\n')
# Write the text version, then outline the text with Inkscape so the published SVG looks the same
# in every browser (Calibri is not installed on macOS/iOS/Android, and an SVG shown as <img>
# cannot load web fonts).
import os, subprocess, sys, tempfile
dst = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'Creation', 'pics', 'GenesisInterpretations.svg')
tmp = os.path.join(tempfile.gettempdir(), 'GenesisInterpretations.text.svg')
open(tmp, 'w', encoding='utf8', newline='\r\n').write(svg)
subprocess.run(['inkscape', tmp, '--export-text-to-path', '--export-plain-svg', '--export-type=svg',
                f'--export-filename={os.path.abspath(dst)}'], check=True, capture_output=True)
print('wrote', os.path.abspath(dst))
