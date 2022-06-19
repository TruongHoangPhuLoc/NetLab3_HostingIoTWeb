import math
from turtle import back
# # def direction_lookup(destination_x, origin_x, destination_y, origin_y):

# #     deltaX = destination_x - origin_x

# #     deltaY = destination_y - origin_y

# #     degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180

# #     if degrees_temp < 0:

# #         degrees_final = 360 + degrees_temp
# #     else:

# #         degrees_final = degrees_temp

# #     compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]

# #     compass_lookup = round(degrees_final / 45)

# #     return compass_brackets[compass_lookup], degrees_final

# n = 4
# arr = 4*[0]
# obj = []

# #longitude = X
# #latitude = Y
# #listing all of cases by backtracking
# def backtracking(index):
#     for choice in range(0,2):
#         arr[index] = choice
#         if index == len(arr) - 1:
#             obj.append({"source['x']":arr[0],"source['y']":arr[1],"des['x']":arr[2],"des['y']":arr[3]})      
#         else:
#             backtracking(index+1)
# backtracking(0)

def direction_lookup(destination_x, origin_x, destination_y, origin_y):

    deltaX = destination_x - origin_x

    deltaY = destination_y - origin_y

    degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180

    # if degrees_temp < 0:

    #     degrees_final = 360 + degrees_temp
    # else:

    #     degrees_final = degrees_temp
    return degrees_temp
# def get_direction(destination_x, origin_x, destination_y, origin_y):
#     deltaX = destination_x - origin_x

#     deltaY = destination_y - origin_y

#     degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180

#     if degrees_temp < 0:

#         degrees_final = 360 + degrees_temp
#     else:

#         degrees_final = degrees_temp

#     compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]

#     compass_lookup = round(degrees_final / 45)

#     return compass_brackets[compass_lookup]

# for i in obj:
#     result = direction_lookup(i["des['x']"],i["source['x']"],i["des['y']"],i["source['y']"])
#     direction = get_direction(i["des['x']"],i["source['x']"],i["des['y']"],i["source['y']"])
#     i["result"] = result
#     i["direction"] = direction
#     print(i)




# {"source['x']": 0, "source['y']": 0, "des['x']": 0, "des['y']": 0, 'result': 0.0}
# {"source['x']": 0, "source['y']": 0, "des['x']": 0, "des['y']": 1, 'result': 0.0}
# {"source['x']": 0, "source['y']": 0, "des['x']": 1, "des['y']": 0, 'result': 90.0}
# {"source['x']": 0, "source['y']": 0, "des['x']": 1, "des['y']": 1, 'result': 45.0}
# {"source['x']": 0, "source['y']": 1, "des['x']": 0, "des['y']": 0, 'result': 180.0}
# {"source['x']": 0, "source['y']": 1, "des['x']": 0, "des['y']": 1, 'result': 0.0}
# {"source['x']": 0, "source['y']": 1, "des['x']": 1, "des['y']": 0, 'result': 135.0}
# {"source['x']": 0, "source['y']": 1, "des['x']": 1, "des['y']": 1, 'result': 90.0}
# {"source['x']": 1, "source['y']": 0, "des['x']": 0, "des['y']": 0, 'result': 270.0}
# {"source['x']": 1, "source['y']": 0, "des['x']": 0, "des['y']": 1, 'result': 315.0}
# {"source['x']": 1, "source['y']": 0, "des['x']": 1, "des['y']": 0, 'result': 0.0}
# {"source['x']": 1, "source['y']": 0, "des['x']": 1, "des['y']": 1, 'result': 0.0}
# {"source['x']": 1, "source['y']": 1, "des['x']": 0, "des['y']": 0, 'result': 225.0}
# {"source['x']": 1, "source['y']": 1, "des['x']": 0, "des['y']": 1, 'result': 270.0}
# {"source['x']": 1, "source['y']": 1, "des['x']": 1, "des['y']": 0, 'result': 180.0}
# {"source['x']": 1, "source['y']": 1, "des['x']": 1, "des['y']": 1, 'result': 0.0}



