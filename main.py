import requests


city = input("Please enter the city whose weather details you want: ").strip()

url = "https://geocoding-api.open-meteo.com/v1/search"# the endpoint for the coordinates API/server

param = {
    "name" : city,
    "count": 1,
    "format": "json",
    "language": "en"
}

response_from_geo = requests.get(url=url,params=param,timeout=10)

response_from_geo.raise_for_status() # for the 4xx (bad requests) or 5xx errors(server side problem)

coordinates = response_from_geo.json()
print(coordinates)
# After I get the coordinates for the city I put them in for the next request 







