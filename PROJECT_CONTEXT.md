# IZrO Literature Survey — Project Context

## How to use this file with Codex

After transferring the complete project to another computer, open the
`literature site` folder as the Codex project and begin with:

> Read `PROJECT_CONTEXT.md` and `manual.md` completely, inspect the current
> repository state, and use them as the context for this task: [describe the
> next task].

Codex should treat this file as orientation, not as a substitute for inspecting
the current files. Before changing the workbook, scripts, skills, or generated
website, it should confirm the current structure and preserve unrelated work.

## Project purpose

This project is a reproducible literature-survey workflow for
zirconium-doped indium oxide (IZrO). It uses:

- `izro_literature.xlsx` as the private research database;
- Python for PDF conversion, figure extraction, Plotly generation, and MkDocs
  site generation;
- repository-scoped Codex skills for bibliographic renaming, figure
  digitisation, and extraction of paper information into Excel;
- MkDocs Material for the published literature website.

The Excel workbook is the source of truth. Generated Markdown, CSV, and Plotly
HTML files under `docs/` are the publishable representation.

## Expected folder arrangement

Keep these two folders beside one another. Their parent folder can be anywhere:

``` text
project parent/
├── literature site/
│   ├── PROJECT_CONTEXT.md
│   ├── manual.md
│   ├── izro_literature.xlsx
│   ├── convert_pdfs.py
│   ├── extract_figures.py
│   ├── build_site.py
│   ├── figures/
│   ├── docs/
│   ├── tests/
│   └── .agents/skills/
└── literature pdfs/
    ├── *.pdf
    ├── markdown/
    └── figures/
```

Most example commands assume this arrangement and are run from the
`literature site` folder.

## Files that must be transferred separately

The following are intentionally excluded from Git and will not be restored by
cloning the online repository:

- `izro_literature.xlsx`, the private working database;
- the sibling `literature pdfs/` folder, including PDFs, Markdown, extracted
  figures, captions, and digitised CSV files;
- anything retained under `old/`;
- a local Python environment such as `.venv/`.

Copy the workbook and literature folder separately. Recreate the Python
environment on the destination computer rather than copying `.venv/`.

## Python environment

The intended conda environment is named `literature` and uses conda-forge.
From an Anaconda Prompt in `literature site`:

``` bat
conda env create -f environment.yml
conda activate literature
```

If the environment already exists, update it with:

``` bat
conda env update -f environment.yml --prune
```

Specialised pip requirement files are also available:

- `requirements-conversion.txt` for AnyDoc PDF-to-Markdown conversion;
- `requirements-figures.txt` for local figure extraction;
- `requirements.txt` for the complete website and plotting stack.

## End-to-end literature workflow

### 1. Convert PDFs to Markdown locally

`convert_pdfs.py` uses Firecrawl AnyDoc locally. It does not call an OpenAI API.
The source PDFs are read from the sibling literature folder and converted into
its `markdown/` subfolder.

``` bat
python convert_pdfs.py
```

### 2. Rename matching PDF and Markdown pairs with Codex

Repository skill:

``` text
.agents/skills/rename-literature-papers/SKILL.md
```

Example Codex request:

``` text
$rename-literature-papers rename every matching literature PDF and Markdown pair now.
```

The skill reads each Markdown paper and immediately renames the matching pair:

``` text
YEAR_FirstAuthor_LastAuthor_JOURNAL_Short-title.pdf
YEAR_FirstAuthor_LastAuthor_JOURNAL_Short-title.md
```

It does not require a review or approval stage.

### 3. Extract figures and panels locally

Every command must specify the PDF folder and exactly one selection mode.

One uniquely identified paper:

``` bat
python extract_figures.py --folder "..\literature pdfs" --pdf 2018_Morales
```

Every top-level PDF in the folder:

``` bat
python extract_figures.py --folder "..\literature pdfs" --all
```

The prefix supplied to `--pdf` is case-insensitive and must uniquely match the
beginning of one filename. Output is placed inside the selected PDF folder:

``` text
figures/
└── 2018_MoralesMasis/
    └── Figure_01/
        ├── Figure_01.jpeg
        ├── Figure_01_panel-a.jpeg
        └── caption.txt
```

The complete figure is always retained. Panel splitting is attempted only when
caption labels and whitespace provide a confident separation. There is no
manifest; researchers inspect the images directly.

### 4. Digitise selected quantitative plots with Codex

Do not digitise photographs, schematics, or every extracted figure
automatically. Select plots containing numerical information useful to the
database.

Repository skill:

``` text
.agents/skills/digitize-figure-data/SKILL.md
```

Example Codex request:

``` text
$digitize-figure-data digitize the selected Figure_01.jpeg.
```

