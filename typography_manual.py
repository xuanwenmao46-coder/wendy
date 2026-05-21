#!/usr/bin/env python3
"""Typography Design Manual – A3 Landscape PPTX  (spacious multi-page layout)"""

from lxml import etree
from pptx import Presentation
from pptx.util import Cm, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import pptx.oxml.ns as ns

A3_W = Cm(42.0)
A3_H = Cm(29.7)

# ── helpers ──────────────────────────────────────────────────────────────────

def new_prs():
    p = Presentation()
    p.slide_width = A3_W
    p.slide_height = A3_H
    return p

def add_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])

def rgb(r, g, b):
    return RGBColor(r, g, b)

BG   = rgb(252, 250, 246)
DARK = rgb(22, 22, 22)
GOLD = rgb(235, 200, 110)
DIV  = rgb(205, 200, 192)

def header(slide, page_no, title, subtitle=""):
    add_rect(slide, 0, 0, A3_W, Cm(2.1), fill_rgb=DARK)
    add_rect(slide, 0, int(Cm(2.1)), A3_W, int(Cm(0.06)), fill_rgb=GOLD)
    add_tb(slide, Cm(1.2), Cm(0.25), Cm(2), Cm(0.9),
           f"{page_no:02d}", 18, True, GOLD, PP_ALIGN.LEFT, "Arial")
    add_tb(slide, Cm(3.5), Cm(0.3), Cm(34), Cm(1),
           title, 14, True, rgb(245, 240, 225), PP_ALIGN.LEFT, "SimHei")
    if subtitle:
        add_tb(slide, Cm(3.5), Cm(1.25), Cm(34), Cm(0.75),
               subtitle, 8.5, False, rgb(160, 155, 145), PP_ALIGN.LEFT, "SimHei")

def footer(slide, note=""):
    add_rect(slide, 0, int(A3_H - Cm(0.9)), A3_W, int(Cm(0.9)), fill_rgb=rgb(235, 232, 225))
    add_tb(slide, Cm(1), int(A3_H - Cm(0.78)), Cm(40), Cm(0.65),
           note, 7.5, False, rgb(110, 105, 98), PP_ALIGN.LEFT, "SimSun")

def add_rect(slide, x, y, w, h, fill_rgb=None, line_rgb=None, line_w=Pt(0.5)):
    sh = slide.shapes.add_shape(1, int(x), int(y), int(w), int(h))
    if fill_rgb:
        sh.fill.solid(); sh.fill.fore_color.rgb = fill_rgb
    else:
        sh.fill.background()
    if line_rgb:
        sh.line.color.rgb = line_rgb; sh.line.width = line_w
    else:
        sh.line.fill.background()
    return sh

def add_tb(slide, x, y, w, h, text, fs=10, bold=False,
           color=None, align=PP_ALIGN.LEFT, font="Arial", italic=False):
    color = color or rgb(30, 30, 30)
    tb = slide.shapes.add_textbox(int(x), int(y), int(w), int(h))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(fs)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    r.font.name = font
    return tb

def add_para(tf, text, fs=9, bold=False, color=None, font="SimSun",
             line_spacing_pct=None, char_spacing_100=0, align=PP_ALIGN.LEFT):
    color = color or rgb(30, 30, 30)
    p = tf.add_paragraph()
    p.alignment = align
    if line_spacing_pct:
        pPr = p._p.get_or_add_pPr()
        lnSpc = etree.SubElement(pPr, ns.qn('a:lnSpc'))
        spc   = etree.SubElement(lnSpc, ns.qn('a:spcPct'))
        spc.set('val', str(int(line_spacing_pct * 100000)))
    r = p.add_run()
    r.text = text
    r.font.size = Pt(fs)
    r.font.bold = bold
    r.font.color.rgb = color
    r.font.name = font
    if char_spacing_100:
        rPr = r._r.get_or_add_rPr()
        rPr.set('spc', str(char_spacing_100))
    return p

def cmyk_to_rgb(c, m, y, k):
    r = int(255*(1-c/100)*(1-k/100))
    g = int(255*(1-m/100)*(1-k/100))
    b = int(255*(1-y/100)*(1-k/100))
    return rgb(max(0,r), max(0,g), max(0,b))

# ── colour swatch block ───────────────────────────────────────────────────────
def color_page(prs, page_no, title, subtitle, colors_12, shade_rows, footer_note):
    """
    colors_12: list of (label, base_cmyk)
    shade_rows: list of (row_label, k_adjust_list) used for multi-level swatches
                if None  → single swatch per color
    """
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=BG)
    header(slide, page_no, title, subtitle)
    footer(slide, footer_note)

    n_cols = 6
    sq_w   = Cm(6.3)
    sq_gap = Cm(0.4)
    start_x = (A3_W - n_cols*sq_w - (n_cols-1)*sq_gap) / 2
    start_y = Cm(2.7)
    row_h   = Cm(10.8)  # swatch + label area

    for i, (label, cmyk) in enumerate(colors_12):
        col = i % n_cols
        row = i // n_cols
        rx = start_x + col*(sq_w + sq_gap)
        ry = start_y + row*row_h

        c, m, y, k = cmyk
        if shade_rows is None:
            # single swatch
            fill = cmyk_to_rgb(c, m, y, k)
            add_rect(slide, rx, ry, sq_w, Cm(7.8), fill_rgb=fill)
            sw_h = Cm(7.8)
        else:
            sub_h = Cm(7.8) / len(shade_rows)
            for si, (_, k_adj) in enumerate(shade_rows):
                k2 = min(100, max(0, k + k_adj))
                fill = cmyk_to_rgb(c, m, y, k2)
                add_rect(slide, rx, ry + si*sub_h, sq_w, sub_h, fill_rgb=fill)
            sw_h = Cm(7.8)

        # colour label
        add_tb(slide, rx, ry+sw_h+Cm(0.18), sq_w, Cm(0.65),
               label, 10.5, True, rgb(40,40,40), PP_ALIGN.CENTER, "SimHei")
        cmyk_str = f"C{c}  M{m}  Y{y}  K{k}"
        add_tb(slide, rx, ry+sw_h+Cm(0.85), sq_w, Cm(0.55),
               cmyk_str, 8.5, False, rgb(90,85,78), PP_ALIGN.CENTER, "Arial")

