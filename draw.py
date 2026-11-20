"""THE WORLD TODAY - a one-page newspaper front page for Friday, Nov 20, 2026.

Everything is drawn with PIL primitives: no photographs, no external assets.
build_image() returns a 1024x1024 RGB image of the front page.
"""

import random

from PIL import Image, ImageDraw, ImageFont

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

W = 1024
MARGIN = 36
RIGHT = W - MARGIN
CONTENT_W = RIGHT - MARGIN

PAPER = (248, 243, 230)
INK = (26, 23, 18)
GRAY = (90, 83, 72)
RULE = (26, 23, 18)
RED = (163, 22, 33)
NAVY = (22, 50, 79)
GREEN = (22, 110, 60)


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_font(d, text, path, max_w, start, floor=11):
    """Largest size <= start at which text fits max_w on one line."""
    size = start
    while size > floor:
        f = font(path, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(path, floor)


def wrap_lines(d, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(d, text, f, x, y, max_w, leading, fill=INK):
    """Draw wrapped text, return the y just below the block."""
    for line in wrap_lines(d, text, f, max_w):
        d.text((x, y), line, font=f, fill=fill)
        y += leading
    return y


def centered(d, text, f, y, fill=INK):
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)


def rule(d, y, weight=2, fill=RULE, x0=MARGIN, x1=RIGHT):
    d.rectangle([x0, y, x1, y + weight - 1], fill=fill)


def kicker(d, text, x, y, fill=RED):
    d.text((x, y), text, font=font(SANS_B, 16), fill=fill)


# ---------------------------------------------------------------- masthead

def masthead(d):
    d.rectangle([10, 10, W - 11, W - 11], outline=(120, 110, 92), width=2)
    d.text((MARGIN, 24), "VOL. I - No. 20", font=font(SANS_B, 15), fill=GRAY)
    d.text((RIGHT - d.textlength("LATE CITY EDITION", font=font(SANS_B, 15)), 24),
           "LATE CITY EDITION", font=font(SANS_B, 15), fill=GRAY)
    rule(d, 48, 1)

    f = fit_font(d, "THE WORLD TODAY", SERIF_B, CONTENT_W, 88)
    centered(d, "THE WORLD TODAY", f, 50)

    f_date = font(SERIF_B, 21)
    centered(d, "Friday, November 20, 2026", f_date, 136)
    f_cities = font(SANS, 13)
    centered(d, "SHENZHEN  ·  THE HAGUE  ·  NEW YORK  ·  BELEM  ·  KYIV  ·  DEEP SPACE",
             f_cities, 160, fill=GRAY)
    rule(d, 174, 6)
    rule(d, 184, 1)


# ------------------------------------------------------- headline story art

def _flag_us(d, x, y, w, h):
    for i in range(7):
        col = (178, 34, 52) if i % 2 == 0 else (245, 245, 240)
        d.rectangle([x, y + i * h / 7, x + w, y + (i + 1) * h / 7], fill=col)
    d.rectangle([x, y, x + w * 0.45, y + h * 4 / 7], fill=(60, 59, 110))


def _star(d, cx, cy, r, fill):
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.polygon(pts, fill=fill)


def _flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    _star(d, x + 13, y + 12, 9, (255, 222, 0))
    for dx, dy in [(27, 5), (31, 12), (31, 20), (27, 27)]:
        d.ellipse([x + dx, y + dy, x + dx + 4, y + dy + 4], fill=(255, 222, 0))


def _flag_ru(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(245, 245, 245))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(0, 57, 166))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(213, 43, 30))


def _figure(d, cx, top, skin, suit):
    d.ellipse([cx - 22, top, cx + 22, top + 44], fill=skin, outline=INK, width=2)
    d.pieslice([cx - 40, top + 38, cx + 40, top + 96], 180, 360, fill=suit, outline=INK)
    d.polygon([(cx - 7, top + 44), (cx + 7, top + 44), (cx, top + 56)], fill=(240, 238, 230))


