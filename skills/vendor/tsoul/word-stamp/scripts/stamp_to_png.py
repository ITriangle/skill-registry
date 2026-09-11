#!/usr/bin/env python3
"""Turn a red-ink seal photo (white paper) into a transparent PNG for Word."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

LOW = 12
HIGH = 42
PAD = 16
MIN_KEPT_RATIO = 0.02


def load_rgba(path: Path):
    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit("需要 Pillow：pip install pillow") from exc
    return Image.open(path).convert("RGBA")


def redness_alpha(r: int, g: int, b: int, low: int, high: int) -> int:
    redness = min(r - g, r - b)
    if redness <= low:
        return 0
    if redness >= high:
        return 255
    return int(round(255 * (redness - low) / (high - low)))


def extract_red_stamp(im, low: int, high: int):
    px = im.load()
    w, h = im.size
    min_x, min_y, max_x, max_y = w, h, 0, 0
    kept = 0
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            a = redness_alpha(r, g, b, low, high)
            px[x, y] = (r, g, b, a)
            if a > 8:
                kept += 1
                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
    if kept == 0:
        raise SystemExit("没有检出红色印油。确认原图是白纸红章，或用 --low/--high 放宽阈值。")
    ratio = kept / (w * h)
    if ratio < MIN_KEPT_RATIO:
        raise SystemExit(
            f"红色像素过少（{ratio:.1%}）。确认原图是白纸红章，或用 --low/--high 放宽阈值。"
        )
    return kept, (min_x, min_y, max_x, max_y)


def square_crop(im, bbox: tuple[int, int, int, int], pad: int):
    w, h = im.size
    min_x, min_y, max_x, max_y = bbox
    min_x = max(0, min_x - pad)
    min_y = max(0, min_y - pad)
    max_x = min(w - 1, max_x + pad)
    max_y = min(h - 1, max_y + pad)
    bw = max_x - min_x + 1
    bh = max_y - min_y + 1
    side = max(bw, bh)
    cx = (min_x + max_x) / 2
    cy = (min_y + max_y) / 2
    left = int(round(cx - side / 2))
    top = int(round(cy - side / 2))
    right = left + side
    bottom = top + side
    if left < 0:
        right -= left
        left = 0
    if top < 0:
        bottom -= top
        top = 0
    if right > w:
        left -= right - w
        right = w
    if bottom > h:
        top -= bottom - h
        bottom = h
    left = max(0, left)
    top = max(0, top)
    return im.crop((left, top, right, bottom))


def write_checker_preview(stamp, dest: Path) -> None:
    from PIL import Image, ImageDraw

    cell = 24
    bg = Image.new("RGB", stamp.size, (240, 240, 240))
    draw = ImageDraw.Draw(bg)
    for y in range(0, stamp.size[1], cell):
        for x in range(0, stamp.size[0], cell):
            if ((x // cell) + (y // cell)) % 2 == 0:
                draw.rectangle([x, y, x + cell - 1, y + cell - 1], fill=(210, 210, 210))
    preview = bg.convert("RGBA")
    preview.alpha_composite(stamp)
    preview.convert("RGB").save(dest, quality=90)


def default_output(src: Path) -> Path:
    return src.with_suffix(".png")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="把白纸红章照片转成 Word 可用的透明底 PNG"
    )
    parser.add_argument("input", type=Path, help="公章照片（jpg/png）")
    parser.add_argument("-o", "--output", type=Path, help="输出 PNG 路径，默认与原图同目录同名")
    parser.add_argument("--preview", action="store_true", help="额外写出棋盘格预览 JPG")
    parser.add_argument("--low", type=int, default=LOW, help=f"透明阈值，默认 {LOW}")
    parser.add_argument("--high", type=int, default=HIGH, help=f"不透明阈值，默认 {HIGH}")
    parser.add_argument("--pad", type=int, default=PAD, help=f"裁切边距像素，默认 {PAD}")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    src = args.input.expanduser()
    if not src.is_file():
        print(f"找不到输入文件：{src}", file=sys.stderr)
        return 1
    if args.low >= args.high:
        print("--low 必须小于 --high", file=sys.stderr)
        return 1

    dest = (args.output or default_output(src)).expanduser()
    dest.parent.mkdir(parents=True, exist_ok=True)

    im = load_rgba(src)
    kept, bbox = extract_red_stamp(im, args.low, args.high)
    cropped = square_crop(im, bbox, args.pad)
    cropped.save(dest, "PNG")

    print(f"saved {dest}")
    print(f"size {cropped.size[0]}x{cropped.size[1]}")
    print(f"kept {kept} bbox {bbox[0]},{bbox[1]} {bbox[2]},{bbox[3]}")

    if args.preview:
        preview = dest.with_name(dest.stem + "-preview.jpg")
        write_checker_preview(cropped, preview)
        print(f"preview {preview}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
