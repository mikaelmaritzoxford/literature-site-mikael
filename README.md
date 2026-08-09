# Excel-to-MkDocs literature survey template

This project turns a structured scientific literature-review workbook into a
small MkDocs Material website. The homepage presents the synthesis written in
the `Main` sheet, while Papers and Reported Data are searchable, sortable,
filterable CSV-backed tables.

The local workbook is intentionally excluded from Git. Generated Markdown,
CSV, and Plotly files under `docs/` are committed and are the inputs used by
GitHub Pages.

## Literature-review workflow

1. Save the working database as `izro_literature.xlsx` in the project root.
2. Add one row to `Papers` for every publication. Assign a stable, unique
   `Paper ID` and record authors, journal, year, title, DOI, source URL, a
   concise abstract summary, keywords, and review notes.
3. Read the full paper and add one row to `Reported Data` for every distinct
   sample, device, composition, processing condition, or control. Reuse the
   exact `Paper ID` from `Papers`.
4. Put each reported quantity in its dedicated column, using the unit stated
   in the header. Examples include mobility, resistivity, sheet resistance,
   carrier concentration, bandgap, work function, thickness, fabrication
   technique, and deposition or annealing temperature. Never combine several
   measurements in one numeric cell.
5. Use `Property name`, `Property value`, and `Property unit` only when the
   publication reports a quantity that has no dedicated column. Preserve the
   source figure/table, evidence type, confidence, and any interpretation in
   their provenance columns. Leave genuinely unreported values blank; do not
   infer or silently convert them.
6. Record paper-level insights and emerging themes in `Notes`. Update `Main`
   when the accumulated evidence changes the survey's conclusions, ranges,
   knowledge gaps, processing guidance, or other synthesis. Figure markers in
   `Main` connect to the corresponding generator in `figures/`.
7. Regenerate the website, inspect Home, Papers, and Reported Data locally,
   then commit the updated generated files under `docs/`.

## PDF intake and naming

PDF intake has two independent stages. Python converts the PDFs locally with
AnyDoc; Codex reads the resulting Markdown and performs the bibliographic
renaming through a repository-scoped skill. No OpenAI API key is required.

```powershell
python -m pip install -r requirements-conversion.txt
python convert_pdfs.py
```

Converted files are written to `../literature pdfs/markdown/`. Then, inside
Codex, invoke:

```text
$rename-literature-papers rename every matching literature PDF and Markdown pair now.
```

The skill immediately renames each paired PDF and Markdown file, then validates
the results and writes a rename log. Scanned or image-only PDFs require a
separate OCR path. See `manual.md`, section 4A, for details.

## Figure extraction

Install the local figure-processing stack through conda-forge:

```powershell
conda install -c conda-forge pymupdf opencv pillow numpy
```

Alternatively, install the pip packages:

```powershell
python -m pip install -r requirements-figures.txt
```

From an Anaconda Prompt, extract one paper by giving the PDF folder and enough
of the beginning of its filename to identify it uniquely:

```powershell
python extract_figures.py --folder "..\literature pdfs" --pdf 2018_Morales
```

Complete figures, captions, and any confidently separated panels are written
under the selected folder at `figures/YEAR_FirstAuthor/Figure_XX/`. To process
every top-level PDF explicitly, run:

```powershell
python extract_figures.py --folder "..\literature pdfs" --all
```

No manifest is produced; researchers must inspect the images directly.

## Generate and preview locally

From PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python build_site.py izro_literature.xlsx
mkdocs serve
```

Open <http://127.0.0.1:8000>. To generate the static `site/` directory without
starting the preview server, run:

```powershell
python build_site.py izro_literature.xlsx --build
```

If the environment has not yet been created:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Reported Data table

Recommended measurement and processing columns appear as normal headers across
the top of the table. Use **Choose reported-data columns** to select the fields
needed for a comparison. All visible columns support header filtering,
sorting, resizing, and reordering; wide selections scroll horizontally.

## Publish with GitHub Pages

Because `izro_literature.xlsx` is private and ignored, website regeneration is
a local step. After running `build_site.py`, commit the changed `docs/` files
and push `main`. `.github/workflows/static.yml` builds those generated files
with MkDocs and publishes the `site/` artifact. In repository settings, select
**GitHub Actions** as the Pages source.

## Verification

Run the reproducible sandbox test before committing:

```powershell
python -m unittest discover -s tests -v
```

The test copies the project into a temporary directory, regenerates and builds
the website, and verifies that Papers and Reported Data resolve to non-empty
published CSV files.

## Main files

- `build_site.py`: workbook parser and site-content generator
- `convert_pdfs.py`: minimal local AnyDoc PDF-to-Markdown converter
- `.agents/skills/rename-literature-papers/`: Codex renaming workflow
- `figures/`: Plotly figure generators referenced by `Main`
- `figures/plotly_style.py`: shared 14-point, boxed-axis, Tableau-colour Plotly style and modebar configuration
- `mkdocs.yml`: theme, navigation, and browser assets
- `docs/javascripts/tabulator.js`: interactive table and column selector
- `docs/stylesheets/extra.css`: site and table styling
- `.github/workflows/static.yml`: GitHub Pages deployment
