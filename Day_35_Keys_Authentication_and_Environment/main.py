from twilio.rest import Client
import requests
import os

account_sid = "AC7aafaa494a04c277a700ffbdcae8a8f5"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

api_key = "349a35d3f3c95904257d35da7e26381d"
latitude = 55.532051
longitude = 28.660320

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data['hourly'][:12]
print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+15077040526",
        to="+375295610381"
    )
    print(message.status)


weather_by_hour = []
for i in range(0, 12):
    weather_by_hour.append(weather_data["hourly"][i]['weather'][0]["id"])
    if weather_data["hourly"][i]['weather'][0]["id"] < 700:
        print(f"Bring an Umbrella hours {i+1}")
    else:
        print(f"fuck hours {i+1}")

print(weather_by_hour)
