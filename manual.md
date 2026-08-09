# Literature Survey Workflow for Doctoral Researchers

## Purpose

This guide defines a practical workflow for conducting, documenting,
analysing, and publishing a doctoral-level literature survey. The aim is
not simply to collect papers, but to build a structured, auditable body
of knowledge that can be updated throughout the doctorate and shared
with the research group.

The workflow uses **Zotero or another reference manager** for papers,
**Excel** as the research workspace, **Python** for reproducible figures
and site generation, **MkDocs** for the website, **Plotly** for
interactive figures, **CSV + Tabulator** for large data tables, and
**GitHub Pages** for publication.

> **Papers are sources. The literature survey is a structured collection
> of evidence, observations, interpretations, and synthesis built from
> those sources.**

------------------------------------------------------------------------

# 1. Define the Research Question

Do not begin by downloading hundreds of papers. Write the initial
scientific question in one or two sentences and identify the
subquestions that determine what information needs to be extracted.

For a materials-science topic, these may include fabrication methods,
compositions, processing conditions, electrical properties, optical
properties, electronic structure, device performance, measurement
methods, and unresolved questions.

The question will evolve during the doctorate. That is expected.

------------------------------------------------------------------------

# 2. Search Broadly Before Searching Deeply

Begin with broad combinations of material names, abbreviations,
alternative chemical names, properties, fabrication methods,
applications, review articles, highly cited papers, and recent papers.

The first objective is to understand the vocabulary and structure of the
field. Do not attempt exhaustive extraction during this stage.

Once important papers appear, follow their references, papers that cite
them, important authors, competing research groups, and alternative
terminology.

------------------------------------------------------------------------

# 3. Build the Paper Library

Store papers in a reference manager such as Zotero.

For every important paper, preserve the DOI, complete title, authors,
journal, year, PDF where legally available, URL, and useful tags.

Use consistent tags such as `core-paper`, `review`, `processing`,
`electrical`, `optical`, `electronic-structure`, `device`, and
`methodology`.

The reference manager is the **paper library**. It is not the structured
scientific database.

------------------------------------------------------------------------

# 4. Triage Before Deep Reading

Not every paper requires line-by-line reading.

A useful first pass is:

1.  Title
2.  Abstract
3.  Figures and tables
4.  Conclusions
5.  Experimental section
6.  Relevant results sections

Then decide whether the paper deserves detailed extraction.

High-value papers should receive substantially more attention than
peripheral papers.

------------------------------------------------------------------------

# 4A. Run the PDF Intake Sub-Workflow

Keep the two intake stages separate:

1.  **Python + AnyDoc:** convert text-based PDFs to Markdown locally.
2.  **Codex project skill:** read the Markdown, reason about bibliographic
    metadata, and immediately rename the PDF/Markdown pairs.

The Python stage performs no AI calls and needs no OpenAI API key. The Codex
stage runs interactively inside the project and uses Codex's existing model
access rather than a Python API client.

## 4A.1 Install the local converter

AnyDoc is the only extra Python package used for conversion. Install the
official Firecrawl Python binding in the active environment:

``` powershell
python -m pip install -r requirements-conversion.txt
```

This installs the package named `firecrawl-anydoc`. In code, it is imported as:

``` python
import anydoc
```

## 4A.2 Convert PDFs locally with AnyDoc

The complete converter is `convert_pdfs.py`. Its essential operation is:

``` python
from pathlib import Path
import anydoc

pdf_dir = Path("../literature pdfs")
markdown_dir = pdf_dir / "markdown"
markdown_dir.mkdir(exist_ok=True)

for pdf_file in pdf_dir.glob("*.pdf"):
    markdown = anydoc.to_markdown(str(pdf_file))
    (markdown_dir / f"{pdf_file.stem}.md").write_text(
        markdown,
        encoding="utf-8",
    )
```

From the literature-site project directory, execute:

``` powershell
python convert_pdfs.py
```

AnyDoc reads each top-level PDF and writes Markdown to:

``` text
literature pdfs/
    paper-a.pdf
    paper-b.pdf
    markdown/
        paper-a.md
        paper-b.md
```

AnyDoc's local PDF path extracts text-based PDFs. It does not perform OCR on
image-only or scanned papers. If conversion fails or produces very little
text, inspect that PDF separately and use an OCR tool before continuing.

## 4A.3 Rename papers inside the Codex project

