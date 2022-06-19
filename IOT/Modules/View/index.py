
from urllib import response
from flask import Blueprint, jsonify,render_template,redirect,request, url_for
import json
import sys
import requests

from httplib2 import Http
#define global variable to save instructions 
index = Blueprint(__name__, "index")
@index.route("/")
def home():
    return render_template("index.html")

@index.route("/car")
def car():
    return render_template("getGPS.html")

@index.route("/manual_control",methods = ["POST"])
def manual_control():
    # global instruction
    # if request.method == "POST":
    #     instruction = json.loads(request.get_data(as_text=True))["value"]
    if request.method == "POST":
        f = open("/var/www/FlaskApp/IOT/Modules/View/instruction.txt","w")
        data = json.loads(request.get_data(as_text=True))["value"]
        f.write(json.dumps(data))
    return "Received manual instruction"

@index.route("/get_instruction")
def get_instruction():
    #result = instruction
    f = open("/var/www/FlaskApp/IOT/Modules/View/instruction.txt","r")
    result = f.readline()
    f.close()
    return json.loads(result)
@index.route("/location")
def manually_control():
    return render_template("manual.html")
@index.route("/car_location",methods = ["POST"])
def car_location():
    if request.method == "POST":
        f = open("/var/www/FlaskApp/IOT/Modules/View/location.txt","w")
        car_location = json.loads(request.get_data(as_text=True))["value"]
        f.write(json.dumps(car_location))
        f.close()
    return "Received GPS's Car"
# @index.route("/get_location")
# def get_location():
#     f = open("/var/www/FlaskApp/IOT/Modules/View/location.txt","r")
#     car_location = f.readline()
#     f.close()
#     return car_location 
@index.route("/get_location")
def get_location():
    response = requests.get("http://192.168.1.10/get_location")
    return response.json()
