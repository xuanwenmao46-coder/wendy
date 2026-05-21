#!/usr/bin/env python3
"""Typography Design Manual Generator - A3 Landscape PPTX"""

import math
from pptx import Presentation
from pptx.util import Inches, Pt, Emu, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import pptx.oxml.ns as ns
from lxml import etree

# A3 landscape: 420mm x 297mm
A3_W = Cm(42.0)
A3_H = Cm(29.7)

def new_prs():
    prs = Presentation()
    prs.slide_width = A3_W
    prs.slide_height = A3_H
    return prs

def add_slide(prs):
    blank = prs.slide_layouts[6]  # blank layout
    return prs.slides.add_slide(blank)

def rgb(r, g, b):
    return RGBColor(r, g, b)

def add_rect(slide, x, y, w, h, fill_rgb=None, line_rgb=None, line_width=Pt(0.5)):
    shape = slide.shapes.add_shape(1, x, y, w, h)  # MSO_SHAPE_TYPE.RECTANGLE = 1
    if fill_rgb:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_rgb
    else:
        shape.fill.background()
    if line_rgb:
        shape.line.color.rgb = line_rgb
        shape.line.width = line_width
    else:
        shape.line.fill.background()
    return shape

def add_textbox(slide, x, y, w, h, text, font_size=Pt(10), bold=False, color=rgb(0,0,0),
                align=PP_ALIGN.LEFT, font_name="Arial", italic=False):
    txBox = slide.shapes.add_textbox(x, y, w, h)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = font_size
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = font_name
    return txBox

def add_multiline_textbox(slide, x, y, w, h, lines, font_size=Pt(10), bold=False,
                           color=rgb(0,0,0), align=PP_ALIGN.LEFT, font_name="Arial",
                           line_spacing=None):
    from pptx.oxml.ns import qn
    from pptx.util import Pt as PPt
    txBox = slide.shapes.add_textbox(x, y, w, h)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.alignment = align
        if line_spacing:
            p.line_spacing = line_spacing
        run = p.add_run()
        run.text = line
        run.font.size = font_size
        run.font.bold = bold
        run.font.color.rgb = color
        run.font.name = font_name
    return txBox

# ─── Color utilities ────────────────────────────────────────────────────────

def cmyk_to_rgb(c, m, y, k):
    r = int(255 * (1 - c/100) * (1 - k/100))
    g = int(255 * (1 - m/100) * (1 - k/100))
    b = int(255 * (1 - y/100) * (1 - k/100))
    return rgb(r, g, b)

def hue_to_rgb_color(hue_deg):
    """Pure hue → RGB (saturation=1, value=1 HSV)"""
    import colorsys
    h = hue_deg / 360.0
    r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    return rgb(int(r*255), int(g*255), int(b*255))

def draw_color_wheel(slide, cx, cy, outer_r, inner_r, n_segments,
                     mix_func, title, label_fn, slide_w):
    """Draw a segmented color ring with labels."""
    import math
    from pptx.util import Emu

    segment_angle = 360.0 / n_segments
    # Draw each segment as a thin rectangle rotated (approximate with many tiny rects)
    # We draw fan-shaped segments via many narrow rectangles or just colored squares arranged in ring

    # Use a simpler grid-free approach: draw n_segments colored wedge-shapes
    # python-pptx doesn't support pie segments natively; use narrow rectangles arranged radially
    seg_w = Cm(0.55)
    seg_h = outer_r - inner_r

    for i in range(n_segments):
        angle = segment_angle * i - 90  # start from top
        mid_r = inner_r + seg_h / 2
        angle_rad = math.radians(angle)
        # center of this segment
        sx = cx + mid_r * math.cos(angle_rad) - seg_w / 2
        sy = cy + mid_r * math.sin(angle_rad) - seg_h / 2
        fill = mix_func(i, n_segments)
        rect = add_rect(slide, int(sx), int(sy), int(seg_w), int(seg_h), fill_rgb=fill)
        # rotate via XML
        sp = rect._element
        spPr = sp.find(ns.qn('p:spPr'))
        xfrm = spPr.find(ns.qn('a:xfrm'))
        xfrm.set('rot', str(int(angle * 60000)))  # EMU rotation units

    # Title
    add_textbox(slide, int(cx - Cm(2.5)), int(cy - Cm(1)), int(Cm(5)), int(Cm(0.7)),
                title, font_size=Pt(9), bold=True, color=rgb(50,50,50), align=PP_ALIGN.CENTER)


# ─── SLIDE 1: Cover ─────────────────────────────────────────────────────────

def slide_cover(prs):
    slide = add_slide(prs)
    # dark background
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(20, 20, 20))

    # decorative stripe
    add_rect(slide, 0, int(A3_H * 0.55), A3_W, int(A3_H * 0.01), fill_rgb=rgb(200, 160, 80))

    add_textbox(slide, Cm(3), Cm(5), Cm(30), Cm(4),
                "字体编排设计手册", font_size=Pt(54), bold=True,
                color=rgb(240, 220, 160), align=PP_ALIGN.LEFT, font_name="SimHei")
    add_textbox(slide, Cm(3), Cm(10), Cm(30), Cm(2),
                "Typography & Type Design Manual", font_size=Pt(22), bold=False,
                color=rgb(180, 180, 180), align=PP_ALIGN.LEFT, font_name="Arial")
    add_textbox(slide, Cm(3), Cm(13), Cm(30), Cm(1.5),
                "色彩系统 · 拉丁字体 · 汉字编排 · 字号规范 · 行距字距实验",
                font_size=Pt(12), bold=False, color=rgb(140, 140, 140),
                align=PP_ALIGN.LEFT, font_name="SimSun")
    add_textbox(slide, Cm(3), Cm(19), Cm(20), Cm(1),
                "公共场域与数字叙事（二）  |  设计编排工作手册  |  2025-2026",
                font_size=Pt(9), color=rgb(100, 100, 100),
                align=PP_ALIGN.LEFT, font_name="SimSun")


