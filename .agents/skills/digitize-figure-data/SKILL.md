---
name: digitize-figure-data
description: Digitize quantitative data from scientific figure JPEG or PNG files with the online WebPlotDigitizer interface, save a calibrated CSV, and cross-check it against values and trends stated in the paper Markdown. Use when a literature figure contains plotted markers, curves, bars, or multiple panels and the underlying numerical data are not otherwise available. Do not use for extracting figures from PDFs or for visually estimating values without axis calibration.
---

# Digitize Figure Data

Extract plotted scientific data with the online WebPlotDigitizer application. Work directly through the browser; do not require Python, an API key, or an OpenAI API call.

## Inputs and outputs

- Accept a figure image path. Read `caption.txt` from the same directory when present.
- Never modify the source image or caption.
- Save the final table beside the image as `<figure-stem>_data.csv`, for example `Figure_01_data.csv`.
- Treat every output value as digitized from a published graphic, not as an author-supplied raw measurement.
- Do not create a manifest or a review plan. Perform the digitization immediately.

## Workflow

1. Inspect the whole image and caption. Identify panels, axis variables, units, scale types, plotted series, marker shapes, colours, and legends.
2. Open [WebPlotDigitizer](https://apps.automeris.io/wpd4/) in the browser and load the image.
3. Choose `2D (X-Y) Plot` for ordinary Cartesian plots. Handle each panel independently when a figure contains separate axes.
4. Calibrate each panel with exact labelled ticks:
   - Select two widely separated x-axis ticks and two widely separated y-axis ticks.
   - Enter the printed tick values exactly.
   - Select linear or logarithmic scaling to match the axis.
   - Use a separate calibration for panels whose plotting rectangles or y axes differ, even when they share an x variable.
5. Create one dataset for each scientifically distinct series. Name datasets with the panel, y variable, and condition, such as `top_Ne_as_deposited`.
6. Collect points at marker centres. Zoom in and click markers rather than connecting lines, error bars, or legend symbols. Use automatic extraction only when colour separation is unambiguous; inspect and correct the result manually.
7. Review the plotted overlay and data table inside WebPlotDigitizer. Check that:
   - the number of points matches the visible markers;
   - x values follow the visible experimental sequence;
   - no legend symbols, axis ticks, or error-bar caps were captured;
   - repeated-series x coordinates agree within the graphical resolution when they represent the same experimental settings.
8. Export every dataset as CSV. Combine the exported datasets into the final table without inventing missing values.
9. Cross-check the result against the Markdown version of the same paper:
   - Locate the matching file in the sibling `markdown/` directory using the paper year and author name from the figure path.
   - Search the paper text for the figure number, caption terms, variables, units, conditions, and any numerical values discussed around the figure.
   - Compare only values or trends explicitly stated in the paper with the digitized table. Treat normal graphical reading uncertainty and rounding as agreement.
   - Classify each comparison as `agrees`, `qualitatively agrees`, `no textual value reported`, or `possible discrepancy`.
   - If a possible discrepancy appears, recheck series identity, units, axis scale, and calibration before reporting it. Do not change CSV values merely to force agreement with the prose.

## Table shape

Use a wide table when multiple series share the same discrete x settings. Put the independent variable first and give every dependent-value column a self-contained name with condition and unit, for example:

```csv
rO2_percent,Ne_as_deposited_1e20_cm-3,Ne_annealed_200C_1e20_cm-3,mobility_as_deposited_cm2_Vs,mobility_annealed_200C_cm2_Vs
0.000,...,...,...,...
```

Use a tidy table when panels or series do not share x settings:

```csv
panel,series,x_variable,x_value,x_unit,y_variable,y_value,y_unit
```

Represent values that cannot be resolved as empty cells, not zero. Preserve scientific sign and exponent conventions in headers. Use only enough decimal places to reflect the graph's resolution; avoid false precision.

## Completion checks

- Reopen the final CSV and verify that headers, rows, decimal separators, and missing cells parse correctly.
- Compare the CSV against the figure once more for swapped series, panel mix-ups, and obvious calibration errors.
- Report the source figure, output path, datasets digitized, point counts, axis calibration values, and a concise Markdown-text cross-check with the comparison classifications above.
- If browser upload, calibration, or export cannot be completed, report the exact blocker. Do not silently replace calibrated digitization with visual estimates.
