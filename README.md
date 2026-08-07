# Excel-to-MkDocs literature survey template

This scaffold keeps the literature site on MkDocs + Material, but replaces the wide spreadsheet-like pages with CSV-backed Tabulator grids.

## What the generator does

- Reads the `Main` sheet and turns it into the homepage.
- Exports `Papers`, `Reported Data`, and `Notes` to CSV in `docs/data/`.
- Writes each sheet page as a Tabulator mount point instead of a Markdown table.
- Keeps Plotly figure insertion for the `Main` sheet exactly as before.

## Local workflow

1. Put your workbook in the project root or pass the path explicitly.
2. Run (the repository's template workbook is shown here):

```bash
python build_site.py data/izro_literature.xlsx --build
```

3. Preview locally (omit `--build` above if using the live server):

```bash
mkdocs serve
```

## Browser libraries

The site loads Tabulator and Papa Parse from CDN URLs declared in `mkdocs.yml`.

If you want the site to be fully offline, download those assets and point `extra_css` / `extra_javascript` to local copies instead.

## Deployment

Pushing `main` runs `.github/workflows/static.yml`. It regenerates all Markdown,
CSV, and Plotly outputs from `data/izro_literature.xlsx`, builds MkDocs, and
publishes the result to GitHub Pages. Enable **GitHub Actions** as the Pages
source in the repository settings.

## Verification

Run `python -m unittest discover -s tests -v`. The test copies the project into
a temporary sandbox, regenerates and builds the site, then checks that Papers,
Reported Data, and Notes each point to an existing, non-empty published CSV.

## Files to edit

- `build_site.py`
- `mkdocs.yml`
- `docs/javascripts/tabulator.js`
- `docs/stylesheets/extra.css`