The repository contains the project skill:

``` text
.agents/skills/rename-literature-papers/SKILL.md
```

Open this folder as a Codex project, then invoke the skill explicitly:

``` text
$rename-literature-papers rename every matching literature PDF and Markdown pair now.
```

No API key or Python OpenAI package is involved. Codex reads the files under
`literature pdfs/markdown/` and proposes matching PDF and Markdown names in
this form:

``` text
YEAR_FirstAuthor_FinalAuthor_JOURNAL_Short-title-phrase.pdf
```

For example:

``` text
2019_Aydin_DeWolf_ADVFNMAT_IZrO-tandem-electrodes.pdf
2019_Aydin_DeWolf_ADVFNMAT_IZrO-tandem-electrodes.md
```

The skill processes every Markdown file immediately and renames its matching PDF
and Markdown pair without a review stage. It resolves metadata from the local
files and, when necessary, an authoritative publisher or DOI page. Afterward it
creates `rename-log.csv`, checks that every PDF still has a same-stem Markdown
partner, and never overwrites an existing file.

## 4A.4 Carry verified metadata into Excel

The verified year, title, author surnames, journal, and source filename are
candidate fields for the `Papers` sheet. They remain proposals until checked
against the paper and assigned a stable Paper ID. Detailed numerical results
belong in `Reported Data`, not in the filename.

> **Conversion improves access; it does not verify scientific content. AI
> proposes metadata; the researcher approves it.**

------------------------------------------------------------------------

# 4B. Extract Figures and Panels Locally

The figure workflow is independent of Markdown conversion. It uses PyMuPDF to
locate captions and render complete figure regions at 300 DPI. OpenCV separates
compound figures only when the caption identifies panels such as `(a)` and
`(b)` and a whitespace gutter can be detected confidently.

Install the packages from conda-forge:

``` powershell
conda install -c conda-forge pymupdf opencv pillow numpy
```

For a pip-based environment, use:

``` powershell
python -m pip install -r requirements-figures.txt
```

Open an **Anaconda Prompt**, change to the project folder, and activate the
environment in which the packages were installed. The `/d` option allows the
command to change drive as well as directory:

``` powershell
cd /d "C:\path\to\literature site"
conda activate literature
```

Every extraction command must identify the source folder with `--folder` and
must select exactly one processing mode: `--pdf PREFIX` or `--all`. To extract
one paper, give enough of the beginning of its filename to identify it uniquely:

``` powershell
python extract_figures.py --folder "..\literature pdfs" --pdf 2018_Morales
```

For example, the prefix above selects
`2018_MoralesMasis_Ballif_JPHOTOV_Broadband-IZrO-electrode.pdf`. It is not
necessary to type the complete filename or `.pdf` extension. Prefix matching is
case-insensitive. If no file matches, or more than one file matches, the script
stops and asks for a more suitable prefix instead of guessing.

The folder can also be an absolute path when the PDFs are stored elsewhere:

``` powershell
python extract_figures.py --folder "D:\Research\Literature PDFs" --pdf 2018_Morales
```

The output structure is deliberately short:

``` text
figures/
    2019_Aydin/
        Figure_01/
            Figure_01.jpeg
            caption.txt
```

When panels can be separated, the same folder also contains files such as
`Figure_01_panel-a.jpeg` and `Figure_01_panel-b.jpeg`. The complete figure is
always retained. No manifest is generated. Inspect every extracted figure and
panel directly because scientific layouts can contain shared axes, inset plots,
or irregular panel arrangements that cannot be separated reliably by whitespace.

The `figures` output folder is always created inside the folder supplied to
`--folder`. After one-paper output has been checked, process every top-level PDF
in that same folder explicitly with:

``` powershell
python extract_figures.py --folder "..\literature pdfs" --all
```

Use `--dpi` only when a resolution other than the 300 DPI default is needed:

``` powershell
python extract_figures.py --folder "..\literature pdfs" --pdf 2018_Morales --dpi 400
```

------------------------------------------------------------------------

# 4C. Digitize Quantitative Figures with Codex

Do not digitize every extracted image automatically. First inspect the JPEGs and
select figures that contain quantitative plots whose underlying values are useful
to the literature database. Photographs, schematics, and figures that merely
repeat values already available in a table normally do not need digitization.

The repository contains the Codex skill:

