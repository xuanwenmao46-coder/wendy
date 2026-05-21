#!/usr/bin/env python3
"""
Typography Design Manual – SVG Generator
A3 横幅 420mm × 297mm，每页独立 SVG，Illustrator 可直接打开编辑
"""

import svgwrite
import colorsys
import os, zipfile

OUT_DIR = "/home/user/wendy/svg_manual"
os.makedirs(OUT_DIR, exist_ok=True)

# ── A3 坐标系：单位 mm，1mm = 1 SVG user unit ──────────────────────────────
W, H = 420, 297

# ── 调色板 ─────────────────────────────────────────────────────────────────
BG        = "#F9F7F3"
DARK      = "#161616"
GOLD      = "#E8C86A"
DIVIDER   = "#C8C3BA"
WHITE     = "#FFFFFF"
TXT_MAIN  = "#1E1E1E"
TXT_SUB   = "#6B6560"
TXT_LIGHT = "#A8A29C"

# ── 字体栈（Illustrator 会尝试本机字体，找不到可手动替换）────────────────
F_SANS    = "Helvetica Neue, Arial, sans-serif"
F_SERIF   = "Times New Roman, Georgia, serif"
F_ZH_SONG = "SimSun, STSong, serif"
F_ZH_HEI  = "SimHei, STHeiti, sans-serif"
F_ZH_YAO  = "Microsoft YaHei, PingFang SC, sans-serif"
F_ZH_KAI  = "KaiTi, STKaiti, cursive"

# ── 基础绘制函数 ───────────────────────────────────────────────────────────

def new_dwg(filename):
    d = svgwrite.Drawing(
        filename,
        size=(f"{W}mm", f"{H}mm"),
        viewBox=f"0 0 {W} {H}",
        profile="full",
    )
    d['xmlns:xlink'] = "http://www.w3.org/1999/xlink"
    return d

def rect(dwg, x, y, w, h, fill=BG, stroke="none", sw=0.2, rx=0, opacity=1):
    return dwg.rect(
        insert=(x, y), size=(w, h),
        fill=fill, stroke=stroke, stroke_width=sw,
        rx=rx, opacity=opacity,
    )

def text(dwg, content, x, y, size=4, fill=TXT_MAIN, font=F_SANS,
         weight="normal", anchor="start", italic=False):
    style = f"font-size:{size}mm;font-family:{font};font-weight:{weight};"
    if italic:
        style += "font-style:italic;"
    return dwg.text(
        content, insert=(x, y),
        fill=fill, text_anchor=anchor,
        style=style,
    )

def line(dwg, x1, y1, x2, y2, stroke=DIVIDER, sw=0.18):
    return dwg.line(start=(x1, y1), end=(x2, y2),
                    stroke=stroke, stroke_width=sw)

def cmyk_to_hex(c, m, y, k):
    r = int(255*(1-c/100)*(1-k/100))
    g = int(255*(1-m/100)*(1-k/100))
    b = int(255*(1-y/100)*(1-k/100))
    return f"#{max(0,r):02X}{max(0,g):02X}{max(0,b):02X}"

def luminance(hex_color):
    """Return perceived luminance 0-1 for choosing label text color."""
    h = hex_color.lstrip('#')
    r, g, b = int(h[0:2],16)/255, int(h[2:4],16)/255, int(h[4:6],16)/255
    return 0.299*r + 0.587*g + 0.114*b

# ── 页面共用的页眉页脚 ────────────────────────────────────────────────────

def draw_header(dwg, g, page_no, title, subtitle=""):
    g.add(rect(dwg, 0, 0, W, 14, fill=DARK))
    g.add(rect(dwg, 0, 14, W, 0.5, fill=GOLD))
    # 页码圆点
    g.add(dwg.circle(center=(9, 7), r=4.5, fill=GOLD))
    g.add(text(dwg, f"{page_no:02d}", 9, 9.2, size=4.2, fill=DARK,
               font=F_SANS, weight="bold", anchor="middle"))
    # 标题
    g.add(text(dwg, title, 18, 7.8, size=5.2, fill="#F5F0E1",
               font=F_ZH_HEI, weight="bold"))
    if subtitle:
        g.add(text(dwg, subtitle, 18, 12.2, size=3.2, fill="#A09890",
                   font=F_ZH_HEI))

def draw_footer(dwg, g, note=""):
    g.add(rect(dwg, 0, H-6, W, 6, fill="#E8E5DE"))
    g.add(line(dwg, 0, H-6, W, H-6, stroke="#C0BBB2", sw=0.3))
    g.add(text(dwg, note, 5, H-2, size=2.8, fill=TXT_SUB, font=F_ZH_SONG))
    g.add(text(dwg, f"Typography Design Manual  ·  A3 {W}×{H}mm",
               W-5, H-2, size=2.6, fill=TXT_LIGHT, font=F_SANS, anchor="end"))

# ═══════════════════════════════════════════════════════════════════════════
# 第 01 页：封面
# ═══════════════════════════════════════════════════════════════════════════
def page_cover():
    dwg = new_dwg(f"{OUT_DIR}/01_封面.svg")
    g = dwg.g(id="cover")

    # 背景
    g.add(rect(dwg, 0, 0, W, H, fill="#111111"))
    # 装饰金线
    g.add(rect(dwg, 0, H*0.62, W, 0.8, fill=GOLD))
    # 左侧金色竖条
    g.add(rect(dwg, 18, 28, 0.8, 60, fill=GOLD))

    # 主标题
    for i, line_txt in enumerate(["字体编排", "设计手册"]):
        g.add(text(dwg, line_txt, 22, 52+i*24, size=22, fill="#EED88A",
                   font=F_ZH_HEI, weight="bold"))

    # 英文副标题
    g.add(text(dwg, "Typography & Type Design Manual",
               22, 104, size=7.5, fill="#AAAA99", font=F_SANS))
    # 说明行
    g.add(text(dwg, "色彩系统  ·  拉丁字体  ·  汉字编排  ·  字号规范  ·  行距字距实验",
               22, 114, size=4.2, fill="#787068", font=F_ZH_SONG))

    # 目录标签
    tags = ["色相环 CMYK", "30款拉丁字体", "汉字8大类", "字号规范表", "行距·字距实验"]
    tag_colors = ["#8B6914","#2D5A9E","#2E7D52","#8B3520","#6B3D7A"]
    for ti, (tag, tc) in enumerate(zip(tags, tag_colors)):
        tx = 22 + ti*77
        g.add(rect(dwg, tx, 152, 72, 9, fill=tc, rx=1))
        g.add(text(dwg, tag, tx+4, 158.5, size=3.8, fill=WHITE,
                   font=F_ZH_HEI, weight="bold"))

    # 底部信息
    g.add(text(dwg, "公共场域与数字叙事（二）  ·  设计编排工作手册  ·  2025–2026",
               22, H-10, size=3.5, fill="#555045", font=F_ZH_SONG))

    # 装饰小方块群
    for xi in range(12):
        for yi in range(4):
            if (xi+yi)%3==0:
                g.add(rect(dwg, W-55+xi*4.5, 20+yi*4.5, 3.5, 3.5,
                           fill=GOLD, opacity=0.12+(xi%4)*0.05))

    dwg.add(g)
    dwg.save()
    print("  ✓ 01_封面.svg")

