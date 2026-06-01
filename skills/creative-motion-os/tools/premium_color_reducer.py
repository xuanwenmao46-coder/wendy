"""
PremiumColorReducer — CIELAB-space Swiss/Morandi Color Enforcement
Part of Creative Motion Operating System V5

Intercepts any AI-generated RGB color and maps it to the nearest color in a
curated premium palette using CIE L*a*b* Delta E distance (perceptually uniform,
not raw RGB distance). No scikit-image dependency — pure numpy implementation.

Usage:
    # As a module
    reducer = PremiumColorReducer()
    rgb_out = reducer.map_to_premium_color([0, 0, 255])   # maps cheap blue → premium

    # CLI — single color
    python premium_color_reducer.py --rgb 0,0,255

    # CLI — batch from JSON
    python premium_color_reducer.py --batch colors.json --out mapped.json

    # CLI — show full palette
    python premium_color_reducer.py --palette
"""

import numpy as np
import json
import argparse
import sys


# ─────────────────────────────────────────────────────────────────────────────
# CIELAB conversion (pure numpy, no skimage required)
# Implements IEC 61966-2-1 sRGB → CIE L*a*b* D65
# ─────────────────────────────────────────────────────────────────────────────

def _srgb_to_linear(c: np.ndarray) -> np.ndarray:
    """sRGB gamma expansion (IEC 61966-2-1)."""
    c = c.astype(np.float64)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _linear_to_xyz(rgb_linear: np.ndarray) -> np.ndarray:
    """Linear sRGB → CIE XYZ (D65 illuminant, IEC 61966-2-1 matrix)."""
    M = np.array([
        [0.4124564, 0.3575761, 0.1804375],
        [0.2126729, 0.7151522, 0.0721750],
        [0.0193339, 0.1191920, 0.9503041],
    ])
    return rgb_linear @ M.T


def _xyz_to_lab(xyz: np.ndarray) -> np.ndarray:
    """CIE XYZ → L*a*b* (D65 reference white)."""
    d65 = np.array([0.95047, 1.00000, 1.08883])
    xyz_n = xyz / d65
    eps, kappa = 0.008856, 903.3
    f = np.where(xyz_n > eps, np.cbrt(xyz_n), (kappa * xyz_n + 16.0) / 116.0)
    L = 116.0 * f[..., 1] - 16.0
    a = 500.0 * (f[..., 0] - f[..., 1])
    b = 200.0 * (f[..., 1] - f[..., 2])
    return np.stack([L, a, b], axis=-1)


def rgb_to_lab(rgb_255: np.ndarray) -> np.ndarray:
    """Convert RGB (0–255) ndarray to CIE L*a*b*. Handles any shape (..., 3)."""
    rgb_01 = np.asarray(rgb_255, dtype=np.float64) / 255.0
    return _xyz_to_lab(_linear_to_xyz(_srgb_to_linear(rgb_01)))


def lab_to_hex(lab: np.ndarray) -> str:
    """Reverse lookup: find hex from a Lab triple (approximate)."""
    # Not a true inverse — only used for display
    pass


def hex_to_rgb(hex_str: str) -> list:
    """Convert '#RRGGBB' or 'RRGGBB' to [R, G, B] (0–255)."""
    h = hex_str.lstrip('#')
    return [int(h[i:i+2], 16) for i in (0, 2, 4)]


def rgb_to_hex(rgb: list) -> str:
    """Convert [R, G, B] to '#RRGGBB'."""
    return '#{:02X}{:02X}{:02X}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


# ─────────────────────────────────────────────────────────────────────────────
# Premium Palette Definition
# ─────────────────────────────────────────────────────────────────────────────

DEFAULT_SWISS_MORANDI_PALETTE = {
    "paper_gray":     ("#EAEAEA", "纸张感浅灰底色 — Base Background"),
    "charcoal_black": ("#1A1A1A", "极端对比深炭黑 — Typography / Main"),
    "forest_green":   ("#0F2D1E", "优雅暗森林绿 — Premium Accent 1"),
    "slate_gray":     ("#2F3E46", "沉稳石板灰 — Sub-text / Data Line"),
    "flesh_pink":     ("#D8B4A6", "低饱和复古肉粉 — Warm Accent 2"),
}

EDITORIAL_LUXURY_PALETTE = {
    "warm_ivory":     ("#F5EFE4", "Warm Ivory — Ground 70%"),
    "fog_white":      ("#EDE8E0", "Fog White — Ground variant"),
    "graphite":       ("#2A2A2A", "Graphite — Typography"),
    "stone":          ("#8B8680", "Stone — Supporting"),
    "charcoal":       ("#3D3D3D", "Charcoal — Supporting"),
    "cobalt":         ("#1B3A8C", "Cobalt — Accent"),
    "burgundy":       ("#7C1D2E", "Burgundy — Accent"),
    "acid_yellow":    ("#D4E317", "Acid Yellow — Accent"),
}