# ─── SLIDE 1  Cover ──────────────────────────────────────────────────────────
def slide_cover(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=rgb(18, 18, 18))
    add_rect(slide, 0, int(A3_H*0.62), A3_W, Cm(0.14), fill_rgb=GOLD)
    add_rect(slide, Cm(3), Cm(4.5), Cm(0.12), Cm(8), fill_rgb=GOLD)

    add_tb(slide, Cm(4.2), Cm(4.5), Cm(34), Cm(5.5),
           "字体编排\n设计手册", 56, True, rgb(238, 215, 145), PP_ALIGN.LEFT, "SimHei")
    add_tb(slide, Cm(4.2), Cm(11.5), Cm(32), Cm(1.8),
           "Typography & Type Design Manual", 22, False,
           rgb(170, 165, 158), PP_ALIGN.LEFT, "Arial")
    add_tb(slide, Cm(4.2), Cm(13.8), Cm(34), Cm(1.2),
           "色彩系统  ·  拉丁字体  ·  汉字编排  ·  字号规范  ·  行距字距实验",
           12, False, rgb(130, 125, 118), PP_ALIGN.LEFT, "SimSun")

    tags = ["色相环 CMYK", "30款拉丁字体", "汉字8大类", "字号规范表", "行距·字距实验"]
    for ti, tag in enumerate(tags):
        tx = Cm(4.2) + ti*Cm(7.5)
        add_rect(slide, int(tx), int(Cm(21.5)), int(Cm(7.0)), int(Cm(0.8)),
                 fill_rgb=rgb(60, 55, 48))
        add_tb(slide, int(tx+Cm(0.2)), int(Cm(21.55)), int(Cm(6.8)), Cm(0.75),
               tag, 8.5, False, GOLD, PP_ALIGN.LEFT, "SimHei")

    add_tb(slide, Cm(4.2), Cm(24.5), Cm(30), Cm(0.8),
           "公共场域与数字叙事（二）  ·  设计编排工作手册  ·  2025–2026",
           9, False, rgb(90,85,78), PP_ALIGN.LEFT, "SimSun")

# ─── SLIDES 2-5  Colour Wheels ───────────────────────────────────────────────
PURE_12 = [
    ("红",   (0,  100, 100, 0)),  ("红橙", (0,   70, 100, 0)),
    ("橙",   (0,   50, 100, 0)),  ("黄橙", (0,   30, 100, 0)),
    ("黄",   (0,    0, 100, 0)),  ("黄绿", (40,   0, 100, 0)),
    ("绿",   (100,  0, 100, 0)),  ("蓝绿", (100,  0,  40, 0)),
    ("蓝",   (100, 60,   0, 0)),  ("蓝紫", (80,  80,   0, 0)),
    ("紫",   (60, 100,   0, 0)),  ("红紫", (20, 100,  20, 0)),
]

TINT_12 = [
    ("浅红",   (0,  50,  50, 0)), ("浅红橙", (0,  35,  50, 0)),
    ("浅橙",   (0,  25,  50, 0)), ("浅黄橙", (0,  15,  50, 0)),
    ("浅黄",   (0,   0,  50, 0)), ("浅黄绿", (20,  0,  50, 0)),
    ("浅绿",   (50,  0,  50, 0)), ("浅蓝绿", (50,  0,  20, 0)),
    ("浅蓝",   (50, 30,   0, 0)), ("浅蓝紫", (40, 40,   0, 0)),
    ("浅紫",   (30, 50,   0, 0)), ("浅红紫", (10, 50,  10, 0)),
]

TONE_12 = [
    ("浊红",   (0,  70,  70, 30)), ("浊红橙", (0,  50,  70, 30)),
    ("浊橙",   (0,  35,  70, 30)), ("浊黄橙", (0,  20,  70, 30)),
    ("浊黄",   (0,   0,  70, 30)), ("浊黄绿", (30,  0,  70, 30)),
    ("浊绿",   (70,  0,  70, 30)), ("浊蓝绿", (70,  0,  28, 30)),
    ("浊蓝",   (70, 42,   0, 30)), ("浊蓝紫", (56, 56,   0, 30)),
    ("浊紫",   (42, 70,   0, 30)), ("浊红紫", (14, 70,  14, 30)),
]

SHADE_12 = [
    ("暗红",   (0,  100, 100, 40)), ("暗红橙", (0,   70, 100, 40)),
    ("暗橙",   (0,   50, 100, 40)), ("暗黄橙", (0,   30, 100, 40)),
    ("暗黄",   (0,    0, 100, 40)), ("暗黄绿", (40,   0, 100, 40)),
    ("暗绿",   (100,  0, 100, 40)), ("暗蓝绿", (100,  0,  40, 40)),
    ("暗蓝",   (100, 60,   0, 40)), ("暗蓝紫", (80,  80,   0, 40)),
    ("暗紫",   (60, 100,   0, 40)), ("暗红紫", (20, 100,  20, 40)),
]

