import requests
import json
import fileinput

#Read in API key from config.env file
for line in fileinput.input(files = "config.env"):
    key = line

#Returns a list of nearby gas stations given latitude and longitude as string
#The closest gas station is listed first
#Default location is the Gale Bullman building
def get_gas_stations(latitude = "37.95098545221008", longitude = "-91.7784092232175"):
    type = "gas%20station" #%20 is escape for space

    #GoogleMaps API works by making an HTTPS request with input parameters in the url link
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + latitude + "%2C" + longitude + "&type=" + type + "&keyword=" + type + "&rankby=distance" + "&key=" + key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    #Convert JSON to a string
    response_string = json.loads(response.text)

    gas_stations = []
    for gas_station in response_string['results']:
        #Check if GoogleMapsAPI reports the gas station as open or not
        try:
            if gas_station["opening_hours"]["open_now"]:
                gas_stations.append(gas_station['name'])
        except KeyError: #GoogleMapsAPI does not report if this gas station is open, assume open
            gas_stations.append(gas_station['name'])
    return gas_stations