# ═══════════════════════════════════════════════════════════════════════════
# 第 02-05 页：色相环
# ═══════════════════════════════════════════════════════════════════════════

PURE_12 = [
    ("红",   (0,100,100,0)), ("红橙",(0,70,100,0)), ("橙",(0,50,100,0)),
    ("黄橙", (0,30,100,0)),  ("黄",  (0,0,100,0)),  ("黄绿",(40,0,100,0)),
    ("绿",   (100,0,100,0)), ("蓝绿",(100,0,40,0)), ("蓝", (100,60,0,0)),
    ("蓝紫", (80,80,0,0)),   ("紫",  (60,100,0,0)), ("红紫",(20,100,20,0)),
]
TINT_12 = [
    ("浅红",  (0,50,50,0)), ("浅红橙",(0,35,50,0)),("浅橙",(0,25,50,0)),
    ("浅黄橙",(0,15,50,0)), ("浅黄",  (0,0,50,0)),  ("浅黄绿",(20,0,50,0)),
    ("浅绿",  (50,0,50,0)), ("浅蓝绿",(50,0,20,0)), ("浅蓝",(50,30,0,0)),
    ("浅蓝紫",(40,40,0,0)), ("浅紫",  (30,50,0,0)), ("浅红紫",(10,50,10,0)),
]
TONE_12 = [
    ("浊红",  (0,70,70,30)), ("浊红橙",(0,50,70,30)),("浊橙",(0,35,70,30)),
    ("浊黄橙",(0,20,70,30)), ("浊黄",  (0,0,70,30)),  ("浊黄绿",(30,0,70,30)),
    ("浊绿",  (70,0,70,30)), ("浊蓝绿",(70,0,28,30)), ("浊蓝",(70,42,0,30)),
    ("浊蓝紫",(56,56,0,30)), ("浊紫",  (42,70,0,30)), ("浊红紫",(14,70,14,30)),
]
SHADE_12 = [
    ("暗红",  (0,100,100,40)),("暗红橙",(0,70,100,40)),("暗橙",(0,50,100,40)),
    ("暗黄橙",(0,30,100,40)), ("暗黄",  (0,0,100,40)), ("暗黄绿",(40,0,100,40)),
    ("暗绿",  (100,0,100,40)),("暗蓝绿",(100,0,40,40)),("暗蓝",(100,60,0,40)),
    ("暗蓝紫",(80,80,0,40)),  ("暗紫",  (60,100,0,40)),("暗红紫",(20,100,20,40)),
]

def page_color_wheel(page_no, svg_name, title, subtitle, colors_12,
                     shade_levels=None, footer_note=""):
    """
    shade_levels: None → 单色块; list of k_adjust → 绘制多层渐变色块
    """
    dwg = new_dwg(f"{OUT_DIR}/{svg_name}")
    g = dwg.g(id="page")
    g.add(rect(dwg, 0, 0, W, H, fill=BG))
    draw_header(dwg, g, page_no, title, subtitle)
    draw_footer(dwg, g, footer_note)

    n_cols = 6
    sw = (W - 14) / n_cols - 2        # swatch width
    sh_total = H - 14 - 6 - 16 - 22  # available swatch height (excl header/footer/label)
    sh_swatch = sh_total * 0.72        # color area
    sh_label  = sh_total * 0.28        # label area
    row_gap   = 4

    rows = [colors_12[:6], colors_12[6:]]
    row_total_h = sh_swatch + sh_label + row_gap

    for ri, row in enumerate(rows):
        for ci, (label, cmyk) in enumerate(row):
            cx = 7 + ci * (sw + 2)
            cy = 15 + ri * row_total_h + 2

            c, m, y, k = cmyk
            if shade_levels is None:
                hex_c = cmyk_to_hex(c, m, y, k)
                g.add(rect(dwg, cx, cy, sw, sh_swatch, fill=hex_c, rx=1.5))
            else:
                sub_h = sh_swatch / len(shade_levels)
                for si, k_adj in enumerate(shade_levels):
                    k2 = min(100, max(0, k + k_adj))
                    hex_c = cmyk_to_hex(c, m, y, k2)
                    sy = cy + si * sub_h
                    corner_top    = 1.5 if si == 0 else 0
                    corner_bottom = 1.5 if si == len(shade_levels)-1 else 0
                    # SVG clip-path workaround: just draw rect without individual corner radius
                    g.add(rect(dwg, cx, sy, sw, sub_h+0.1, fill=hex_c))
                # outline
                g.add(rect(dwg, cx, cy, sw, sh_swatch,
                           fill="none", stroke="#AAAAAA", sw=0.3, rx=1.5))

            # 色名
            lum = luminance(cmyk_to_hex(c, m, y, k))
            txt_col = "#1A1A1A"
            g.add(text(dwg, label,
                       cx + sw/2, cy + sh_swatch + 5.5,
                       size=4.2, fill=txt_col, font=F_ZH_HEI,
                       weight="bold", anchor="middle"))
            # CMYK 值
            cmyk_str = f"C{c}  M{m}  Y{y}  K{k}"
            g.add(text(dwg, cmyk_str,
                       cx + sw/2, cy + sh_swatch + 11,
                       size=3.0, fill=TXT_SUB, font=F_SANS, anchor="middle"))
            # 印刷色条（色值可视化小条）
            sub_colors = [(c,m,0,0,"C"),(0,m,0,0,"M"),(0,0,y,0,"Y"),(0,0,0,k,"K")]
            bar_total_w = sw - 6
            bar_w = bar_total_w / 4 - 0.8
            for bi, (bc,bm,by,bk,bl) in enumerate(sub_colors):
                bx = cx + 3 + bi*(bar_w+0.8)
                by2 = cy + sh_swatch + 13.5
                g.add(rect(dwg, bx, by2, bar_w, 3.0,
                           fill=cmyk_to_hex(bc,bm,by,bk), rx=0.5))
                g.add(text(dwg, bl, bx+bar_w/2, by2+2.3,
                           size=1.8, fill="#888", font=F_SANS, anchor="middle"))

    dwg.add(g)
    dwg.save()
    print(f"  ✓ {svg_name}")