def slides_color_wheels(prs):
    color_page(prs, 2,
               "色相环 · 纯色系（Pure Hue）",
               "12色相  ·  印刷 CMYK 标准色值  ·  色相角 0°→330°（每30°一色）",
               PURE_12, None,
               "纯色色相环 / Pure Hue  ·  色值基于 ISO 12647 印刷四色标准")

    color_page(prs, 3,
               "色相环 · 混白淡色调（Tint）",
               "纯色 + 白色混合  ·  每色展示 25% / 50% / 75% 三级明度梯度",
               TINT_12, [("25%",0),("50%",0),("75%",0)],
               "混白淡色调 / Tint  ·  C/M/Y值×50%示例（50%混白）·  CMYK印刷参考值")

    color_page(prs, 4,
               "色相环 · 混灰浊色调（Tone）",
               "纯色 + 中性灰混合  ·  每色展示 K+10 / K+20 / K+30 三级灰度叠加",
               TONE_12, [("K+10",-20),("K+20",-10),("K+30",0)],
               "混灰浊色调 / Tone  ·  通过增加K值模拟加灰效果  ·  CMYK印刷参考值")

    color_page(prs, 5,
               "色相环 · 混黑暗色调（Shade）",
               "纯色 + 黑色混合  ·  每色展示 K+20 / K+40 / K+60 三级加深梯度",
               SHADE_12, [("K+20",-20),("K+40",0),("K+60",20)],
               "混黑暗色调 / Shade  ·  K值叠加加深色相  ·  CMYK印刷参考值")

# ─── SLIDES 6-8  Latin Fonts (10 per page) ───────────────────────────────────
LATIN_FONTS = [
    # no, name, display_font, category, corel_note
    ( 1,"Helvetica",          "Arial",            "无衬线体","Corel: Swiss 721"),
    ( 2,"Avant Garde",        "Century Gothic",   "无衬线体","Corel: AvantGarde Bk BT"),
    ( 3,"Bell Centennial",    "Arial Narrow",     "无衬线体","Bell Centennial Std"),
    ( 4,"Bell Gothic",        "Arial",            "无衬线体","Bell Gothic Std"),
    ( 5,"DIN",                "Arial",            "无衬线体","DIN Next LT Pro"),
    ( 6,"Franklin Gothic",    "Franklin Gothic Book","无衬线体","Franklin Gothic Demi"),
    ( 7,"Frutiger",           "Arial",            "无衬线体","Corel: Humanist 777"),
    ( 8,"Futura",             "Century Gothic",   "无衬线体","Futura Bk BT"),
    ( 9,"Gill Sans",          "Gill Sans MT",     "无衬线体","Gill Sans MT"),
    (10,"Eurostile",          "Arial",            "无衬线体","Eurostile BT"),
    (11,"Eras",               "Arial",            "无衬线体","Eras Medium ITC"),
    (12,"News Gothic",        "Arial Narrow",     "无衬线体","News Gothic MT"),
    (13,"Optima",             "Gill Sans MT",     "无衬线体","Corel: ZapfHumnsl"),
    (14,"Univers",            "Arial",            "无衬线体","Corel: Zurich BT"),
    (15,"VAG Rounded",        "Century Gothic",   "无衬线体","VAG Rounded BT"),
    (16,"Caslon",             "Garamond",         "有衬线体","Adobe Caslon Pro"),
    (17,"Garamond",           "Garamond",         "有衬线体","Garamond"),
    (18,"Bembo",              "Georgia",          "有衬线体","Corel: Aldine 401 BT"),
    (19,"Bodoni",             "Bodoni MT",        "有衬线体","Bodoni MT"),
    (20,"Clarendon",          "Georgia",          "有衬线体","Clarendon BT"),
    (21,"Courier PS",         "Courier New",      "有衬线体","Courier New"),
    (22,"Excelsior",          "Century Schoolbook","有衬线体","Corel: Century 791"),
    (23,"Lucida Bright",      "Lucida Bright",    "有衬线体","Lucida Bright"),
    (24,"Minion",             "Garamond",         "有衬线体","Minion Pro"),
    (25,"Perpetua",           "Perpetua",         "有衬线体","Perpetua"),
    (26,"Sabon",              "Garamond",         "有衬线体","Corel: Class Garamond"),
    (27,"Stempel Schneidler", "Georgia",          "有衬线体","Corel: Schneidler BT"),
    (28,"Times New Roman",    "Times New Roman",  "有衬线体","Times New Roman"),
    (29,"Trajan",             "Perpetua",         "有衬线体","Trajan Pro"),
    (30,"Modern No.20",       "Georgia",          "有衬线体","Modern No.20"),
]

ALPHA   = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
SYMBOLS = "0123456789  !?&@#$.,;:—()[]{}'\""

TAG_COL = { "无衬线体": rgb(50, 90, 160), "有衬线体": rgb(140, 50, 40) }