The skill uses the online WebPlotDigitizer interface, calibrates the axes, and
saves a CSV beside the source image. It then compares extracted values and
trends with statements in the matching paper Markdown. Digitised values are
graphical estimates and must retain appropriate provenance and precision.

### 5. Add one paper to the Excel database with Codex

Repository skill:

``` text
.agents/skills/extract-paper-info/SKILL.md
```

Example Codex request:

``` text
$extract-paper-info add the 2018 Morales-Masis paper to izro_literature.xlsx.
```

The skill reads the paper Markdown and any relevant captions or digitised CSVs,
then updates only these sheets:

- `Papers`: one row per paper;
- `Reported Data`: one row per distinct observation, using `O#` identifiers;
- `Notes`: one row per paper with four or five knowledge nuggets of fewer than
  30 words each.

It must follow existing Paper ID and formatting conventions, preserve evidence
and confidence, and never invent unreported measurements. It does not edit
`Main` unless a separate request explicitly asks for synthesis changes.

## Workbook conventions

### Papers

One row represents one publication. Paper IDs are stable and reused exactly in
all other sheets, normally following the existing `Author_Year` convention.

### Reported Data

One row represents one sample, condition, device, or other distinct
observation. Use the next available `O#` identifier. Quantities belong in their
dedicated numeric columns, with units defined in the headers.

Current transport standards include:

- mobility in `cm^2/Vs`;
- carrier concentration in `cm^-3`;
- resistivity in `mohm·cm`;
- sheet resistance in `ohm/sq`.

If resistivity is missing but positive carrier concentration `N` and mobility
`μ` are both available, it may be calculated transparently as:

``` text
ρ (mΩ·cm) = 1000 / (q × μ × N)
q = 1.602176634 × 10^-19 C
```

Derived workbook values should be formulas, and their origin should be stated
in `Comments`. Do not calculate values when either input is absent or invalid.

### Notes

Use one row per paper. Knowledge nuggets should be concise, independently
meaningful statements rather than fragments or copied abstract text.

### Main

`Main` controls the homepage narrative and Figure placement. Column C contains
markers such as `Figure 1`, which load the matching Python generator from the
`figures/` package.

## Plotly figure standard

Each independent scientific figure is generated by `figures/figureN.py`.
All figure scripts should export through:

``` python
from figures.plotly_style import write_figure_html

write_figure_html(fig, out_html)
```

The shared style applies:

- 14-point text;
- complete black boxes around both axes;
- outside ticks;
- Matplotlib Tableau 10 colours for categorical traces;
- optional line, path, circle, rectangle, and erase-shape modebar tools.

Continuous numerical variables may use a suitable continuous colour map such
as Viridis.

Figure 1 currently plots mobility against carrier concentration. Marker colour
represents log10 resistivity in mΩ·cm. Its generator also calculates a missing
resistivity at runtime when valid mobility and carrier concentration values are
available.

## Generate and preview the website

Regenerate Markdown, CSV tables, and Plotly HTML from the workbook:

``` bat
python build_site.py izro_literature.xlsx
```

Preview locally:

``` bat
mkdocs serve
```

Then open `http://127.0.0.1:8000` and inspect the homepage, figures, Papers, and
Reported Data.

To generate the static `site/` output as well:

``` bat
python build_site.py izro_literature.xlsx --build
```

The private workbook is not published. Commit the regenerated files under
`docs/` so GitHub Pages can build the website from them.

## Verification before committing

Run:

``` bat
python -m unittest discover -s tests -v
git diff --check
git status --short
```

The tests validate figure-extraction selection, Plotly styling, and a complete
disposable website build. Inspect generated scientific figures and spreadsheet
changes manually as well; passing tests do not validate scientific judgement.

## Git and cleanup conventions

- Preserve unrelated user changes in a dirty worktree.
- Do not commit the private workbook, PDFs, generated `site/`, local virtual
  environments, caches, editor settings, or temporary Codex artifacts.
- `old/` is ignored and is used for recoverable archives of obsolete workflow
  files and pre-change workbook copies.
- Do not move active source scripts, skills, requirement files, or the Plotly
  generators into `old/`.
- Regenerate and commit `docs/` after workbook or figure changes that affect the
  published site.

## Important reference files

- `manual.md`: detailed student-facing workflow manual;
- `README.md`: concise repository setup and publishing instructions;
- `environment.yml`: preferred conda environment;
- `.gitignore`: private/generated-file exclusions;
- `.agents/skills/`: repository-scoped Codex workflows;
- `figures/plotly_style.py`: standard interactive-figure appearance;
- `tests/`: reproducible project checks.

When this context and the actual repository disagree, inspect the repository,
identify whether the workflow evolved, and update this file alongside the code.
