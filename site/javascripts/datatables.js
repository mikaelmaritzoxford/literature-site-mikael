(function () {
  function initDataTables() {
    if (typeof window.DataTable === "undefined") {
      console.warn("DataTables is not loaded.");
      return;
    }

    document.querySelectorAll("article table").forEach(function (table) {
      if (table.dataset.dtReady === "1") return;
      table.dataset.dtReady = "1";

      new DataTable(table, {
        scrollX: true,
        autoWidth: false,
        paging: false,
        searching: true,
        ordering: true,
        info: false,
        layout: {
          topStart: "search",
          topEnd: null,
          bottomStart: null,
          bottomEnd: null
        }
      });
    });
  }

  if (window.document$ && typeof document$.subscribe === "function") {
    document$.subscribe(initDataTables);
  } else {
    window.addEventListener("load", initDataTables);
  }
})();