def latin_font_slide(prs, page_no, fonts_10, title):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=BG)
    header(slide, page_no, title,
           "完整字母表 A–Z a–z + 数字与常用符号标本")
    footer(slide, "字体标本 / Typeface Specimen  ·  字库版权归各字体公司所有  ·  仅供学习编排参考")

    ROW_H   = Cm(2.55)
    Y_START = Cm(2.55)
    NUM_W   = Cm(1.8)
    NAME_W  = Cm(5.5)
    TAG_W   = Cm(2.4)
    SPEC_W  = A3_W - NUM_W - NAME_W - TAG_W - Cm(1.8)

    for ri, (no, name, font, cat, note) in enumerate(fonts_10):
        ry = Y_START + ri * ROW_H
        bg = rgb(246, 244, 239) if ri % 2 == 0 else rgb(254, 252, 248)
        add_rect(slide, Cm(0.6), ry, A3_W - Cm(1.2), ROW_H - Cm(0.08), fill_rgb=bg)

        # number
        add_tb(slide, Cm(0.8), ry+Cm(0.35), NUM_W, Cm(0.9),
               f"{no:02d}", 20, True, rgb(180,165,130), PP_ALIGN.LEFT, "Arial")
        # font name
        add_tb(slide, Cm(0.8)+NUM_W, ry+Cm(0.15), NAME_W, Cm(0.7),
               name, 10, True, rgb(40,35,28), PP_ALIGN.LEFT, "Arial")
        add_tb(slide, Cm(0.8)+NUM_W, ry+Cm(0.85), NAME_W, Cm(0.55),
               note, 7, False, rgb(130,120,108), PP_ALIGN.LEFT, "Arial")
        # category tag
        tc = TAG_COL[cat]
        add_rect(slide, int(Cm(0.8)+NUM_W+NAME_W), int(ry+Cm(0.4)),
                 int(TAG_W-Cm(0.1)), int(Cm(0.7)), fill_rgb=tc)
        add_tb(slide, int(Cm(0.8)+NUM_W+NAME_W+Cm(0.1)), int(ry+Cm(0.43)),
               int(TAG_W-Cm(0.3)), Cm(0.65),
               cat, 8, True, rgb(255,255,255), PP_ALIGN.CENTER, "SimHei")
        # specimen
        spec_x = Cm(0.8) + NUM_W + NAME_W + TAG_W + Cm(0.1)
        add_tb(slide, spec_x, ry+Cm(0.1), SPEC_W, Cm(1.1),
               ALPHA, 11, False, rgb(25,25,25), PP_ALIGN.LEFT, font)
        add_tb(slide, spec_x, ry+Cm(1.15), SPEC_W, Cm(0.8),
               SYMBOLS, 10, False, rgb(70,65,60), PP_ALIGN.LEFT, font)

        add_rect(slide, Cm(0.6), int(ry+ROW_H-Cm(0.08)),
                 int(A3_W-Cm(1.2)), int(Cm(0.04)), fill_rgb=DIV)

def slides_latin_fonts(prs):
    latin_font_slide(prs, 6,  LATIN_FONTS[0:10],
                     "常用拉丁字体全字母编排（01–10）无衬线体")
    latin_font_slide(prs, 7,  LATIN_FONTS[10:20],
                     "常用拉丁字体全字母编排（11–20）无衬线体·有衬线体")
    latin_font_slide(prs, 8,  LATIN_FONTS[20:30],
                     "常用拉丁字体全字母编排（21–30）有衬线体")

# ─── SLIDES 9-10  Chinese Font Categories ────────────────────────────────────
ZI_CATS = [
    ("有衬线体 Serif", rgb(130,45,35), [
        ("方正书宋  FZ ShuSong",      "SimSun",
         "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。"),
        ("方正仿宋  FZ FangSong",     "FangSong",
         "海内存知己，天涯若比邻。无为在歧路，儿女共沾巾。"),
        ("汉仪中宋  HY ZhongSong",    "SimSun",
         "大漠孤烟直，长河落日圆。萧关逢候骑，都护在燕然。"),
        ("文鼎细宋  WT XiSong",       "SimSun",
         "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。"),
    ]),
    ("无衬线体 Sans-Serif", rgb(35,70,145), [
        ("方正黑体  FZ HeiTi",        "SimHei",
         "会当凌绝顶，一览众山小。荡胸生层云，决眦入归鸟。"),
        ("汉仪黑体  HY HeiTi",        "SimHei",
         "举头望明月，低头思故乡。床前明月光，疑是地上霜。"),
        ("方正兰亭黑  FZ LanTingHei", "Microsoft YaHei",
         "烽火连三月，家书抵万金。白头搔更短，浑欲不胜簪。"),
        ("文鼎中黑  WT ZhongHei",     "Microsoft YaHei",
         "随风潜入夜，润物细无声。好雨知时节，当春乃发生。"),
    ]),
    ("圆体 Rounded", rgb(28,110,85), [
        ("方正准圆  FZ ZhunYuan",     "Microsoft YaHei",
         "两岸猿声啼不住，轻舟已过万重山。"),
        ("汉仪圆体  HY YuanTi",       "Microsoft YaHei",
         "黄河之水天上来，奔流到海不复回。"),
        ("文鼎圆体  WT YuanTi",       "Microsoft YaHei",
         "天生我材必有用，千金散尽还复来。"),
    ]),
    ("手写体 Script / Handwriting", rgb(150,75,15), [
        ("方正行楷  FZ XingKai",      "STXingkai",
         "问君能有几多愁，恰似一江春水向东流。"),
        ("汉仪行楷  HY XingKai",      "KaiTi",
         "无边落木萧萧下，不尽长江滚滚来。"),
        ("文鼎行书  WT XingShu",      "STKaiti",
         "飞流直下三千尺，疑是银河落九天。"),
    ]),
]

ZI_CATS_2 = [
    ("古体字 / 过渡体 Transitional", rgb(80,50,110), [
        ("方正楷体  FZ KaiTi",        "KaiTi",
         "但愿人长久，千里共婵娟。明月几时有，把酒问青天。"),
        ("文鼎隶书  WT LiShu",        "STKaiti",
         "落霞与孤鹜齐飞，秋水共长天一色。渔舟唱晚，响穷彭蠡之滨。"),
        ("汉仪魏碑  HY WeiBei",       "SimSun",
         "羌笛何须怨杨柳，春风不度玉门关。黄沙百战穿金甲。"),
    ]),
    ("混合体 Hybrid", rgb(60,110,55), [
        ("方正综艺体  FZ ZongYi",     "STXingkai",
         "桃花潭水深千尺，不及汪伦送我情。李白乘舟将欲行。"),
        ("汉仪综艺体  HY ZongYi",     "STXingkai",
         "横看成岭侧成峰，远近高低各不同。不识庐山真面目。"),
    ]),
    ("展示体 Display", rgb(170,45,80), [
        ("方正粗圆  FZ CuYuan",       "SimHei",
         "长风破浪会有时，直挂云帆济沧海。"),
        ("汉仪展宋  HY ZhanSong",     "SimSun",
         "仰天大笑出门去，我辈岂是蓬蒿人。"),
        ("文鼎特明体  WT TeMingTi",   "SimSun",
         "安得广厦千万间，大庇天下寒士俱欢颜。"),
    ]),
    ("超类别体 Super-Family", rgb(70,70,70), [
        ("方正超粗黑  FZ ChaoHei",    "SimHei",
         "黄沙百战穿金甲，不破楼兰终不还。"),
        ("汉仪超黑  HY ChaoHei",      "SimHei",
         "羌笛何须怨杨柳，春风不度玉门关。"),
        ("文鼎超圆  WT ChaoYuan",     "Microsoft YaHei",
         "秦时明月汉时关，万里长征人未还。"),
    ]),
]