``` text
.agents/skills/digitize-figure-data/SKILL.md
```

Invoke it with the target image:

``` text
$digitize-figure-data digitize Figure_01.jpeg
```

The skill uses the online WebPlotDigitizer interface. For each relevant panel it
selects exact labelled ticks, calibrates linear or logarithmic axes, creates one
dataset per scientific series, and collects marker centres or curve points. A
compound figure receives separate calibrations when its panels have different
axes.

WebPlotDigitizer may require the researcher to select the local JPEG manually in
the browser. After loading, Codex can continue the calibration and extraction.
The resulting table is stored beside the figure:

``` text
figures/
    2018_MoralesMasis/
        Figure_01/
            Figure_01.jpeg
            caption.txt
            Figure_01_data.csv
```

The CSV headers preserve variables, conditions, and units. Digitized values are
graphical estimates rather than author-supplied raw measurements, so they must be
labelled accordingly and should not contain unjustified precision. The skill also
checks values and trends against the matching paper Markdown and reports whether
they agree, qualitatively agree, lack a textual comparator, or show a possible
discrepancy.

------------------------------------------------------------------------

# 4D. Extract Paper Information into Excel with Codex

After the Markdown and any useful digitized tables are ready, invoke:

``` text
$extract-paper-info extract the 2018 Morales-Masis paper into izro_literature.xlsx
```

The repository skill is stored at:

``` text
.agents/skills/extract-paper-info/SKILL.md
```

The skill reads the complete paper Markdown, related captions, and available
`Figure_*_data.csv` files. It then inspects the existing workbook before editing
and updates only these database sheets:

- `Papers`: exactly one row per publication, using the established
  `FirstAuthor_Year` Paper ID convention.
- `Reported Data`: one row per reported observation, sample, condition, or
  digitized data point, using the next unused global `O#` identifier.
- `Notes`: exactly one row per paper containing tags and four or five knowledge
  nuggets, each shorter than 30 words.

The operation is idempotent. Before inserting, Codex checks both Paper ID and DOI.
If the publication already exists, it enriches the existing rows instead of
creating a duplicate. Missing values remain blank, figure-derived observations
are identified as digitized and given an appropriate confidence, and the `Main`
sheet is not changed.

After editing, Codex verifies the inserted ranges, checks for formula errors,
renders the affected sheets to confirm formatting, saves the workbook, and gives
a short on-screen summary of the paper's main findings. The spreadsheet remains
the authoritative editable database; Markdown, captions, and CSV files preserve
the source trail used to populate it.

------------------------------------------------------------------------

# 5. Use Excel as the Literature Workspace

The literature workbook contains four principal sheets:

-   `Main`
-   `Papers`
-   `Reported Data`
-   `Notes`

Each sheet has a different purpose. Do not collapse everything into one
enormous table.

Excel is deliberately used as the primary editing interface because it
allows researchers to rapidly compare heterogeneous numerical values,
processing information, comments, and knowledge fragments.

------------------------------------------------------------------------

# 6. Populate the Papers Sheet

The `Papers` sheet contains one row per publication.

Useful fields include:

-   Paper ID
-   DOI
-   Title
-   First author
-   Last author
-   Journal
-   Year
-   Abstract
-   URL
-   Topic tags
-   Relevance
-   Comments

Give every paper a stable identifier such as `P001`, `P002`, and `P003`.
Observations, notes, and analyses can then refer reliably to the same
source.

------------------------------------------------------------------------

# 7. Populate the Reported Data Sheet

The fundamental rule is:

> **One row represents one reported observation or experimental data
> point, not one paper.**

A paper may therefore produce one row, ten rows, or hundreds of rows.

Useful fields may include source paper, figure/table/page, material,
dopant, dopant concentration, composition, thickness, fabrication
technique, deposition temperature, pressure, gas environment,
post-treatment, annealing temperature and time, mobility, carrier
concentration, resistivity, sheet resistance, conductivity, work
function, Fermi energy, refractive index, extinction coefficient,
wavelength, bandgap, electron affinity, vacuum level, and valence-band
edge.

Do not force every paper to populate every field. Missing information is
itself useful information.

------------------------------------------------------------------------

# 8. Preserve Experimental Context

A value without context can be misleading.

`Mobility = 80 cm² V⁻¹ s⁻¹`

is much less useful than a record containing mobility together with
zirconium concentration, deposition method, thickness, annealing
temperature, atmosphere, measurement method, and source location.

