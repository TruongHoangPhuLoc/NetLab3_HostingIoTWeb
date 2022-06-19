import requests
import json
def getGeo():
    #API KEY is required
    response = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAAc0PA_-mO3_MdQ_gknqhd4ZtP_3saJi8")
    obj = json.loads(response.text)
    print(obj)
    return {"lat":obj["location"]["lat"],"lng":obj["location"]["lng"]}


getGeo()