# ═══════════════════════════════════════════════════════════════════════════
# 第 06-08 页：拉丁字体全字母编排
# ═══════════════════════════════════════════════════════════════════════════
LATIN_FONTS = [
    ( 1,"Helvetica",         "Helvetica Neue, Arial",    "无衬线","Swiss 721 BT"),
    ( 2,"Avant Garde",       "Century Gothic",            "无衬线","AvantGarde Bk BT"),
    ( 3,"Bell Centennial",   "Arial Narrow",              "无衬线","Bell Centennial Std"),
    ( 4,"Bell Gothic",       "Arial",                     "无衬线","Bell Gothic Std"),
    ( 5,"DIN",               "Arial, sans-serif",         "无衬线","DIN Next LT Pro"),
    ( 6,"Franklin Gothic",   "Franklin Gothic Medium",    "无衬线","Franklin Gothic Demi"),
    ( 7,"Frutiger",          "Gill Sans MT, Arial",       "无衬线","Humanist 777 BT"),
    ( 8,"Futura",            "Century Gothic",            "无衬线","Futura Bk BT"),
    ( 9,"Gill Sans",         "Gill Sans MT",              "无衬线","Gill Sans MT"),
    (10,"Eurostile",         "Arial",                     "无衬线","Eurostile BT"),
    (11,"Eras",              "Arial",                     "无衬线","Eras Medium ITC"),
    (12,"News Gothic",       "Arial Narrow",              "无衬线","News Gothic MT"),
    (13,"Optima",            "Gill Sans MT",              "无衬线","ZapfHumnsl BT"),
    (14,"Univers",           "Arial",                     "无衬线","Zurich BT"),
    (15,"VAG Rounded",       "Century Gothic",            "无衬线","VAG Rounded BT"),
    (16,"Caslon",            "Garamond, Georgia",         "有衬线","Adobe Caslon Pro"),
    (17,"Garamond",          "Garamond",                  "有衬线","Garamond"),
    (18,"Bembo",             "Georgia",                   "有衬线","Aldine 401 BT"),
    (19,"Bodoni",            "Bodoni MT, Didot",          "有衬线","Bodoni MT"),
    (20,"Clarendon",         "Georgia",                   "有衬线","Clarendon BT"),
    (21,"Courier PS",        "Courier New",               "有衬线","Courier New"),
    (22,"Excelsior",         "Century Schoolbook",        "有衬线","Century 791 BT"),
    (23,"Lucida Bright",     "Lucida Bright, Georgia",    "有衬线","Lucida Bright"),
    (24,"Minion",            "Garamond",                  "有衬线","Minion Pro"),
    (25,"Perpetua",          "Perpetua, Georgia",         "有衬线","Perpetua"),
    (26,"Sabon",             "Garamond",                  "有衬线","Class Garamond BT"),
    (27,"Stempel Schneidler","Georgia",                   "有衬线","Schneidler BT"),
    (28,"Times New Roman",   "Times New Roman",           "有衬线","Times New Roman"),
    (29,"Trajan",            "Trajan Pro, Perpetua",      "有衬线","Trajan Pro"),
    (30,"Modern No.20",      "Georgia",                   "有衬线","Modern No.20"),
]
ALPHA   = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
ALPHA_L = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
SYMB    = "0 1 2 3 4 5 6 7 8 9   ! ? & @ # $ % . , ; : — ( ) [ ]"

TAG_FILL = {"无衬线":"#2B508E", "有衬线":"#8B2E1E"}
TAG_DESC = {"无衬线":"Sans-Serif", "有衬线":"Serif"}

def page_latin_fonts(page_no, svg_name, fonts_10, title):
    dwg = new_dwg(f"{OUT_DIR}/{svg_name}")
    g = dwg.g(id="page")
    g.add(rect(dwg, 0, 0, W, H, fill=BG))
    draw_header(dwg, g, page_no, title,
                "完整字母表 A–Z  a–z  +  数字与常用符号")
    draw_footer(dwg, g, "字体标本 / Typeface Specimen  ·  字库版权归各字体公司所有  ·  仅供教学编排参考")

    row_h   = (H - 14 - 6 - 4) / 10  # 10 fonts per page
    y_start = 15.5

    NUM_W  = 14
    NAME_W = 38
    TAG_W  = 18
    SPEC_X = NUM_W + NAME_W + TAG_W + 7

    for ri, (no, name, font, cat, note) in enumerate(fonts_10):
        ry = y_start + ri * row_h
        bg = "#F5F3EE" if ri%2==0 else "#FDFBF8"
        g.add(rect(dwg, 3, ry, W-6, row_h-0.4, fill=bg, rx=0.8))

        # 编号
        g.add(text(dwg, f"{no:02d}", 5, ry+row_h*0.62,
                   size=6.5, fill="#C8AD70", font=F_SANS, weight="bold"))

        # 字体名
        g.add(text(dwg, name, 3+NUM_W, ry+row_h*0.38,
                   size=4.2, fill=TXT_MAIN, font=F_SANS, weight="bold"))
        # Corel 注记
        g.add(text(dwg, f"Corel: {note}", 3+NUM_W, ry+row_h*0.75,
                   size=2.6, fill=TXT_LIGHT, font=F_SANS))

        # 类别标签
        tc = TAG_FILL[cat]
        g.add(rect(dwg, 3+NUM_W+NAME_W, ry+row_h*0.18,
                   TAG_W-1, row_h*0.58, fill=tc, rx=1.2))
        g.add(text(dwg, f"{cat}", 3+NUM_W+NAME_W+TAG_W*0.5, ry+row_h*0.53,
                   size=3.0, fill=WHITE, font=F_ZH_HEI, anchor="middle"))
        g.add(text(dwg, TAG_DESC[cat], 3+NUM_W+NAME_W+TAG_W*0.5, ry+row_h*0.73,
                   size=2.4, fill="#CCCCCC", font=F_SANS, anchor="middle"))

        # 字母标本
        g.add(text(dwg, ALPHA, 3+SPEC_X, ry+row_h*0.38,
                   size=4.5, fill=TXT_MAIN, font=font))
        g.add(text(dwg, ALPHA_L, 3+SPEC_X, ry+row_h*0.62,
                   size=4.5, fill="#3A3530", font=font))
        g.add(text(dwg, SYMB, 3+SPEC_X, ry+row_h*0.85,
                   size=3.5, fill=TXT_SUB, font=font))

        # 分割线
        g.add(line(dwg, 3, ry+row_h-0.2, W-3, ry+row_h-0.2))

    dwg.add(g)
    dwg.save()
    print(f"  ✓ {svg_name}")

