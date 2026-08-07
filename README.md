# Tabulator-backed MkDocs scaffold

This scaffold keeps the literature site on MkDocs + Material, but replaces the wide spreadsheet-like pages with CSV-backed Tabulator grids.

## What the generator does

- Reads the `Main` sheet and turns it into the homepage.
- Exports `Papers`, `Reported Data`, and `Notes` to CSV in `docs/data/`.
- Writes each sheet page as a Tabulator mount point instead of a Markdown table.
- Keeps Plotly figure insertion for the `Main` sheet exactly as before.

## Local workflow

1. Put your workbook in the project root or pass the path explicitly.
2. Run:

```bash
python build_site.py path/to/workbook.xlsx
```

3. Preview locally:

```bash
mkdocs serve
```

## Browser libraries

The site loads Tabulator and Papa Parse from CDN URLs declared in `mkdocs.yml`.

If you want the site to be fully offline, download those assets and point `extra_css` / `extra_javascript` to local copies instead.

## Files to edit

- `build_site.py`
- `mkdocs.yml`
- `docs/javascripts/tabulator.js`
- `docs/stylesheets/extra.css`