def chinese_font_slide(prs, page_no, cats, title):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=BG)
    header(slide, page_no, title,
           "字库参考：方正字库 / 汉仪字库 / 文鼎字库  ·  示例文本选自中国古典诗词")
    footer(slide, "字体分类参考 DIN 16518 标准及中文字体行业分类  ·  版权归各字库厂商所有")

    n_cats = len(cats)
    col_w = (A3_W - Cm(1.4)) / 2
    y_cursors = [Cm(2.55), Cm(2.55)]

    for ci, (cat_name, cat_color, fonts) in enumerate(cats):
        col = ci % 2
        cx  = Cm(0.7) + col * col_w
        cy  = y_cursors[col]

        # category header bar
        hbar_h = Cm(0.7)
        add_rect(slide, cx, cy, col_w-Cm(0.2), hbar_h, fill_rgb=cat_color)
        add_tb(slide, cx+Cm(0.25), cy+Cm(0.08), col_w-Cm(0.5), hbar_h-Cm(0.1),
               cat_name, 10.5, True, rgb(255,255,255), PP_ALIGN.LEFT, "SimHei")
        cy += hbar_h + Cm(0.12)

        for font_name, sys_font, sample in fonts:
            # font label
            add_tb(slide, cx+Cm(0.15), cy, col_w-Cm(0.4), Cm(0.52),
                   font_name, 8, True, rgb(80,65,45), PP_ALIGN.LEFT, "SimSun")
            cy += Cm(0.5)
            # sample text – large and visible
            add_tb(slide, cx+Cm(0.15), cy, col_w-Cm(0.4), Cm(1.3),
                   sample, 12.5, False, rgb(25,25,25), PP_ALIGN.LEFT, sys_font)
            cy += Cm(1.4)
            # thin divider
            add_rect(slide, cx+Cm(0.1), cy, col_w-Cm(0.4), Cm(0.03), fill_rgb=DIV)
            cy += Cm(0.12)

        y_cursors[col] = cy + Cm(0.5)

def slides_chinese_fonts(prs):
    chinese_font_slide(prs, 9, ZI_CATS,
                       "汉字字体分类编排（一）有衬线·无衬线·圆体·手写体")
    chinese_font_slide(prs, 10, ZI_CATS_2,
                       "汉字字体分类编排（二）古体·过渡体·混合·展示·超类别")

# ─── SLIDES 11-12  Font Size Reference Tables ────────────────────────────────
HAOZU = [
    ("初号",42),("小初",36),("一号",26),("小一",24),
    ("二号",22),("小二",18),("三号",16),("小三",15),
    ("四号",14),("小四",12),("五号",10.5),("小五",9),
    ("六号",7.5),("小六",6.5),("七号",5.5),("八号",5),
]
SAMPLE_ZI = "永字八法"

def slide_chinese_size_table(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=BG)
    header(slide, 11,
           "汉字字号规范表  ·  宋体 · 黑体 · 圆体",
           "号数系统（中文传统印刷规格）对照 PostScript pt 磅值  ·  从初号 42pt 到八号 5pt")
    footer(slide, "字号规范 / Type Size Reference  ·  号数制为中国传统活字印刷规格  ·  pt 为 PostScript 磅值（1pt ≈ 0.353mm）")

    CH_FONTS = [
        ("宋体 SimSun",      "SimSun",           rgb(90,55,25)),
        ("黑体 SimHei",      "SimHei",            rgb(25,50,110)),
        ("圆体 YaHei",       "Microsoft YaHei",   rgb(25,100,70)),
    ]

    # column positions
    col_no   = Cm(0.8)
    col_pt   = Cm(3.5)
    col_f = [Cm(6.5), Cm(20.5), Cm(34.5)]  # 3 font columns start x

    col_header_y = Cm(2.6)
    row_h = Cm(1.55)

    # header labels
    add_rect(slide, int(col_no), int(col_header_y), int(Cm(2.5)), int(Cm(0.7)),
             fill_rgb=DARK)
    add_tb(slide, int(col_no+Cm(0.1)), int(col_header_y+Cm(0.08)), int(Cm(2.4)), Cm(0.6),
           "号数", 9, True, rgb(255,255,255), PP_ALIGN.CENTER, "SimHei")
    add_rect(slide, int(col_pt), int(col_header_y), int(Cm(2.8)), int(Cm(0.7)),
             fill_rgb=DARK)
    add_tb(slide, int(col_pt+Cm(0.1)), int(col_header_y+Cm(0.08)), int(Cm(2.7)), Cm(0.6),
           "pt 值", 9, True, rgb(255,255,255), PP_ALIGN.CENTER, "SimHei")

    fc_colors = [rgb(130,60,25), rgb(25,55,120), rgb(20,100,65)]
    for fi, (fn, _, _) in enumerate(CH_FONTS):
        add_rect(slide, int(col_f[fi]), int(col_header_y), int(Cm(13.0)), int(Cm(0.7)),
                 fill_rgb=fc_colors[fi])
        add_tb(slide, int(col_f[fi]+Cm(0.2)), int(col_header_y+Cm(0.08)), int(Cm(12.8)), Cm(0.6),
               fn, 9.5, True, rgb(255,255,255), PP_ALIGN.CENTER, "SimHei")

    # rows
    for ri, (hao, pt) in enumerate(HAOZU):
        ry = col_header_y + Cm(0.75) + ri * row_h
        bg = rgb(246,244,240) if ri%2==0 else rgb(254,252,248)
        add_rect(slide, int(col_no), int(ry), int(A3_W - Cm(0.8) - col_no), int(row_h - Cm(0.04)),
                 fill_rgb=bg)
        add_tb(slide, int(col_no+Cm(0.1)), int(ry+Cm(0.25)), int(Cm(2.4)), Cm(0.9),
               hao, 10.5, True, rgb(80,60,30), PP_ALIGN.CENTER, "SimHei")
        add_tb(slide, int(col_pt+Cm(0.1)), int(ry+Cm(0.25)), int(Cm(2.7)), Cm(0.9),
               f"{pt}pt", 10, False, rgb(70,70,70), PP_ALIGN.CENTER, "Arial")
        for fi, (_, ff, fc) in enumerate(CH_FONTS):
            disp = min(pt, 14)
            add_tb(slide, int(col_f[fi]+Cm(0.2)), int(ry+Cm(0.05)), int(Cm(12.6)), Cm(1.4),
                   SAMPLE_ZI, disp, False, fc, PP_ALIGN.LEFT, ff)
        add_rect(slide, int(col_no), int(ry+row_h-Cm(0.04)),
                 int(A3_W-Cm(0.8)-col_no), int(Cm(0.04)), fill_rgb=DIV)

