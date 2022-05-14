function changeClass(getClass) {
  var infoThree = document.getElementById("infoThree").value;
  $.ajax({
    type: "GET",
    url: "/my/url/",
    data: {
      check_this: $("#this_field").val(),
    },
    success: function (data) {
      console.log("success");
      console.log(data);
    },
    failure: function (data) {
      console.log("failure");
      console.log(data);
    },
  });
}