# ─── SLIDE 2: Color Wheel – Pure Hues ───────────────────────────────────────

def slide_color_wheel_pure(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(248, 246, 240))

    # Header
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(20), Cm(1.2),
                "01  色相环 · 纯色系 CMYK 色值表", font_size=Pt(13), bold=True,
                color=rgb(240, 220, 150), font_name="SimHei")

    import math, colorsys

    n = 12
    colors_12 = [
        ("红",       0,   (0,  100, 100, 0)),
        ("红橙",    30,   (0,   70, 100, 0)),
        ("橙",      60,   (0,   50, 100, 0)),
        ("黄橙",    90,   (0,   30, 100, 0)),
        ("黄",     120,   (0,    0, 100, 0)),
        ("黄绿",   150,   (40,   0, 100, 0)),
        ("绿",     180,   (100,  0, 100, 0)),
        ("蓝绿",   210,   (100,  0,  40, 0)),
        ("蓝",     240,   (100, 60,   0, 0)),
        ("蓝紫",   270,   (80,  80,   0, 0)),
        ("紫",     300,   (60, 100,   0, 0)),
        ("红紫",   330,   (20, 100,  20, 0)),
    ]

    # Draw 12 big colored squares in two rows of 6
    sq = Cm(3.5)
    gap = Cm(0.25)
    start_x = Cm(1.2)
    row1_y = Cm(2.5)
    row2_y = row1_y + sq + Cm(2.0)

    for i, (name, hue, cmyk) in enumerate(colors_12):
        col = i % 6
        row = i // 6
        rx = start_x + col * (sq + gap)
        ry = row1_y if row == 0 else row2_y
        c, m, y, k = cmyk
        fill = cmyk_to_rgb(c, m, y, k)
        add_rect(slide, int(rx), int(ry), int(sq), int(sq), fill_rgb=fill)

        # Color name
        add_textbox(slide, int(rx), int(ry + sq + Cm(0.1)), int(sq), Cm(0.5),
                    name, font_size=Pt(9), bold=True, color=rgb(40, 40, 40),
                    align=PP_ALIGN.CENTER, font_name="SimHei")
        # CMYK values
        cmyk_text = f"C{c} M{m} Y{y} K{k}"
        add_textbox(slide, int(rx), int(ry + sq + Cm(0.55)), int(sq), Cm(0.45),
                    cmyk_text, font_size=Pt(7), color=rgb(80, 80, 80),
                    align=PP_ALIGN.CENTER, font_name="Arial")

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "纯色色相环 / Pure Hue Color Wheel  ·  基于印刷四色CMYK标准色值",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


# ─── SLIDE 3: Color Wheel – Mixed with White (Tints) ────────────────────────

def slide_color_wheel_white(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(248, 246, 240))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(36), Cm(1.2),
                "02  色相环 · 纯色混白（淡色调 Tint）CMYK 色值表", font_size=Pt(13), bold=True,
                color=rgb(240, 220, 150), font_name="SimHei")

    colors_12 = [
        ("浅红",      (0,   50,  50, 0)),
        ("浅红橙",    (0,   35,  50, 0)),
        ("浅橙",      (0,   25,  50, 0)),
        ("浅黄橙",    (0,   15,  50, 0)),
        ("浅黄",      (0,    0,  50, 0)),
        ("浅黄绿",    (20,   0,  50, 0)),
        ("浅绿",      (50,   0,  50, 0)),
        ("浅蓝绿",    (50,   0,  20, 0)),
        ("浅蓝",      (50,  30,   0, 0)),
        ("浅蓝紫",    (40,  40,   0, 0)),
        ("浅紫",      (30,  50,   0, 0)),
        ("浅红紫",    (10,  50,  10, 0)),
    ]

    sq = Cm(3.5)
    gap = Cm(0.25)
    start_x = Cm(1.2)
    row1_y = Cm(2.5)
    row2_y = row1_y + sq + Cm(2.0)

    tint_levels = [25, 50, 75]  # white mix percentages shown as 3 sub-swatches

    for i, (name, cmyk_base) in enumerate(colors_12):
        col = i % 6
        row = i // 6
        rx = start_x + col * (sq + gap)
        ry = row1_y if row == 0 else row2_y

        # Draw 3 tint sub-swatches stacked
        sub_h = sq / 3
        for ti, tint_pct in enumerate(tint_levels):
            factor = tint_pct / 100.0
            c = int(cmyk_base[0] * factor)
            m = int(cmyk_base[1] * factor)
            y = int(cmyk_base[2] * factor)
            k = cmyk_base[3]
            fill = cmyk_to_rgb(c, m, y, k)
            add_rect(slide, int(rx), int(ry + ti * sub_h), int(sq), int(sub_h), fill_rgb=fill)

        # Representative CMYK (50% tint)
        c = int(cmyk_base[0] * 0.5)
        m = int(cmyk_base[1] * 0.5)
        y = int(cmyk_base[2] * 0.5)
        k = cmyk_base[3]

        add_textbox(slide, int(rx), int(ry + sq + Cm(0.1)), int(sq), Cm(0.5),
                    name, font_size=Pt(9), bold=True, color=rgb(40, 40, 40),
                    align=PP_ALIGN.CENTER, font_name="SimHei")
        cmyk_text = f"C{c} M{m} Y{y} K{k}"
        add_textbox(slide, int(rx), int(ry + sq + Cm(0.55)), int(sq), Cm(0.45),
                    cmyk_text, font_size=Pt(7), color=rgb(80, 80, 80),
                    align=PP_ALIGN.CENTER, font_name="Arial")

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "混白淡色调 / Tint  ·  纯色+白色混合（25% / 50% / 75%渐进）·  CMYK印刷参考值",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


