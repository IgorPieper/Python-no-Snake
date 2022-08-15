import requests
import datetime as dt

# api = "nutritionix"

API_ID = "YOUR ID"
API_TOKEN = "YOUR TOKEN"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_TOKEN,
}

exercises = input("Tell me which exercises you did: ")

parameters = {
    "query": exercises,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 180,
    "age": 20,
}

response = requests.post(endpoint, json=parameters, headers=headers)
result = response.json()

# api = "Sheety"

sh_endpoint = "YOUR ENDPOINT"

for n in result["exercises"]:
    new_row = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": n["name"].title(),
            "duration": n["duration_min"],
            "calories": n["nf_calories"],
        }
    }

    sh_response = requests.post(sh_endpoint, json=new_row)
    print(sh_response.text)