# ═══════════════════════════════════════════════════════════════════════════
# 第 09-10 页：汉字分类编排
# ═══════════════════════════════════════════════════════════════════════════
ZI_CATS_A = [
    ("有衬线体 Serif", "#7A2A20", [
        ("方正书宋  FZ ShuSong",   F_ZH_SONG, 5.8,
         "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。"),
        ("方正仿宋  FZ FangSong",  "FangSong, STFangsong, serif", 5.8,
         "海内存知己，天涯若比邻。无为在歧路，儿女共沾巾。"),
        ("汉仪中宋  HY ZhongSong", F_ZH_SONG, 5.8,
         "大漠孤烟直，长河落日圆。萧关逢候骑，都护在燕然。"),
        ("文鼎细宋  WT XiSong",    F_ZH_SONG, 5.8,
         "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。"),
    ]),
    ("无衬线体 Sans-Serif", "#1E4A8A", [
        ("方正黑体  FZ HeiTi",         F_ZH_HEI, 5.8,
         "会当凌绝顶，一览众山小。荡胸生层云，决眦入归鸟。"),
        ("汉仪黑体  HY HeiTi",         F_ZH_HEI, 5.8,
         "举头望明月，低头思故乡。床前明月光，疑是地上霜。"),
        ("方正兰亭黑  FZ LanTingHei",  F_ZH_YAO, 5.8,
         "烽火连三月，家书抵万金。白头搔更短，浑欲不胜簪。"),
        ("文鼎中黑  WT ZhongHei",      F_ZH_YAO, 5.8,
         "随风潜入夜，润物细无声。好雨知时节，当春乃发生。"),
    ]),
    ("圆体 Rounded", "#1A6E4A", [
        ("方正准圆  FZ ZhunYuan",  F_ZH_YAO, 5.8,
         "两岸猿声啼不住，轻舟已过万重山。"),
        ("汉仪圆体  HY YuanTi",   F_ZH_YAO, 5.8,
         "黄河之水天上来，奔流到海不复回。"),
        ("文鼎圆体  WT YuanTi",   F_ZH_YAO, 5.8,
         "天生我材必有用，千金散尽还复来。"),
    ]),
    ("手写体 Script", "#8A4510", [
        ("方正行楷  FZ XingKai",  "STXingkai, KaiTi, cursive", 5.8,
         "问君能有几多愁，恰似一江春水向东流。"),
        ("汉仪行楷  HY XingKai",  F_ZH_KAI, 5.8,
         "无边落木萧萧下，不尽长江滚滚来。"),
        ("文鼎行书  WT XingShu",  "STKaiti, KaiTi, cursive", 5.8,
         "飞流直下三千尺，疑是银河落九天。"),
    ]),
]

ZI_CATS_B = [
    ("古体 / 过渡体 Transitional", "#4A2878", [
        ("方正楷体  FZ KaiTi",    F_ZH_KAI, 5.8,
         "但愿人长久，千里共婵娟。明月几时有，把酒问青天。"),
        ("文鼎隶书  WT LiShu",   "STKaiti, serif", 5.8,
         "落霞与孤鹜齐飞，秋水共长天一色。"),
        ("汉仪魏碑  HY WeiBei",  F_ZH_SONG, 5.8,
         "羌笛何须怨杨柳，春风不度玉门关。"),
    ]),
    ("混合体 Hybrid", "#2E6630", [
        ("方正综艺体  FZ ZongYi", "STXingkai, cursive", 5.8,
         "桃花潭水深千尺，不及汪伦送我情。"),
        ("汉仪综艺体  HY ZongYi", "STXingkai, cursive", 5.8,
         "横看成岭侧成峰，远近高低各不同。"),
    ]),
    ("展示体 Display", "#8C2646", [
        ("方正粗圆  FZ CuYuan",    F_ZH_HEI, 5.8,
         "长风破浪会有时，直挂云帆济沧海。"),
        ("汉仪展宋  HY ZhanSong",  F_ZH_SONG, 5.8,
         "仰天大笑出门去，我辈岂是蓬蒿人。"),
        ("文鼎特明体  WT TeMing",  F_ZH_SONG, 5.8,
         "安得广厦千万间，大庇天下寒士俱欢颜。"),
    ]),
    ("超类别体 Super-Family", "#444444", [
        ("方正超粗黑  FZ ChaoHei", F_ZH_HEI, 7.0,
         "黄沙百战穿金甲，不破楼兰终不还。"),
        ("汉仪超黑  HY ChaoHei",  F_ZH_HEI, 7.0,
         "羌笛何须怨杨柳，春风不度玉门关。"),
        ("文鼎超圆  WT ChaoYuan", F_ZH_YAO, 7.0,
         "秦时明月汉时关，万里长征人未还。"),
    ]),
]

