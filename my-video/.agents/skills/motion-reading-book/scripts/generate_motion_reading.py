#!/usr/bin/env python3
"""
motion-reading-book generator
Fills motion_reading_template.html with book-specific parameters.
"""

import argparse
import os
import re
import sys
import json
import shutil
from pathlib import Path

GENRE_PALETTES = {
    "fantasy":  dict(bg="#0D1427", panel="#E8DFC8", accent="#9B1515", gold="#C9A050",
                     ink="#1A1A2E", text="#EDE8D0"),
    "scifi":    dict(bg="#080E1C", panel="#D0DFF0", accent="#0D4FA0", gold="#40C4C4",
                     ink="#0A1830", text="#D8ECF8"),
    "thriller": dict(bg="#0D0D0D", panel="#F0F0F0", accent="#C41A1A", gold="#AAAAAA",
                     ink="#111111", text="#F0F0F0"),
    "romance":  dict(bg="#1A0A12", panel="#F5E4E8", accent="#8B1A3A", gold="#D4967A",
                     ink="#2A0A18", text="#F5E4EE"),
    "literary": dict(bg="#0F1208", panel="#F0EDE0", accent="#1A4A20", gold="#C8A456",
                     ink="#0F1208", text="#EDEAD8"),
}

def parse_args():
    p = argparse.ArgumentParser(description="Generate a Motion Reading book video HTML")
    p.add_argument("--book-title",        default="BOOK TITLE")
    p.add_argument("--title-line1",       default="BOOK")
    p.add_argument("--title-line2",       default="TITLE")
    p.add_argument("--author",            default="Author Name")
    p.add_argument("--year",              default="2024")
    p.add_argument("--series-name",       default="Motion Reading")
    p.add_argument("--series-no",         default="01")
    p.add_argument("--genre",             default="fantasy",
                   choices=list(GENRE_PALETTES.keys()))
    # colors (override genre palette)
    p.add_argument("--color-bg",          default=None)
    p.add_argument("--color-panel",       default=None)
    p.add_argument("--color-accent",      default=None)
    p.add_argument("--color-gold",        default=None)
    p.add_argument("--color-ink",         default=None)
    p.add_argument("--color-text",        default=None)
    # content
    p.add_argument("--key-quote",         default='"A great book opens a window."')
    p.add_argument("--quote-speaker",     default="Author · Chapter One")
    p.add_argument("--protagonist",       default="HERO")
    p.add_argument("--protagonist-traits",
                   default="BORN TO|TWO WORLDS,MARKED|BY FATE,TESTED|BY FIRE,RETURNED|TO LIGHT,YOU ARE|THE ONE",
                   help="5 traits separated by commas, each trait 2 lines separated by |")
    p.add_argument("--antagonist-lines",  default="THE,DARK,FORCE",
                   help="3 lines for antagonist name, comma-separated")
    p.add_argument("--antagonist-bio",    default="The Shadow · Origin Unknown|Alignment: Chaos")
    p.add_argument("--closing-word",      default="Always.")
    p.add_argument("--closing-quote",     default='"After all this time?"')
    p.add_argument("--closing-speaker",   default="Unknown · Final Chapter")
    p.add_argument("--stats-number",      default="1,234")
    p.add_argument("--stats-label",       default="PAGES · WORDS · CHAPTERS")
    p.add_argument("--book-bars",         default="100,150,200,320,480,350,400",
                   help="7 page counts, comma-separated (used for bar chart heights)")
    p.add_argument("--book-labels",       default="B1,B2,B3,B4,B5,B6,B7",
                   help="7 book abbreviations, comma-separated")
    p.add_argument("--peak-bar",          type=int, default=4,
                   help="0-indexed position of tallest bar (gets highlight badge)")
    p.add_argument("--peak-label",        default="PEAK")
    p.add_argument("--endcard-quote",     default='"The best books leave you changed."')
    # images
    p.add_argument("--img-protagonist",   default="assets/protagonist.png")
    p.add_argument("--img-antagonist",    default="assets/antagonist.png")
    p.add_argument("--img-emotional",     default="assets/emotional.png")
    # output
    p.add_argument("--output",            default="index.html")
    p.add_argument("--copy-assets",       action="store_true",
                   help="Copy image files into the same directory as output")
    return p.parse_args()


