import requests
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data = response.json()
removed_data = data.pop("response_code")
question_data = data['results']
