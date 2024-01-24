document.addEventListener("DOMContentLoaded", function () {
  let latitudeElement = document.getElementById("user-latitude");
  let longitudeElement = document.getElementById("user-longitude");

  let latitudeString = latitudeElement.getAttribute("data-user-latitude");
  let longitudeString = longitudeElement.getAttribute("data-user-longitude");

  let latitude = parseFloat(latitudeString.replace(",", "."));
  let longitude = parseFloat(longitudeString.replace(",", "."));

  console.log(latitude, longitude);
  let map = L.map("map").setView([latitude, longitude], 16);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);

  L.marker([latitude, longitude]).addTo(map);
});
