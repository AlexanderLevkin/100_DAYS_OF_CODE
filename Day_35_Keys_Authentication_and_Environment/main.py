import requests

api_key = "f86e6a4afd3eb7c5fc434f4e601e9efe"

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 55.53,
    "lon": 28.66,
    "appid": api_key,
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
print(response.json())