LATIN_6 = [
    ("Times New Roman",  "Times New Roman",  "有衬线", rgb(130,50,25)),
    ("Garamond",         "Garamond",         "有衬线", rgb(100,40,60)),
    ("Bodoni MT",        "Bodoni MT",        "有衬线", rgb(80,30,90)),
    ("Helvetica/Arial",  "Arial",            "无衬线", rgb(30,70,145)),
    ("Futura/Century Gothic","Century Gothic","无衬线",rgb(25,95,120)),
    ("Gill Sans MT",     "Gill Sans MT",     "无衬线", rgb(20,110,80)),
]
LATIN_PT_SIZES = [6,7,8,9,10,11,12,14,16,18,20,24,28,32,36,42,48]

def slide_latin_size_table(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=BG)
    header(slide, 12,
           "常用拉丁字体字号对照表（6款）",
           "Times New Roman · Garamond · Bodoni · Helvetica · Futura · Gill Sans  ·  6pt → 48pt")
    footer(slide, "拉丁字体字号对照 / Latin Type Size Chart  ·  示例文本：Aa Bb 123")

    n_fonts = len(LATIN_6)
    col_w   = (A3_W - Cm(3.8)) / n_fonts
    pt_col  = Cm(0.8)
    row_h   = Cm(1.53)

    hdr_y = Cm(2.6)
    # "pt" column header
    add_rect(slide, int(pt_col), int(hdr_y), int(Cm(2.8)), int(Cm(0.7)), fill_rgb=DARK)
    add_tb(slide, int(pt_col+Cm(0.1)), int(hdr_y+Cm(0.08)), int(Cm(2.6)), Cm(0.6),
           "pt 值", 9, True, rgb(255,255,255), PP_ALIGN.CENTER, "Arial")

    for fi, (fname, ffont, fcat, fcol) in enumerate(LATIN_6):
        fx = Cm(3.8) + fi*col_w
        add_rect(slide, int(fx), int(hdr_y), int(col_w-Cm(0.1)), int(Cm(0.7)), fill_rgb=fcol)
        add_tb(slide, int(fx+Cm(0.1)), int(hdr_y+Cm(0.08)), int(col_w-Cm(0.3)), Cm(0.6),
               fname, 8.5, True, rgb(255,255,255), PP_ALIGN.CENTER, "Arial")

    for ri, lpt in enumerate(LATIN_PT_SIZES):
        ry = hdr_y + Cm(0.75) + ri * row_h
        bg = rgb(246,244,240) if ri%2==0 else rgb(254,252,248)
        add_rect(slide, int(pt_col), int(ry), int(A3_W - pt_col - Cm(0.1)), int(row_h - Cm(0.04)),
                 fill_rgb=bg)
        add_tb(slide, int(pt_col+Cm(0.1)), int(ry+Cm(0.25)), int(Cm(2.6)), Cm(0.9),
               f"{lpt}pt", 10, True, rgb(80,65,30), PP_ALIGN.CENTER, "Arial")
        for fi, (_, ffont, _, fcol) in enumerate(LATIN_6):
            fx = Cm(3.8) + fi*col_w
            disp = min(lpt, 13)
            add_tb(slide, int(fx+Cm(0.1)), int(ry+Cm(0.05)), int(col_w-Cm(0.3)), Cm(1.4),
                   "Aa Bb Cc 123", disp, False, rgb(25,25,25), PP_ALIGN.LEFT, ffont)
        add_rect(slide, int(pt_col), int(ry+row_h-Cm(0.04)),
                 int(A3_W-pt_col-Cm(0.1)), int(Cm(0.04)), fill_rgb=DIV)

# ─── SLIDES 13-15  Line-spacing Experiment ───────────────────────────────────
POEM = [
    "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
    "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    "欲穷千里目，更上一层楼。白日依山尽，黄河入海流。",
    "海内存知己，天涯若比邻。无为在歧路，儿女共沾巾。",
    "会当凌绝顶，一览众山小。荡胸生层云，决眦入归鸟。",
    "大漠孤烟直，长河落日圆。萧关逢候骑，都护在燕然。",
]