def summit_panel(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(233, 226, 205), outline=INK, width=2)
    flags = [_flag_us, _flag_cn, _flag_ru]
    names = ["TRUMP", "XI", "PUTIN"]
    skins = [(232, 190, 160), (238, 200, 165), (226, 182, 150)]
    suits = [(30, 34, 60), (40, 40, 44), (52, 46, 40)]
    span = (x1 - x0)
    for i, draw_flag in enumerate(flags):
        cx = x0 + span * (0.22 + 0.28 * i)
        draw_flag(d, cx - 33, y0 + 8, 66, 38)
        d.rectangle([cx - 33, y0 + 8, cx + 33, y0 + 46], outline=INK, width=1)
        _figure(d, cx, y0 + 48, skins[i], suits[i])
    # the round table
    ty = y1 - 38
    d.ellipse([x0 + 56, ty, x1 - 56, ty + 34], fill=(122, 74, 33), outline=INK, width=2)
    d.ellipse([x0 + 72, ty + 5, x1 - 72, ty + 27], outline=(90, 54, 22), width=2)
    # the declaration, on the table
    px = (x0 + x1) / 2
    d.rectangle([px - 30, ty + 3, px + 30, ty + 17], fill=(252, 250, 244), outline=INK, width=1)
    for j in range(2):
        d.line([px - 22, ty + 8 + j * 5, px + 22, ty + 8 + j * 5], fill=GRAY, width=1)
    f_name = font(SANS_B, 12)
    for i, name in enumerate(names):
        cx = x0 + span * (0.22 + 0.28 * i)
        w = d.textlength(name, font=f_name)
        d.text((cx - w / 2, ty + 19), name, font=f_name, fill=(252, 248, 235))


def headline_story(d):
    y = 196
    kicker(d, "APEC SUMMIT · SHENZHEN · DIPLOMACY", MARGIN, y)
    y += 24
    f = fit_font(d, "THREE LEADERS, ONE TABLE", SERIF_B, CONTENT_W, 62)
    d.text((MARGIN, y), "THREE LEADERS, ONE TABLE", font=f, fill=INK)
    y += int(f.size * 1.18)
    dek = ("\"Peace declaration\" at the first-ever trilateral summit: Trump, Xi and Putin "
           "pledge talks on nuclear risk - and more fuel for the world")
    y = draw_text_block(d, dek, font(SERIF, 20), MARGIN, y, CONTENT_W, 26)
    y += 6
    panel_y1 = y + 112
    summit_panel(d, MARGIN, y, 596, panel_y1)
    body = ("SHENZHEN - Donald Trump, Xi Jinping and Vladimir Putin met face to face for "
            "the first time, on the sidelines of the APEC summit, and issued a joint "
            "\"peace declaration\" pledging talks on cutting nuclear risks and more "
            "refined fuel. Likened abroad to a new Yalta and watched closely in "
            "Europe, it brought no breakthrough on nuclear arms.")
    body_end = draw_text_block(d, body, font(SANS, 14), 616, y + 2, RIGHT - 616, 20)
    cap = "The three leaders around one table in Shenzhen: a first trilateral meeting."
    d.text((MARGIN, panel_y1 + 6), cap, font=font(SANS, 12), fill=GRAY)
    return max(panel_y1 + 26, body_end + 4)


# ------------------------------------------------------------ story art

def scales_icon(d, cx, top):
    """Scales of justice, drawn small beside the court story."""
    d.line([cx, top, cx, top + 44], fill=INK, width=3)
    d.line([cx - 28, top + 6, cx + 28, top + 6], fill=INK, width=3)
    for sgn in (-1, 1):
        px = cx + sgn * 28
        d.line([px, top + 6, px - 9, top + 27], fill=INK, width=2)
        d.line([px, top + 6, px + 9, top + 27], fill=INK, width=2)
        d.arc([px - 12, top + 16, px + 12, top + 36], 0, 180, fill=INK, width=3)
    d.rectangle([cx - 13, top + 44, cx + 13, top + 49], fill=INK)


def chart_icon(d, x, y, w, h):
    """A market chart leaping upward."""
    d.line([x, y + h, x + w, y + h], fill=GRAY, width=2)
    d.line([x, y, x, y + h], fill=GRAY, width=2)
    pts = [(x + 4, y + h - 14), (x + w * 0.3, y + h - 22), (x + w * 0.45, y + h - 16),
           (x + w * 0.65, y + h - 40), (x + w * 0.8, y + h - 36), (x + w - 8, y + 8)]
    d.line(pts, fill=GREEN, width=4)
    ax, ay = pts[-1]
    d.polygon([(ax + 12, ay - 3), (ax - 5, ay - 5), (ax, ay + 10)], fill=GREEN)