def compute_bar_heights(page_counts, max_height=300):
    """Scale page counts to pixel bar heights, max bar = max_height px."""
    pages = [int(x) for x in page_counts]
    mx = max(pages)
    return [max(30, round(p / mx * max_height)) for p in pages]


def bar_colors(labels, heights, accent, text_color):
    """Return list of CSS background colors: taller bars get accent color."""
    max_h = max(heights)
    threshold = max_h * 0.6
    return [accent if h >= threshold else text_color for h in heights]


def build_protagonist_annotations(traits_str):
    """Parse '5 traits' string into list of (line1, line2) tuples."""
    parts = traits_str.split(",")
    result = []
    for t in parts[:5]:
        lines = t.strip().split("|")
        result.append((lines[0].strip(), lines[1].strip() if len(lines) > 1 else ""))
    while len(result) < 5:
        result.append(("TRAIT", "UNKNOWN"))
    return result


def render_template(template: str, replacements: dict) -> str:
    for key, val in replacements.items():
        template = template.replace("{{" + key + "}}", str(val))
    return template


def main():
    args = parse_args()

    # Resolve palette
    palette = dict(GENRE_PALETTES[args.genre])
    for k, attr in [("bg","color_bg"),("panel","color_panel"),("accent","color_accent"),
                    ("gold","color_gold"),("ink","color_ink"),("text","color_text")]:
        v = getattr(args, attr)
        if v:
            palette[k] = v

    # Bar data
    bar_pages = [x.strip() for x in args.book_bars.split(",")]
    bar_labels = [x.strip() for x in args.book_labels.split(",")]
    while len(bar_labels) < 7: bar_labels.append(f"B{len(bar_labels)+1}")
    while len(bar_pages) < 7: bar_pages.append("100")
    bar_heights = compute_bar_heights(bar_pages[:7])
    bar_clrs = bar_colors(bar_labels[:7], bar_heights, palette["accent"], palette["text"])

    # Peak bar position (pixels from bottom baseline)
    peak_idx = min(args.peak_bar, 6)
    peak_left_positions = [60, 280, 500, 720, 940, 1160, 1380]
    peak_bottom = bar_heights[peak_idx] + 56  # 48px baseline offset + 8px gap

    # Protagonist annotations
    traits = build_protagonist_annotations(args.protagonist_traits)

    # Antagonist lines
    ant_lines = [x.strip() for x in args.antagonist_lines.split(",")]
    while len(ant_lines) < 3: ant_lines.append("")
    ant_bio_lines = args.antagonist_bio.replace("|", "<br>")

    # Build bar CSS blocks
    bl_css_parts = []
    bl_left = [60, 280, 500, 720, 940, 1160, 1380]
    for i, (h, c, lx) in enumerate(zip(bar_heights, bar_clrs, bl_left)):
        bl_css_parts.append(f"#bl{i+1}{{left:{lx}px;height:{h}px;background:{c};}}")
    bl_css = " ".join(bl_css_parts)

    # Build bar page-count CSS positions
    bp_css_parts = []
    for i, (h, lx) in enumerate(zip(bar_heights, bl_left)):
        bp_css_parts.append(f"#bp{i+1}{{bottom:{h+53}px;left:{lx}px;}}")
    bp_css = " ".join(bp_css_parts)

    # Bar HTML (labels + page numbers)
    ba_html = "".join(
        f'<div class="bab" id="ba{i+1}">{bar_labels[i]}</div>'
        for i in range(7)
    )
    bp_html = "".join(
        f'<div class="bpg" id="bp{i+1}">{bar_pages[i]}</div>'
        for i in range(7)
    )

    # Protagonist letter CSS (staggered tops)
    letter_tops  = [55, 152, 82, 165, 105]
    letter_lefts = [0, 178, 356, 534, 712]
    prot_letters = list(args.protagonist.upper()[:5])
    while len(prot_letters) < 5: prot_letters.append("")
    letter_css = " ".join(
        f"#l{i}{{top:{letter_tops[i]}px;left:{letter_lefts[i]}px;}}"
        for i in range(5)
    )
    letter_html = "".join(
        f'<div class="lt" id="l{i}">{prot_letters[i]}</div>'
        for i in range(5)
    )

    # Annotation CSS + HTML (anchored 265px below letter top)
    ann_ids = ["ah","aa","ar1","ar2","ay"]
    ann_css = " ".join(
        f"#{ann_ids[i]}{{top:{letter_tops[i]+267}px;left:{letter_lefts[i]+6}px;}}"
        for i in range(5)
    )
    ann_html = "".join(
        f'<div class="an" id="{ann_ids[i]}">{traits[i][0]}<br>{traits[i][1]}</div>'
        for i in range(5)
    )

    # Closingword color: use gold
    gold = palette["gold"]

    replacements = {
        # palette
        "COLOR_BG":      palette["bg"],
        "COLOR_PANEL":   palette["panel"],
        "COLOR_ACCENT":  palette["accent"],
        "COLOR_GOLD":    gold,
        "COLOR_INK":     palette["ink"],
        "COLOR_TEXT":    palette["text"],
        # rgba versions of accent (used in shadows)
        "COLOR_ACCENT_R": int(palette["accent"][1:3], 16),
        "COLOR_ACCENT_G": int(palette["accent"][3:5], 16),
        "COLOR_ACCENT_B": int(palette["accent"][5:7], 16),
        "COLOR_GOLD_R":  int(gold[1:3], 16),
        "COLOR_GOLD_G":  int(gold[3:5], 16),
        "COLOR_GOLD_B":  int(gold[5:7], 16),
        # book info
        "BOOK_TITLE":    args.book_title,
        "TITLE_LINE1":   args.title_line1.upper(),
        "TITLE_LINE2":   args.title_line2.upper(),
        "AUTHOR":        args.author,
        "YEAR":          args.year,
        "SERIES_NAME":   args.series_name,
        "SERIES_NO":     args.series_no.zfill(2),
        # content
        "KEY_QUOTE":     args.key_quote,
        "QUOTE_SPEAKER": args.quote_speaker,
        "PROTAGONIST":   args.protagonist.upper(),
        "ANTAGONIST_L1": ant_lines[0].upper(),
        "ANTAGONIST_L2": ant_lines[1].upper(),
        "ANTAGONIST_L3": ant_lines[2].upper(),
        "ANTAGONIST_BIO":    ant_bio_lines,
        "ANTAGONIST_QUOTE":  f"I AM {ant_lines[0].upper()} {ant_lines[1].upper()}{ant_lines[2].upper()}",
        "CLOSING_WORD":  args.closing_word,
        "CLOSING_QUOTE": args.closing_quote,
        "CLOSING_SPEAKER": args.closing_speaker,
        "STATS_NUMBER":  args.stats_number,
        "STATS_LABEL":   args.stats_label,
        "PEAK_LEFT":     peak_left_positions[peak_idx] - 30,
        "PEAK_BOTTOM":   peak_bottom,
        "PEAK_LABEL":    args.peak_label,
        "ENDCARD_QUOTE": args.endcard_quote,
        # images
        "IMG_PROTAGONIST": args.img_protagonist,
        "IMG_ANTAGONIST":  args.img_antagonist,
        "IMG_EMOTIONAL":   args.img_emotional,
        # generated CSS/HTML blocks
        "BAR_CSS":     bl_css,
        "BARPG_CSS":   bp_css,
        "LETTER_CSS":  letter_css,
        "ANN_CSS":     ann_css,
        "LETTER_HTML": letter_html,
        "ANN_HTML":    ann_html,
        "BA_HTML":     ba_html,
        "BP_HTML":     bp_html,
    }

    # Load template
    skill_dir = Path(__file__).parent.parent
    template_path = skill_dir / "assets" / "motion_reading_template.html"
    if not template_path.exists():
        print(f"ERROR: template not found at {template_path}", file=sys.stderr)
        sys.exit(1)

    template = template_path.read_text(encoding="utf-8")
    output_html = render_template(template, replacements)

    # Write output
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output_html, encoding="utf-8")

    if args.copy_assets:
        out_dir = out_path.parent / "assets"
        out_dir.mkdir(exist_ok=True)
        for img_arg in [args.img_protagonist, args.img_antagonist, args.img_emotional]:
            src = Path(img_arg)
            if src.exists():
                shutil.copy2(src, out_dir / src.name)

    print(str(out_path.resolve()))


if __name__ == "__main__":
    main()