# ─── SLIDE 4: Color Wheel – Mixed with Gray ─────────────────────────────────

def slide_color_wheel_gray(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(248, 246, 240))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(36), Cm(1.2),
                "03  色相环 · 纯色混灰（浊色调 Tone）CMYK 色值表", font_size=Pt(13), bold=True,
                color=rgb(240, 220, 150), font_name="SimHei")

    colors_12 = [
        ("浊红",    (0,   70,  70, 30)),
        ("浊红橙",  (0,   50,  70, 30)),
        ("浊橙",    (0,   35,  70, 30)),
        ("浊黄橙",  (0,   20,  70, 30)),
        ("浊黄",    (0,    0,  70, 30)),
        ("浊黄绿",  (30,   0,  70, 30)),
        ("浊绿",    (70,   0,  70, 30)),
        ("浊蓝绿",  (70,   0,  28, 30)),
        ("浊蓝",    (70,  42,   0, 30)),
        ("浊蓝紫",  (56,  56,   0, 30)),
        ("浊紫",    (42,  70,   0, 30)),
        ("浊红紫",  (14,  70,  14, 30)),
    ]

    sq = Cm(3.5)
    gap = Cm(0.25)
    start_x = Cm(1.2)
    row1_y = Cm(2.5)
    row2_y = row1_y + sq + Cm(2.0)

    gray_levels = [20, 40, 60]

    for i, (name, cmyk) in enumerate(colors_12):
        col = i % 6
        row = i // 6
        rx = start_x + col * (sq + gap)
        ry = row1_y if row == 0 else row2_y

        sub_h = sq / 3
        for ti, k_add in enumerate(gray_levels):
            c, m, y, k = cmyk
            k_new = min(100, k + k_add - 30)
            fill = cmyk_to_rgb(c, m, y, k_new)
            add_rect(slide, int(rx), int(ry + ti * sub_h), int(sq), int(sub_h), fill_rgb=fill)

        c, m, y, k = cmyk
        add_textbox(slide, int(rx), int(ry + sq + Cm(0.1)), int(sq), Cm(0.5),
                    name, font_size=Pt(9), bold=True, color=rgb(40, 40, 40),
                    align=PP_ALIGN.CENTER, font_name="SimHei")
        cmyk_text = f"C{c} M{m} Y{y} K{k}"
        add_textbox(slide, int(rx), int(ry + sq + Cm(0.55)), int(sq), Cm(0.45),
                    cmyk_text, font_size=Pt(7), color=rgb(80, 80, 80),
                    align=PP_ALIGN.CENTER, font_name="Arial")

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "混灰浊色调 / Tone  ·  纯色+灰色混合（加黑K值渐进）·  CMYK印刷参考值",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


# ─── SLIDE 5: Color Wheel – Mixed with Black (Shades) ───────────────────────

def slide_color_wheel_black(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(248, 246, 240))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(36), Cm(1.2),
                "04  色相环 · 纯色混黑（暗色调 Shade）CMYK 色值表", font_size=Pt(13), bold=True,
                color=rgb(240, 220, 150), font_name="SimHei")

    colors_12 = [
        ("暗红",    (0,   100, 100, 40)),
        ("暗红橙",  (0,    70, 100, 40)),
        ("暗橙",    (0,    50, 100, 40)),
        ("暗黄橙",  (0,    30, 100, 40)),
        ("暗黄",    (0,     0, 100, 40)),
        ("暗黄绿",  (40,    0, 100, 40)),
        ("暗绿",    (100,   0, 100, 40)),
        ("暗蓝绿",  (100,   0,  40, 40)),
        ("暗蓝",    (100,  60,   0, 40)),
        ("暗蓝紫",  (80,   80,   0, 40)),
        ("暗紫",    (60,  100,   0, 40)),
        ("暗红紫",  (20,  100,  20, 40)),
    ]

    sq = Cm(3.5)
    gap = Cm(0.25)
    start_x = Cm(1.2)
    row1_y = Cm(2.5)
    row2_y = row1_y + sq + Cm(2.0)

    shade_levels = [20, 40, 60]

    for i, (name, cmyk) in enumerate(colors_12):
        col = i % 6
        row = i // 6
        rx = start_x + col * (sq + gap)
        ry = row1_y if row == 0 else row2_y

        sub_h = sq / 3
        c, m, y, k_base = cmyk
        for ti, shade_k in enumerate(shade_levels):
            k_new = min(100, k_base - 20 + shade_k)
            fill = cmyk_to_rgb(c, m, y, k_new)
            add_rect(slide, int(rx), int(ry + ti * sub_h), int(sq), int(sub_h), fill_rgb=fill)

        add_textbox(slide, int(rx), int(ry + sq + Cm(0.1)), int(sq), Cm(0.5),
                    name, font_size=Pt(9), bold=True, color=rgb(40, 40, 40),
                    align=PP_ALIGN.CENTER, font_name="SimHei")
        cmyk_text = f"C{c} M{m} Y{y} K{k_base}"
        add_textbox(slide, int(rx), int(ry + sq + Cm(0.55)), int(sq), Cm(0.45),
                    cmyk_text, font_size=Pt(7), color=rgb(80, 80, 80),
                    align=PP_ALIGN.CENTER, font_name="Arial")

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "混黑暗色调 / Shade  ·  纯色+黑色混合（K值20/40/60渐进）·  CMYK印刷参考值",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


