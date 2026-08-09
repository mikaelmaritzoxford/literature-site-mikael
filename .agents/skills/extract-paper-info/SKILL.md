---
name: extract-paper-info
description: Read one locally converted scientific-paper Markdown file and its related figure captions or digitized CSVs, then populate the existing izro_literature.xlsx Papers, Reported Data, and Notes sheets using the workbook's established IDs, columns, formatting, and evidence conventions. Use for adding or enriching one literature paper in the IZrO Excel database. Do not edit the Main sheet or invent unreported measurements.
---

# Extract Paper Info

Populate `izro_literature.xlsx` from one paper using Codex language-model analysis. Use the spreadsheet skill and its required artifact-tool workflow for every workbook edit.

## Source discovery

1. Identify the target paper Markdown under the sibling `literature pdfs/markdown/` directory.
2. Read the complete Markdown, emphasizing metadata, abstract, experimental methods, results, figures, tables, and conclusions.
3. Read matching `caption.txt` and `Figure_*_data.csv` files under `literature pdfs/figures/<paper-folder>/` when present.
4. Treat the Markdown as the primary textual source and digitized CSV values as approximate graphical extractions. Never present digitized values as author-supplied raw data.

## Inspect before editing

1. Import the existing workbook and inspect the used ranges, tables, headers, recent IDs, and formatting in `Papers`, `Reported Data`, and `Notes`.
2. Render those sheets before editing and preserve their established visual style.
3. Build the Paper ID from the first author's surname and year, matching forms such as `Morales-Masis_2018`.
4. Search Paper ID and DOI before inserting. If either already exists, update and enrich the existing paper, observations, and Notes row instead of creating a duplicate.

## Populate Papers

- Maintain exactly one row per publication.
- Fill only the existing columns and preserve the workbook's Paper ID convention.
- Record verified author names, journal, year, title, DOI, DOI or publisher URL, a concise abstract summary, keywords, and useful provenance notes.
- Do not edit `Main`.

## Populate Reported Data

- Maintain one row per distinct observation, sample, condition, or plotted data point.
- Reuse existing observations for the paper when they describe the same evidence; otherwise append rows with the next unused global `O#` identifiers.
- Put numeric values in the dedicated typed columns whenever a matching column exists. Use `Property name`, `Property value`, and `Property unit` for additional or mixed observations.
- Preserve fabrication method, deposition and annealing conditions, gas ratio, thickness, measurement context, and source figure/table whenever reported.
- Label digitized values in `Source figure/table` and `Comments`, and use confidence reflecting graphical resolution.
- Leave unavailable fields blank. Never infer a missing value from a nearby sample.

## Populate Notes

- Maintain exactly one Notes row per paper.
- Fill `Paper ID`, `Tags`, and four or five knowledge-nugget columns.
- Write each nugget as one standalone scientific statement of fewer than 30 words.
- Separate reported evidence from author interpretation; avoid generic praise or unsupported synthesis.

## Verify and report

1. Preserve table coverage and copy the adjacent row formatting to new rows.
2. Inspect the added or updated ranges, scan for formula errors, and render `Papers`, `Reported Data`, and `Notes` after editing.
3. Save the completed workbook as the requested project workbook without producing multiple competing versions.
4. Report the Paper ID, affected sheets, observation IDs, number of nuggets, source files used, and any uncertainty.
5. End with a short on-screen summary of the paper's main findings.
