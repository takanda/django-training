$(function () {
  $.ajax({
    url: "http://localhost:10001/book/authers/",
    method: "GET",
    dataType: "json",
    success: function (data) {
      console.log(data)
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error("データの取得に失敗しました:", textStatus, errorThrown);
      $("#user-info").html("<p>データの取得に失敗しました。</p>");
    },
  });
  $(".select-container .select-button").click(function () {
    $(".select-button").after("test");
  });
});
