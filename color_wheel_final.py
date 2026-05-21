#!/usr/bin/env python3
"""
Three circular CMYK color wheels:
  Tint (混白) · Tone (混灰) · Shade (混黑)
A3 landscape 420×297mm — Illustrator-ready SVG
"""
import math, svgwrite, os

W, H   = 420, 297
OUTDIR = "/home/user/wendy/svg_manual"
os.makedirs(OUTDIR, exist_ok=True)
OUT    = f"{OUTDIR}/00_三类色相环_圆形.svg"

# ─── 12 hues ────────────────────────────────────────────────────────────────
COLORS = [
    ("红",   "Red",       0, 100, 100,  0),
    ("红橙", "R-Orange",  0,  70, 100,  0),
    ("橙",   "Orange",    0,  50, 100,  0),
    ("黄橙", "Y-Orange",  0,  30, 100,  0),
    ("黄",   "Yellow",    0,   0, 100,  0),
    ("黄绿", "Y-Green",  40,   0, 100,  0),
    ("绿",   "Green",   100,   0, 100,  0),
    ("蓝绿", "B-Green", 100,   0,  40,  0),
    ("蓝",   "Blue",    100,  60,   0,  0),
    ("蓝紫", "B-Violet", 80,  80,   0,  0),
    ("紫",   "Violet",   60, 100,   0,  0),
    ("红紫", "R-Violet", 20, 100,  20,  0),
]

# ─── colour math ─────────────────────────────────────────────────────────────
def cmyk_hex(c, m, y, k):
    r = max(0, min(255, int(255*(1-c/100)*(1-k/100))))
    g = max(0, min(255, int(255*(1-m/100)*(1-k/100))))
    b = max(0, min(255, int(255*(1-y/100)*(1-k/100))))
    return f"#{r:02X}{g:02X}{b:02X}"

def lum(hx):
    h = hx.lstrip('#')
    r,g,b = int(h[:2],16)/255, int(h[2:4],16)/255, int(h[4:],16)/255
    return 0.299*r + 0.587*g + 0.114*b

def apply_mix(c, m, y, k, wtype, level):
    """
    level 0 = pure, 1 = light, 2 = medium, 3 = heavy
    tint  → reduce CMY  (add white)
    tone  → raise K by mod amounts  (add gray)
    shade → raise K by large amounts (add black)
    """
    if wtype == 'tint':
        factors = [1.0, 0.70, 0.45, 0.22]
        f = factors[level]
        return round(c*f), round(m*f), round(y*f), k
    elif wtype == 'tone':
        k_adds = [0, 18, 36, 52]
        return c, m, y, min(100, k + k_adds[level])
    else:                      # shade
        k_adds = [0, 27, 52, 72]
        return c, m, y, min(100, k + k_adds[level])

# ─── SVG primitives ──────────────────────────────────────────────────────────
def arc_path(cx, cy, r1, r2, a1_deg, a2_deg):
    a1  = math.radians(a1_deg - 90)
    a2  = math.radians(a2_deg - 90)
    la  = 1 if (a2_deg - a1_deg) > 180 else 0
    ox1 = cx + r2*math.cos(a1);  oy1 = cy + r2*math.sin(a1)
    ox2 = cx + r2*math.cos(a2);  oy2 = cy + r2*math.sin(a2)
    ix1 = cx + r1*math.cos(a2);  iy1 = cy + r1*math.sin(a2)
    ix2 = cx + r1*math.cos(a1);  iy2 = cy + r1*math.sin(a1)
    return (f"M{ox1:.2f},{oy1:.2f} "
            f"A{r2},{r2} 0 {la} 1 {ox2:.2f},{oy2:.2f} "
            f"L{ix1:.2f},{iy1:.2f} "
            f"A{r1},{r1} 0 {la} 0 {ix2:.2f},{iy2:.2f} Z")

def T(dwg, s, x, y, fs, fill, font, weight="normal", anchor="start", italic=False):
    style = (f"font-size:{fs}mm;font-family:{font};"
             f"font-weight:{weight};fill:{fill};"
             + ("font-style:italic;" if italic else ""))
    return dwg.text(s, insert=(x, y), text_anchor=anchor, style=style)

def R(dwg, x, y, w, h, fill, stroke="none", sw=0.3, rx=0):
    kw = dict(fill=fill, stroke=stroke, stroke_width=sw)
    if rx: kw['rx'] = rx
    return dwg.rect(insert=(x, y), size=(w, h), **kw)

def L(dwg, x1, y1, x2, y2, stroke="#CCC", sw=0.3):
    return dwg.line(start=(x1,y1), end=(x2,y2), stroke=stroke, stroke_width=sw)

