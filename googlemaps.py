import requests
import json
import fileinput
import pandas


for line in fileinput.input(files = "config.env"):
    key = line

def get_gas_stations():
    #This wil get the gas stations around the longitude and latitude
    type = "gas%20station" #%20 is escape for space
    latitude = "37.95098545221008"
    longitude = "-91.77840922372175"

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + latitude + "%2C" + longitude + "&type=" + type + "&keyword=" + type + "&rankby=distance" + "&key=" + key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_string = json.loads(response.text)

    gas_stations = []
    for gas_station in response_string['results']:
        gas_stations.append(gas_station['name'])
    return gas_stations

print(get_gas_stations())

#Output- pandas data frame
#column 1 - name
#column 2 - distance
#list for Carter
#dictionary with appropriate data


