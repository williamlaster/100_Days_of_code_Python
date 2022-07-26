import requests
import os
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY_NUTRITIONIX")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise/"
SHEETY_ENDPOINT = "https://api.sheety.co/a24998a301b4f9247910ff636c9336b7/workoutTracking/workouts"
SHEETY_ID = os.environ.get("SHEETY_ID")
SHEETY_KEY = os.environ.get("SHEETY_KEY")

today = datetime.now()

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

workout = input("Tell me which exercises you did: ")

workout_params = {
    "query": workout,
    "gender": "male",
}

response = requests.post(url=EXERCISE_ENDPOINT,
                         json=workout_params, headers=headers)
data = response.json()

sheety_headers = {
    "Authorization": f"{SHEETY_ID} {SHEETY_KEY}"
}

sheety_inputs = {}
for exercise in data["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    print(sheety_inputs)

    sheety_response = requests.post(
        url=SHEETY_ENDPOINT, json=sheety_inputs, headers=sheety_headers)
    print(sheety_response.status_code)
