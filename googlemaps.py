import requests
import json
import fileinput

for line in fileinput.input(files = "config.env"):
    key = line

#This wil get the gas stations in x meters around the longitude and latitude
type = "gas%20station"
radius = 2000
latitude = "37.95098545221008"
longitude = "-91.77840922372175"
#url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + latitude + "%2C" + longitude + "&radius=" + str(radius) + "%40" + latitude + "%2C" + longitude + "&fields=formatted_address%2Cname%2Copening_hours%2Cgeometry&key=" + key
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + latitude + "%2C" + longitude + "&radius=" + str(radius) + "&type=" + type + "&keyword=" + type + "&key=" + key


payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)



response_string = json.loads(response.text)

#print(response_string)

for gas_station in response_string['results']:
    print(gas_station['name'])
