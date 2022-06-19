import math
#convert coordinates to digital signals 
def getGreaterExchange_Rate(source,destination):
    latitude_subtraction = abs(destination["lat"]) - abs(source["lat"])
    longitude_subtraction = abs(destination["lng"]) - abs(source["lng"])
    return "lng" if abs(longitude_subtraction) > abs(latitude_subtraction) else "lat"

def direction_lookup_modify(source,destination):
    #based on (x,y) if source[x] > destination[x] we assign sour[x] = 1 and des[x] = 0
    #Opposite, des[x] = 1 and sour[x] = 0
    #Get which coordinates is greater between longitude and latitude
    selection = getGreaterExchange_Rate(source,destination)
    #initialize source and destination
    if selection == "lng":
        if source["lng"] > destination["lng"]:
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
def get_instructions(markers):
    instructions = []
    for index in range(0,len(markers)-1):
        if index != len(markers) - 1:
            direction = direction_lookup_modify(markers[index],markers[index + 1])
            source = {"lat":markers[index]["lat"],"lng":markers[index]["lng"]}
            des = {"lat":markers[index+1]["lat"],"lng":markers[index+1]["lng"]}
            instructions.append({"source":source,"des":des,"direction":direction})
    return instructions