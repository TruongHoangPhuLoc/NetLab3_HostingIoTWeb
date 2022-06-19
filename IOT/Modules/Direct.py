from urllib import response
import requests
import json
source = {"lat":13.92655689659678,"long":107.93661406496243}
destination = {"lat":15.13624882749528,"long":106.68795669568348}
url = str.format("https://maps.googleapis.com/maps/api/directions/json?origin={},{}&destination={},{}&key=AIzaSyCV7EHyN-qOilgx_e_IIGtwaDy1_cn5YRs",source["lat"],source["long"],destination["lat"],destination["long"])
payloat = {}
header = {}
response = requests.request("GET",url)
print(response.text)