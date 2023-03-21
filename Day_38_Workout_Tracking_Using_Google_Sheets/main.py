import requests
import pprint

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

APP_ID = "de21c256"
API_KEY = "5ceae0e6fa43755d33894d0ade9890bd"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

body = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=exercise_endpoint, json=body, headers=HEADERS)
print(response.text)