def page_chinese_fonts(page_no, svg_name, cats, title):
    dwg = new_dwg(f"{OUT_DIR}/{svg_name}")
    g = dwg.g(id="page")
    g.add(rect(dwg, 0, 0, W, H, fill=BG))
    draw_header(dwg, g, page_no, title,
                "字库参考：方正字库 / 汉仪字库 / 文鼎字库  ·  示例文本：中国古典诗词")
    draw_footer(dwg, g, "汉字字体分类 / Chinese Type Classification  ·  字体版权归各字库厂商所有")

    n_cols = 2
    col_w  = (W - 8) / n_cols
    y_curs = [15.5, 15.5]

    for ci, (cat_name, cat_color, fonts) in enumerate(cats):
        col = ci % n_cols
        cx  = 4 + col * col_w
        cy  = y_curs[col]

        # 类别标题栏
        g.add(rect(dwg, cx, cy, col_w-2, 7.5, fill=cat_color, rx=1.5))
        g.add(text(dwg, cat_name, cx+4, cy+5.3,
                   size=4.6, fill=WHITE, font=F_ZH_HEI, weight="bold"))
        cy += 8.5

        for fname, ffont, fsize, sample in fonts:
            # 字体名标签
            g.add(rect(dwg, cx+1, cy, col_w-4, 5, fill="#EDE9E0", rx=0.8))
            g.add(text(dwg, fname, cx+3, cy+3.6,
                       size=3.0, fill="#6B5535", font=F_ZH_SONG, weight="bold"))
            cy += 5.8

            # 示例文字（大）
            g.add(text(dwg, sample, cx+2, cy+fsize*0.9,
                       size=fsize, fill=TXT_MAIN, font=ffont))
            cy += fsize*1.05 + 2

            # 分割线
            g.add(line(dwg, cx+1, cy, cx+col_w-3, cy))
            cy += 2.5

        y_curs[col] = cy + 3

    dwg.add(g)
    dwg.save()
    print(f"  ✓ {svg_name}")

# ═══════════════════════════════════════════════════════════════════════════
# 第 11 页：汉字字号规范表
# ═══════════════════════════════════════════════════════════════════════════
HAOZU = [
    ("初号",42),("小初",36),("一号",26),("小一",24),
    ("二号",22),("小二",18),("三号",16),("小三",15),
    ("四号",14),("小四",12),("五号",10.5),("小五",9),
    ("六号",7.5),("小六",6.5),("七号",5.5),("八号",5),
]

def page_chinese_size_table():
    dwg = new_dwg(f"{OUT_DIR}/11_汉字字号规范表.svg")
    g = dwg.g(id="page")
    g.add(rect(dwg, 0, 0, W, H, fill=BG))
    draw_header(dwg, g, 11, "汉字字号规范表  ·  宋体 · 黑体 · 圆体",
                "号数（中文传统印刷）对照 PostScript pt 磅值  ·  初号 42pt → 八号 5pt")
    draw_footer(dwg, g, "字号规范 / Type Size Reference  ·  1pt ≈ 0.353mm  ·  号数为中国传统活字印刷规格")

    CH_FONTS = [
        ("宋体 SimSun",    F_ZH_SONG, "#6E3A10"),
        ("黑体 SimHei",    F_ZH_HEI,  "#1A3872"),
        ("圆体 YaHei",     F_ZH_YAO,  "#1A6440"),
    ]

    NO_W   = 14
    PT_W   = 16
    COL_W  = (W - 6 - NO_W - PT_W) / 3
    X0     = 3
    HDR_Y  = 15.5
    ROW_H  = (H - HDR_Y - 7.5) / (len(HAOZU)+1)

    # 表头
    for bi, (label, bfill) in enumerate([
        ("号数",DARK),("pt值",DARK),
        ("宋体 SimSun","#7A3810"),
        ("黑体 SimHei","#1A3872"),
        ("圆体 YaHei", "#1A6440"),
    ]):
        bx = X0 + (NO_W if bi>=1 else 0) + (PT_W if bi>=2 else 0) + (COL_W*(bi-2) if bi>=2 else 0)
        bw = NO_W if bi==0 else (PT_W if bi==1 else COL_W-0.5)
        g.add(rect(dwg, bx, HDR_Y, bw, ROW_H*0.9, fill=bfill, rx=1))
        g.add(text(dwg, label, bx+bw/2, HDR_Y+ROW_H*0.62,
                   size=3.5, fill=WHITE, font=F_ZH_HEI,
                   weight="bold", anchor="middle"))

    for ri, (hao, pt) in enumerate(HAOZU):
        ry = HDR_Y + ROW_H*(ri+1)
        bg = "#F5F3EE" if ri%2==0 else "#FDFBF8"
        g.add(rect(dwg, X0, ry, W-6, ROW_H-0.3, fill=bg))

        # 号数 / pt
        g.add(text(dwg, hao, X0+NO_W/2, ry+ROW_H*0.7,
                   size=3.8, fill="#7A5020", font=F_ZH_HEI,
                   weight="bold", anchor="middle"))
        g.add(text(dwg, f"{pt}pt", X0+NO_W+PT_W/2, ry+ROW_H*0.7,
                   size=3.4, fill=TXT_SUB, font=F_SANS, anchor="middle"))

        # 三种字体示例
        for fi, (_, ff, fc) in enumerate(CH_FONTS):
            fx = X0 + NO_W + PT_W + fi*COL_W
            disp = min(pt, ROW_H*0.85)
            g.add(text(dwg, "永字八法", fx+2, ry+ROW_H*0.78,
                       size=disp, fill=fc, font=ff))

        g.add(line(dwg, X0, ry+ROW_H-0.3, W-3, ry+ROW_H-0.3))

    dwg.add(g)
    dwg.save()
    print("  ✓ 11_汉字字号规范表.svg")

