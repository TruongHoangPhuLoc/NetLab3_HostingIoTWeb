import json
import requests
def outPutdata(obj):
    print(obj)

def distanceCalculation(arrayObj):
    response = requests.get()


import requests

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=10.822445410414515,106.68826566827614&destinations=10.822474966239396,106.68832467687447&key=AIzaSyB8DKlqACwhsXV3splf60RvQJQrqQJNb4c"
str = str.format("https://maps.googleapis.com/maps/api/distancematrix/json?origins={},{}&destinations={},{}&key=AIzaSyB8DKlqACwhsXV3splf60RvQJQrqQJNb4c",10.822027878316499,106.68846930589224,10.82192043983734,106.68851624455)

payload={}
headers = {}

response = requests.request("GET", str, headers=headers, data=payload)
# Latitude: 10.822445410414515 | Longitude: 106.68826566827614
# Latitude: 10.822474966239396 | Longitude: 106.68832467687447

#10.798069581461503 | 106.62215620611718
#10.442276496893571 | 107.16711717487851
print(response.text) 
