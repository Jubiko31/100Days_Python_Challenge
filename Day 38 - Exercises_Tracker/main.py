# Advanced Exercise Tracker
# Stores exercise data in google sheet
import os
import requests
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

AGE = 20
GENDER = 'male'
WEIGHT_KG = 82
HEIGHT_CM = 180
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GOOGLE_SHEETS_ENDPOINT = "https://api.sheety.co/9ded8262ccb7a3a2a14ed43fa21dc089/myWorkouts/workouts"
APP_ID = os.getenv('NUTRIX_APP_ID')
APP_KEY = os.getenv('NUTRIX_APP_KEY')

exercise = input("Tell me which exercises you did today: ")  # run 4 kms, swim 200 m...

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=params, headers=headers)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
new_date = datetime.now().strftime("%X")

for workout in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today,
            "time": new_date,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }
    
    res = requests.post(GOOGLE_SHEETS_ENDPOINT, json=sheet_input)
    
    print(res.text)