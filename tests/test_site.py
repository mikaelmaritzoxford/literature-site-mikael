from __future__ import annotations

import csv
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import urljoin, urlparse


PROJECT = Path(__file__).resolve().parents[1]
GRID_SLUGS = ("papers", "reported-data", "notes")


class SiteBuildTest(unittest.TestCase):
    def test_generated_grid_pages_load_published_csvs(self):
        """Build in a disposable sandbox and validate each grid's resolved URL."""
        with tempfile.TemporaryDirectory(prefix="literature-site-") as tmp:
            sandbox = Path(tmp) / "project"
            shutil.copytree(
                PROJECT,
                sandbox,
                ignore=shutil.ignore_patterns(
                    ".git", ".venv", "old", "site", "__pycache__", "*.pyc"
                ),
            )
            subprocess.run(
                [sys.executable, "build_site.py", "data/izro_literature.xlsx", "--build"],
                cwd=sandbox,
                check=True,
            )

            for slug in GRID_SLUGS:
                html_path = sandbox / "site" / slug / "index.html"
                html = html_path.read_text(encoding="utf-8")
                match = re.search(r'class="csv-grid"[^>]+data-csv="([^"]+)"', html)
                self.assertIsNotNone(match, f"No CSV grid found on {slug}")

                page_url = f"https://example.test/project/{slug}/"
                csv_url = urljoin(page_url, match.group(1))
                relative_url = urlparse(csv_url).path.split("/project/", 1)[1]
                published_path = sandbox / "site" / relative_url
                self.assertTrue(published_path.is_file(), f"Missing {csv_url}")

                with published_path.open(encoding="utf-8", newline="") as handle:
                    rows = list(csv.reader(handle))
                self.assertGreaterEqual(len(rows), 2, f"{slug} CSV has no data rows")
                self.assertTrue(all(rows[0]), f"{slug} CSV contains blank headers")


if __name__ == "__main__":
    unittest.main()
