"""Build Holy Grawlix Games logo SVGs (outlined Bangers glyphs, no font dependency).

Outputs (in ./logo):
  holygrawlix-horizontal-{dark,light}.svg   one-line lockup: HOLY [#$@!] GAMES
  holygrawlix-stacked-{dark,light}.svg      three-row lockup: HOLY / [#$@!] / GAMES
  holygrawlix-icon.svg                      grawlix burst only (#$ over @!), transparent
  holygrawlix-icon-app.svg                  icon on a dark rounded square (app/touch icon)
"dark" = for dark backgrounds (cream letters), "light" = for light backgrounds (black letters).
"""
import math, sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else 'logo'
os.makedirs(OUT, exist_ok=True)
f = TTFont(FONT); gs = f.getGlyphSet(); cmap = f.getBestCmap(); hm = f['hmtx']; UPM = f['head'].unitsPerEm
CAP = 721  # cap height in font units

YELLOW, BLACK, CREAM = '#FFD23F', '#0B0B10', '#F4F1EA'
BURST = [(0,18),(9,0),(24,12),(38,0),(52,10),(66,0),(80,12),(93,2),(100,20),(94,38),(100,56),(94,74),(100,92),
         (84,88),(70,100),(56,90),(42,100),(28,90),(14,100),(4,84),(0,64),(6,44)]

def adv(s, size, track=0):
    return sum(hm[cmap[ord(c)]][0] for c in s) * size / UPM + track * (len(s) - 1)

def text(s, x, baseline, size, fill, track=0):
    """Outlined text as a single <path>; x = left edge, baseline in SVG coords."""
    pen = SVGPathPen(gs); k = size / UPM; cx = x
    for c in s:
        g = cmap[ord(c)]
        gs[g].draw(TransformPen(pen, (k, 0, 0, -k, cx, baseline)))
        cx += hm[g][0] * k + track
    return f'<path fill="{fill}" d="{pen.getCommands()}"/>'