# ═══════════════════════════════════════════════════════════════════════════
# 第 12 页：拉丁字体字号表
# ═══════════════════════════════════════════════════════════════════════════
LATIN_6 = [
    ("Times New Roman",      "Times New Roman, serif",   "#8A3214"),
    ("Garamond",             "Garamond, serif",          "#6A2060"),
    ("Bodoni MT",            "Bodoni MT, Didot, serif",  "#4A1A6A"),
    ("Helvetica / Arial",    "Helvetica Neue, Arial",    "#1E4A9E"),
    ("Futura / Century Goth","Century Gothic, sans-serif","#1A6E7A"),
    ("Gill Sans MT",         "Gill Sans MT, sans-serif", "#1A6E40"),
]
LATIN_PTS = [6,7,8,9,10,11,12,14,16,18,20,24,28,32,36,42,48]

def page_latin_size_table():
    dwg = new_dwg(f"{OUT_DIR}/12_拉丁字体字号表.svg")
    g = dwg.g(id="page")
    g.add(rect(dwg, 0, 0, W, H, fill=BG))
    draw_header(dwg, g, 12, "常用拉丁字体字号对照表（6款）",
                "Times · Garamond · Bodoni · Helvetica · Futura · Gill Sans  ·  6pt → 48pt")
    draw_footer(dwg, g, "拉丁字体字号对照 / Latin Type Size Chart  ·  示例文本：Aa Bb Cc 123")

    PT_W  = 14
    COL_W = (W - 6 - PT_W) / len(LATIN_6)
    HDR_Y = 15.5
    ROW_H = (H - HDR_Y - 7.5) / (len(LATIN_PTS)+1)
    X0    = 3

    # 表头
    g.add(rect(dwg, X0, HDR_Y, PT_W, ROW_H*0.9, fill=DARK, rx=1))
    g.add(text(dwg, "pt", X0+PT_W/2, HDR_Y+ROW_H*0.65,
               size=3.5, fill=WHITE, font=F_SANS, anchor="middle"))
    for fi, (fname, _, fc) in enumerate(LATIN_6):
        fx = X0 + PT_W + fi*COL_W
        g.add(rect(dwg, fx, HDR_Y, COL_W-0.5, ROW_H*0.9, fill=fc, rx=1))
        g.add(text(dwg, fname, fx + COL_W/2, HDR_Y+ROW_H*0.65,
                   size=3.0, fill=WHITE, font=F_SANS,
                   weight="bold", anchor="middle"))

    for ri, lpt in enumerate(LATIN_PTS):
        ry = HDR_Y + ROW_H*(ri+1)
        bg = "#F5F3EE" if ri%2==0 else "#FDFBF8"
        g.add(rect(dwg, X0, ry, W-6, ROW_H-0.3, fill=bg))
        g.add(text(dwg, f"{lpt}pt", X0+PT_W/2, ry+ROW_H*0.7,
                   size=3.5, fill="#7A5020", font=F_SANS,
                   weight="bold", anchor="middle"))
        for fi, (_, ff, fc) in enumerate(LATIN_6):
            fx = X0 + PT_W + fi*COL_W
            disp = min(lpt, ROW_H*0.82)
            g.add(text(dwg, "Aa Bb 123", fx+1, ry+ROW_H*0.78,
                       size=disp, fill=TXT_MAIN, font=ff))
        g.add(line(dwg, X0, ry+ROW_H-0.3, W-3, ry+ROW_H-0.3))

    dwg.add(g)
    dwg.save()
    print("  ✓ 12_拉丁字体字号表.svg")

# ═══════════════════════════════════════════════════════════════════════════
# 第 13-14 页：行距实验
# ═══════════════════════════════════════════════════════════════════════════
POEM = [
    "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
    "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    "欲穷千里目，更上一层楼。白日依山尽，黄河入海流。",
    "海内存知己，天涯若比邻。无为在歧路，儿女共沾巾。",
    "会当凌绝顶，一览众山小。荡胸生层云，决眦入归鸟。",
]

CELL_COLORS = ["#3E3268","#2A5580","#2A6848"]

def page_line_spacing(page_no, svg_name, configs, title, subtitle):
    dwg = new_dwg(f"{OUT_DIR}/{svg_name}")
    g = dwg.g(id="page")
    g.add(rect(dwg, 0, 0, W, H, fill=BG))
    draw_header(dwg, g, page_no, title, subtitle)
    draw_footer(dwg, g, "行距实验 / Line Spacing  ·  宋体 SimSun  ·  CDR=CorelDRAW  AI=Illustrator  PS=Photoshop")

    n = len(configs)
    n_cols = 3
    n_rows = (n + n_cols-1)//n_cols
    cell_w = (W - 6) / n_cols
    cell_h = (H - 14 - 7) / n_rows
    Y0 = 15.5

    for ci, (label, pt_size, ls_factor) in enumerate(configs):
        col = ci % n_cols
        row = ci // n_cols
        cx = 3 + col*cell_w
        cy = Y0 + row*cell_h

        # 色标
        bar_col = CELL_COLORS[col%3]
        g.add(rect(dwg, cx+0.5, cy+0.5, cell_w-1.5, 6.5, fill=bar_col, rx=1.5))
        g.add(text(dwg, label, cx+2.5, cy+4.0,
                   size=3.5, fill=WHITE, font=F_ZH_HEI, weight="bold"))
        sw_lbl = f"CDR:{int(ls_factor*100)}%  AI:×{ls_factor}  PS:{int(ls_factor*100)}%"
        g.add(text(dwg, sw_lbl, cx+2.5, cy+6.2,
                   size=2.4, fill="#CCCCCC", font=F_SANS))

        # 正文（用 tspan 模拟行距）
        line_gap = pt_size * ls_factor * 0.353  # mm
        base_y   = cy + 9.5
        txt_grp  = dwg.g(id=f"txt_{ci}")
        for li, poem_line in enumerate(POEM):
            txt_grp.add(text(dwg, poem_line,
                             cx+2.5, base_y + li*line_gap,
                             size=pt_size*0.353, fill=TXT_MAIN, font=F_ZH_SONG))
        g.add(txt_grp)

        # 外框
        g.add(rect(dwg, cx+0.5, cy+0.5, cell_w-1.5, cell_h-1,
                   fill="none", stroke="#C0BBB2", sw=0.4, rx=1.5))

    dwg.add(g)
    dwg.save()
    print(f"  ✓ {svg_name}")