# ─── wheel drawing ────────────────────────────────────────────────────────────
# Ring layout (outer → inner)  [r_outer, r_inner, mix_level]
RINGS = [(52, 40, 0), (39, 29, 1), (28, 18, 2), (17, 9, 3)]

def draw_wheel(dwg, g, cx, cy, wtype, center_hex, spoke_color):
    n_seg  = len(COLORS)
    seg_dg = 360 / n_seg        # 30°

    # ── draw all ring segments ──
    for ci, (_n, _e, c, m, y, k) in enumerate(COLORS):
        a1 = ci * seg_dg
        a2 = a1 + seg_dg
        for r2, r1, lvl in RINGS:
            rc, rm, ry, rk = apply_mix(c, m, y, k, wtype, lvl)
            g.add(dwg.path(d=arc_path(cx, cy, r1, r2, a1, a2),
                           fill=cmyk_hex(rc, rm, ry, rk),
                           stroke="#FFFFFF", stroke_width=0.55))

    # ── thin separator circle at outer edge ──
    g.add(dwg.circle(center=(cx, cy), r=52.3,
                     fill="none", stroke="#FFFFFF", stroke_width=0.6))

    # ── center circle ──
    g.add(dwg.circle(center=(cx, cy), r=8.5, fill=center_hex,
                     stroke="#DDDDDD", stroke_width=0.5))
    lc = "#FFF" if lum(center_hex) < 0.5 else "#333"
    g.add(T(dwg, "●", cx, cy+2, 3.0, lc, "Arial", anchor="middle"))

    # ── color name inside outer ring ──
    for ci, (cname, _e, c, m, y, k) in enumerate(COLORS):
        mid_r = math.radians((ci + 0.5)*seg_dg - 90)
        r_mid = 46        # midpoint of outer ring (52+40)/2
        lx = cx + r_mid * math.cos(mid_r)
        ly = cy + r_mid * math.sin(mid_r) + 1.3
        fill = cmyk_hex(c, m, y, k)
        tc = "#FFF" if lum(fill) < 0.52 else "#111"
        g.add(T(dwg, cname, lx, ly, 3.4, tc, "SimHei,sans-serif",
                weight="bold", anchor="middle"))

    # ── spoke labels: color name + pure CMYK ──
    #  spokes extend from r=56 to r=73  (outside outer ring)
    for ci, (cname, _e, c, m, y, k) in enumerate(COLORS):
        mid_deg = (ci + 0.5)*seg_dg
        mid_r   = math.radians(mid_deg - 90)

        # spoke line
        sx1 = cx + 53 * math.cos(mid_r);  sy1 = cy + 53 * math.sin(mid_r)
        sx2 = cx + 60 * math.cos(mid_r);  sy2 = cy + 60 * math.sin(mid_r)
        g.add(L(dwg, sx1, sy1, sx2, sy2, stroke=spoke_color, sw=0.35))

        # label dot
        g.add(dwg.circle(center=(sx2, sy2), r=0.7, fill=spoke_color))

        # label position
        lx = cx + 63.5 * math.cos(mid_r)
        ly = cy + 63.5 * math.sin(mid_r)

        # angle-aware anchor + offset
        if -30 < mid_deg < 30 or mid_deg > 330:
            anchor = "middle"; ly -= 1.5          # top
        elif 150 < mid_deg < 210:
            anchor = "middle"; ly += 4.5          # bottom
        elif mid_deg <= 180:
            anchor = "start"                       # right half
        else:
            anchor = "end"                         # left half

        # color name label on spoke
        g.add(T(dwg, cname, lx, ly, 3.4, "#1A1A1A", "SimHei,sans-serif",
                weight="bold", anchor=anchor))
        # CMYK value (2nd line) – only for hues that fit (mid 4 on each side)
        show_cmyk = not (60 <= mid_deg <= 120 or 240 <= mid_deg <= 300)  # skip tight top/bottom corners
        if show_cmyk:
            cmyk_str = f"C{c} M{m} Y{y} K{k}"
            g.add(T(dwg, cmyk_str, lx, ly+4.0, 2.3, "#666666", "Arial,sans-serif",
                    anchor=anchor))


