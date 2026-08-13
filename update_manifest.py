from pathlib import Path
from datetime import datetime
import csv

LITERATURE_DIR = Path("literature")
CSV_FILE = Path("literature_manifest.csv")

FIELDS = ["filename", "path", "size_bytes", "modified"]


def load_existing():
    if not CSV_FILE.exists():
        return []

    with CSV_FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def scan_literature():
    existing = load_existing()
    known_paths = {row["path"] for row in existing}

    for file in LITERATURE_DIR.rglob("*"):
        if not file.is_file():
            continue

        relative_path = str(file.relative_to(LITERATURE_DIR))
        stat = file.stat()

        if relative_path not in known_paths:
            existing.append({
                "filename": file.name,
                "path": relative_path,
                "size_bytes": stat.st_size,
                "modified": datetime.fromtimestamp(
                    stat.st_mtime
                ).isoformat(timespec="seconds"),
            })

    with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(existing)


if __name__ == "__main__":
    scan_literature()
    print(f"Updated {CSV_FILE}")