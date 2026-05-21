#!/usr/bin/env python3
"""
Three circular CMYK color wheels: Tint / Tone / Shade
Single A3 landscape SVG (420×297mm) — Illustrator-ready
"""
import math, svgwrite, os

W, H = 420, 297
OUT = "/home/user/wendy/svg_manual/00_三类色相环_圆形.svg"

# ── 12 standard color hues ────────────────────────────────────────────────
COLORS = [
    ("红",   "Red",        0,100,100, 0),
    ("红橙", "R-Orange",   0, 70,100, 0),
    ("橙",   "Orange",     0, 50,100, 0),
    ("黄橙", "Y-Orange",   0, 30,100, 0),
    ("黄",   "Yellow",     0,  0,100, 0),
    ("黄绿", "Y-Green",   40,  0,100, 0),
    ("绿",   "Green",    100,  0,100, 0),
    ("蓝绿", "B-Green",  100,  0, 40, 0),
    ("蓝",   "Blue",     100, 60,  0, 0),
    ("蓝紫", "B-Violet",  80, 80,  0, 0),
    ("紫",   "Violet",    60,100,  0, 0),
    ("红紫", "R-Violet",  20,100, 20, 0),
]

# ── helpers ───────────────────────────────────────────────────────────────
def cmyk_hex(c, m, y, k):
    r = max(0, min(255, int(255*(1-c/100)*(1-k/100))))
    g = max(0, min(255, int(255*(1-m/100)*(1-k/100))))
    b = max(0, min(255, int(255*(1-y/100)*(1-k/100))))
    return f"#{r:02X}{g:02X}{b:02X}"

def lum(hx):
    h = hx.lstrip('#')
    r,g,b = int(h[:2],16)/255, int(h[2:4],16)/255, int(h[4:],16)/255
    return 0.299*r + 0.587*g + 0.114*b

def arc_path(cx, cy, r1, r2, a1_deg, a2_deg):
    a1 = math.radians(a1_deg - 90)
    a2 = math.radians(a2_deg - 90)
    la = 1 if (a2_deg - a1_deg) > 180 else 0
    ox1,oy1 = cx+r2*math.cos(a1), cy+r2*math.sin(a1)
    ox2,oy2 = cx+r2*math.cos(a2), cy+r2*math.sin(a2)
    ix1,iy1 = cx+r1*math.cos(a2), cy+r1*math.sin(a2)
    ix2,iy2 = cx+r1*math.cos(a1), cy+r1*math.sin(a1)
    return (f"M{ox1:.3f},{oy1:.3f} "
            f"A{r2},{r2} 0 {la} 1 {ox2:.3f},{oy2:.3f} "
            f"L{ix1:.3f},{iy1:.3f} "
            f"A{r1},{r1} 0 {la} 0 {ix2:.3f},{iy2:.3f} Z")

def mix_cmyk(c, m, y, k, wheel, level):
    """
    level: 0=pure, 1=light mix, 2=medium mix, 3=heavy mix
    tint:  mix with white → reduce CMY proportionally
    tone:  mix with gray  → raise K by moderate amounts
    shade: mix with black → raise K by larger amounts
    """
    if wheel == 'tint':
        pcts = [0, 30, 55, 75]
        f = 1 - pcts[level]/100
        return round(c*f), round(m*f), round(y*f), k
    elif wheel == 'tone':
        k_adds = [0, 18, 35, 50]
        return c, m, y, min(100, k + k_adds[level])
    else:  # shade
        k_adds = [0, 25, 50, 70]
        return c, m, y, min(100, k + k_adds[level])

def txt(dwg, content, x, y, fs, fill, font, weight="normal", anchor="start"):
    return dwg.text(content, insert=(x, y),
                    text_anchor=anchor,
                    style=f"font-size:{fs}mm;font-family:{font};"
                          f"font-weight:{weight};fill:{fill};")

# ── draw one wheel ────────────────────────────────────────────────────────
RING_LEVELS = [
    (50, 38, 0),   # outer  ring → pure / 0 % mix
    (37, 27, 1),   # ring 2 → light mix
    (26, 17, 2),   # ring 3 → medium mix
    (16,  9, 3),   # inner  ring → heavy mix
]