def burst(cx, cy, w, h, rot, stroke, sw):
    pts = []
    a = math.radians(rot)
    for px, py in BURST:
        x = (px / 100 - .5) * w; y = (py / 100 - .5) * h
        pts.append(f'{cx + x*math.cos(a) - y*math.sin(a):.1f},{cy + x*math.sin(a) + y*math.cos(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{YELLOW}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'

def grawlix_rows(rows, cx, cy, size, rot, track):
    """Symbols centred on (cx, cy), one or more rows, rotated with the burst."""
    lh = size * 0.92; total = lh * (len(rows) - 1)
    parts = []
    for i, r in enumerate(rows):
        w = adv(r, size, track)
        base = cy - total / 2 + i * lh + CAP * size / UPM / 2
        parts.append(text(r, cx - w / 2, base, size, BLACK, track))
    return f'<g transform="rotate({rot} {cx:.1f} {cy:.1f})">{"".join(parts)}</g>'

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>\n')

S = 200; ROT = -4; SW = 8; capH = CAP * S / UPM; TR = 6
TITLE = 'Holy Grawlix Games'

def horizontal(ink):
    # Optical spacing: Bangers' slanted Y overhangs its advance by ~0.138em and G starts ~0.042em in,
    # so the gaps are set from the visible ink, not the letter boxes. VIS = visible gap to the burst edge.
    pad = 40; VIS = 0.17 * S
    gap_l = VIS + 0.138 * S; gap_r = VIS - 0.042 * S
    holy_w = adv('HOLY', S); games_w = adv('GAMES', S); sym_w = adv('#$@!', S, TR)
    bw, bh = sym_w + 0.62 * S, capH + 0.62 * S
    W = pad + holy_w + gap_l + bw + gap_r + games_w + pad + 0.03 * S; H = bh + 2 * pad + 20
    cy = H / 2; base = cy + capH / 2
    x = pad; body = text('HOLY', x, base, S, ink)
    bx = x + holy_w + gap_l + bw / 2
    body += burst(bx, cy, bw, bh, ROT, ink, SW) + grawlix_rows(['#$@!'], bx, cy, S, ROT, TR)
    body += text('GAMES', bx + bw / 2 + gap_r, base, S, ink)
    return svg(W, H, body, TITLE)

def stacked(ink):
    pad = 40; row = capH; gap = 0.16 * S
    holy_w = adv('HOLY', S); games_w = adv('GAMES', S); sym_w = adv('#$@!', S, TR)
    bw, bh = sym_w + 0.62 * S, capH + 0.62 * S
    W = max(bw, games_w, holy_w) + 2 * pad + 30; cx = W / 2
    y1 = pad + row                      # HOLY baseline
    by = y1 + gap + bh / 2              # burst centre
    y3 = by + bh / 2 + gap + row        # GAMES baseline
    H = y3 + pad
    body = text('HOLY', cx - holy_w / 2, y1, S, ink)
    body += burst(cx, by, bw, bh, ROT, ink, SW) + grawlix_rows(['#$@!'], cx, by, S, ROT, TR)
    body += text('GAMES', cx - games_w / 2, y3, S, ink)
    return svg(W, H, body, TITLE)

def icon(bg=None):
    W = H = 512; size = 230; c = W / 2
    body = f'<rect width="512" height="512" rx="112" fill="{bg}"/>' if bg else ''
    inset = 92 if bg else 40
    body += burst(c, c, W - 2 * inset, H - 2 * inset - 10, ROT, CREAM if bg else BLACK, 14)
    body += grawlix_rows(['#$', '@!'], c, c + 4, size * (0.82 if bg else 1), ROT, 10)
    return svg(W, H, body, 'Holy Grawlix Games icon')

files = {
    'holygrawlix-horizontal-dark.svg': horizontal(CREAM), 'holygrawlix-horizontal-light.svg': horizontal(BLACK),
    'holygrawlix-stacked-dark.svg': stacked(CREAM), 'holygrawlix-stacked-light.svg': stacked(BLACK),
    'holygrawlix-icon.svg': icon(), 'holygrawlix-icon-app.svg': icon(BLACK),
}
for n, s in files.items():
    open(os.path.join(OUT, n), 'w').write(s); print(n, len(s))
# Width of the one-line lockup in em (for the website's layout switch)
print('ONE_LINE_EM', round((adv('HOLY', 1) + 0.308 + adv('#$@!', 1, TR / S) + 0.62 + 0.128 + adv('GAMES', 1)), 3))

# ---------- Icon (simplified burst, few symbols fully inside) ----------
def icon_burst(c, r_out, r_in, n, rot, stroke, sw, jitter):
    pts = []
    for i in range(2 * n):
        r = (r_out if i % 2 == 0 else r_in) * jitter[i % len(jitter)]
        a = math.radians(rot + i * 180 / n - 90)
        pts.append(f'{c + r*math.cos(a):.1f},{c + r*math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{YELLOW}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'

JIT = [1.0, 1.0, .93, 1.0, 1.04, 1.0, .95, 1.0, 1.02, 1.0, .92, 1.0, 1.03, 1.0, .96, 1.0, 1.0, 1.0, .94, 1.0]

def icon_v2(chars, size, bg=None, dy=0, track=0):
    W = 512; c = W / 2
    body = f'<rect width="512" height="512" rx="112" fill="{bg}"/>' if bg else ''
    k = 0.78 if bg else 1.0
    body += icon_burst(c, 246 * k, 196 * k, 10, -4, CREAM if bg else BLACK, (16 if bg else 20), JIT)
    w = adv(chars, size * k, track)
    base = c + CAP * size * k / UPM / 2 + dy * k
    body += f'<g transform="rotate(-4 {c} {c})">{text(chars, c - w / 2 - 0.03 * size * k, base, size * k, BLACK, track)}</g>'
    return svg(W, W, body, 'Holy Grawlix Games icon')

# Chosen icon: '#!' in the simplified burst (option B)
open(os.path.join(OUT, 'holygrawlix-icon.svg'), 'w').write(icon_v2('#!', 300, None, 0, 4))
open(os.path.join(OUT, 'holygrawlix-icon-app.svg'), 'w').write(icon_v2('#!', 300, BLACK, 0, 4))

if len(sys.argv) > 3 and sys.argv[3] == 'icon-options':
    opts = {'A-bang': ('!', 360, 0, 0), 'B-hash-bang': ('#!', 300, 0, 4), 'C-at-bang': ('@!', 250, 0, 4), 'D-hash': ('#', 330, 0, 0)}
    for k_, (ch, sz, dy, tr) in opts.items():
        open(os.path.join(OUT, f'opt-{k_}.svg'), 'w').write(icon_v2(ch, sz, None, dy, tr))
        open(os.path.join(OUT, f'opt-{k_}-app.svg'), 'w').write(icon_v2(ch, sz, BLACK, dy, tr))
    print('options written')
