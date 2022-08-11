import requests

QUESTION_AMOUNT = 50
question_data = []

parameters = {
    "amount": QUESTION_AMOUNT,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

for n in data["results"]:
    question_data.append({"question": n["question"], "correct_answer": n["correct_answer"]})