def stacks_icon(d, x, y):
    """Smokestacks with drifting smoke; fits a box about 70 wide, 84 tall."""
    base = y + 84
    for sx, sh in [(0, 48), (36, 64)]:
        d.polygon([(x + sx, base), (x + sx + 5, base - sh), (x + sx + 21, base - sh),
                   (x + sx + 26, base)], fill=(104, 96, 86), outline=INK)
        d.rectangle([x + sx + 3, base - sh, x + sx + 23, base - sh + 5], fill=RED)
        for j in range(2):
            r = 5 + j * 2.5
            cx = x + sx + 13 + j * 8
            cy = base - sh - 8 - j * 8
            d.ellipse([cx - r, cy - r * 0.7, cx + r, cy + r * 0.7], fill=(196, 190, 178))


def bridge_icon(d, x, y, w):
    """A great bridge, its middle span down; about 48 tall."""
    deck = y + 14
    for px in (x + 24, x + w - 38):
        d.rectangle([px, y - 2, px + 13, deck + 18], fill=(104, 96, 86), outline=INK)
    d.line([x, deck, x + w * 0.42, deck], fill=INK, width=4)
    d.line([x + w * 0.58, deck, x + w, deck], fill=INK, width=4)
    d.line([x + w * 0.42, deck, x + w * 0.5, deck + 11], fill=INK, width=4)
    d.line([x + w * 0.58, deck, x + w * 0.5, deck + 11], fill=INK, width=4)
    for fx in (0.08, 0.2, 0.32, 0.66, 0.78, 0.9):
        d.line([x + w * fx, deck - 10, x + w * fx, deck], fill=GRAY, width=2)
    for wx in range(0, int(w), 34):
        d.arc([x + wx, deck + 22, x + wx + 22, deck + 34], 180, 360, fill=NAVY, width=2)


def story_headline(d, text, x, y, w, start=36, one_line_floor=27):
    """One bold line if it fits big enough, else two wrapped lines."""
    f = fit_font(d, text, SERIF_B, w, start, floor=20)
    if f.size >= one_line_floor:
        d.text((x, y), text, font=f, fill=INK)
        return y + int(f.size * 1.15)
    size = min(start, 32)
    lines = wrap_lines(d, text, font(SERIF_B, size), w)
    while len(lines) > 2 and size > 20:
        size -= 1
        lines = wrap_lines(d, text, font(SERIF_B, size), w)
    f = font(SERIF_B, size)
    for line in lines:
        d.text((x, y), line, font=f, fill=INK)
        y += int(size * 1.14)
    return y


# ------------------------------------------------------------ story bands

def band_one(d, y):
    """ICJ verdict (left) and the Anthropic listing (right)."""
    rule(d, y, 2)
    y += 14
    col_w = 452
    lx, rx = MARGIN, 536
    d.line([512, y, 512, y + 196], fill=(170, 160, 144), width=1)

    kicker(d, "THE HAGUE · WORLD COURT", lx, y)
    scales_icon(d, lx + col_w - 40, y - 2)
    hy = story_headline(d, "MYANMAR GUILTY OF GENOCIDE", lx, y + 22, col_w - 96)
    body = ("The International Court of Justice ruled that Myanmar committed genocide "
            "against the Rohingya - the first time an international court has formally "
            "made such a finding over the military's campaign.")
    left_end = draw_text_block(d, body, font(SANS, 14), lx, hy + 6, col_w, 19)

    kicker(d, "MARKETS · NEW YORK", rx, y, fill=NAVY)
    hy = story_headline(d, "ANTHROPIC'S RECORD DEBUT", rx, y + 22, col_w)
    body = ("Anthropic became the first \"pure-play\" AI company to go public, in a "
            "record-breaking listing. Shares leapt in a record debut as investors "
            "scrambled for a piece of the artificial-intelligence boom.")
    by = draw_text_block(d, body, font(SANS, 14), rx, hy + 6, col_w, 19)
    chart_icon(d, rx + 6, by + 8, 180, 38)
    d.text((rx + 200, by + 20), "FIRST PURE-PLAY AI LISTING", font=font(SANS_B, 12), fill=GREEN)
    return max(left_end, by + 50)