FESTIVAL_PALETTE = {
    "near_black":     ("#0E0E0E", "Near Black — Ground"),
    "ultra_white":    ("#F5F5F5", "Ultra White — Ground"),
    "acid_green":     ("#A8E63D", "Acid Green — Accent"),
    "electric_purple":("#7B2FBE", "Electric Purple — Accent"),
    "hot_pink":       ("#E83E8C", "Hot Pink — Accent"),
    "signal_red":     ("#E52222", "Signal Red — Accent"),
    "ultra_yellow":   ("#FFE500", "Ultra Yellow — Accent"),
}

PALETTE_REGISTRY = {
    "swiss_morandi": DEFAULT_SWISS_MORANDI_PALETTE,
    "editorial_luxury": EDITORIAL_LUXURY_PALETTE,
    "festival": FESTIVAL_PALETTE,
}


# ─────────────────────────────────────────────────────────────────────────────
# PremiumColorReducer
# ─────────────────────────────────────────────────────────────────────────────

class PremiumColorReducer:
    """
    Maps any AI-generated RGB color to the nearest color in a curated
    premium palette using CIE L*a*b* Delta E Euclidean distance.

    Delta E (Euclidean in Lab) is perceptually uniform — a ΔE of 1.0
    corresponds approximately to the smallest color difference the human
    eye can perceive. This gives results dramatically better than RGB
    distance, which does not correspond to human perception.
    """

    def __init__(self, palette_name: str = "swiss_morandi", custom_palette: dict = None):
        """
        Args:
            palette_name: One of "swiss_morandi", "editorial_luxury", "festival".
            custom_palette: Optional dict of {name: (hex, description)} to override.
        """
        if custom_palette:
            palette = custom_palette
        elif palette_name in PALETTE_REGISTRY:
            palette = PALETTE_REGISTRY[palette_name]
        else:
            raise ValueError(f"Unknown palette '{palette_name}'. "
                             f"Choose from: {list(PALETTE_REGISTRY.keys())}")

        self.palette_name = palette_name
        self.palette_meta = palette

        # Build numpy arrays for fast vectorized distance
        self._names = list(palette.keys())
        self._hexes = [v[0] for v in palette.values()]
        self._descriptions = [v[1] for v in palette.values()]
        self._rgb_palette = np.array([hex_to_rgb(h) for h in self._hexes], dtype=np.float64)
        self._lab_palette = rgb_to_lab(self._rgb_palette)

    def map_to_premium_color(self, input_rgb) -> tuple:
        """
        Map a single [R, G, B] (0–255) to the nearest palette color.

        Returns:
            (r, g, b) tuple of the mapped color (0–255 integers)
        """
        input_arr = np.array(input_rgb, dtype=np.float64).reshape(1, 3)
        input_lab = rgb_to_lab(input_arr)[0]

        # Euclidean distance in Lab space (Delta E)
        delta_e = np.linalg.norm(self._lab_palette - input_lab, axis=1)
        best_idx = int(np.argmin(delta_e))

        rgb = self._rgb_palette[best_idx]
        return (int(rgb[0]), int(rgb[1]), int(rgb[2]))

    def map_to_premium_hex(self, input_hex: str) -> str:
        """Map a hex string to the nearest palette color hex."""
        rgb = hex_to_rgb(input_hex)
        mapped = self.map_to_premium_color(rgb)
        return rgb_to_hex(mapped)

    def map_batch(self, colors: list) -> list:
        """
        Map a list of colors. Each item may be:
          - [R, G, B] list/tuple
          - '#RRGGBB' hex string

        Returns list of {'input': ..., 'output_rgb': ..., 'output_hex': ..., 'palette_name': ...}
        """
        results = []
        for c in colors:
            if isinstance(c, str):
                input_rgb = hex_to_rgb(c)
                input_repr = c
            else:
                input_rgb = list(c)
                input_repr = rgb_to_hex(input_rgb)

            mapped_rgb = self.map_to_premium_color(input_rgb)
            mapped_hex = rgb_to_hex(list(mapped_rgb))

            # Find palette entry name
            idx = self._rgb_palette.tolist().index(list(mapped_rgb)) \
                  if list(mapped_rgb) in self._rgb_palette.tolist() \
                  else self._find_index(input_rgb)

            results.append({
                "input_hex": input_repr if input_repr.startswith('#') else rgb_to_hex(input_rgb),
                "input_rgb": input_rgb,
                "output_hex": mapped_hex,
                "output_rgb": list(mapped_rgb),
                "palette_slot": self._names[idx] if idx < len(self._names) else "?",
                "delta_e": self._compute_delta_e(input_rgb, mapped_rgb),
            })
        return results

    def _find_index(self, input_rgb) -> int:
        input_lab = rgb_to_lab(np.array(input_rgb, dtype=np.float64).reshape(1, 3))[0]
        return int(np.argmin(np.linalg.norm(self._lab_palette - input_lab, axis=1)))

    def _compute_delta_e(self, rgb1, rgb2) -> float:
        lab1 = rgb_to_lab(np.array(rgb1, dtype=np.float64).reshape(1, 3))[0]
        lab2 = rgb_to_lab(np.array(rgb2, dtype=np.float64).reshape(1, 3))[0]
        return round(float(np.linalg.norm(lab1 - lab2)), 2)

    def show_palette(self):
        """Print the active palette to stdout."""
        print(f"\n{'─'*60}")
        print(f"  PREMIUM PALETTE: {self.palette_name.upper()}")
        print(f"{'─'*60}")
        for name, hex_val, desc in zip(self._names, self._hexes, self._descriptions):
            rgb = hex_to_rgb(hex_val)
            print(f"  {hex_val}  [{rgb[0]:3d},{rgb[1]:3d},{rgb[2]:3d}]  {name:<18}  {desc}")
        print(f"{'─'*60}\n")


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="PremiumColorReducer — map AI colors to Swiss/Morandi palette via CIELAB ΔE"
    )
    parser.add_argument("--rgb", type=str,
        help="Single color as R,G,B (e.g. 0,0,255)")
    parser.add_argument("--hex", type=str,
        help="Single color as hex (e.g. #FF0000 or FF0000)")
    parser.add_argument("--batch", type=str,
        help="Path to JSON file containing list of hex strings or [R,G,B] arrays")
    parser.add_argument("--out", type=str,
        help="Output JSON path for batch results (default: stdout)")
    parser.add_argument("--palette", type=str, default="swiss_morandi",
        choices=list(PALETTE_REGISTRY.keys()),
        help="Palette to enforce (default: swiss_morandi)")
    parser.add_argument("--show-palette", action="store_true",
        help="Display the active palette and exit")
    args = parser.parse_args()

    reducer = PremiumColorReducer(palette_name=args.palette)

    if args.show_palette:
        reducer.show_palette()
        return

    if args.rgb:
        parts = [int(x.strip()) for x in args.rgb.split(",")]
        mapped = reducer.map_to_premium_color(parts)
        delta = reducer._compute_delta_e(parts, list(mapped))
        print(f"Input  RGB: {parts} → {rgb_to_hex(list(parts))}")
        print(f"Output RGB: {list(mapped)} → {rgb_to_hex(list(mapped))}")
        print(f"ΔE (Lab):   {delta}")
        return

    if args.hex:
        mapped_hex = reducer.map_to_premium_hex(args.hex)
        input_rgb = hex_to_rgb(args.hex)
        mapped_rgb = hex_to_rgb(mapped_hex)
        delta = reducer._compute_delta_e(input_rgb, mapped_rgb)
        print(f"Input:  {args.hex}")
        print(f"Output: {mapped_hex}")
        print(f"ΔE:     {delta}")
        return

    if args.batch:
        with open(args.batch, "r") as f:
            colors = json.load(f)
        results = reducer.map_batch(colors)
        out_json = json.dumps(results, indent=2)
        if args.out:
            with open(args.out, "w") as f:
                f.write(out_json)
            print(f"Mapped {len(results)} colors → {args.out}")
        else:
            print(out_json)
        return

    # No args — run demo
    reducer.show_palette()
    demo_colors = [
        ([0, 0, 255],   "cheap blue"),
        ([255, 0, 0],   "signal red"),
        ([0, 255, 0],   "lime green"),
        ([255, 200, 0], "gold"),
        ([200, 100, 255], "AI purple"),
        ([0, 255, 255], "AI cyan"),
    ]
    print("  DEMO — mapping AI-generated colors to premium palette:")
    print(f"  {'INPUT':>12}  →  {'OUTPUT':>12}  ΔE")
    for rgb, label in demo_colors:
        mapped = reducer.map_to_premium_color(rgb)
        delta = reducer._compute_delta_e(rgb, list(mapped))
        print(f"  {rgb_to_hex(rgb):>12}  →  {rgb_to_hex(list(mapped)):>12}  {delta:5.1f}  ({label})")
    print()


if __name__ == "__main__":
    main()
