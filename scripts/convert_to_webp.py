#!/usr/bin/env python3
"""Convert PNG images to WebP for the Tornade Hugo site."""

import pathlib
from PIL import Image

DIRS = [
    pathlib.Path("static/images/slideshow"),
    pathlib.Path("static/images"),
]

def convert(src: pathlib.Path, quality: int = 85) -> None:
    dst = src.with_suffix(".webp")
    if dst.exists():
        print(f"  skip  {src.name} (WebP already exists)")
        return
    img = Image.open(src)
    img.save(dst, "WEBP", quality=quality, method=6)
    ratio = dst.stat().st_size / src.stat().st_size * 100
    print(f"  ok    {src.name}  {src.stat().st_size // 1024} KB  ->  {dst.stat().st_size // 1024} KB  ({ratio:.0f}%)")

if __name__ == "__main__":
    for d in DIRS:
        pngs = sorted(d.glob("*.png")) if d.exists() else []
        if not pngs:
            continue
        print(f"\n{d}/")
        for png in pngs:
            convert(png)
