# from datetime import datetime
#
# import requests
# import pprint
#
# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = "https://api.sheety.co/ba78c813be217d53517d29d03421df29/workoutTracking/workouts"
#
# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")
#
# # This part refers to the nutritionix API
# GENDER = "male"
# WEIGHT_KG = 78
# HEIGHT_CM = 182
# AGE = 31
#
# APP_ID = "de21c256"
# API_KEY = "5ceae0e6fa43755d33894d0ade9890bd"
#
# exercise_text = input("Tell me which exercises you did: ")
#
# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }
#
# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }
#
# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
#
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#
#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#     print(sheet_response.text)


for i in range(0, 19000):
    print(f"{i};", end="")
