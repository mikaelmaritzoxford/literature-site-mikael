document$.subscribe(function () {
  document.querySelectorAll("article table").forEach(function (table) {
    if (table.dataset.dtReady === "1") return;
    table.dataset.dtReady = "1";

    new DataTable(table, {
      scrollX: true,
      autoWidth: false,
      paging: false,
      searching: true,
      ordering: true,
      info: false
    });
  });
});