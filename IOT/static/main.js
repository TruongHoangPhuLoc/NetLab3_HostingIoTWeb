let map;
let marker;
var test = 10;
function initialMap(){
 map = L.map('map' ,{
  center: [0, 0],
  zoom: 1
});
  // L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=yllyE2xjroSx8oZFIod0',
  // {
  //     attribution:'<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
  // }).addTo(map);
 const tilesURL = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
 const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>';
 const tiles = L.tileLayer(tilesURL,{attribution});
 tiles.addTo(map);
 marker = L.marker([0,0]).addTo(map);
 marker.setOpacity(0);
}
initialMap();
/*
function httpPost(theUrl,obj)
{
  var xhr = new XMLHttpRequest();
  xhr.open("POST", theUrl, false);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({
    value: obj
}));
  return xhr.responseText
}

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // true for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}*/
async function httpPost(theUrl,obj){
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      value: obj
    })
  };
  const response = await fetch(theUrl,requestOptions);
  const result = await response.text();
  return result;  
}
async function httpGet(theUrl){
  var response = await fetch(theUrl);
  var result = await response.text();
  return result;
}