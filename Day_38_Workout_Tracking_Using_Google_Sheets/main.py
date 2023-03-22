from datetime import datetime

import requests
import pprint

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/ba78c813be217d53517d29d03421df29/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

customer_choice = input("Tell me which the ex you did: ")
GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 182
AGE = 31

APP_ID = "de21c256"
API_KEY = "5ceae0e6fa43755d33894d0ade9890bd"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

body = {
    "query": customer_choice,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=body, headers=HEADERS)
print(response.text)

response_of_sheety_get = requests.get(sheety_endpoint)
print(response_of_sheety_get.text)
