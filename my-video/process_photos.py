#!/usr/bin/env python3
"""
Run after placing these files in assets/:
  snape.jpg / snape.png
  harry.jpg / harry.png
  tomriddle.jpg / tomriddle.png
"""
import subprocess, sys, os

assets = "assets"
pairs = [
    ("snape",     "snape"),
    ("harry",     "harry"),
    ("tomriddle", "tomriddle"),
]

for src_base, out_base in pairs:
    # Find whichever extension exists
    src = None
    for ext in ("jpg", "jpeg", "png", "webp"):
        candidate = f"{assets}/{src_base}.{ext}"
        if os.path.exists(candidate):
            src = candidate
            break
    if not src:
        print(f"  ✗  {src_base}.* not found in assets/ — skipping")
        continue

    out = f"{assets}/{out_base}-nobg.png"
    print(f"  Removing background: {src} → {out}")
    result = subprocess.run(
        ["npx", "--yes", "hyperframes@0.6.20", "remove-background", src, "-o", out],
        capture_output=False
    )
    if result.returncode == 0:
        print(f"  ✓  {out}")
    else:
        print(f"  ✗  remove-background failed for {src}")

print("\nDone. Now run: npm run check && npm run render")
