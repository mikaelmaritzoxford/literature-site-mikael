import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np
from PIL import Image

from extract_figures import panel_labels, select_pdfs, short_paper_name, split_panels


class FigureExtractionTest(unittest.TestCase):
    def test_short_paper_name(self):
        pdf = Path("2019_Aydin_DeWolf_ADVFUNMAT_IZrO-tandem-electrodes.pdf")
        self.assertEqual(short_paper_name(pdf), "2019_Aydin")

    def test_panel_labels_are_unique_and_ordered(self):
        caption = "Fig. 3. (a) First plot. (b) Second plot; see (a)."
        self.assertEqual(panel_labels(caption), ["a", "b"])

    def test_splits_two_panels_at_white_gutter(self):
        pixels = np.full((120, 240, 3), 255, dtype=np.uint8)
        pixels[10:110, 10:105] = 80
        pixels[10:110, 135:230] = 120
        panels = split_panels(Image.fromarray(pixels), 2)
        self.assertEqual(len(panels), 2)
        self.assertLess(panels[0].width, 150)
        self.assertLess(panels[1].width, 150)

    def test_selects_one_pdf_by_case_insensitive_prefix(self):
        with TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory)
            target = folder / "2018_MoralesMasis_Ballif_JPHOTOV_Broadband.pdf"
            target.touch()
            (folder / "2019_Aydin_DeWolf_ADVFUNMAT_Electrodes.PDF").touch()

            self.assertEqual(select_pdfs(folder, "2018_morales", False), [target])

    def test_selects_all_top_level_pdfs_in_name_order(self):
        with TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory)
            second = folder / "2020_Li_Yu_SOLENER_Humidity.pdf"
            first = folder / "2018_MoralesMasis_Ballif_JPHOTOV_Broadband.pdf"
            second.touch()
            first.touch()
            (folder / "notes.txt").touch()

            self.assertEqual(select_pdfs(folder, None, True), [first, second])

    def test_rejects_ambiguous_pdf_prefix(self):
        with TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory)
            (folder / "2019_Aydin_DeWolf_First.pdf").touch()
            (folder / "2019_Aydin_DeWolf_Second.pdf").touch()

            with self.assertRaisesRegex(ValueError, "ambiguous"):
                select_pdfs(folder, "2019_Aydin", False)


if __name__ == "__main__":
    unittest.main()
