import math
#cre: https://www.analytics-link.com/post/2018/08/21/calculating-the-compass-direction-between-two-points-in-python
def direction_lookup(destination_x, origin_x, destination_y, origin_y):

    deltaX = destination_x - origin_x

    deltaY = destination_y - origin_y

    degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180

    if degrees_temp < 0:

        degrees_final = 360 + degrees_temp
    else:

        degrees_final = degrees_temp

    compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]

    compass_lookup = round(degrees_final / 45)

    return compass_brackets[compass_lookup], degrees_final
#above link is used to data analyze so we can adjust sth to be more simple in lab for 4 basic directions  

source = {"lat":9,"long": 6}
destination = {"lat":1,"long":1}
#origination_x = source.lat
#origination_y = source.long
#destination_x = des.lat
#destination_y = des.long

print(direction_lookup(destination["lat"],source["lat"],destination["long"],source["long"]))
#print(direction_lookup(7,2,7,3))
def getDegrees(lat1, lon1, lat2, lon2,head):
    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)
    bearing = math.degrees(math.atan2(dLon, dLat))
    return head-bearing
print("-----------------------")

#here is exchange-function to be more simple than above function
def direction_lookup_modify(origin_x, origin_y, destination_x, destination_y):
    #based on (x,y) if source[x] > destination[x] we assign sour[x] = 1 and des[x] = 0
    #Opposite, des[x] = 1 and sour[x] = 0
    if destination_x > origin_x:
        destination_x = 1
        origin_x = 0
    elif destination_x < origin_x:
        destination_x = 0
        origin_x = 1
    else:
        destination_x = 1
        origin_x = 1
    #continously, we begin at source[y] and destination[y]
    if destination_y > origin_y:
        destination_y = 1
        origin_y = 0
    elif destination_y < origin_y:
        destination_y = 0
        origin_y = 1
    else:
        destination_y = 1
        origin_y = 1
    deltaX = destination_x - origin_x
    deltaY = destination_y - origin_y
    degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180
    if degrees_temp < 0:
        degrees_final = 360 + degrees_temp
    else:
        degrees_final = degrees_temp
    result = ""
    if degrees_final > 0 and degrees_final <= 90:
        result = "E"
    elif degrees_final > 90 and degrees_final <= 180:
        result = "S"
    elif degrees_final > 180 and degrees_final <= 270:
        result = "W"
    else:
        result = "N"
    return  result,degrees_final

source = {"lat":10.817958540619,"long":106.62731654014631}
destination = {"lat":10.818131761709301,"long":106.63132268713805}
#longitude = x
#latitude = y
#How can i detect what value is greater exchange-rate between longitude and latitude to select?
#May i convert to string then compare them? 
# def getGreaterExchange_Rate(source,destination):
#     count_latitude = 0
#     count_longitude = 0
#     #compare X
#     str_source = str(source["long"])
#     str_destination = str(destination["long"])
#     leng = 0
#     if len(str_source) < len(str_destination):
#         leng = len(str_source)
#     else:
#         leng = len(str_destination)
#     for i in range(0,leng):
#         if str_source[i] != str_destination[i]:
#             break
#         count_longitude += 1
#     #compare Y
#     str_source = str(source["lat"])
#     str_destination = str(destination["lat"])
#     if len(str_source) < len(str_destination):
#         leng = len(str_source)
#     else:
#         leng = len(str_destination)
#     for i in range(0,leng):
#         if str_source[i] != str_destination[i]:
#             break
#         count_latitude += 1
#     if count_longitude < count_latitude:
#         return "long"
#     else:
#         return "lat"
#it's done
def getGreaterExchange_Rate(source,destination):
    latitude_subtraction = destination["lat"] - source["lat"]
    longitude_subtraction = destination["long"] - source["long"]
    return "long" if abs(longitude_subtraction) > abs(latitude_subtraction) else "lat"
source = {"lat":10.817958540619,"long":106.62731654014631}
destination = {"lat":10.818131761709301,"long":106.63132268713805}
print(direction_lookup_modify(source["long"],source["lat"],destination["long"],destination["lat"]))