Whenever comparing literature values, ask:

> **Are these measurements genuinely comparable?**

------------------------------------------------------------------------

# 9. Preserve Units and Traceability

Use consistent units wherever practical and include units in column
names or dedicated unit fields.

Examples include `cm² V⁻¹ s⁻¹` for mobility, `cm⁻³` for carrier
concentration, `Ω cm` for resistivity, `Ω/sq` for sheet resistance, `°C`
for temperature, `nm` for thickness, and `eV` for energy.

Every important numerical observation should ideally preserve the Paper
ID, DOI, figure/table/page, value, units, and relevant measurement
conditions.

A future researcher should be able to find the original evidence without
repeating the literature search.

------------------------------------------------------------------------

# 10. Build Knowledge Packets in Notes

The `Notes` sheet contains **knowledge packets**, not raw measurements.

A knowledge packet should normally communicate one scientific idea in
roughly 30--100 words.

Useful fields include:

-   Section
-   Heading
-   Knowledge packet
-   Supporting papers
-   Confidence
-   Contradicting papers
-   Tags
-   Student comments

Packets should be small enough to rearrange, revise, replace, and reuse.

------------------------------------------------------------------------

# 11. Separate Evidence, Author Interpretation, and Your Synthesis

Students should distinguish:

### Reported result

What the paper directly reports.

### Authors' interpretation

What the authors claim explains the observation.

### Researcher's synthesis

What you conclude after comparing the paper with other evidence.

Do not casually merge these three levels.

------------------------------------------------------------------------

# 12. Use AI as an Assistant, Not as Evidence

ChatGPT and Codex can accelerate discovery, terminology searches,
extraction schemas, summarisation, structured-record generation,
consistency checking, Python coding, figure generation, and drafting
knowledge packets.

For important scientific claims:

1.  Locate the original source.
2.  Inspect the relevant figure, table, methods section, or text.
3.  Verify the value and units.
4.  Record the source location.
5.  Only then accept the database entry.

> **AI proposes; the researcher verifies.**

------------------------------------------------------------------------

# 13. Follow Citation Networks

Once an important paper is identified:

-   inspect papers it cites;
-   inspect later papers that cite it;
-   search important authors;
-   identify related terminology;
-   identify competing research groups;
-   identify review articles;
-   look deliberately for contradictory results.

This iterative process is often more productive than repeatedly running
generic searches.

------------------------------------------------------------------------

# 14. Search Until the Topic Becomes Saturated

Useful coverage is approaching when new searches repeatedly return known
papers, new papers mostly reinforce existing knowledge packets, major
research groups and methods recur, and remaining knowledge gaps become
increasingly specific.

The initial intensive literature survey can finish at this point. The
literature database should remain alive throughout the doctorate.

------------------------------------------------------------------------

# 15. Use Main as the Website Narrative

The `Main` sheet controls the principal literature-review page.

The agreed structure is:

-   **A1**: overall page title.
-   **Column A populated and Column B empty**: level-one section.
-   **Columns A and B populated**: Column A is a subsection heading and
    Column B begins its narrative.
-   **Further Column B entries**: additional narrative belonging to the
    active subsection.
-   **Column C**: figure-placement markers such as `Figure 1`.

This lets the researcher control narrative order from Excel without
manually editing HTML.

------------------------------------------------------------------------

# 16. Keep Every Scientific Figure Independent

Store individual figure scripts as:

``` text
figures/
    figure1.py
    figure2.py
    figure3.py
```

Each script should generate one figure and read its underlying
observations directly from the workbook wherever practical.

Independent figure scripts are easier to understand, modify, debug,
reproduce, and reuse than one enormous plotting program.

------------------------------------------------------------------------

# 17. Generate Figures from Reported Data

A simple figure script might begin:

``` python
import pandas as pd
import plotly.express as px

df = pd.read_excel(
    "data/literature.xlsx",
    sheet_name="Reported Data"
)

fig = px.scatter(
    df,
    x="Dopant concentration",
    y="Mobility",
)

fig.write_html("docs/assets/plots/figure1.html")
```

The exact column names depend on the workbook.

Do not manually duplicate workbook values inside plotting scripts unless
there is a compelling scientific reason.

------------------------------------------------------------------------

# 18. Use Plotly for Interactive Scientific Figures

