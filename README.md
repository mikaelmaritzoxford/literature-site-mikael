# IZrO literature MkDocs scaffold

## Local setup

```bash
conda env create -f environment.yml
conda activate literature
python build_site.py data/izro_literature_v3.xlsx
mkdocs serve
```

## Figure placement

Put `Figure N` in column C on the row where the figure should appear.

The build script scans the `Main` sheet, generates `figures/figureN.py` outputs as Plotly HTML, and inserts the matching iframe into the rendered `index.md` at that point in the page.

## Adding a new figure

1. Create `figures/figure3.py`
2. Make it define `generate_figure(workbook_path, out_html)`
3. Put `Figure 3` in column C where you want it inserted
4. Run `python build_site.py ...`

## GitHub Pages

The included workflow publishes the generated `docs/` folder to GitHub Pages.
