import math
import hw04_util as z

zip_codes = z.read_zip_all()

temp = True

"""
function location_by_zip(zip_codes, code)
inputs:
zip_codes => the full list of zip code tuples
code = the zip code to search for

returns:
a tuple that match the zip_code (code) provided
if no match, an empty tuple is returned
"""
def location_by_zip(zip_codes, code):
    max_length = len(zip_codes)
    found_zip = ()
     
    for i in range(0, max_length):   
        if zip_codes[i][0] == code: 
            found_zip = zip_codes[i]
    return found_zip[1:]                      

"""
function lat_long(zip_code)
converts a value into deg, min, sec along with latitude or longitude direction
""" 
def lat_long(zip_code):
    if zip_code[0] < 0:
        lat_sign = 'S'
    elif zip_code[0] > 0:
        lat_sign = 'N'
    else:
        lat_sign = ''
          
    latitude = abs(zip_code[0])
    lat_deg = int(latitude)
    lat_min = int((latitude - lat_deg) * 60)
    lat_sec = ((latitude - lat_deg - lat_min/60) * 3600) 
     
    if zip_code[1] < 0:
        long_sign = 'W'
    elif zip_code[1] > 0:
        long_sign = 'E'
    else:
        long_sign = ''
          
    longitude = abs(zip_code[1])
    long_deg = int(longitude)
    long_min = int((longitude - long_deg) * 60)
    long_sec = ((longitude - long_deg - long_min/60) * 3600)       
     
    return ("\n\tcoordinates: ({:03d}".format(lat_deg) + "\xb0" + str(lat_min)\
           + "'" + str(round(lat_sec, 2)) + "\"" + lat_sign +\
           ",{:03d}".format(long_deg) + "\xb0" + str(long_min) + "'" +\
           str(round(long_sec, 2)) + "\"" + long_sign + ")")     

"""
function zip_by_location(zip_codes, location)
inputs:
zip_codes => the full list of zip code tuples
location = tuple of city and state

returns:
a list of zips that match the location provided
if no match, an empty list is returned
"""  
def zip_by_location(zip_codes, location):

    max_length = int(len(zip_codes))
    zip_codes_list = []     
    for i in range(0, max_length): 
        if zip_codes[i][3] == location[0] and zip_codes[i][4] == location[1]:
            zip_codes_list.append(zip_codes[i][0]) 
    return zip_codes_list  

"""
calculates distance between two zip codes
inputs: z1 and z2
outputs: distance
"""
def find_distance(z1, z2):
    R = 3959.191
     
    first_lat = z1[0]
    f_lat_rad = first_lat * math.pi / 180
               
    first_long = z1[1]
    f_long_rad = first_long * math.pi / 180
     
    second_lat = z2[0]
    s_lat_rad = second_lat * math.pi / 180
               
    second_long = z2[1]
    s_long_rad = second_long * math.pi / 180
     
    delta_lat = s_lat_rad - f_lat_rad
    delta_long = s_long_rad - f_long_rad
    
    a = math.pow(math.sin(delta_lat/2), 2) + (math.cos(f_lat_rad) *\
    math.cos(s_lat_rad) * math.pow(math.sin(delta_long/2), 2))
     
    distance = 2 * R * math.asin(math.sqrt(a))
     
    return distance

"""
Main program, asks for user input, calls appropriate function depending on
input and print results
"""
while temp is True:
    #asks user for input command
    user_input = input("Command ('loc', 'zip', 'dist', 'end') => ")
    print(user_input) 
    user_input = user_input.lower()
     
    if user_input == "loc":
        #asks user for zip
        user_zip_code = input("Enter a ZIP code to lookup => ")
        print(user_zip_code)
          
        #gets info for user inputed zip
        found_zip = location_by_zip(zip_codes, user_zip_code)
         
        #print info for valid zip 
        if not found_zip:
            print("Invalid or unknown ZIP code")
        else:
            str_lat_long = lat_long(found_zip)
            print("ZIP code", user_zip_code, "is in " + str(found_zip[2]) +\
                  ", " + str(found_zip[3]) + ", " + str(found_zip[4]) +\
                  " county," + str_lat_long)               
        print()
          
    elif user_input == "zip":
        #asks user for city and state
        user_city = input("Enter a city name to lookup => ")
        print(user_city)
        user_city = user_city.title()
          
        user_state = input("Enter the state name to lookup => ")
        print(user_state)
        user_state = user_state.upper()
            
        location = (user_city, user_state)
        
        #get zips for specified location 
        num_zips = zip_by_location(zip_codes, location)
        
        #print zips for valid location  
        if not num_zips:
            print("No ZIP code found for " + user_city + ", " + user_state)                         
        else:
            print("The following ZIP code(s) found for", user_city + ", " +\
                  user_state + ": "+ ", ".join(num_zips))   
        print()
     
    elif user_input == "dist":
        #asks users to input two zips
        first_zip = input("Enter the first ZIP code => ")
        print(first_zip)
          
        second_zip = input("Enter the second ZIP code => ")
        print(second_zip)  
        
        #gets lat and long info from zips provided  
        first_info = location_by_zip(zip_codes, first_zip)
        second_info = location_by_zip(zip_codes, second_zip)
        
        #prints error for invalid zip  
        if not first_info or not second_info:
            print("The distance between", first_zip, "and", second_zip,\
                  "cannot be determined")
        else:
            #calculates and prints distance between two zips
            distance = find_distance(first_info, second_info)
            print("The distance between", first_zip, "and", second_zip,\
                  "is {0:.2f}".format(distance), "miles")
        print()
                                     
    elif user_input == "end":
        temp = False
        print()
        print("Done")
          
    else:
        print("Invalid command, ignoring")
        print()
          
if __name__ == "__main__":
    temp = True