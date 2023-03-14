import requests

api_key = "0564af452ff5dc7be4147cedd3b6284d"

endpoint = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": 55.532051,
    "lon": 28.660320,
    "appid": api_key,
}

response = requests.get(url=endpoint, params="parameters")
response.raise_for_status()
print(response.json())