# ─── SLIDE 6-7: 30 Latin Fonts ──────────────────────────────────────────────

LATIN_FONTS = [
    # Sans-serif (无衬线)
    ("1", "Helvetica",          "Swiss 721 BT",           "无衬线体"),
    ("2", "Avant Garde",        "AvantGarde Bk BT",       "无衬线体"),
    ("3", "Bell Centennial",    "Bell Centennial Std",    "无衬线体"),
    ("4", "Bell Gothic",        "Bell Gothic Std",        "无衬线体"),
    ("5", "DIN",                "DIN Next LT Pro",        "无衬线体"),
    ("6", "Franklin Gothic",    "Franklin Gothic Book",   "无衬线体"),
    ("7", "Frutiger",           "Humanist 777 BT",        "无衬线体"),
    ("8", "Futura",             "Futura Bk BT",           "无衬线体"),
    ("9", "Gill Sans",          "Gill Sans MT",           "无衬线体"),
    ("10","Eurostile",          "Eurostile",              "无衬线体"),
    ("11","Eras",               "Eras Medium ITC",        "无衬线体"),
    ("12","News Gothic",        "News Gothic MT",         "无衬线体"),
    ("13","Optima",             "Optima LT Pro",          "无衬线体"),
    ("14","Univers",            "Zurich BT",              "无衬线体"),
    ("15","VAG Rounded",        "VAG Rounded BT",         "无衬线体"),
    # Serif (有衬线)
    ("16","Caslon",             "Adobe Caslon Pro",       "有衬线体"),
    ("17","Garamond",           "Garamond",               "有衬线体"),
    ("18","Bembo",              "Bembo MT",               "有衬线体"),
    ("19","Bodoni",             "Bodoni MT",              "有衬线体"),
    ("20","Clarendon",          "Clarendon BT",           "有衬线体"),
    ("21","Courier PS",         "Courier New",            "有衬线体"),
    ("22","Excelsior",          "Century 791 BT",         "有衬线体"),
    ("23","Lucida Bright",      "Lucida Bright",          "有衬线体"),
    ("24","Minion",             "Minion Pro",             "有衬线体"),
    ("25","Perpetua",           "Perpetua",               "有衬线体"),
    ("26","Sabon",              "Sabon LT Std",           "有衬线体"),
    ("27","Stempel Schneidler", "Schneidler BT",          "有衬线体"),
    ("28","Times New Roman",    "Times New Roman",        "有衬线体"),
    ("29","Trajan",             "Trajan Pro",             "有衬线体"),
    ("30","Modern No.20",       "Modern No. 20",          "有衬线体"),
]

ALPHABET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
NUMS     = "0123456789 !@#$%&*().,;:?!\"'"

def slide_latin_fonts_1(prs):
    """Slide 6 – Latin fonts 1-15"""
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(250, 248, 244))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(36), Cm(1.2),
                "05  常用拉丁字体全字母编排（1–15款）无衬线体", font_size=Pt(13), bold=True,
                color=rgb(240, 220, 150), font_name="SimHei")

    row_h = Cm(1.62)
    for idx in range(15):
        num, name, font, cat = LATIN_FONTS[idx]
        ry = Cm(2.0) + idx * row_h

        # number + name
        add_textbox(slide, Cm(0.5), int(ry), Cm(3.5), row_h,
                    f"{num}. {name}", font_size=Pt(8), bold=True,
                    color=rgb(60, 60, 60), font_name="Arial")
        # alphabet specimen
        display_font = font if font in ["Arial", "Times New Roman", "Courier New",
                                         "Gill Sans MT", "Garamond", "Perpetua",
                                         "News Gothic MT", "Futura Bk BT",
                                         "Franklin Gothic Book", "Bodoni MT",
                                         "Lucida Bright"] else "Arial"
        add_textbox(slide, Cm(4), int(ry), Cm(32), row_h,
                    ALPHABET + "  " + NUMS,
                    font_size=Pt(10), color=rgb(30, 30, 30),
                    font_name=display_font)

        # category tag
        tag_color = rgb(180, 60, 60) if cat == "无衬线体" else rgb(60, 80, 160)
        add_textbox(slide, Cm(37.5), int(ry + Cm(0.2)), Cm(3.5), Cm(0.7),
                    cat, font_size=Pt(7), color=tag_color, font_name="SimSun")

        # divider
        add_rect(slide, Cm(0.5), int(ry + row_h - Cm(0.05)), int(A3_W - Cm(1)),
                 int(Cm(0.03)), fill_rgb=rgb(210, 205, 200))


def slide_latin_fonts_2(prs):
    """Slide 7 – Latin fonts 16-30"""
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(250, 248, 244))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(36), Cm(1.2),
                "06  常用拉丁字体全字母编排（16–30款）有衬线体", font_size=Pt(13), bold=True,
                color=rgb(240, 220, 150), font_name="SimHei")

    row_h = Cm(1.62)
    for idx in range(15, 30):
        num, name, font, cat = LATIN_FONTS[idx]
        ry = Cm(2.0) + (idx - 15) * row_h

        add_textbox(slide, Cm(0.5), int(ry), Cm(3.5), row_h,
                    f"{num}. {name}", font_size=Pt(8), bold=True,
                    color=rgb(60, 60, 60), font_name="Arial")

        display_font = font if font in ["Times New Roman", "Courier New", "Garamond",
                                         "Perpetua", "Bodoni MT", "Lucida Bright",
                                         "Century Schoolbook"] else "Georgia"
        add_textbox(slide, Cm(4), int(ry), Cm(32), row_h,
                    ALPHABET + "  " + NUMS,
                    font_size=Pt(10), color=rgb(30, 30, 30), font_name=display_font)

        tag_color = rgb(60, 80, 160)
        add_textbox(slide, Cm(37.5), int(ry + Cm(0.2)), Cm(3.5), Cm(0.7),
                    cat, font_size=Pt(7), color=tag_color, font_name="SimSun")

        add_rect(slide, Cm(0.5), int(ry + row_h - Cm(0.05)), int(A3_W - Cm(1)),
                 int(Cm(0.03)), fill_rgb=rgb(210, 205, 200))


