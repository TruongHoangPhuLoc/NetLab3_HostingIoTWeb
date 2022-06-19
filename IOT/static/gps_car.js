setInterval(() => {
  getLocation();
}, 1000);
function getLocation() {
  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(positionProcessing, showError);
  } else { 
      x.innerHTML = "Geolocation is not supported by this browser.";
  }
}       
function renderMarker(position){
  marker.setLatLng([position.coords.latitude,position.coords.longitude]);
  marker.setOpacity(1);
  map.setView([position.coords.latitude,position.coords.longitude],150);
}
function sendPositionToServer(position)
{
  var obj = {lat:position.coords.latitude,lng: position.coords.longitude};
  httpPost('/car_location',obj);
}
function positionProcessing(position)
{
  renderMarker(position);
  sendPositionToServer(position);
}
function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
      "<br>Longitude: " + position.coords.longitude;
}

function showError(error) {
switch(error.code) {
  case error.PERMISSION_DENIED:
  x.innerHTML = "User denied the request for Geolocation."
  break;
  case error.POSITION_UNAVAILABLE:
  x.innerHTML = "Location information is unavailable."
  break;
  case error.TIMEOUT:
  x.innerHTML = "The request to get user location timed out."
  break;
  case error.UNKNOWN_ERROR:
  x.innerHTML = "An unknown error occurred."
  break;
}
}   