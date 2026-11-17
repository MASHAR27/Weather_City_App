from geocoding import get_coordinates
from weather import get_weather, display_weather,weather_descriptions
from history import save_history
from datetime import datetime

def main():
    """Runs all the above functions smoothly"""
    while True:
         city = input("Please enter the city whose weather details you want: ").strip()
         if not city:
             print("Please enter a city name, it can't be empty!")
             continue
         if city.lower() == "exit":
             print("Exiting the program")
             break
         results = get_coordinates(city)
         if results is None:
              continue
         weather_info = get_weather(results["latitude"], results["longitude"])
         if weather_info is None:
              continue
         display_weather(weather_info)
         weather_code = weather_info["current"]["weather_code"]
         
         new_record = {
        "city": city,
        "latitude": results["latitude"],
        "longitude": results["longitude"],
        "weather": weather_descriptions.get(
            weather_code,
            "Weather condition not known!"
        ),
        "weather_code": weather_code,
        "search_time": datetime.now().isoformat()
    }
         save_history(new_record)


if __name__ == "__main__":
    main()
