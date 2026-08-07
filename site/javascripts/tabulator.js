(function () {
  const REPORTED_DATA_DEFAULTS = [
    "Paper ID",
    "Sample / condition",
    "Dopant (at.%)",
    "Fabrication technique",
    "Deposition temp (C)",
    "Post-deposition temp (C)",
    "Atmosphere",
    "Thickness (nm)",
    "Mobility (cm^2/Vs)",
    "Resistivity (ohm·cm)",
    "Carrier concentration (cm^-3)",
    "Bandgap (eV)",
    "Property name",
    "Property value",
    "Property unit",
  ];

  function inferColumnOptions(field) {
    const key = String(field || "");
    const lower = key.toLowerCase();

    const textish = /(title|abstract|summary|notes?|comment|description|citation|journal|author|process|method|environment|device|stack|keyword)/i.test(key);
    const numerish = /(year|temperature|temp|mobility|resist|sheet|dopant|concentration|efficiency|bandgap|work function|affinity|fermi|vacuum|pressure|thickness|value)$/i.test(key);

    const base = {
      title: key,
      field: key,
      headerFilter: "input",
      headerFilterPlaceholder: "filter",
      headerSort: true,
      minWidth: textish ? 220 : 120,
      widthGrow: textish ? 3 : 1,
    };

    if (textish) {
      base.formatter = "textarea";
      base.variableHeight = true;
    }

    if (numerish) {
      base.hozAlign = "right";
    }

    return base;
  }

  async function loadCsv(csvUrl) {
    const response = await fetch(csvUrl, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Failed to load CSV: ${csvUrl}`);
    }
    return await response.text();
  }

  function renderGrid(container) {
    const csvPath = container.dataset.csv;
    const title = container.dataset.title || "Data";
    const hasColumnPicker = container.dataset.columnPicker === "true";

    const csvUrl = new URL(csvPath, window.location.href).toString();

    container.innerHTML = `<div class="grid-loading">Loading ${title}&hellip;</div>`;

    loadCsv(csvUrl)
      .then((csvText) => {
        const parsed = Papa.parse(csvText, {
          header: true,
          skipEmptyLines: true,
        });

        if (parsed.errors && parsed.errors.length) {
          throw parsed.errors[0];
        }

        const data = (parsed.data || []).filter((row) =>
          Object.values(row).some((v) => String(v ?? "").trim() !== "")
        );

        const fields = data.length ? Object.keys(data[0]) : [];
        if (!fields.length) {
          container.innerHTML = `<div class="grid-empty">No rows found in ${title}.</div>`;
          return;
        }

        const defaultFields = new Set(
          hasColumnPicker
            ? REPORTED_DATA_DEFAULTS.filter((field) => fields.includes(field))
            : fields
        );
        const columns = fields.map((field) => ({
          ...inferColumnOptions(field),
          visible: defaultFields.has(field),
        }));

        // Better first impression for literature tables:
        // search, sort, resize, and compact enough to fit scientific columns.
        const table = new Tabulator(container, {
          data,
          columns,
          layout: "fitDataStretch",
          responsiveLayout: "collapse",
          movableColumns: true,
          resizableColumnFit: true,
          placeholder: `No rows in ${title}`,
          pagination: true,
          paginationSize: 15,
          paginationSizeSelector: [10, 15, 25, 50],
          index: fields[0],
          height: "680px",
        });

        if (hasColumnPicker) {
          addColumnPicker(container, table, fields, defaultFields);
        }
      })
      .catch((err) => {
        console.error(err);
        container.innerHTML = `<div class="grid-error">Failed to render ${title}. Check the browser console.</div>`;
      });
  }

  function addColumnPicker(container, table, fields, defaultFields) {
    const controls = document.createElement("details");
    controls.className = "column-picker";
    controls.innerHTML = `
      <summary>Choose reported-data columns</summary>
      <p>Select the measurements you want to compare. Every visible column can be filtered and sorted from its header.</p>
      <div class="column-picker-actions">
        <button type="button" data-action="defaults">Recommended columns</button>
        <button type="button" data-action="all">Show all columns</button>
      </div>
      <div class="column-picker-options"></div>
    `;

    const options = controls.querySelector(".column-picker-options");
    fields.forEach((field) => {
      const label = document.createElement("label");
      const input = document.createElement("input");
      input.type = "checkbox";
      input.value = field;
      input.checked = defaultFields.has(field);
      input.addEventListener("change", () => {
        if (input.checked) table.showColumn(field);
        else table.hideColumn(field);
      });
      label.append(input, document.createTextNode(field));
      options.append(label);
    });

    function applySelection(selected) {
      options.querySelectorAll('input[type="checkbox"]').forEach((input) => {
        input.checked = selected.has(input.value);
        if (input.checked) table.showColumn(input.value);
        else table.hideColumn(input.value);
      });
    }

    controls.querySelector('[data-action="defaults"]').addEventListener("click", () => {
      applySelection(defaultFields);
    });
    controls.querySelector('[data-action="all"]').addEventListener("click", () => {
      applySelection(new Set(fields));
    });
    container.before(controls);
  }

  function init() {
    if (typeof window.Tabulator === "undefined" || typeof window.Papa === "undefined") {
      console.warn("Tabulator or Papa Parse is not loaded.");
      return;
    }

    document.querySelectorAll(".csv-grid[data-csv]").forEach((container) => {
      if (container.dataset.gridReady === "1") return;
      container.dataset.gridReady = "1";
      renderGrid(container);
    });
  }

  if (window.document$ && typeof document$.subscribe === "function") {
    document$.subscribe(init);
  } else {
    window.addEventListener("load", init);
  }
})();