def draw_wheel(dwg, g, cx, cy, wheel_type, label, center_color, legend_box):
    n = 12
    seg = 360 / n

    # ── rings ─────────────────────────────────────────────────────────
    for ci, (cname, ename, c, m, y, k) in enumerate(COLORS):
        a1 = ci * seg
        a2 = a1 + seg
        for r2, r1, lvl in RING_LEVELS:
            rc,rm,ry,rk = mix_cmyk(c, m, y, k, wheel_type, lvl)
            fill = cmyk_hex(rc, rm, ry, rk)
            g.add(dwg.path(d=arc_path(cx, cy, r1, r2, a1, a2),
                           fill=fill,
                           stroke="#FFFFFF", stroke_width=0.45))

    # ── outer gap ring (thin white ring) ──────────────────────────────
    g.add(dwg.circle(center=(cx, cy), r=51.2,
                     fill="none", stroke="#FFFFFF", stroke_width=0.5))

    # ── center dot ────────────────────────────────────────────────────
    g.add(dwg.circle(center=(cx, cy), r=8.8,
                     fill=center_color,
                     stroke="#DDDDDD", stroke_width=0.5))
    # center label
    lbl_col = "#FFFFFF" if lum(center_color) < 0.5 else "#333333"
    g.add(txt(dwg, label.split('\n')[0], cx, cy+1.5,
              2.8, lbl_col, "SimHei,sans-serif", anchor="middle"))

    # ── outer ring: color names ────────────────────────────────────────
    r_name = 44  # midpoint of outer ring (50+38)/2 = 44
    for ci, (cname, ename, c, m, y, k) in enumerate(COLORS):
        mid_a  = math.radians((ci + 0.5) * seg - 90)
        lx = cx + r_name * math.cos(mid_a)
        ly = cy + r_name * math.sin(mid_a) + 1.2  # +vertical offset for center align

        fill = cmyk_hex(c, m, y, k)
        txt_col = "#FFFFFF" if lum(fill) < 0.55 else "#111111"
        g.add(txt(dwg, cname, lx, ly,
                  3.2, txt_col, "SimHei,sans-serif",
                  weight="bold", anchor="middle"))

    # ── label wheel type / title ───────────────────────────────────────
    # Title inside bottom of wheel
    titles = {'tint':'混白淡色调\nTint', 'tone':'混灰浊色调\nTone', 'shade':'混黑暗色调\nShade'}
    g.add(txt(dwg, titles[wheel_type].split('\n')[0], cx, cy+62,
              4.2, "#333333", "SimHei,sans-serif", weight="bold", anchor="middle"))
    g.add(txt(dwg, titles[wheel_type].split('\n')[1], cx, cy+67.5,
              3.2, "#888888", "Arial,sans-serif", anchor="middle"))

    # ── ring level legend (small indicators) ──────────────────────────
    keys = {
        'tint':  ["纯色", "浅 30%", "浅 55%", "浅 75%"],
        'tone':  ["纯色", "+K18", "+K35", "+K50"],
        'shade': ["纯色", "+K25", "+K50", "+K70"],
    }[wheel_type]
    ring_label_r = [44, 32, 21.5, 12.5]  # mid-radius of each ring
    # place at 3 o'clock position (angle=0 from right)
    angle_legend = math.radians(0)   # pointing right
    for li, (key, rl) in enumerate(zip(keys, ring_label_r)):
        lx = cx + rl * math.cos(angle_legend)
        ly = cy + rl * math.sin(angle_legend)
        # small dot + label
        pass  # handled in table below

    return keys   # return for use in legend


