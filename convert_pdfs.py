from pathlib import Path

import anydoc


PDF_DIR = Path(__file__).resolve().parent.parent / "literature pdfs"
MARKDOWN_DIR = PDF_DIR / "markdown"

MARKDOWN_DIR.mkdir(exist_ok=True)

pdf_files = sorted(PDF_DIR.glob("*.pdf"))

for pdf_file in pdf_files:
    markdown = anydoc.to_markdown(str(pdf_file))
    output_file = MARKDOWN_DIR / f"{pdf_file.stem}.md"
    output_file.write_text(markdown, encoding="utf-8")

print(f"Converted {len(pdf_files)} PDFs to {MARKDOWN_DIR}")