#---------------------------------------------------------------------------------------


# {"source['x']": 0, "source['y']": 0, "des['x']": 0, "des['y']": 0, 'result': 0.0, 'direction': 'N'}
# {"source['x']": 0, "source['y']": 0, "des['x']": 0, "des['y']": 1, 'result': 0.0, 'direction': 'N'}
# {"source['x']": 0, "source['y']": 0, "des['x']": 1, "des['y']": 0, 'result': 90.0, 'direction': 'E'}
# {"source['x']": 0, "source['y']": 0, "des['x']": 1, "des['y']": 1, 'result': 45.0, 'direction': 'NE'}
# {"source['x']": 0, "source['y']": 1, "des['x']": 0, "des['y']": 0, 'result': 180.0, 'direction': 'S'}
# {"source['x']": 0, "source['y']": 1, "des['x']": 0, "des['y']": 1, 'result': 0.0, 'direction': 'N'}
# {"source['x']": 0, "source['y']": 1, "des['x']": 1, "des['y']": 0, 'result': 135.0, 'direction': 'SE'}
# {"source['x']": 0, "source['y']": 1, "des['x']": 1, "des['y']": 1, 'result': 90.0, 'direction': 'E'}
# {"source['x']": 1, "source['y']": 0, "des['x']": 0, "des['y']": 0, 'result': -90.0, 'direction': 'W'}
# {"source['x']": 1, "source['y']": 0, "des['x']": 0, "des['y']": 1, 'result': -45.0, 'direction': 'NW'}
# {"source['x']": 1, "source['y']": 0, "des['x']": 1, "des['y']": 0, 'result': 0.0, 'direction': 'N'}
# {"source['x']": 1, "source['y']": 0, "des['x']": 1, "des['y']": 1, 'result': 0.0, 'direction': 'N'}
# {"source['x']": 1, "source['y']": 1, "des['x']": 0, "des['y']": 0, 'result': -135.0, 'direction': 'SW'}
# {"source['x']": 1, "source['y']": 1, "des['x']": 0, "des['y']": 1, 'result': -90.0, 'direction': 'W'}
# {"source['x']": 1, "source['y']": 1, "des['x']": 1, "des['y']": 0, 'result': 180.0, 'direction': 'S'}
# {"source['x']": 1, "source['y']": 1, "des['x']": 1, "des['y']": 1, 'result': 0.0, 'direction': 'N'}



#convert coordinates to digital signals 
def getGreaterExchange_Rate(source,destination):
    latitude_subtraction = destination["lat"] - source["lat"]
    longitude_subtraction = destination["long"] - source["long"]
    return "long" if abs(longitude_subtraction) > abs(latitude_subtraction) else "lat"

def direction_lookup_modify(source,destination):
    #based on (x,y) if source[x] > destination[x] we assign sour[x] = 1 and des[x] = 0
    #Opposite, des[x] = 1 and sour[x] = 0
    #Get which coordinates is greater between longitude and latitude
    selection = getGreaterExchange_Rate(source,destination)
    #initialize source and destination
    if selection == "long":
        if source["long"] > destination["long"]:
            destination_x = 0
            origin_x = 1
        else:
            destination_x = 1
            origin_x = 0
        #set y = 0
        origin_y = 0
        destination_y = 0
    else:
        if source["lat"] > destination["lat"]:
            destination_y = 0
            origin_y = 1
        else:
            destination_y = 1
            origin_y = 0
        #set x = 0
        origin_x = 0
        destination_x = 0
    deltaX = destination_x - origin_x
    deltaY = destination_y - origin_y
    degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180
    return degrees_temp
source = {"lat":10.523394737470575,"long":106.61131771246664}
destination = {"lat":10.505132837063009,"long":108.00493333454006}
#latitude = Y
#longitude = X
print(direction_lookup_modify(source,destination))

#Latitude: 10.821637414566116 | Longitude: 106.68801536900568

#Latitude: 10.821582233931487 | Longitude: 106.6879758064227