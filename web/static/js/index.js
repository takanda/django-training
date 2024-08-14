const books = {};

function CreateSelectBox(authers, selectLength) {
  const selectBox = $(`<div></div>`).attr("id", `selectbox-${selectLength}`);
  const select = $(`<select></select>`).attr("name", `selectbox-${selectLength}`);
  const button = $(`<button>追加</button>`).attr("class", "select-button");

  select.append('<option value="">--default--</option>');
  for (const auther of authers) {
    select.append(`<option value="${auther}">${auther}</option>`);
  }
  selectBox.append(select).append(button);
  $(".select-container").append(selectBox);

  return selectLength + 1;
}

$(function () {
  authers = [];
  selectLength = 0;

  $.ajax({
    url: "http://localhost:10001/book/authers/",
    method: "GET",
    dataType: "json",
    success: function (data) {
      console.log(data);
      for (const d of data) {
        authers.push(d["name"]);
        books[d["name"]] = d["books"];
      }
      selectLength = CreateSelectBox(authers, selectLength);
    },
    error: function (textStatus, errorThrown) {
      console.error("データの取得に失敗しました:", textStatus, errorThrown);
    },
  });

  $(document).on("change", "select", function () {
    const selectedAuther = $(this).val();

    if (selectedAuther && books[selectedAuther]) {
      const bookList = $("<ul></ul>");
      for (const book of books[selectedAuther]) {
        bookList.append(`<li>${book.title} (${book.published_at})</li>`);
      }
      $(this).parent().append(bookList);
    }
  });

  $(document).on("click", ".select-button", function () {
    selectLength = CreateSelectBox(authers, selectLength);
  });
});
