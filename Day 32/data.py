import requests
response=requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean")

question_data = response.json()["results"]
