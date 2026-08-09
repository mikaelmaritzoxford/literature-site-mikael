from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np
import pymupdf
from PIL import Image


CAPTION_RE = re.compile(
    r"^\s*fig(?:ure)?\.?\s*(\d+)\s*[.:]\s*(.*)",
    re.IGNORECASE | re.DOTALL,
)
PANEL_RE = re.compile(r"\(([a-h])\)", re.IGNORECASE)


@dataclass(frozen=True)
class Caption:
    number: int
    text: str
    rect: pymupdf.Rect
    region: str


def short_paper_name(pdf_file: Path) -> str:
    parts = pdf_file.stem.split("_")
    if len(parts) < 2 or not re.fullmatch(r"\d{4}", parts[0]):
        raise ValueError(f"Expected renamed PDF beginning YEAR_FirstAuthor: {pdf_file.name}")
    return f"{parts[0]}_{parts[1]}"


def find_captions(page: pymupdf.Page) -> list[Caption]:
    captions: list[Caption] = []
    page_width = page.rect.width

    for block in page.get_text("blocks", sort=True):
        text = block[4].strip()
        match = CAPTION_RE.match(text)
        if not match:
            continue

        rect = pymupdf.Rect(block[:4])
        if rect.width > page_width * 0.62:
            region = "full"
        elif rect.x0 < page_width / 2:
            region = "left"
        else:
            region = "right"

        caption_text = re.sub(r"\s+", " ", text).strip()
        captions.append(Caption(int(match.group(1)), caption_text, rect, region))

    return captions


def figure_clip(
    page: pymupdf.Page,
    caption: Caption,
    previous_captions: list[Caption],
) -> pymupdf.Rect:
    width = page.rect.width
    height = page.rect.height
    side_margin = width * 0.055

    if caption.region == "full":
        x0, x1 = side_margin, width - side_margin
        crop_height = min(300.0, height * 0.38)
    elif caption.region == "left":
        x0, x1 = side_margin, width / 2
        crop_height = min(230.0, height * 0.30)
    else:
        x0, x1 = width / 2, width - side_margin
        crop_height = min(230.0, height * 0.30)

    y1 = caption.rect.y0 - 4
    y0 = max(height * 0.055, y1 - crop_height)

    image_candidates = []
    for image_info in page.get_image_info():
        image_rect = pymupdf.Rect(image_info["bbox"])
        overlap = max(0.0, min(x1, image_rect.x1) - max(x0, image_rect.x0))
        overlap_ratio = overlap / max(image_rect.width, 1.0)
        gap = caption.rect.y0 - image_rect.y1
        if overlap_ratio > 0.65 and -2 <= gap <= 50:
            image_candidates.append(image_rect)
    if image_candidates:
        nearest_image = max(image_candidates, key=lambda rect: rect.width * rect.height)
        y0 = min(y0, max(height * 0.03, nearest_image.y0 - 4))

    earlier_same_region = [
        item for item in previous_captions
        if item.region == caption.region and item.rect.y1 < caption.rect.y0
    ]
    if earlier_same_region:
        y0 = max(y0, max(item.rect.y1 for item in earlier_same_region) + 4)

    if y1 - y0 < 40:
        raise ValueError(f"Figure {caption.number} crop is too short")

    return pymupdf.Rect(x0, y0, x1, y1)


def render_clip(page: pymupdf.Page, clip: pymupdf.Rect, dpi: int) -> Image.Image:
    pixmap = page.get_pixmap(clip=clip, dpi=dpi, alpha=False)
    return Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)


def white_runs(values: np.ndarray, threshold: float = 0.012) -> list[tuple[int, int]]:
    mask = values < threshold
    runs: list[tuple[int, int]] = []
    start: int | None = None

    for index, is_white in enumerate(mask):
        if is_white and start is None:
            start = index
        elif not is_white and start is not None:
            runs.append((start, index))
            start = None

    if start is not None:
        runs.append((start, len(mask)))
    return runs


def best_gutter(gray: np.ndarray) -> tuple[str, int, int] | None:
    height, width = gray.shape
    dark = gray < 245
    candidates: list[tuple[float, str, int, int]] = []

    for axis, density, dimension in (
        ("vertical", dark.mean(axis=0), width),
        ("horizontal", dark.mean(axis=1), height),
    ):
        minimum = max(2, round(dimension * 0.002))
        for start, end in white_runs(density):
            midpoint = (start + end) / 2
            if end - start < minimum or midpoint < dimension * 0.25 or midpoint > dimension * 0.75:
                continue
            score = (end - start) / dimension
            candidates.append((score, axis, start, end))

    if not candidates:
        return None
    _, axis, start, end = max(candidates)
    return axis, start, end