# ─── SLIDE 8: Chinese Font Categories ───────────────────────────────────────

CHINESE_FONT_CATS = [
    ("有衬线体", [
        ("方正书宋",    "SimSun",  "春风又绿江南岸，明月何时照我还。"),
        ("方正仿宋",    "FangSong","床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
        ("汉仪中宋",    "SimSun",  "大漠孤烟直，长河落日圆。"),
    ]),
    ("无衬线体", [
        ("方正黑体",    "SimHei",  "海内存知己，天涯若比邻。无为在歧路，儿女共沾巾。"),
        ("汉仪黑体",    "SimHei",  "欲穷千里目，更上一层楼。"),
        ("方正兰亭黑",  "Microsoft YaHei", "会当凌绝顶，一览众山小。"),
    ]),
    ("圆体", [
        ("方正圆体",    "Microsoft YaHei", "黄河之水天上来，奔流到海不复回。"),
        ("汉仪圆体",    "Microsoft YaHei", "两岸猿声啼不住，轻舟已过万重山。"),
    ]),
    ("手写体", [
        ("方正行楷",    "KaiTi",   "问君能有几多愁，恰似一江春水向东流。"),
        ("汉仪行楷",    "KaiTi",   "天生我材必有用，千金散尽还复来。"),
    ]),
    ("古体／过渡体", [
        ("方正楷体",    "KaiTi",   "但愿人长久，千里共婵娟。"),
        ("文鼎隶书",    "STKaiti", "落霞与孤鹜齐飞，秋水共长天一色。"),
    ]),
    ("混合体", [
        ("方正综艺体",  "STXingkai","桃花潭水深千尺，不及汪伦送我情。"),
    ]),
    ("展示体", [
        ("方正综艺",    "STXingkai","横看成岭侧成峰，远近高低各不同。"),
        ("汉仪综艺体",  "STXingkai","不识庐山真面目，只缘身在此山中。"),
    ]),
    ("超类别体", [
        ("方正超粗黑",  "SimHei",  "羌笛何须怨杨柳，春风不度玉门关。"),
        ("汉仪超黑",    "SimHei",  "黄沙百战穿金甲，不破楼兰终不还。"),
    ]),
]

def slide_chinese_fonts(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(252, 250, 246))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(36), Cm(1.2),
                "07  汉字字体分类编排  ·  有衬线·无衬线·圆体·手写·古体·混合·展示·超类别",
                font_size=Pt(11), bold=True, color=rgb(240, 220, 150), font_name="SimHei")

    cat_colors = [
        rgb(140, 30, 30), rgb(30, 80, 150), rgb(30, 130, 100),
        rgb(150, 80, 20), rgb(100, 60, 130), rgb(60, 120, 60),
        rgb(160, 50, 90), rgb(80, 80, 80),
    ]

    y_cursor = Cm(2.1)
    col_w = Cm(19.5)

    for ci, (cat_name, fonts) in enumerate(CHINESE_FONT_CATS):
        col = ci % 2
        if ci > 0 and ci % 2 == 0:
            y_cursor += Cm(0.3)
        rx = Cm(0.8) + col * col_w
        ry = y_cursor if col == 0 else y_cursor  # both columns share same row start

        if col == 0 and ci > 0:
            y_cursor += Cm(0.3)  # add gap between category pairs

        # Category header
        cat_col = cat_colors[ci % len(cat_colors)]
        add_rect(slide, int(rx), int(ry), int(col_w - Cm(0.5)), int(Cm(0.55)),
                 fill_rgb=cat_col)
        add_textbox(slide, int(rx + Cm(0.2)), int(ry + Cm(0.05)), int(col_w - Cm(0.8)),
                    Cm(0.5), cat_name, font_size=Pt(9), bold=True,
                    color=rgb(255, 255, 255), font_name="SimHei")

        sub_y = ry + Cm(0.65)
        for font_name, system_font, sample in fonts:
            add_textbox(slide, int(rx), int(sub_y), int(Cm(3.2)), Cm(0.48),
                        font_name, font_size=Pt(7.5), bold=True,
                        color=rgb(80, 60, 40), font_name="SimSun")
            add_textbox(slide, int(rx + Cm(3.2)), int(sub_y), int(col_w - Cm(3.7)),
                        Cm(0.55), sample, font_size=Pt(9.5),
                        color=rgb(30, 30, 30), font_name=system_font)
            sub_y += Cm(0.7)

        if col == 1 or ci == len(CHINESE_FONT_CATS) - 1:
            y_cursor = max(y_cursor, sub_y + Cm(0.2))

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "字库资源参考：方正字库 / 汉仪字库 / 文鼎字库  ·  示例文本选自中国古典诗词",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


# ─── SLIDE 9: Chinese Font Size Table ───────────────────────────────────────

