---
name: rename-literature-papers
description: Inspect locally extracted scientific-paper Markdown and immediately rename matching PDF and Markdown pairs with consistent bibliographic names. Use for autonomous literature-library cleanup, publisher-download filenames, DOI-style filenames, or requests to rename papers as year, first author, final author, journal acronym, and short title without a review or approval step. Do not use for converting PDFs or extracting experimental data into Excel.
---

# Rename Literature Papers

Use Codex's model access to interpret the Markdown directly. Do not call the OpenAI API and do not require an API key.

## Inputs

- Read PDFs from `../literature pdfs/*.pdf`.
- Read extracted text from `../literature pdfs/markdown/*.md`.
- Require one PDF and one Markdown file with the same stem before renaming the pair.
- Ignore `old/`, logs, and nested PDFs.

## Naming rule

Build one ASCII-safe stem in this form:

`YEAR_FirstAuthor_FinalAuthor_JOURNAL_Short-title-phrase`

Apply these constraints:

- Use the year of the formal journal citation, not submission or acceptance year.
- Use the surnames of the first and final authors in the paper's author list.
- Preserve compound surnames as one token, for example `DeWolf` or `MoralesMasis`.
- Use a recognisable journal or conference acronym containing at most 9 letters or digits.
- Use a two-to-four-word title phrase, normally 16-28 characters including hyphens.
- Use underscores between bibliographic fields and hyphens within the title phrase.
- Remove accents and filesystem-unsafe punctuation.
- Give the PDF and Markdown partner exactly the same stem.

Example: `2019_Aydin_DeWolf_ADVFNMAT_IZrO-tandem-electrodes.pdf`.

## Workflow

1. Inventory every top-level Markdown file and its same-stem PDF partner. Report and skip only files that have no partner.
2. Read each Markdown file. Locate the title, formal publication year, ordered author list, and journal name. Search throughout the file when the opening text is disordered.
3. Resolve uncertain metadata without asking the user: inspect the PDF title page, then use an official publisher or DOI page if local evidence is insufficient. Use the strongest available evidence and continue.
4. Build all target stems in memory. Check for duplicate targets, existing destinations, Windows-reserved characters, and filenames over 180 characters. Resolve a duplicate by selecting a more distinctive short-title phrase.
5. Immediately rename every valid PDF and Markdown pair using exact literal paths. Do not display a plan or wait for confirmation. If either member of a pair cannot be renamed, restore the other member's original name before continuing.
6. Write `../literature pdfs/rename-log.csv` after the operation with a timestamp, every old-to-new mapping, and any skipped pair with its reason.
7. Verify that every top-level PDF has a same-stem Markdown partner and report the completed count and any failures.

Never edit paper contents, overwrite an existing file, or invent bibliographic facts unsupported by the paper or an authoritative source.