def band_two(d, y):
    """COP31 fallout (left) and the Crimea bridge (right)."""
    rule(d, y, 2)
    y += 14
    col_w = 452
    lx, rx = MARGIN, 536
    d.line([512, y, 512, y + 182], fill=(170, 160, 144), width=1)

    kicker(d, "CLIMATE · COP31", lx, y)
    stacks_icon(d, lx + col_w - 76, y - 4)
    hy = story_headline(d, "FOSSIL-FUEL WORDS VANISH FROM DRAFT", lx, y + 22, col_w - 88, start=30)
    body = ("Uproar at the COP31 climate talks as the latest draft text quietly drops "
            "any mention of a fossil-fuel phase-out. What the draft once promised:")
    by = draw_text_block(d, body, font(SANS, 14), lx, hy + 6, col_w, 19)
    f_del = font(SERIF_B, 19)
    gone = "\"fossil-fuel phase-out\""
    d.text((lx + 8, by + 6), gone, font=f_del, fill=GRAY)
    gw = d.textlength(gone, font=f_del)
    d.line([lx + 4, by + 18, lx + 12 + gw, by + 18], fill=RED, width=3)
    d.text((lx + 20 + gw, by + 6), "- deleted.", font=font(SERIF, 19), fill=RED)
    left_end = by + 34

    kicker(d, "UKRAINE WAR", rx, y)
    hy = story_headline(d, "CRIMEA BRIDGE HIT AGAIN", rx, y + 22, col_w, one_line_floor=25)
    body = ("Ukraine struck the Crimea bridge for the third time this week, leaving "
            "part of the span collapsed. European leaders say they are now ready to "
            "talk with Russia to end the war.")
    by = draw_text_block(d, body, font(SANS, 14), rx, hy + 6, col_w, 19)
    bridge_icon(d, rx + 4, by + 10, col_w - 12)
    return max(left_end, by + 58)


# ------------------------------------------------------------ bottom strip

def voyager_strip(d, y):
    d.rectangle([MARGIN, y, RIGHT, y + 52], fill=(13, 22, 44))
    rng = random.Random(20261120)
    for _ in range(70):
        sx = rng.randint(MARGIN + 6, RIGHT - 6)
        sy = rng.randint(y + 4, y + 48)
        r = rng.choice([1, 1, 1, 2])
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(235, 238, 250))
    # the probe: dish, body, long boom
    px, py = 74, y + 26
    d.ellipse([px - 13, py - 13, px + 13, py + 13], outline=(240, 240, 245), width=3)
    d.polygon([(px + 10, py), (px + 36, py - 8), (px + 36, py + 8)], fill=(200, 170, 90))
    d.line([px + 36, py, px + 82, py], fill=(240, 240, 245), width=2)
    d.ellipse([px + 80, py - 3, px + 86, py + 3], fill=(240, 240, 245))
    f = fit_font(d, "VOYAGER 1 CALLS HOME FROM ONE LIGHT-DAY AWAY", SANS_B, 720, 21)
    d.text((178, y + 5), "VOYAGER 1 CALLS HOME FROM ONE LIGHT-DAY AWAY",
           font=f, fill=(255, 255, 255))
    d.text((178, y + 31),
           "NASA's farthest probe, launched 49 years ago, radios back across a full "
           "light-day of empty space.",
           font=font(SANS, 12), fill=(190, 200, 225))


def build_image():
    img = Image.new("RGB", (W, W), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    y = headline_story(d)
    y = band_one(d, y + 6)
    y = band_two(d, y + 6)
    voyager_strip(d, y + 8)
    d.text((MARGIN, W - 21),
           "Set in type by an AI agent · Sources: BBC, France 24, Le Monde, AP and agency reports",
           font=font(SANS, 11), fill=GRAY)
    return img


if __name__ == "__main__":
    build_image().save("entry.png")