# ── CMYK reference table ──────────────────────────────────────────────────
def draw_cmyk_table(dwg, g, y_top, wheels_keys):
    """
    Three column groups (tint/tone/shade), 12 rows for 12 colors.
    Layout: 6 colors per side (left half, right half).
    """
    COL_W  = 140        # mm per wheel column group
    ROW_H  = 8.6        # mm
    SWS    = 5.5        # swatch size (mm)
    MARGIN = 2

    wheel_info = [
        ('tint',  '混白淡色调 Tint',  "#2A5A8A", [0,1,2,3]),
        ('tone',  '混灰浊色调 Tone',  "#4A6A3A", [0,1,2,3]),
        ('shade', '混黑暗色调 Shade', "#6A3A2A", [0,1,2,3]),
    ]

    # header
    for wi, (wt, wlabel, wcolor, lvls) in enumerate(wheel_info):
        bx = MARGIN + wi*COL_W
        g.add(dwg.rect(insert=(bx, y_top), size=(COL_W-1, 6),
                       fill=wcolor, rx=1))
        g.add(txt(dwg, wlabel, bx + COL_W/2, y_top+4.3,
                  3.5, "#FFFFFF", "SimHei,sans-serif",
                  weight="bold", anchor="middle"))

    # sub-header: ring levels
    sub_y = y_top + 6.8
    for wi, (wt, _, wcolor, _) in enumerate(wheel_info):
        bx = MARGIN + wi*COL_W
        g.add(dwg.rect(insert=(bx, sub_y), size=(COL_W-1, 5.5),
                       fill="#F0EDE6", rx=0))
        keys = wheels_keys[wt]
        sub_col_w = (COL_W-1-8) / 4  # 4 swatches per wheel
        # show ring level labels
        for li, key in enumerate(keys):
            lx = bx + 8 + li*sub_col_w + sub_col_w/2
            g.add(txt(dwg, key, lx, sub_y+4.0,
                      2.5, "#666", "SimHei,sans-serif", anchor="middle"))

    data_y = sub_y + 6.5

    # data rows: 12 colors, arranged 6+6 in two halves vertically
    for ci, (cname, ename, c, m, y, k) in enumerate(COLORS):
        # split: 6 per column group...
        # Actually: 12 rows under each wheel column
        if ci < 6:
            row_y = data_y + ci * ROW_H
        else:
            row_y = data_y + (ci-6) * ROW_H
            # put col 7-12 to the right... but we have 3 wheel columns
            # Let me just do 12 rows under each wheel column
            pass

    # Simpler: 12 rows, full width, one per color
    # Each row has 3 column groups (tint/tone/shade), each showing 4 swatches

    for ci, (cname, ename, c, m, y, k) in enumerate(COLORS):
        row_y = data_y + ci * ROW_H
        bg = "#F8F6F0" if ci%2==0 else "#FDFBF7"
        g.add(dwg.rect(insert=(MARGIN, row_y), size=(W-MARGIN*2, ROW_H-0.3),
                       fill=bg))

        # color name label (left side)
        g.add(txt(dwg, cname, MARGIN+2, row_y+ROW_H*0.68,
                  3.4, "#222222", "SimHei,sans-serif", weight="bold"))
        g.add(txt(dwg, f"C{c} M{m} Y{y} K{k}", MARGIN+11, row_y+ROW_H*0.68,
                  2.6, "#666", "Arial,sans-serif"))

        # 3 wheel groups
        for wi, (wt, _, wcolor, _) in enumerate(wheel_info):
            gx = MARGIN + 60 + wi * ((W-62-MARGIN*2)/3)
            sub_col_w = ((W-62-MARGIN*2)/3 - 2) / 4

            for li in range(4):
                rc,rm,ry2,rk = mix_cmyk(c, m, y, k, wt, li)
                fx = cmyk_hex(rc, rm, ry2, rk)
                sx = gx + li*sub_col_w + (sub_col_w-SWS)/2
                sy = row_y + (ROW_H-SWS)/2

                g.add(dwg.rect(insert=(sx, sy), size=(SWS, SWS),
                               fill=fx, rx=0.8,
                               stroke="#BBBBBB", stroke_width=0.2))

                # CMYK value under swatch (very small)
                cmyk_s = f"C{rc}M{rm}\nY{ry2}K{rk}"
                # too small to show all, just hover

    # divider line
    g.add(dwg.line(start=(MARGIN, data_y-0.5), end=(W-MARGIN, data_y-0.5),
                   stroke="#CCCCCC", stroke_width=0.4))


