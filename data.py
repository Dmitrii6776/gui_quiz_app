import requests

parametrs = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean', params=parametrs).json()
question_data = response['results']
