#from pathlib import Path
#
#import anydoc
#
##Path(__file__).resolve().parent.parent / "literature pdfs"    
## point to the directory containing the PDF files (literature\read or scanned)
#PDF_DIR = Path(__file__).parent / "literature" / "read or scanned"
#MARKDOWN_DIR = PDF_DIR / "markdown"
#
#MARKDOWN_DIR.mkdir(parents=True, exist_ok=True) 
#
#pdf_files = sorted(PDF_DIR.glob("*.pdf"))
#
#for pdf_file in pdf_files:
#    try: # attempt
#        markdown = anydoc.to_markdown(str(pdf_file))
#    except anydoc.UnsupportedError as e: # catch any exception
#        print(f"Error converting {pdf_file}: {e}")
#        continue
#    output_file = MARKDOWN_DIR / f"{pdf_file.stem}.md"
#    output_file.write_text(markdown, encoding="utf-8")
#
#
#print(f"Converted {len(pdf_files)} PDFs to {MARKDOWN_DIR}")


from pathlib import Path
import subprocess
import sys
import tempfile
import shutil

import anydoc

from pypdf import PdfReader

# Directory containing the PDF files
PDF_DIR = Path(__file__).parent / "literature" / "read or scanned"
MARKDOWN_DIR = PDF_DIR / "markdown"

OCR_DIR = PDF_DIR / "ocr"
OCR_DIR.mkdir(parents=True, exist_ok=True)

MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)

pdf_files = sorted(PDF_DIR.glob("*.pdf"))


for pdf_file in pdf_files:
    print(f"Processing: {pdf_file.name}")

    try:
        # 1. Try normal text extraction first
        markdown = anydoc.to_markdown(str(pdf_file))

    except anydoc.UnsupportedError as e:
        print(f"  Normal conversion failed: {e}")
        print("  Trying OCR...")

        OCR_DIR.mkdir(parents=True, exist_ok=True)
        ocr_pdf = OCR_DIR / f"{pdf_file.stem}_ocr.pdf"

        try:
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "ocrmypdf",
                    str(pdf_file),
                    str(ocr_pdf),
                ],
                check=True,
            )

        except subprocess.CalledProcessError:
            print("  OCR failed; trying redo-ocr...")

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "ocrmypdf",
                    "--redo-ocr",
                    str(pdf_file),
                    str(ocr_pdf),
                ],
                check=True,
            )

        try:
            markdown = anydoc.to_markdown(str(ocr_pdf))

        except Exception as ocr_convert_error:
            print("  OCR PDF still cannot be converted with anydoc:")
            print(f"    {type(ocr_convert_error).__name__}: {ocr_convert_error}")
            print(f"    Falling back to PDF text extraction: {ocr_pdf}")

            reader = PdfReader(str(ocr_pdf))
            markdown_parts = []

            for page in reader.pages:
                text = page.extract_text() or ""
                markdown_parts.append(text)

            markdown = "\n\n".join(markdown_parts)

    output_file = MARKDOWN_DIR / f"{pdf_file.stem}.md"
    output_file.write_text(markdown, encoding="utf-8")

    print(f"  Converted -> {output_file.name}")


print(f"\nConverted PDFs to: {MARKDOWN_DIR}")