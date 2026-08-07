# MkDocs scaffold for zirconium-doped indium oxide literature notes

This scaffold turns the workbook into a static MkDocs website.

## Files

- `build_site.py` generates the Markdown pages from the workbook and can run `mkdocs build`
- `mkdocs.yml` configures the website
- `docs/` contains generated Markdown pages
- `data/zr_indium_oxide_literature_v2.xlsx` is the source workbook

## Local setup

```bash
conda create -n literature python=3.12 -y
conda activate literature
pip install -r requirements.txt
python build_site.py data/zr_indium_oxide_literature_v2.xlsx
mkdocs serve
```

## Build HTML

```bash
python build_site.py data/zr_indium_oxide_literature_v2.xlsx --build
```

That creates the static site in the `site/` folder.

## Plotly figures

To add Plotly figures later, generate them in Python and either:

1. embed the Plotly HTML directly into a Markdown page, or
2. export static images with Plotly + Kaleido and place them under `docs/assets/`.

## GitHub Pages test

For a simple GitHub test:

1. push this repository to GitHub
2. run `python build_site.py data/zr_indium_oxide_literature_v2.xlsx --build` locally or in GitHub Actions
3. publish the generated `site/` folder with GitHub Pages, or commit `site/` if you prefer a simple first test

