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
        if "results" not in coordinates:
             print("City couldn't be found")
             return None
        else:
            longitude = coordinates["results"][0]["longitude"]
            latitude = coordinates["results"][0]["latitude"]  
            return {
    "latitude": latitude,
    "longitude": longitude
}
            

            
   
          
            
            
   