# ═══════════════════════════════════════════════════════════════════════════
# 第 15 页：字距实验
# ═══════════════════════════════════════════════════════════════════════════
KERN_POEM = [
    "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
    "欲穷千里目，更上一层楼。白日依山尽，黄河入海流。",
    "海内存知己，天涯若比邻。无为在歧路，儿女共沾巾。",
]

def page_char_spacing():
    dwg = new_dwg(f"{OUT_DIR}/15_字距实验.svg")
    g = dwg.g(id="page")
    g.add(rect(dwg, 0, 0, W, H, fill=BG))
    draw_header(dwg, g, 15, "宋体字距实验  ·  紧缩 −50 → 极疏 +500",
                "8级字距对比  ·  字号固定 9pt  ·  参考软件：CDR / AI / PS")
    draw_footer(dwg, g, "字距实验 / Character Spacing  ·  宋体 SimSun 9pt  ·  CDR=字距微调(μ) | AI=字距调整(pt) | PS=字符间距(pt)")

    configs = [
        ("字距 −50  紧缩 Tight",  "-50", "letter-spacing:-1.8mm"),
        ("字距   0  标准 Normal",  "0",   "letter-spacing:0mm"),
        ("字距 +50  加宽",        "+50",  "letter-spacing:1.8mm"),
        ("字距 +100",            "+100",  "letter-spacing:3.5mm"),
        ("字距 +150",            "+150",  "letter-spacing:5.3mm"),
        ("字距 +200",            "+200",  "letter-spacing:7mm"),
        ("字距 +300  疏松 Loose","+300",  "letter-spacing:10.5mm"),
        ("字距 +500  极疏",      "+500",  "letter-spacing:17.5mm"),
    ]

    n_cols = 2
    cell_w = (W-6)/n_cols
    cell_h = (H - 14 - 7)/4
    Y0     = 15.5
    bar_colors = ["#30604A","#3D3568"]

    for ci, (label, val, ls_style) in enumerate(configs):
        col = ci % n_cols
        row = ci // n_cols
        cx  = 3 + col*cell_w
        cy  = Y0 + row*cell_h

        g.add(rect(dwg, cx+0.5, cy+0.5, cell_w-1.5, 6.5,
                   fill=bar_colors[col%2], rx=1.5))
        g.add(text(dwg, label, cx+2.5, cy+3.8,
                   size=3.5, fill=WHITE, font=F_ZH_HEI, weight="bold"))
        sw_lbl = f"CDR:{val}μ  AI:{val}pt  PS:{val}pt"
        g.add(text(dwg, sw_lbl, cx+2.5, cy+6.0,
                   size=2.4, fill="#CCCCCC", font=F_SANS))

        # 诗文（用 SVG letter-spacing）
        font_mm = 9*0.353
        for li, line_txt in enumerate(KERN_POEM):
            style_str = f"font-size:{font_mm}mm;font-family:{F_ZH_SONG};{ls_style};"
            g.add(dwg.text(line_txt,
                           insert=(cx+2.5, cy+9.5+li*font_mm*1.6),
                           fill=TXT_MAIN,
                           style=style_str))

        g.add(rect(dwg, cx+0.5, cy+0.5, cell_w-1.5, cell_h-1,
                   fill="none", stroke="#C0BBB2", sw=0.4, rx=1.5))

    dwg.add(g)
    dwg.save()
    print("  ✓ 15_字距实验.svg")

# ═══════════════════════════════════════════════════════════════════════════
# 第 16 页：综合矩阵
# ═══════════════════════════════════════════════════════════════════════════
def page_combined_matrix():
    dwg = new_dwg(f"{OUT_DIR}/16_综合矩阵_行距×字距.svg")
    g = dwg.g(id="page")
    g.add(rect(dwg, 0, 0, W, H, fill=BG))
    draw_header(dwg, g, 16, "宋体综合实验  ·  行距 × 字距 矩阵对照",
                "3×3 矩阵  ·  行距 100%/150%/200%  ×  字距 0/+100/+300  ·  CDR · AI · PS 参数")
    draw_footer(dwg, g, "综合实验 / Combined Matrix  ·  宋体 SimSun 9pt  ·  CDR=CorelDRAW | AI=Illustrator | PS=Photoshop")

    LS_LIST = [(1.0,"100%"),(1.5,"150%"),(2.0,"200%")]
    CS_LIST = [(0,"字距 0"),("1.8mm","字距 +50"),("3.5mm","字距 +100")]
    CS_LS   = ["letter-spacing:0mm","letter-spacing:1.8mm","letter-spacing:3.5mm"]
    CS_VAL  = [0, 50, 100]

    LC_W   = 14      # row-label width (mm)
    LR_H   = 8       # col-label height
    Y0     = 15.5
    cell_w = (W - 6 - LC_W) / 3
    cell_h = (H - Y0 - 7 - LR_H) / 3

    col_colors = ["#304880","#306050","#803020"]
    row_colors = ["#502870","#2A6030","#803820"]

    # 列标题
    for ci, (_, cs_lbl) in enumerate(CS_LIST):
        hx = 3+LC_W + ci*cell_w
        g.add(rect(dwg, hx+0.2, Y0, cell_w-0.4, LR_H-0.5, fill=col_colors[ci], rx=1.5))
        g.add(text(dwg, cs_lbl, hx+cell_w/2, Y0+LR_H*0.65,
                   size=4.0, fill=WHITE, font=F_ZH_HEI, weight="bold", anchor="middle"))

    sample = ["床前明月光，疑是地上霜。",
              "举头望明月，低头思故乡。",
              "欲穷千里目，更上一层楼。"]
    font_mm = 9*0.353

    for ri, (ls, ls_lbl) in enumerate(LS_LIST):
        ry = Y0 + LR_H + ri*cell_h
        # 行标题
        g.add(rect(dwg, 3, ry+0.2, LC_W-0.5, cell_h-0.4, fill=row_colors[ri], rx=1.5))
        g.add(text(dwg, f"行距\n{ls_lbl}", 3+LC_W*0.5, ry+cell_h*0.4,
                   size=3.8, fill=WHITE, font=F_ZH_HEI, weight="bold", anchor="middle"))

        for ci, (cs_ls, _, cs_v) in enumerate(zip(CS_LS, CS_LIST, CS_VAL)):
            cx  = 3+LC_W + ci*cell_w
            bg  = "#F0EEE8" if (ri+ci)%2==0 else "#E8E5DE"
            g.add(rect(dwg, cx+0.2, ry+0.2, cell_w-0.4, cell_h-0.4,
                       fill=bg, stroke=DIVIDER, sw=0.4, rx=1))

            # 软件参数注记
            sw_note = (f"CDR: 行距{int(ls*100)}%  字距{cs_v}μ\n"
                       f"AI: ×{ls}  字距{cs_v}pt\n"
                       f"PS: {int(ls*100)}%  间距{cs_v}pt")
            for si, note_line in enumerate(sw_note.split("\n")):
                g.add(text(dwg, note_line, cx+2, ry+1.5+si*3.0,
                           size=2.5, fill="#9A8A70", font=F_SANS))

            # 正文示例
            line_gap = font_mm * ls
            for li, poem_line in enumerate(sample):
                style_str = f"font-size:{font_mm}mm;font-family:{F_ZH_SONG};{cs_ls};"
                g.add(dwg.text(poem_line,
                               insert=(cx+2, ry+11+li*line_gap),
                               fill=TXT_MAIN, style=style_str))

    dwg.add(g)
    dwg.save()
    print("  ✓ 16_综合矩阵_行距×字距.svg")