Plotly is useful where hover information, zoom, pan, selectable traces,
interactive legends, and exploration add scientific value.

The site generator embeds each generated Plotly HTML file at the
location specified by its `Figure N` marker in Column C of `Main`.

Static figures remain appropriate when interactivity provides no useful
benefit.

------------------------------------------------------------------------

# 19. Export Large Sheets to CSV for the Website

Do not publish `Papers` and `Reported Data` as enormous Markdown tables.

The Python build process should export them to:

``` text
docs/
    data/
        papers.csv
        reported-data.csv
        notes.csv
```

Excel remains the editing environment. CSV is a generated interchange
format for the browser.

------------------------------------------------------------------------

# 20. Render Large Tables as Interactive Grids

Use a browser grid such as Tabulator to load the generated CSV.

This provides sorting, searching, column filtering, resizable columns,
movable columns, horizontal navigation, and much better handling of wide
scientific datasets.

A generated page only needs a mount point such as:

``` html
<div
  class="csv-grid"
  data-csv="../data/reported-data.csv"
  data-title="Reported Data">
</div>
```

JavaScript then loads the CSV and renders the interactive grid.

------------------------------------------------------------------------

# 21. Recommended Project Structure

``` text
literature-project/
│
├── data/
│   └── literature.xlsx
│
├── figures/
│   ├── figure1.py
│   └── figure2.py
│
├── docs/
│   ├── index.md
│   ├── papers.md
│   ├── reported-data.md
│   ├── notes.md
│   │
│   ├── data/
│   │   ├── papers.csv
│   │   ├── reported-data.csv
│   │   └── notes.csv
│   │
│   ├── assets/
│   │   └── plots/
│   │
│   ├── javascripts/
│   │   └── tabulator.js
│   │
│   └── stylesheets/
│       └── extra.css
│
├── build_site.py
├── mkdocs.yml
└── environment.yml
```

Students may extend this structure as their literature site becomes more
sophisticated.

------------------------------------------------------------------------

# 22. What build_site.py Does

`build_site.py` is the bridge between the workbook and website.

Its responsibilities are:

1.  Read the workbook.
2.  Interpret `Main`.
3.  Generate `index.md`.
4.  Export database sheets to CSV.
5.  Find figure markers in Column C.
6.  Run the appropriate figure scripts.
7.  Place figure embeds in the correct narrative locations.

MkDocs then converts the generated Markdown and web assets into the
final static website.

------------------------------------------------------------------------

# 23. Set Up the Conda Environment

A typical `environment.yml` is:

``` yaml
name: literature

channels:
  - conda-forge

dependencies:
  - python>=3.11
  - pandas
  - openpyxl
  - plotly
  - mkdocs
  - mkdocs-material
```

Create the environment with:

``` bash
conda env create -f environment.yml
```

Then activate it:

``` bash
conda activate literature
```

Students can extend their own environments when their sites require
additional packages.

------------------------------------------------------------------------

# 24. Build and Preview Locally

From the project directory:

``` bash
python build_site.py data/literature.xlsx
mkdocs serve
```

MkDocs normally provides the local preview at:

``` text
http://127.0.0.1:8000/
```

`mkdocs serve` is a development preview only. It does not publish the
site.

Stop it with `Ctrl+C`.

------------------------------------------------------------------------

# 25. Use Material for MkDocs as a Starting Point

A minimal `mkdocs.yml` can contain:

``` yaml
theme:
  name: material
```

For wide literature pages, a useful CSS rule is:

``` css
.md-grid {
    max-width: initial;
}
```

and in `mkdocs.yml`:

``` yaml
extra_css:
  - stylesheets/extra.css
```

The template is a starting point. Students should be free to redesign
and extend their own sites.

------------------------------------------------------------------------

# 26. Publish with GitHub Pages

The preferred deployment route is GitHub Actions.

The researcher:

1.  creates a GitHub repository;
2.  pushes the project to the default branch;
3.  opens **Settings → Pages**;
4.  selects **GitHub Actions** as the publishing source;
5.  uses an Actions workflow that installs the site dependencies, runs
    `mkdocs build`, uploads the generated `site/` directory, and deploys
    it to Pages.

After configuration, publishing becomes automatic whenever relevant
changes are pushed.

There is no need to run `mkdocs gh-deploy` manually.

------------------------------------------------------------------------

