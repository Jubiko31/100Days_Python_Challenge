import requests

API = 'https://opentdb.com/api.php'
parameters = {
    "amount": 31,
    "category": 18,
    "type": "boolean"
}

response = requests.get(API, params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
