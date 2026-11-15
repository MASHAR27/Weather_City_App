import json
from datetime import datetime
from functions import get_coordinates,get_weather,display_weather

city = input("Please enter the city whose weather details you want: ").strip()

results = get_coordinates(city)
weather_info =get_weather(results["latitude"], results["longitude"])
display_weather(weather_info)

    


 new_record ={
    "city": city,
    "latitude":latitude,
    "longitude":longitude,
    "weather" : weather_descriptions.get(weather_code, "Weather condition not known!"),
    "weather_code" :	weather_code,
    "search_time" : datetime.now().isoformat()
}
    

history_file = "weather_history.json"

try:
    with open(history_file,"r") as file:
        existing = json.load(file)

except FileNotFoundError:
    existing = []

except json.JSONDecodeError:
    existing = []
    
existing.append(new_record)

with open(history_file,"w") as new_file:
    json.dump(existing,new_file)

print("Weather history updated successfully!")



    

