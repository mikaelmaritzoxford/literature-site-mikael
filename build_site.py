\
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path

from openpyxl import load_workbook


def slugify(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name or "page"


def cell_str(v):
    if v is None:
        return ""
    return str(v).strip()


def nonempty(v):
    return v is not None and str(v).strip() != ""


def md_escape(s):
    if s is None:
        return ""
    s = str(s).replace("\r\n", "\n").replace("\r", "\n")
    return s.replace("|", r"\|")


def markdown_table(headers, rows):
    esc = lambda x: md_escape(x).replace("\n", "<br>")
    out = []
    out.append("| " + " | ".join(esc(h) for h in headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        row = [esc(x) for x in row]
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out)


def parse_main(ws):
    title = ws["A1"].value or "Literature Website"
    sections = []
    current_section = None
    current_sub = None
    max_row = ws.max_row

    for r in range(2, max_row + 1):
        a = cell_str(ws[f"A{r}"].value)
        b = cell_str(ws[f"B{r}"].value)

        if not a and not b:
            continue

        if a and not b:
            if current_sub and current_section is not None:
                current_section.setdefault("subsections", []).append(current_sub)
                current_sub = None
            if current_section is not None:
                sections.append(current_section)
            current_section = {"heading": a, "subsections": []}
            continue

        if a and b:
            if current_sub and current_section is not None:
                current_section.setdefault("subsections", []).append(current_sub)
            current_sub = {"heading": a, "paragraphs": [b]}
            continue

        if (not a) and b:
            if current_sub is None:
                if current_section is None:
                    current_section = {"heading": "Untitled", "subsections": []}
                current_section.setdefault("intro", []).append(b)
            else:
                current_sub.setdefault("paragraphs", []).append(b)

    if current_sub and current_section is not None:
        current_section.setdefault("subsections", []).append(current_sub)
    if current_section is not None:
        sections.append(current_section)

    return title, sections


def write_index(title, sections, out_path: Path):
    lines = [f"# {title}", ""]
    for sec in sections:
        lines.append(f"## {sec['heading']}")
        lines.append("")
        for p in sec.get("intro", []):
            lines.append(md_escape(p))
            lines.append("")
        for sub in sec.get("subsections", []):
            lines.append(f"### {sub['heading']}")
            lines.append("")
            for p in sub.get("paragraphs", []):
                lines.append(md_escape(p))
                lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def write_sheet_page(ws, title: str, out_path: Path):
    rows = []
    headers = []
    max_col = ws.max_column
    max_row = ws.max_row

    header_row = None
    for r in range(1, max_row + 1):
        vals = [ws.cell(r, c).value for c in range(1, max_col + 1)]
        if any(nonempty(v) for v in vals):
            header_row = r
            headers = [cell_str(v) if nonempty(v) else f"Column {i}" for i, v in enumerate(vals, start=1)]
            break

    if header_row is None:
        out_path.write_text(f"# {title}\n\n_No data found._\n", encoding="utf-8")
        return

    for r in range(header_row + 1, max_row + 1):
        vals = [ws.cell(r, c).value for c in range(1, max_col + 1)]
        if not any(nonempty(v) for v in vals):
            continue
        rows.append([cell_str(v) for v in vals[:len(headers)]])

    md = [f"# {title}", ""]
    md.append(markdown_table(headers, rows))
    md.append("")
    out_path.write_text("\n".join(md), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Generate MkDocs pages from an Excel workbook and build the site.")
    parser.add_argument("workbook", type=Path, help="Path to the .xlsx workbook")
    parser.add_argument("--project-dir", type=Path, default=Path(__file__).resolve().parent, help="Project root")
    parser.add_argument("--build", action="store_true", help="Run mkdocs build after generating pages")
    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    docs_dir = project_dir / "docs"
    docs_dir.mkdir(exist_ok=True)

    wb = load_workbook(args.workbook, data_only=True)

    main_title, main_sections = parse_main(wb["Main"])
    write_index(main_title, main_sections, docs_dir / "index.md")

    for sheet_name, out_name in [
        ("Papers", "papers.md"),
        ("Reported Data", "reported-data.md"),
        ("Notes", "notes.md"),
    ]:
        write_sheet_page(wb[sheet_name], sheet_name, docs_dir / out_name)

    if "how_to_use" in wb.sheetnames:
        write_sheet_page(wb["how_to_use"], "how_to_use", docs_dir / "how-to-use.md")

    if args.build:
        subprocess.run(["mkdocs", "build"], cwd=project_dir, check=True)


if __name__ == "__main__":
    main()
