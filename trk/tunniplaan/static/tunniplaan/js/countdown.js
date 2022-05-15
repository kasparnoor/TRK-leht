window.onload = function () {
  /* Add your logic here */
  // Get todays date and time
  var now = new Date();
  console.log("Now1: " + now);
  var day = now.getDate();
  console.log("Day1: " + day);
  var month = now.getMonth() + 1;
  console.log("Month1: " + month);
  var year = now.getFullYear();
  console.log("Year1: " + year);
  var hours = now.getHours();
  console.log("Hours1: " + hours);
  var minutes = now.getMinutes();
  console.log("Minutes1: " + minutes);
  var seconds = now.getSeconds();
  console.log("Seconds1: " + seconds);
  var infoTwo = parseFloat(document.getElementById("infoTwo").value);
  console.log("InfoTwo1: " + infoTwo);
  var newseconds = seconds + Math.floor(infoTwo);
  console.log("NewSeconds: " + newseconds);

  if (newseconds > 60) {
    var extraminutes = Math.floor(newseconds / 60);
    var leftseconds = newseconds - extraminutes * 60;
  } else {
    leftminutes = minutes;
  }

  if (minutes + extraminutes > 60) {
    var extrahours = Math.floor((minutes + extraminutes) / 60);
    var leftminutes = minutes + extraminutes - extrahours * 60;
  } else {
    extrahours = 0;
    leftminutes = minutes + extraminutes;
  }
  minutes = minutes + extraminutes;
  newseconds = leftseconds;
  hours = hours + extrahours;
  console.warn(
    minutes +
      " minutes - " +
      extraminutes +
      " extraminutes - " +
      extrahours +
      " extrahours"
  );
  var nextlesson =
    year +
    "-" +
    month +
    "-" +
    day +
    " " +
    hours +
    ":" +
    minutes +
    ":" +
    newseconds;
  var nextlesson2 = nextlesson.replace(/-/g, "/");
  var countDownDate = new Date(nextlesson2);
  // Update the count down every 1 second
  setInterval(function () {
    console.log("nextlesson2: " + nextlesson);
    console.log("countDownDate: " + countDownDate);
    var now = new Date().getTime();
    console.log("Now: " + now);

    // Find the distance between now and the count down date
    var distance = countDownDate - now;
    console.log("Distance: " + distance);
    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    console.log("Days: " + days);
    var hours = Math.floor(
      (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
    );
    console.log("Hours: " + hours);
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    console.log("Minutes: " + minutes);
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    console.log("Seconds: " + seconds);
    // document.querySelector(".days").innerHTML = parseInt(days);
    document.querySelector(".hours").innerHTML = parseInt(hours);
    document.querySelector(".minutes").innerHTML = parseInt(minutes);
    document.querySelector(".seconds").innerHTML = parseInt(seconds);

    console.log(
      "input content: " + document.querySelector(".seconds").innerHTML
    );
    // If the count down is finished, write some text
    if (distance < 0) {
      clearInterval(x);
      document.location.reload();
    }
  }, 1000);
};
