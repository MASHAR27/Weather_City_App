import requests
import sys
import json
from datetime import datetime

def get_coordinates(city):
    """ Receives a city name and then makes a request to the Open-Meteo's geocoding API to retrieve the coordinates for that city """
    geo_url = "https://geocoding-api.open-meteo.com/v1/search" # the endpoint for the coordinates API/server
    param = {
    "name" : city,
    "count": 1,
    "format": "json",
    "language": "en"
}
    try:
        sent = requests.get(url=geo_url,params=param,timeout=10)
        sent.raise_for_status() # for the 4xx (bad requests) or 5xx errors(server side problem)
    except requests.exceptions.Timeout:
        print("The request took too long ")
        return None
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to the server")
        return None
    except requests.exceptions.HTTPError:
        print("There was either a 4xx or 5xx error basically a bad request or a server side problem")
        return None
    else:
        coordinates = sent.json()
        if not coordinates.get("results"):
             print("City couldn't be found")
             return None
        else:
            longitude = coordinates["results"][0]["longitude"]
            latitude = coordinates["results"][0]["latitude"]  
            return {
    "latitude": latitude,
    "longitude": longitude
}

def get_weather(latitude, longitude):
    """Takes the coordinates of the previous call as argument and then sends a request to the endpoint of open-meteo for their weather details as a dictionary """
    weather_url = "https://api.open-meteo.com/v1/forecast" # the endpoint for this request
    weather_para = {
    "latitude" :latitude,
    "longitude":longitude,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m", # I ask for temp at 2m ,Relative humidity at 2 metres, and wind speed at 10m
    "current": "weather_code" # this will ensure that the response will have this weather code 
}
    try:
        weath_response = requests.get(url=weather_url,params=weather_para,timeout=10)
        weath_response.raise_for_status() # again for 4xx and 5xx errors
    except requests.exceptions.Timeout:
        print("The request took too long ") 
        return None
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to the server")
        return None
    except requests.exceptions.HTTPError:
        print("There was either a 4xx or 5xx error basically a bad request or a server side problem")
        return None
    else:
        weath_response_data = weath_response.json()
        return weath_response_data
        


   
   
            

            
   
          
            
            
   