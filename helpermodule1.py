import requests
import json
import sys
import csv
from math import sin, cos, sqrt, atan2, radians


def getlatlong(ip):

    ##url = "http://api.ipstack.com/163.118.241.234"

    url = "http://api.ipstack.com/" + ip

    print (url)


    querystring = {"access_key":"91224a4223a5f29f868752bc83c3b2a4"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "555d33f0-66df-431e-b1cc-2f049b21249e"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    ##print(response.text)


    j = json.loads(response.text)

    lat = j["latitude"]
    lon = j["longitude"]

    print (j["latitude"])
    print (j["longitude"])

    return (lat, lon)


def getgeodistance(lat1, lon1, lat2, lon2):
    

    # approximate radius of earth in km
    R = 6373.0

##    lat1 = radians(52.2296756)
##    lon1 = radians(21.0122287)
##    lat2 = radians(52.406374)
##    lon2 = radians(16.9251681)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    distance = distance / 1.6  ##convert to miles

    ##print("Result:", distance)

    return (distance)


def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
            print("I/O error")    
    return 