def line_spacing_slide(prs, page_no, configs, title, subtitle):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=BG)
    header(slide, page_no, title, subtitle)
    footer(slide, "行距实验 / Line Spacing  ·  宋体 SimSun  ·  参考软件：CDR=CorelDRAW  AI=Illustrator  PS=Photoshop")

    n = len(configs)
    n_cols = 3 if n > 3 else n
    n_rows = (n + n_cols - 1) // n_cols
    cell_w = (A3_W - Cm(1.4)) / n_cols
    cell_h = (A3_H - Cm(4.2)) / n_rows

    for ci, (label, pt_size, ls) in enumerate(configs):
        col = ci % n_cols
        row = ci // n_cols
        cx  = Cm(0.7) + col * cell_w
        cy  = Cm(2.6) + row * cell_h

        # label bar
        bar_colors = [rgb(80,55,110), rgb(40,85,130), rgb(50,105,80)]
        add_rect(slide, cx, cy, cell_w-Cm(0.15), Cm(0.72), fill_rgb=bar_colors[col%3])
        sw_label = f"{label}   [ CDR: 行距{int(ls*100)}% | AI: ×{ls} | PS: {int(ls*100)}% ]"
        add_tb(slide, cx+Cm(0.2), cy+Cm(0.09), cell_w-Cm(0.5), Cm(0.6),
               sw_label, 8, True, rgb(255,255,255), PP_ALIGN.LEFT, "SimHei")

        # text block
        tb = slide.shapes.add_textbox(int(cx+Cm(0.1)), int(cy+Cm(0.82)),
                                       int(cell_w-Cm(0.3)), int(cell_h-Cm(1.1)))
        tf = tb.text_frame
        tf.word_wrap = True
        first = True
        for line in POEM:
            if first:
                p = tf.paragraphs[0]; first = False
            else:
                p = tf.add_paragraph()
            p.alignment = PP_ALIGN.LEFT
            pPr = p._p.get_or_add_pPr()
            lnSpc = etree.SubElement(pPr, ns.qn('a:lnSpc'))
            spc   = etree.SubElement(lnSpc, ns.qn('a:spcPct'))
            spc.set('val', str(int(ls * 100000)))
            r = p.add_run()
            r.text = line
            r.font.size = Pt(pt_size)
            r.font.name = "SimSun"
            r.font.color.rgb = rgb(35,35,35)

        # cell border
        add_rect(slide, cx, cy, cell_w-Cm(0.15), cell_h-Cm(0.1),
                 line_rgb=rgb(200,195,185))

def slides_line_spacing(prs):
    line_spacing_slide(prs, 13,
        [("9pt  行距100%", 9, 1.0),
         ("9pt  行距125%", 9, 1.25),
         ("9pt  行距150%", 9, 1.5),
         ("9pt  行距175%", 9, 1.75),
         ("9pt  行距200%", 9, 2.0),
         ("9pt  行距250%", 9, 2.5),],
        "宋体行距实验（一）  ·  9pt × 行距 100%–250%",
        "固定字号 9pt  ·  行距从100%到250%  ·  对比段落密度与阅读节奏变化")

    line_spacing_slide(prs, 14,
        [("10pt 行距100%",10, 1.0),
         ("10pt 行距150%",10, 1.5),
         ("10pt 行距200%",10, 2.0),
         ("12pt 行距100%",12, 1.0),
         ("12pt 行距150%",12, 1.5),
         ("12pt 行距200%",12, 2.0),],
        "宋体行距实验（二）  ·  10pt / 12pt × 行距 100%–200%",
        "不同字号下行距变化的对比  ·  体现字号与行距的配合关系")

# ─── SLIDE 16  Character-spacing Experiment ──────────────────────────────────
KERN_LINES = [
    "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
    "欲穷千里目，更上一层楼。白日依山尽，黄河入海流。",
    "海内存知己，天涯若比邻。无为在歧路，儿女共沾巾。",
]

def slide_char_spacing(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=BG)
    header(slide, 15,
           "宋体字距实验  ·  紧缩 −50 → 加宽 +500",
           "字距从紧缩到疏松的8级对比  ·  字号固定 9pt  ·  参考软件 CDR / AI / PS")
    footer(slide, "字距实验 / Character Spacing  ·  宋体 SimSun 9pt  ·  CDR: 字距微调(μ) | AI: 字距调整(pt) | PS: 字符间距(pt)")

    configs = [
        ("字距 −50   紧缩 Tight",   -5000),
        ("字距    0   标准 Normal",      0),
        ("字距 +50   加宽 Wide",      5000),
        ("字距 +100  加宽",          10000),
        ("字距 +150  加宽",          15000),
        ("字距 +200  加宽",          20000),
        ("字距 +300  疏松 Loose",    30000),
        ("字距 +500  极疏 XL-Loose", 50000),
    ]

    n_cols = 2
    cell_w = (A3_W - Cm(1.4)) / n_cols
    cell_h = (A3_H - Cm(4.2)) / 4   # 4 rows

    bar_colors = [rgb(50,90,70), rgb(70,55,100)]

    for ci, (label, spc_val) in enumerate(configs):
        col = ci % n_cols
        row = ci // n_cols
        cx  = Cm(0.7) + col * cell_w
        cy  = Cm(2.6) + row * cell_h

        add_rect(slide, cx, cy, cell_w-Cm(0.15), Cm(0.72), fill_rgb=bar_colors[col])
        add_tb(slide, cx+Cm(0.2), cy+Cm(0.09), cell_w-Cm(0.5), Cm(0.6),
               label, 9, True, rgb(255,255,255), PP_ALIGN.LEFT, "SimHei")

        tb = slide.shapes.add_textbox(int(cx+Cm(0.15)), int(cy+Cm(0.82)),
                                       int(cell_w-Cm(0.35)), int(cell_h-Cm(1.1)))
        tf = tb.text_frame
        tf.word_wrap = True
        first = True
        for line in KERN_LINES:
            if first:
                p = tf.paragraphs[0]; first = False
            else:
                p = tf.add_paragraph()
            p.alignment = PP_ALIGN.LEFT
            r = p.add_run()
            r.text = line
            r.font.size = Pt(9)
            r.font.name = "SimSun"
            r.font.color.rgb = rgb(35,35,35)
            rPr = r._r.get_or_add_rPr()
            rPr.set('spc', str(spc_val))

        add_rect(slide, cx, cy, cell_w-Cm(0.15), cell_h-Cm(0.1),
                 line_rgb=rgb(200,195,185))

