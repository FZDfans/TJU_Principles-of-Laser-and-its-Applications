#!/usr/bin/env python
"""Render and inspect PDF pages with optional OCR.

Examples:
  python tools/pdf_visual_read.py book.pdf --pages 1-3 --dpi 220
  python tools/pdf_visual_read.py book.pdf --pages 12 --ocr
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import fitz
from PIL import Image


def parse_pages(spec: str, page_count: int) -> list[int]:
    if not spec:
        return list(range(page_count))

    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))

    invalid = [p for p in pages if p < 1 or p > page_count]
    if invalid:
        raise ValueError(f"Page(s) out of range: {invalid}; PDF has {page_count} pages")

    return [p - 1 for p in sorted(pages)]


def configure_tesseract() -> None:
    try:
        import pytesseract
    except ImportError:
        return

    if os.name == "nt":
        candidate = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
        if candidate.exists():
            pytesseract.pytesseract.tesseract_cmd = str(candidate)


def ocr_image(image_path: Path, lang: str) -> str:
    configure_tesseract()
    import pytesseract

    with Image.open(image_path) as image:
        return pytesseract.image_to_string(image, lang=lang)


def make_json_safe(value):
    if isinstance(value, bytes):
        return {"type": "bytes", "length": len(value)}
    if isinstance(value, dict):
        return {str(k): make_json_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [make_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [make_json_safe(item) for item in value]
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Render PDF pages and extract visual metadata.")
    parser.add_argument("pdf", type=Path, help="PDF path")
    parser.add_argument("--pages", default="", help="1-based pages, e.g. 1,3-5. Default: all")
    parser.add_argument("--dpi", type=int, default=220, help="Render DPI")
    parser.add_argument("--out", type=Path, default=Path("pdf_visual_out"), help="Output folder")
    parser.add_argument("--ocr", action="store_true", help="Run OCR on rendered pages")
    parser.add_argument("--lang", default="chi_sim+eng", help="Tesseract language, e.g. chi_sim+eng")
    args = parser.parse_args()

    pdf_path = args.pdf.resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    args.out.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    page_indexes = parse_pages(args.pages, doc.page_count)
    zoom = args.dpi / 72
    matrix = fitz.Matrix(zoom, zoom)

    summary = {
        "pdf": str(pdf_path),
        "page_count": doc.page_count,
        "dpi": args.dpi,
        "pages": [],
    }

    for page_index in page_indexes:
        page = doc[page_index]
        page_no = page_index + 1
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        png_path = args.out / f"page-{page_no:04d}.png"
        pix.save(str(png_path))

        text_dict = page.get_text("dict")
        text = page.get_text("text")
        page_info = {
            "page": page_no,
            "width_pt": page.rect.width,
            "height_pt": page.rect.height,
            "image": str(png_path),
            "text": text,
            "blocks": make_json_safe(text_dict.get("blocks", [])),
        }

        if args.ocr:
            page_info["ocr_text"] = ocr_image(png_path, args.lang)

        json_path = args.out / f"page-{page_no:04d}.json"
        json_path.write_text(json.dumps(page_info, ensure_ascii=False, indent=2), encoding="utf-8")
        summary["pages"].append({"page": page_no, "image": str(png_path), "json": str(json_path)})

    summary_path = args.out / "summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