# 27. Use GitHub as the Research History

Commit meaningful changes regularly.

Useful messages include:

``` text
Add sputtered IZrO papers
Extract mobility data from five papers
Add processing-temperature comparison
Revise electronic-structure synthesis
Correct carrier concentration units
```

Avoid histories consisting entirely of `update`, `changes`, or `test`.

Git history should help reconstruct how the literature understanding
developed.

------------------------------------------------------------------------

# 28. Verify Before Publishing

Before publishing an update, verify:

### Data

-   Values are transcribed correctly.
-   Units are correct.
-   Experimental conditions are recorded.
-   Sources are identifiable.
-   Duplicates are intentional.

### Knowledge

-   Claims have supporting evidence.
-   Disagreements are represented.
-   Author interpretations are distinguished from your synthesis.
-   AI-assisted text has been checked against sources.

### Figures

-   Axes and units are labelled.
-   Categories are defined.
-   Unusual points have been checked.
-   Figures can be regenerated from the workbook.

### Website

-   Links work.
-   Plotly figures load.
-   CSV grids load.
-   Headings appear in the intended order.
-   Figures appear after the intended paragraphs.

------------------------------------------------------------------------

# 29. Conduct Periodic Synthesis

At regular intervals ask:

-   What have I learned?
-   Which conclusions are robust?
-   Which conclusions depend on one paper?
-   Which variables explain differences between studies?
-   Which measurements are missing?
-   Which contradictions remain unresolved?
-   Which experiments would resolve them?

Update the knowledge packets rather than waiting until thesis writing.

------------------------------------------------------------------------

# 30. Let the Database Guide New Searches

Once structured data exist, search for missing evidence.

If the database contains many mobility measurements but almost no
work-function measurements, search specifically for work-function
evidence instead of continuing broad searches.

The literature database should progressively determine what the next
literature search needs to answer.

------------------------------------------------------------------------

# 31. Use Figures as Reasoning Tools

Figures should test scientific questions, not merely decorate the
website.

Examples:

-   Does mobility depend on dopant concentration?
-   Does resistivity correlate with annealing temperature?
-   Are sputtered films systematically different from solution-processed
    films?
-   Does bandgap correlate with carrier concentration?
-   Which processing regions remain unexplored?

Unexpected patterns should trigger renewed examination of the underlying
papers.

------------------------------------------------------------------------

# 32. Record Negative Knowledge and Contradictions

Important conclusions include:

> This property has not been systematically reported.

and:

> Existing measurements cannot be directly compared because measurement
> conditions differ.

When papers disagree, do not simply average their results. Examine
differences in measurement technique, fabrication, composition,
thickness, temperature, atmosphere, uncertainty, and physical
interpretation.

Contradictions often reveal the most valuable doctoral research
questions.

------------------------------------------------------------------------

# 33. End the Initial Survey with a Research Map

The initial doctoral survey should eventually produce:

### A structured paper library

The important literature has been identified and organised.

### A structured observations database

Important measurements and experimental conditions have been extracted.

### A knowledge compendium

Major scientific conclusions have been distilled into maintainable
packets.

### Comparative figures

Important relationships, trends, and disagreements can be visually
inspected.

### A knowledge-gap statement

The student can explain what is known, what remains uncertain, and why
new research is required.

### A living website

The literature survey is accessible, navigable, reproducible, and
capable of evolving throughout the doctorate.

------------------------------------------------------------------------

# 34. Maintain the Survey Throughout the Doctorate

The intensive initial survey should end. The knowledge base should not.

Continue to:

-   add important papers;
-   update knowledge packets;
-   add newly relevant observations;
-   regenerate figures;
-   record contradictions;
-   revise the synthesis.

A useful weekly habit is to identify new papers, triage them, deeply
extract the important ones, update `Reported Data`, update knowledge
packets, regenerate useful figures, inspect the website, and commit
meaningful changes.

------------------------------------------------------------------------

# 35. Final Principle

The purpose of this workflow is not to create the largest possible
spreadsheet or website.

It is to make scientific knowledge:

-   **traceable** to its source;
-   **structured** enough to compare;
-   **visual** enough to interrogate;
-   **modular** enough to update;
-   **reproducible** enough to trust;
-   **accessible** enough to share.

The final literature website is therefore not simply a collection of
summaries.

It is a continuously maintained **research knowledge base built from
published evidence**.