def slide_chinese_font_size_table(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(252, 250, 246))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(38), Cm(1.2),
                "08  宋体·黑体·圆体 字号规范表  +  常用拉丁体（6款）", font_size=Pt(13), bold=True,
                color=rgb(240, 220, 150), font_name="SimHei")

    # Chinese font size table
    # Traditional Chinese print sizes (号数) + pt equivalent
    sizes = [
        ("初号", 42), ("小初", 36), ("一号", 26), ("小一", 24),
        ("二号", 22), ("小二", 18), ("三号", 16), ("小三", 15),
        ("四号", 14), ("小四", 12), ("五号", 10.5), ("小五", 9),
        ("六号", 7.5), ("小六", 6.5), ("七号", 5.5), ("八号", 5),
    ]

    chinese_fonts = [
        ("宋体", "SimSun",  rgb(60, 40, 20)),
        ("黑体", "SimHei",  rgb(20, 40, 80)),
        ("圆体", "Microsoft YaHei", rgb(20, 100, 70)),
    ]

    # Header row
    col_xs = [Cm(0.5), Cm(1.8), Cm(3.2), Cm(7.8), Cm(12.4), Cm(17.0)]
    headers = ["号数", "pt值", "宋体 SimSun", "黑体 SimHei", "圆体 YaHei", "字形示例"]
    header_y = Cm(2.0)
    for hx, ht in zip(col_xs, headers):
        add_rect(slide, int(hx), int(header_y), int(Cm(4.4)), int(Cm(0.6)),
                 fill_rgb=rgb(50, 50, 50))
        add_textbox(slide, int(hx + Cm(0.1)), int(header_y + Cm(0.05)),
                    int(Cm(4.2)), Cm(0.5),
                    ht, font_size=Pt(8), bold=True,
                    color=rgb(255, 255, 255), font_name="SimHei")

    # Size rows
    sample_text = "永字八法"
    for si, (size_name, pt_val) in enumerate(sizes):
        row_y = Cm(2.7) + si * Cm(1.55)
        bg = rgb(245, 243, 238) if si % 2 == 0 else rgb(255, 253, 250)
        add_rect(slide, int(Cm(0.5)), int(row_y), int(A3_W / 2 - Cm(0.5)),
                 int(Cm(1.5)), fill_rgb=bg)

        add_textbox(slide, int(col_xs[0]), int(row_y + Cm(0.3)), int(Cm(1.2)), Cm(0.9),
                    size_name, font_size=Pt(8), bold=True,
                    color=rgb(80, 60, 30), font_name="SimHei")
        add_textbox(slide, int(col_xs[1]), int(row_y + Cm(0.3)), int(Cm(1.3)), Cm(0.9),
                    f"{pt_val}pt", font_size=Pt(8), color=rgb(80, 80, 80), font_name="Arial")

        for fi, (fn, ff, fc) in enumerate(chinese_fonts):
            tx = col_xs[2 + fi]
            disp_pt = min(pt_val, 14)
            add_textbox(slide, int(tx + Cm(0.1)), int(row_y + Cm(0.05)),
                        int(Cm(4.3)), Cm(1.4),
                        sample_text, font_size=Pt(disp_pt), color=fc, font_name=ff)

    # ── Latin fonts section (right half) ──────────────────────────────
    latin_6 = [
        ("Times New Roman",  "Times New Roman",  "有衬线"),
        ("Garamond",         "Garamond",         "有衬线"),
        ("Bodoni MT",        "Bodoni MT",        "有衬线"),
        ("Helvetica/Arial",  "Arial",            "无衬线"),
        ("Futura",           "Century Gothic",   "无衬线"),
        ("Gill Sans MT",     "Gill Sans MT",     "无衬线"),
    ]

    add_textbox(slide, int(A3_W / 2 + Cm(0.5)), Cm(2.0), Cm(19), Cm(0.7),
                "常用拉丁字体字号对照（6款）", font_size=Pt(10), bold=True,
                color=rgb(50, 50, 50), font_name="SimHei")

    latin_sizes_pt = [6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42]
    sample_lat = "Abc Xyz 123"

    col_gap = Cm(3.2)
    for fi, (name, font, cat) in enumerate(latin_6):
        lx = int(A3_W / 2) + int(Cm(0.5)) + fi * int(col_gap)
        add_rect(slide, lx, int(Cm(2.7)), int(Cm(3.0)), int(Cm(0.55)),
                 fill_rgb=rgb(70, 70, 130) if cat == "无衬线" else rgb(130, 70, 40))
        add_textbox(slide, lx + int(Cm(0.1)), int(Cm(2.75)), int(Cm(2.9)), Cm(0.5),
                    name, font_size=Pt(7), bold=True,
                    color=rgb(255, 255, 255), font_name="Arial")

        for si2, lpt in enumerate(latin_sizes_pt):
            ly = Cm(3.35) + si2 * Cm(1.48)
            disp = min(lpt, 14)
            add_textbox(slide, lx, int(ly), int(Cm(3.0)), Cm(1.4),
                        f"{lpt}pt\n{sample_lat}",
                        font_size=Pt(disp), color=rgb(30, 30, 30), font_name=font)

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "注：号数为中文印刷传统规格  ·  pt值为PostScript标准磅值  ·  展示字号受版面限制已缩放",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


# ─── SLIDE 10-12: Line Spacing & Character Spacing Experiments ──────────────

POEM = [
    "静夜思",
    "唐·李白",
    "",
    "床前明月光，疑是地上霜。",
    "举头望明月，低头思故乡。",
    "",
    "春晓",
    "唐·孟浩然",
    "",
    "春眠不觉晓，处处闻啼鸟。",
    "夜来风雨声，花落知多少。",
]

POEM_SHORT = [
    "床前明月光，疑是地上霜。",
    "举头望明月，低头思故乡。",
    "春眠不觉晓，处处闻啼鸟。",
    "夜来风雨声，花落知多少。",
    "欲穷千里目，更上一层楼。",
    "海内存知己，天涯若比邻。",
    "会当凌绝顶，一览众山小。",
    "大漠孤烟直，长河落日圆。",
]