def split_panels(image: Image.Image, panel_count: int) -> list[Image.Image]:
    if panel_count < 2:
        return []

    rgb = np.asarray(image.convert("RGB"))
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    rectangles = [(0, 0, gray.shape[1], gray.shape[0])]

    while len(rectangles) < panel_count:
        options: list[tuple[float, int, str, int, int]] = []
        for index, (x0, y0, x1, y1) in enumerate(rectangles):
            gutter = best_gutter(gray[y0:y1, x0:x1])
            if gutter:
                axis, start, end = gutter
                area = (x1 - x0) * (y1 - y0)
                options.append((area, index, axis, start, end))

        if not options:
            return []

        _, index, axis, start, end = max(options)
        x0, y0, x1, y1 = rectangles.pop(index)
        midpoint = (start + end) // 2
        if axis == "vertical":
            split = x0 + midpoint
            new_rectangles = [(x0, y0, split, y1), (split, y0, x1, y1)]
        else:
            split = y0 + midpoint
            new_rectangles = [(x0, y0, x1, split), (x0, split, x1, y1)]
        rectangles.extend(new_rectangles)

    rectangles.sort(key=lambda rect: (rect[1], rect[0]))
    return [image.crop(rect) for rect in rectangles]


def panel_labels(caption: str) -> list[str]:
    labels: list[str] = []
    for label in PANEL_RE.findall(caption):
        label = label.lower()
        if label not in labels:
            labels.append(label)
    return labels


def save_jpeg(image: Image.Image, path: Path) -> None:
    image.convert("RGB").save(path, format="JPEG", quality=95, subsampling=0)


def extract_pdf(pdf_file: Path, figure_root: Path, dpi: int) -> tuple[int, int, list[str]]:
    paper_dir = figure_root / short_paper_name(pdf_file)
    paper_dir.mkdir(parents=True, exist_ok=True)
    figure_count = 0
    panel_count = 0
    warnings: list[str] = []

    with pymupdf.open(pdf_file) as document:
        for page in document:
            captions = find_captions(page)
            for caption in captions:
                figure_dir = paper_dir / f"Figure_{caption.number:02d}"
                figure_dir.mkdir(parents=True, exist_ok=True)

                try:
                    clip = figure_clip(page, caption, captions)
                    figure = render_clip(page, clip, dpi)
                except ValueError as error:
                    warnings.append(f"Figure {caption.number}: {error}")
                    continue

                save_jpeg(figure, figure_dir / f"Figure_{caption.number:02d}.jpeg")
                (figure_dir / "caption.txt").write_text(caption.text + "\n", encoding="utf-8")
                figure_count += 1

                labels = panel_labels(caption.text)
                panels = split_panels(figure, len(labels))
                if labels and not panels:
                    warnings.append(
                        f"Figure {caption.number}: found panel labels {labels} but no confident whitespace split"
                    )
                    continue

                for label, panel in zip(labels, panels):
                    save_jpeg(panel, figure_dir / f"Figure_{caption.number:02d}_panel-{label}.jpeg")
                    panel_count += 1

    return figure_count, panel_count, warnings


def select_pdfs(pdf_folder: Path, prefix: str | None, process_all: bool) -> list[Path]:
    """Select all PDFs or one PDF identified by a unique filename prefix."""
    pdf_folder = pdf_folder.expanduser().resolve()
    if not pdf_folder.is_dir():
        raise NotADirectoryError(f"PDF folder does not exist: {pdf_folder}")

    pdf_files = sorted(
        (
            path
            for path in pdf_folder.iterdir()
            if path.is_file() and path.suffix.casefold() == ".pdf"
        ),
        key=lambda path: path.name.casefold(),
    )
    if not pdf_files:
        raise FileNotFoundError(f"No top-level PDF files found in: {pdf_folder}")
    if process_all:
        return pdf_files

    if prefix is None or not prefix.strip():
        raise ValueError("--pdf requires a non-empty filename prefix")

    normalized_prefix = prefix.strip().casefold()
    matches = [path for path in pdf_files if path.stem.casefold().startswith(normalized_prefix)]
    if not matches:
        raise FileNotFoundError(
            f'No PDF filename begins with "{prefix}" in: {pdf_folder}'
        )
    if len(matches) > 1:
        match_names = ", ".join(path.name for path in matches)
        raise ValueError(
            f'PDF prefix "{prefix}" is ambiguous; use more of the filename. Matches: {match_names}'
        )
    return matches


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract captioned figures and whitespace-separated panels.")
    parser.add_argument(
        "--folder",
        type=Path,
        required=True,
        help="Folder containing the source PDFs; output is written to its figures subfolder.",
    )
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument(
        "--pdf",
        metavar="PREFIX",
        help="Process the single PDF whose filename begins with this unique prefix.",
    )
    selection.add_argument(
        "--all",
        action="store_true",
        dest="process_all",
        help="Process every top-level PDF in --folder.",
    )
    parser.add_argument("--dpi", type=int, default=300, help="Rendering resolution (default: 300).")
    args = parser.parse_args()

    try:
        pdf_files = select_pdfs(args.folder, args.pdf, args.process_all)
    except (FileNotFoundError, NotADirectoryError, ValueError) as error:
        parser.error(str(error))

    figure_root = args.folder.expanduser().resolve() / "figures"

    for pdf_file in pdf_files:
        figures, panels, warnings = extract_pdf(pdf_file, figure_root, args.dpi)
        print(f"{pdf_file.name}: {figures} figures, {panels} panels")
        for warning in warnings:
            print(f"  Warning: {warning}")


if __name__ == "__main__":
    main()