# ─── page composer ───────────────────────────────────────────────────────────
def make_page():
    dwg = svgwrite.Drawing(OUT, size=(f"{W}mm", f"{H}mm"),
                           viewBox=f"0 0 {W} {H}", profile="full")
    g = dwg.g(id="root")

    # background
    g.add(R(dwg, 0, 0, W, H, "#F6F4EF"))

    # ── page header ──────────────────────────────────────────────────────
    g.add(R(dwg, 0, 0, W, 13.5, "#161616"))
    g.add(R(dwg, 0, 13.5, W, 0.7, "#E8C86A"))
    g.add(T(dwg, "三类色相环  ·  纯色混白（Tint）· 混灰（Tone）· 混黑（Shade）  ·  CMYK 色值完整标注",
            W/2, 9.3, 5.5, "#F5EFD0", "SimHei,sans-serif",
            weight="bold", anchor="middle"))
    g.add(T(dwg, "Color Wheel Series  ·  12 Hues × 4 Mix Levels  ·  CMYK Print Reference  ·  A3 420×297mm",
            W/2, 13.0, 2.8, "#9A9080", "Arial,sans-serif", anchor="middle"))

    # ── wheel column headers ──────────────────────────────────────────────
    WH_CENTERS = [(82, 104), (210, 104), (338, 104)]
    WH_CFG = [
        ('tint',  "混白淡色调  Tint",   "#FFFFFF", "#2A558A", "#1A4070"),
        ('tone',  "混灰浊色调  Tone",   "#808080", "#3A6A3A", "#2A5028"),
        ('shade', "混黑暗色调  Shade",  "#181818", "#7A3A1A", "#5A2A10"),
    ]

    for (cx, cy), (wt, wlabel, wcenter, hcol, dcol) in zip(WH_CENTERS, WH_CFG):
        # column background strip
        g.add(R(dwg, cx-73, 14.8, 146, 7.0, hcol, rx=1.5))
        g.add(T(dwg, wlabel, cx, 20.2, 4.5, "#FFFFFF", "SimHei,sans-serif",
                weight="bold", anchor="middle"))

        # ring level legend strip
        leg_y = 15.5
        lvl_labels = {
            'tint':  ["纯色/Pure", "混白30%", "混白55%", "混白75%"],
            'tone':  ["纯色/Pure", "+K18 灰", "+K36 灰", "+K52 灰"],
            'shade': ["纯色/Pure", "+K27 黑", "+K52 黑", "+K72 黑"],
        }[wt]
        lring_r = [46, 34, 23, 13]   # visual mid-radius of each ring
        pass  # ring label handled by outer ring text and legend strip

        # wheel
        wg = dwg.g(id=f"w_{wt}")
        draw_wheel(dwg, wg, cx, cy, wt, wcenter, dcol)
        g.add(wg)

        # Ring legend (bottom of wheel)
        ly_leg = cy + 58
        ring_info = {
            'tint':  [("纯色","Pure",0),("混白30%","Tint30",1),("混白55%","Tint55",2),("混白75%","Tint75",3)],
            'tone':  [("纯色","Pure",0),("+K18","Tone",1),("+K36","Tone",2),("+K52","Tone",3)],
            'shade': [("纯色","Pure",0),("+K27","Shade",1),("+K52","Shade",2),("+K72","Shade",3)],
        }[wt]
        swatch_w = 12; gap = 3.5
        total_w = 4*swatch_w + 3*gap
        sx0 = cx - total_w/2
        g.add(T(dwg, "由外向内", cx, ly_leg-1, 2.8, "#666", "SimHei,sans-serif", anchor="middle"))
        for ri, (rl_zh, rl_en, lvl) in enumerate(ring_info):
            sx = sx0 + ri*(swatch_w+gap)
            # sample swatch using "红"
            c,m,y,k = 0,100,100,0
            rc,rm,ry,rk = apply_mix(c,m,y,k, wt, lvl)
            g.add(R(dwg, sx, ly_leg+1.5, swatch_w, 5, cmyk_hex(rc,rm,ry,rk), rx=0.8))
            g.add(T(dwg, rl_zh, sx+swatch_w/2, ly_leg+10, 2.5, "#555",
                    "SimHei,sans-serif", anchor="middle"))

    # ── separator ────────────────────────────────────────────────────────────
    SEP_Y = 178
    g.add(R(dwg, 0, SEP_Y, W, 0.5, "#C8C3BA"))
    g.add(T(dwg, "CMYK 色值参考表  ·  12色相 × 纯色 / 混白50% / 混灰50% / 混黑50%  完整数值",
            W/2, SEP_Y+5.5, 3.5, "#333", "SimHei,sans-serif",
            weight="bold", anchor="middle"))

    # ── CMYK table ────────────────────────────────────────────────────────────
    TABLE_Y = SEP_Y + 8
    ROW_H   = 8.0
    # Column positions
    C_NAME  = 3           # color swatch+name col x
    C_PURE  = 30          # pure CMYK col x
    C_TINT  = 95          # tint 50% col x
    C_TONE  = 195         # tone 50% col x
    C_SHADE = 295         # shade 50% col x
    COL_WS  = [27, 65, 100, 100, 100]   # widths: name, pure, tint, tone, shade

    # table header row
    hdr_y = TABLE_Y
    g.add(R(dwg, C_NAME, hdr_y, W-6, 6.5, "#2A2A2A"))
    heads = [
        (C_NAME+2,    "色名 / Hue"),
        (C_PURE+2,    "纯色 Pure  (外环 Ring 1)"),
        (C_TINT+2,    "混白 Tint 55%  (Ring 3)"),
        (C_TONE+2,    "混灰 Tone +K36  (Ring 3)"),
        (C_SHADE+2,   "混黑 Shade +K52  (Ring 3)"),
    ]
    for hx, ht in heads:
        g.add(T(dwg, ht, hx, hdr_y+4.8, 2.8, "#F0EAD6",
                "SimHei,sans-serif", weight="bold"))

    # data rows
    for ri, (cname, ename, c, m, y, k) in enumerate(COLORS):
        ry = TABLE_Y + 7 + ri * ROW_H
        bg = "#F4F2EC" if ri%2==0 else "#FBFAF6"
        g.add(R(dwg, C_NAME, ry, W-6, ROW_H-0.3, bg))

        # color swatch (pure)
        pure_hex = cmyk_hex(c,m,y,k)
        g.add(R(dwg, C_NAME+1, ry+1.2, 5.5, ROW_H-2.7, pure_hex, rx=0.6))

        # color name
        g.add(T(dwg, cname, C_NAME+8, ry+ROW_H*0.65, 4.0, "#1A1A1A",
                "SimHei,sans-serif", weight="bold"))
        g.add(T(dwg, ename, C_NAME+8, ry+ROW_H*0.92, 2.5, "#888",
                "Arial,sans-serif"))

        # pure CMYK
        g.add(T(dwg, f"C{c}  M{m}  Y{y}  K{k}", C_PURE+1, ry+ROW_H*0.65,
                3.2, "#222", "Arial,sans-serif", weight="bold"))
        # CMYK color bars (C M Y K)
        for bi, (bv, bcol) in enumerate([(c,"#00AACC"),(m,"#EE2255"),(y,"#FFDD00"),(k,"#333333")]):
            bar_x = C_PURE + 1 + bi*14
            if bar_x + 12 > C_TINT - 2: break
            bar_h = max(0.5, bv/100 * 3.0)
            g.add(R(dwg, bar_x, ry+ROW_H-2.5, 11.5, bar_h, bcol, rx=0.3))

        # tint 50% (level 2)
        def cell(wt, lvl, col_x):
            rc,rm,ry2,rk = apply_mix(c,m,y,k, wt, lvl)
            fx = cmyk_hex(rc,rm,ry2,rk)
            g.add(R(dwg, col_x+1, ry+1.2, 5.5, ROW_H-2.7, fx, rx=0.6))
            g.add(T(dwg, f"C{rc}  M{rm}  Y{ry2}  K{rk}",
                    col_x+9, ry+ROW_H*0.65, 3.0, "#333", "Arial,sans-serif"))
            # show delta vs pure
            if wt == 'tint':
                delta = f"↓CMY×{int((1-[1,.7,.45,.22][lvl])*100)}%"
            elif wt in ('tone','shade'):
                kd = rk - k
                delta = f"+K{kd}" if kd else "—"
            g.add(T(dwg, delta, col_x+9, ry+ROW_H*0.90, 2.3, "#999",
                    "Arial,sans-serif", italic=True))

        cell('tint',  2, C_TINT)
        cell('tone',  2, C_TONE)
        cell('shade', 2, C_SHADE)

        # row divider
        g.add(L(dwg, C_NAME, ry+ROW_H-0.2, W-3, ry+ROW_H-0.2, "#DEDAD3"))

    # column dividers in table
    for divx in [C_PURE-1, C_TINT-1, C_TONE-1, C_SHADE-1]:
        g.add(L(dwg, divx, TABLE_Y, divx, TABLE_Y+7+12*ROW_H, "#DEDAD3"))

    # ── footer ────────────────────────────────────────────────────────────────
    g.add(R(dwg, 0, H-5.5, W, 5.5, "#E5E2DB"))
    g.add(L(dwg, 0, H-5.5, W, H-5.5, "#C0BBB2", 0.3))
    g.add(T(dwg,
            "色相环 / Color Wheel  ·  Tint=纯色+白  Tone=纯色+灰  Shade=纯色+黑  ·  "
            "CMYK值基于 ISO 12647 印刷四色标准  ·  色相自红(0°)顺时针排列至红紫(330°)",
            5, H-1.7, 2.6, "#888", "SimHei,sans-serif"))
    g.add(T(dwg, f"A3 {W}×{H}mm  ·  Adobe Illustrator SVG",
            W-4, H-1.7, 2.5, "#AAA", "Arial,sans-serif", anchor="end"))

    dwg.add(g)
    dwg.save()
    sz = os.path.getsize(OUT)//1024
    print(f"✓  {OUT}  ({sz} KB)")


if __name__ == "__main__":
    make_page()