def slide_line_spacing(prs):
    """Line spacing experiment with 宋体"""
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(252, 250, 246))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(38), Cm(1.2),
                "09  宋体行距实验  ·  9pt / 10pt / 12pt × 行距 100%·125%·150%·175%·200%",
                font_size=Pt(11), bold=True, color=rgb(240, 220, 150), font_name="SimHei")

    configs = [
        ("9pt  行距100%",  9,  1.0),
        ("9pt  行距125%",  9,  1.25),
        ("9pt  行距150%",  9,  1.5),
        ("10pt 行距125%", 10,  1.25),
        ("10pt 行距150%", 10,  1.5),
        ("10pt 行距175%", 10,  1.75),
        ("12pt 行距150%", 12,  1.5),
        ("12pt 行距175%", 12,  1.75),
        ("12pt 行距200%", 12,  2.0),
    ]

    col_w = Cm(13.0)
    n_cols = 3
    for ci, (label, pt_size, ls_factor) in enumerate(configs):
        col = ci % n_cols
        row = ci // n_cols
        cx = Cm(0.8) + col * col_w
        cy = Cm(2.1) + row * Cm(8.5)

        # Label
        add_rect(slide, int(cx), int(cy), int(col_w - Cm(0.3)), int(Cm(0.55)),
                 fill_rgb=rgb(80, 60, 100))
        add_textbox(slide, int(cx + Cm(0.2)), int(cy + Cm(0.05)), int(col_w - Cm(0.5)),
                    Cm(0.5), label, font_size=Pt(8), bold=True,
                    color=rgb(255, 255, 255), font_name="SimHei")

        # Poem text block
        from pptx.util import Pt as PPt
        from pptx.oxml.ns import qn
        txBox = slide.shapes.add_textbox(int(cx), int(cy + Cm(0.65)),
                                          int(col_w - Cm(0.3)), int(Cm(7.5)))
        tf = txBox.text_frame
        tf.word_wrap = True

        for li, line in enumerate(POEM_SHORT):
            if li == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.alignment = PP_ALIGN.LEFT
            from pptx.oxml.ns import qn as ons
            pPr = p._p.get_or_add_pPr()
            lnSpc = etree.SubElement(pPr, ons('a:lnSpc'))
            spcPct = etree.SubElement(lnSpc, ons('a:spcPct'))
            spcPct.set('val', str(int(ls_factor * 100000)))
            run = p.add_run()
            run.text = line
            run.font.size = PPt(pt_size)
            run.font.name = "SimSun"
            run.font.color.rgb = rgb(40, 40, 40)

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "行距实验  ·  宋体 SimSun  ·  参考软件：CDR / AI / PS  ·  文本选自唐诗",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