# ═══════════════════════════════════════════════════════════════════════════
# 打包 ZIP
# ═══════════════════════════════════════════════════════════════════════════
def make_zip():
    zip_path = "/home/user/wendy/字体编排设计手册_SVG.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for fname in sorted(os.listdir(OUT_DIR)):
            if fname.endswith('.svg'):
                zf.write(os.path.join(OUT_DIR, fname),
                         arcname=f"字体编排设计手册/{fname}")
    print(f"\n  ✓ ZIP → {zip_path}")
    return zip_path

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    print("生成 SVG 页面…\n")

    page_cover()

    # 色相环 4 页
    page_color_wheel(2,"02_纯色色相环.svg",
                     "色相环 · 纯色系（Pure Hue）",
                     "12色相  ·  CMYK 标准色值  ·  色相角 0°→330°（每30°一色）",
                     PURE_12, None,
                     "纯色色相环 / Pure Hue  ·  基于 ISO 12647 印刷四色 CMYK 标准")
    page_color_wheel(3,"03_混白淡色调.svg",
                     "色相环 · 混白淡色调（Tint）",
                     "纯色 + 白色混合  ·  展示 25% / 50% / 75% 三级明度梯度",
                     TINT_12, [0, 0, 0],
                     "混白淡色调 / Tint  ·  C/M/Y 降低至 25%→75%  ·  CMYK 印刷参考值")
    page_color_wheel(4,"04_混灰浊色调.svg",
                     "色相环 · 混灰浊色调（Tone）",
                     "纯色 + 中性灰  ·  展示 K+10 / K+20 / K+30 三级灰度叠加",
                     TONE_12, [-20, -10, 0],
                     "混灰浊色调 / Tone  ·  增加 K 值模拟加灰效果  ·  CMYK 印刷参考值")
    page_color_wheel(5,"05_混黑暗色调.svg",
                     "色相环 · 混黑暗色调（Shade）",
                     "纯色 + 黑色  ·  展示 K+20 / K+40 / K+60 三级加深梯度",
                     SHADE_12, [-20, 0, 20],
                     "混黑暗色调 / Shade  ·  K 值叠加加深色相  ·  CMYK 印刷参考值")

    # 拉丁字体 3 页
    page_latin_fonts(6,"06_拉丁字体01-10.svg", LATIN_FONTS[0:10],
                     "常用拉丁字体全字母编排（01–10）无衬线体")
    page_latin_fonts(7,"07_拉丁字体11-20.svg", LATIN_FONTS[10:20],
                     "常用拉丁字体全字母编排（11–20）无衬线体·有衬线体")
    page_latin_fonts(8,"08_拉丁字体21-30.svg", LATIN_FONTS[20:30],
                     "常用拉丁字体全字母编排（21–30）有衬线体")

    # 汉字分类 2 页
    page_chinese_fonts(9,"09_汉字分类一.svg", ZI_CATS_A,
                       "汉字字体分类编排（一）有衬线·无衬线·圆体·手写体")
    page_chinese_fonts(10,"10_汉字分类二.svg", ZI_CATS_B,
                       "汉字字体分类编排（二）古体·过渡·混合·展示·超类别")

    # 字号表 2 页
    page_chinese_size_table()
    page_latin_size_table()

    # 行距实验 2 页
    page_line_spacing(13,"13_行距实验一_9pt.svg",
        [("9pt  行距 100%", 9, 1.0),
         ("9pt  行距 125%", 9, 1.25),
         ("9pt  行距 150%", 9, 1.5),
         ("9pt  行距 175%", 9, 1.75),
         ("9pt  行距 200%", 9, 2.0),
         ("9pt  行距 250%", 9, 2.5)],
        "宋体行距实验（一）· 9pt × 行距 100%–250%",
        "固定 9pt  ·  六级行距对比  ·  观察段落密度与阅读节奏变化")

    page_line_spacing(14,"14_行距实验二_10_12pt.svg",
        [("10pt 行距 100%",10,1.0),
         ("10pt 行距 150%",10,1.5),
         ("10pt 行距 200%",10,2.0),
         ("12pt 行距 100%",12,1.0),
         ("12pt 行距 150%",12,1.5),
         ("12pt 行距 200%",12,2.0)],
        "宋体行距实验（二）· 10pt / 12pt × 行距 100%–200%",
        "字号增大时行距配合关系  ·  对比 10pt 与 12pt 的版面节奏差异")

    # 字距 + 综合
    page_char_spacing()
    page_combined_matrix()

    # 打包
    zip_path = make_zip()
    import os
    size_kb = os.path.getsize(zip_path)//1024
    n_svg   = len([f for f in os.listdir(OUT_DIR) if f.endswith('.svg')])
    print(f"\n✓ 完成：{n_svg} 个 SVG 页面  ·  ZIP 大小 {size_kb} KB")

if __name__ == "__main__":
    main()
