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
        

def display_weather(weath_response_data):
    """Shows the weather data after receving it as an argument """ 
    weather_descriptions = {
	0: "Clear sky",
	1: "Mainly clear",
	2: "Partly cloudy",
	3: "Overcast",
	45: "Fog",
	48: "Depositing rime fog",
	51: "Light drizzle",
	53: "Moderate drizzle",
	55: "Dense drizzle",
	56: "Light freezing drizzle",
	57: "Dense freezing drizzle",
	61: "Slight rain",
	63: "Moderate rain",
	65: "Heavy rain",
	66: "Light freezing rain",
	67: "Heavy freezing rain",
	71: "Slight snowfall",
	73: "Moderate snowfall",
	75: "Heavy snowfall",
	77: "Snow grains",
	80: "Slight rain showers",
	81: "Moderate rain showers",
	82: "Violent rain showers",
	85: "Slight snow showers",
	86: "Heavy snow showers",
	95: "Thunderstorm",
	96: "Thunderstorm with slight hail",
	97: "Heavy thunderstorm",
	99: "Thunderstorm with heavy hail"
} # from the official Open-Meteo.com - the weather codes keys and their values 
    weather_code = weath_response_data["current"]["weather_code"]
    weather_description = weather_descriptions.get(
    weather_code,
    "Weather condition not known!"
)
    print("Current weather:", weather_description)
    
    print("The temeperatures,relative humidity and windspeed  in this city for each time is given below: ")
    for i in range(len(weath_response_data["hourly"]["time"])):
        print(weath_response_data["hourly"]["time"][i]," has temperature: " ,weath_response_data["hourly"]["temperature_2m"][i]," and relative humidity of ",weath_response_data["hourly"]["relative_humidity_2m"][i]," and wind speed of ",weath_response_data["hourly"]["wind_speed_10m"][i] )
            
            
def save_history(record):
    """Receives the new record(basically this search's data and saves it into the json file for persistence)"""
    try:
        with open("weather_history.json", "r") as file:
             existing = json.load(file)
    except FileNotFoundError:
        existing = []  
    except json.JSONDecodeError:
        existing = []
    existing.append(record)
    with open("weather_history.json","w") as new_file:
        json.dump(existing,new_file)
    print("Weather history updated successfully!")
    
   
            


        
   
   
            

            
   
          
            
            
   