def slide_char_spacing(prs):
    """Character spacing experiment with 宋体"""
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(252, 250, 246))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(38), Cm(1.2),
                "10  宋体字距实验  ·  紧缩 -50 / 标准 0 / 加宽 +50 / +100 / +200 / +300",
                font_size=Pt(11), bold=True, color=rgb(240, 220, 150), font_name="SimHei")

    # Character spacing levels in hundredths of a point (pptx unit)
    spacing_configs = [
        ("字距 −50（紧缩）",  -50),
        ("字距   0（标准）",    0),
        ("字距 +50（加宽）",   50),
        ("字距 +100",         100),
        ("字距 +150",         150),
        ("字距 +200",         200),
        ("字距 +300",         300),
        ("字距 +500（疏松）", 500),
    ]

    sample_lines = [
        "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
        "欲穷千里目，更上一层楼。",
        "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    ]

    from pptx.oxml.ns import qn as ons

    row_h = Cm(3.1)
    for ri, (label, kern_val) in enumerate(spacing_configs):
        col = ri % 2
        row = ri // 2
        rx = Cm(0.8) + col * Cm(20.5)
        ry = Cm(2.1) + row * row_h

        add_rect(slide, int(rx), int(ry), int(Cm(19.5)), int(Cm(0.55)),
                 fill_rgb=rgb(60, 90, 70))
        add_textbox(slide, int(rx + Cm(0.2)), int(ry + Cm(0.05)), int(Cm(19)),
                    Cm(0.5), label, font_size=Pt(8), bold=True,
                    color=rgb(255, 255, 255), font_name="SimHei")

        txBox = slide.shapes.add_textbox(int(rx), int(ry + Cm(0.65)),
                                          int(Cm(19.5)), int(Cm(2.3)))
        tf = txBox.text_frame
        tf.word_wrap = True

        for li, line in enumerate(sample_lines):
            if li == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.alignment = PP_ALIGN.LEFT
            run = p.add_run()
            run.text = line
            run.font.size = Pt(9)
            run.font.name = "SimSun"
            run.font.color.rgb = rgb(40, 40, 40)
            # apply character spacing via XML
            rPr = run._r.get_or_add_rPr()
            rPr.set('spc', str(kern_val * 100))  # in hundredths of a point

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "字距实验  ·  宋体 SimSun 9pt  ·  参考软件：CDR字距微调 / AI字距调整 / PS字符间距  ·  文本选自唐诗",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


def slide_combined_spacing(prs):
    """Combined line+char spacing grid (宋体)"""
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(252, 250, 246))
    add_rect(slide, 0, 0, A3_W, Cm(1.8), fill_rgb=rgb(30, 30, 30))
    add_textbox(slide, Cm(1), Cm(0.3), Cm(38), Cm(1.2),
                "11  宋体综合实验  ·  行距×字距矩阵对照（CDR / AI / PS 软件标注）",
                font_size=Pt(11), bold=True, color=rgb(240, 220, 150), font_name="SimHei")

    line_spacings = [1.0, 1.5, 2.0]
    char_spacings = [0, 100, 300]
    ls_labels = ["行距100%", "行距150%", "行距200%"]
    cs_labels = ["字距0", "字距+100", "字距+300"]

    sample = "床前明月光，疑是地上霜。\n举头望明月，低头思故乡。\n欲穷千里目，更上一层楼。"

    cell_w = Cm(13.0)
    cell_h = Cm(8.0)

    from pptx.oxml.ns import qn as ons

    # Column headers
    for ci, cs_lbl in enumerate(cs_labels):
        cx = Cm(0.8) + ci * cell_w
        add_rect(slide, int(cx), int(Cm(1.9)), int(cell_w - Cm(0.1)), int(Cm(0.55)),
                 fill_rgb=rgb(50, 80, 120))
        add_textbox(slide, int(cx + Cm(0.2)), int(Cm(1.95)), int(cell_w - Cm(0.3)), Cm(0.5),
                    cs_lbl, font_size=Pt(9), bold=True,
                    color=rgb(255, 255, 255), font_name="SimHei")

    for ri, (ls, ls_lbl) in enumerate(zip(line_spacings, ls_labels)):
        ry = Cm(2.55) + ri * cell_h
        # Row label
        add_rect(slide, int(Cm(0)), int(ry), int(Cm(0.75)), int(cell_h - Cm(0.1)),
                 fill_rgb=rgb(100, 60, 40))
        add_textbox(slide, int(Cm(0.05)), int(ry + Cm(2.5)), int(Cm(0.65)), Cm(3),
                    ls_lbl, font_size=Pt(8), bold=True,
                    color=rgb(255, 255, 255), font_name="SimHei")

        for ci, (cs, cs_lbl) in enumerate(zip(char_spacings, cs_labels)):
            cx = Cm(0.8) + ci * cell_w
            bg = rgb(248, 246, 240) if (ri + ci) % 2 == 0 else rgb(238, 236, 230)
            add_rect(slide, int(cx), int(ry), int(cell_w - Cm(0.1)), int(cell_h - Cm(0.1)),
                     fill_rgb=bg, line_rgb=rgb(200, 195, 185))

            # Software labels
            sw_label = f"CDR: 行距{int(ls*100)}%  字距{cs}‰\nAI: 行间距×{ls}  字距{cs}pt\nPS: 行距{int(ls*100)}%  字距{cs}pt"
            add_textbox(slide, int(cx + Cm(0.2)), int(ry + Cm(0.1)), int(cell_w - Cm(0.4)),
                        Cm(0.9), sw_label, font_size=Pt(6.5),
                        color=rgb(120, 100, 80), font_name="Arial")

            txBox = slide.shapes.add_textbox(int(cx + Cm(0.2)), int(ry + Cm(1.1)),
                                              int(cell_w - Cm(0.4)), int(cell_h - Cm(1.3)))
            tf = txBox.text_frame
            tf.word_wrap = True

            for li, line in enumerate(sample.split("\n")):
                if li == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.alignment = PP_ALIGN.LEFT
                pPr = p._p.get_or_add_pPr()
                lnSpc = etree.SubElement(pPr, ons('a:lnSpc'))
                spcPct = etree.SubElement(lnSpc, ons('a:spcPct'))
                spcPct.set('val', str(int(ls * 100000)))
                run = p.add_run()
                run.text = line
                run.font.size = Pt(9)
                run.font.name = "SimSun"
                run.font.color.rgb = rgb(40, 40, 40)
                rPr = run._r.get_or_add_rPr()
                rPr.set('spc', str(cs * 100))

    add_textbox(slide, Cm(1), Cm(26.5), Cm(40), Cm(0.8),
                "行距×字距矩阵实验  ·  宋体 SimSun 9pt  ·  CDR=CorelDRAW / AI=Illustrator / PS=Photoshop",
                font_size=Pt(8), color=rgb(120, 120, 120), font_name="SimSun")


# ─── MAIN ───────────────────────────────────────────────────────────────────

def main():
    prs = new_prs()

    print("Building slide 01: Cover...")
    slide_cover(prs)

    print("Building slide 02: Color Wheel – Pure Hues...")
    slide_color_wheel_pure(prs)

    print("Building slide 03: Color Wheel – Mixed White (Tints)...")
    slide_color_wheel_white(prs)

    print("Building slide 04: Color Wheel – Mixed Gray (Tones)...")
    slide_color_wheel_gray(prs)

    print("Building slide 05: Color Wheel – Mixed Black (Shades)...")
    slide_color_wheel_black(prs)

    print("Building slide 06: Latin Fonts 1-15...")
    slide_latin_fonts_1(prs)

    print("Building slide 07: Latin Fonts 16-30...")
    slide_latin_fonts_2(prs)

    print("Building slide 08: Chinese Font Categories...")
    slide_chinese_fonts(prs)

    print("Building slide 09: Chinese Font Size Table...")
    slide_chinese_font_size_table(prs)

    print("Building slide 10: Line Spacing Experiment...")
    slide_line_spacing(prs)

    print("Building slide 11: Character Spacing Experiment...")
    slide_char_spacing(prs)

    print("Building slide 12: Combined Spacing Matrix...")
    slide_combined_spacing(prs)

    out = "/home/user/wendy/字体编排设计手册_A3横幅.pptx"
    prs.save(out)
    print(f"\n✓ Saved: {out}")

if __name__ == "__main__":
    main()