# ─── SLIDE 17  Combined Spacing Matrix ───────────────────────────────────────
def slide_combined_matrix(prs):
    slide = add_slide(prs)
    add_rect(slide, 0, 0, A3_W, A3_H, fill_rgb=BG)
    header(slide, 16,
           "宋体综合实验  ·  行距 × 字距 矩阵对照",
           "3×3 矩阵  ·  行距 100% / 150% / 200%  ×  字距 0 / +100 / +300  ·  CDR · AI · PS 参数对照")
    footer(slide, "综合实验 / Combined Matrix  ·  宋体 SimSun 9pt  ·  CDR=CorelDRAW | AI=Illustrator | PS=Photoshop")

    line_spacings  = [(1.0,"100%"), (1.5,"150%"), (2.0,"200%")]
    char_spacings  = [(0,"字距0"), (10000,"字距+100"), (30000,"字距+300")]

    # label column/row sizes
    LC_W = Cm(2.0)   # row-label column width
    LR_H = Cm(0.8)   # col-label row height
    cell_w = (A3_W - Cm(1.4) - LC_W) / 3
    cell_h = (A3_H - Cm(4.2) - LR_H) / 3

    base_x = Cm(0.7) + LC_W
    base_y = Cm(2.6) + LR_H

    col_colors = [rgb(50,80,125), rgb(60,105,80), rgb(110,55,40)]
    row_colors = [rgb(80,60,110), rgb(50,95,80),  rgb(115,60,35)]

    # column headers
    for ci, (_, cs_lbl) in enumerate(char_spacings):
        hx = base_x + ci * cell_w
        add_rect(slide, hx, Cm(2.6), cell_w-Cm(0.1), LR_H, fill_rgb=col_colors[ci])
        add_tb(slide, hx+Cm(0.2), Cm(2.62), cell_w-Cm(0.4), LR_H-Cm(0.1),
               cs_lbl, 10, True, rgb(255,255,255), PP_ALIGN.CENTER, "SimHei")

    # row headers + cells
    sample = ["床前明月光，疑是地上霜。","举头望明月，低头思故乡。","欲穷千里目，更上一层楼。"]
    for ri, (ls, ls_lbl) in enumerate(line_spacings):
        ry = base_y + ri * cell_h
        # row label
        add_rect(slide, Cm(0.7), ry, LC_W-Cm(0.1), cell_h-Cm(0.1), fill_rgb=row_colors[ri])
        add_tb(slide, Cm(0.75), ry+Cm(0.5), LC_W-Cm(0.2), Cm(2),
               f"行距\n{ls_lbl}", 9, True, rgb(255,255,255), PP_ALIGN.CENTER, "SimHei")

        for ci, (cs_val, cs_lbl) in enumerate(char_spacings):
            cx = base_x + ci * cell_w
            bg = rgb(248,246,240) if (ri+ci)%2==0 else rgb(238,236,230)
            add_rect(slide, cx, ry, cell_w-Cm(0.1), cell_h-Cm(0.1),
                     fill_rgb=bg, line_rgb=rgb(200,195,185))

            # software annotation
            sw = (f"CDR: 行距{int(ls*100)}%  字距{cs_val//100}μ\n"
                  f"AI:  ×{ls}行间距  字距{cs_val//100}pt\n"
                  f"PS:  {int(ls*100)}%  间距{cs_val//100}pt")
            add_tb(slide, cx+Cm(0.15), ry+Cm(0.12), cell_w-Cm(0.3), Cm(1.0),
                   sw, 7, False, rgb(110,95,75), PP_ALIGN.LEFT, "Arial")

            # poem block
            tb = slide.shapes.add_textbox(int(cx+Cm(0.15)), int(ry+Cm(1.15)),
                                           int(cell_w-Cm(0.35)), int(cell_h-Cm(1.4)))
            tf = tb.text_frame
            tf.word_wrap = True
            first = True
            for line in sample:
                if first:
                    p = tf.paragraphs[0]; first = False
                else:
                    p = tf.add_paragraph()
                p.alignment = PP_ALIGN.LEFT
                pPr = p._p.get_or_add_pPr()
                lnSpc = etree.SubElement(pPr, ns.qn('a:lnSpc'))
                spc   = etree.SubElement(lnSpc, ns.qn('a:spcPct'))
                spc.set('val', str(int(ls * 100000)))
                r = p.add_run()
                r.text = line
                r.font.size = Pt(9)
                r.font.name = "SimSun"
                r.font.color.rgb = rgb(35,35,35)
                rPr = r._r.get_or_add_rPr()
                rPr.set('spc', str(cs_val))

# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    prs = new_prs()
    steps = [
        ("01 封面",                   slide_cover),
        ("02-05 色相环四类",          slides_color_wheels),
        ("06-08 拉丁字体30款",        slides_latin_fonts),
        ("09-10 汉字分类",            slides_chinese_fonts),
        ("11 汉字字号表",             slide_chinese_size_table),
        ("12 拉丁字号表",             slide_latin_size_table),
        ("13-14 行距实验",            slides_line_spacing),
        ("15 字距实验",               slide_char_spacing),
        ("16 综合矩阵",               slide_combined_matrix),
    ]
    for label, fn in steps:
        print(f"  Building {label}…")
        fn(prs)

    out = "/home/user/wendy/字体编排设计手册_A3横幅.pptx"
    prs.save(out)
    print(f"\n✓ Saved → {out}  ({len(prs.slides)} slides)")

if __name__ == "__main__":
    main()
