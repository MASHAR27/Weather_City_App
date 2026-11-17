import json

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
    