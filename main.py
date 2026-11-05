import requests
import sys

city = input("Please enter the city whose weather details you want: ").strip()

geo_url = "https://geocoding-api.open-meteo.com/v1/search"# the endpoint for the coordinates API/server

param = {
    "name" : city,
    "count": 1,
    "format": "json",
    "language": "en"
}

response_from_geo = requests.get(url=geo_url,params=param,timeout=10)

response_from_geo.raise_for_status() # for the 4xx (bad requests) or 5xx errors(server side problem)

coordinates = response_from_geo.json()

# After I get the coordinates for the city I put them in for the next request 
if "results" not in coordinates:
    print("City couldn't be found")
    sys.exit()
    
longitude = coordinates["results"][0]["longitude"]
latitude = coordinates["results"][0]["latitude"]
print("The Longitude is ",longitude)
print("The Latitude is ",latitude)



weather_url = "https://api.open-meteo.com/v1/forecast"

weather_para = {
    "latitude" :latitude,
    "longitude":longitude,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m" # I ask for temp at 2m ,Relative humidity at 2 metres, and wind speed at 10m
}

weath_response = requests.get(url=weather_url,params=weather_para,timeout=10)

weath_response.raise_for_status() # again for 4xx and 5xx errors

if weath_response.status_code != 200:
    print("Weather for the city couldn't be found")
    sys.exit()
    
weath_response_data = weath_response.json()
print("The temeperatures,relative humidity and windspeed  in this city for each time is given below: ")
for i in range(len(weath_response_data["hourly"]["time"])):
    print(weath_response_data["hourly"]["time"][i]," has temperature: " ,weath_response_data["hourly"]["temperature_2m"][i]," and relative humidity of ",weath_response_data["hourly"]["relative_humidity_2m"][i]," and wind speed of ",weath_response_data["hourly"]["wind_speed_10m"][i] )
    
    
    