# ── full page ─────────────────────────────────────────────────────────────
def make_svg():
    dwg = svgwrite.Drawing(OUT, size=(f"{W}mm", f"{H}mm"),
                           viewBox=f"0 0 {W} {H}", profile="full")
    g = dwg.g(id="page")

    # background
    g.add(dwg.rect(insert=(0,0), size=(W,H), fill="#F7F5F0"))

    # ── header ────────────────────────────────────────────────────────
    g.add(dwg.rect(insert=(0,0), size=(W,13.5), fill="#161616"))
    g.add(dwg.rect(insert=(0,13.5), size=(W,0.6), fill="#E8C86A"))
    g.add(txt(dwg, "三类色相环  ·  纯色混白 · 混灰 · 混黑  ·  CMYK 色值完整标注",
              W/2, 9.5, 5.5, "#F5EFD0", "SimHei,sans-serif",
              weight="bold", anchor="middle"))
    g.add(txt(dwg, "Color Wheel Tint · Tone · Shade  ·  12 Hue Segments × 4 Mix Levels  ·  CMYK Print Reference",
              W/2, 13.0, 2.8, "#A09880", "Arial,sans-serif", anchor="middle"))

    # ── three wheels ──────────────────────────────────────────────────
    CENTERS = [(75, 103), (210, 103), (345, 103)]
    WHEEL_CONFIGS = [
        ('tint',  '混白\nTint',   "#FFFFFF"),
        ('tone',  '混灰\nTone',   "#808080"),
        ('shade', '混黑\nShade',  "#111111"),
    ]

    wheels_keys = {}
    for (cx, cy), (wt, wlabel, wc) in zip(CENTERS, WHEEL_CONFIGS):
        sub_g = dwg.g(id=f"wheel_{wt}")
        keys = draw_wheel(dwg, sub_g, cx, cy, wt, wlabel, wc, None)
        wheels_keys[wt] = keys
        g.add(sub_g)

    # ── ring level legend (between wheels and table) ───────────────────
    legend_y = 174
    g.add(dwg.rect(insert=(0, legend_y), size=(W, 0.5), fill="#C8C3BA"))
    legend_items = [
        ("■ 纯色 / Pure  (Ring 1)", "#555"),
        ("■ 轻混 / Light Mix (Ring 2)", "#777"),
        ("■ 中混 / Medium Mix (Ring 3)", "#999"),
        ("■ 重混 / Heavy Mix (Ring 4, innermost)", "#BBB"),
    ]
    for li, (txt_lbl, col) in enumerate(legend_items):
        g.add(txt(dwg, txt_lbl, 8 + li*107, legend_y+6,
                  3.0, col, "SimHei,sans-serif"))
    g.add(txt(dwg, "由外向内：色相越混越接近 白色 / 灰色 / 黑色",
              W-6, legend_y+6, 3.0, "#888", "SimHei,sans-serif", anchor="end"))

    # ── CMYK table ────────────────────────────────────────────────────
    draw_cmyk_table(dwg, g, 183, wheels_keys)

    # ── footer ────────────────────────────────────────────────────────
    g.add(dwg.rect(insert=(0, H-5.5), size=(W, 5.5), fill="#E5E2DB"))
    g.add(dwg.line(start=(0,H-5.5), end=(W,H-5.5), stroke="#C0BBB2", stroke_width=0.3))
    g.add(txt(dwg, "色相环 / Color Wheel  ·  CMYK印刷四色标准  ·  Tint=混白淡色调  Tone=混灰浊色调  Shade=混黑暗色调",
              5, H-1.8, 2.6, "#888", "SimHei,sans-serif"))
    g.add(txt(dwg, f"A3 {W}×{H}mm  ·  Adobe Illustrator SVG",
              W-5, H-1.8, 2.5, "#AAA", "Arial,sans-serif", anchor="end"))

    dwg.add(g)
    dwg.save()
    print(f"✓ {OUT}")


if __name__ == "__main__":
    make_svg()
