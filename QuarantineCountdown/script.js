"use struct";
const d = document.getElementById("d");
const h = document.getElementById("h");
const m = document.getElementById("m");
const s = document.getElementById("s");

function countdown() {
  const currentDate = new Date();
  const departureDate = new Date("27 Jan 2021");

  if (currentDate > departureDate) {
    departureDate.setDate(departureDate.getDate() + 10);
  }

  const differanceInSeconds = Math.abs(departureDate - currentDate) / 1000;
  const days = Math.floor(differanceInSeconds / 3600 / 24);
  const hours = Math.floor(differanceInSeconds / 3600) % 24;
  const min = Math.floor(differanceInSeconds / 60) % 60;
  const sec = Math.floor(differanceInSeconds) % 60;
  d.innerHTML = days;
  h.innerHTML = hours;
  m.innerHTML = min;
  s.innerHTML = sec;
}

setInterval(countdown, 1000);
