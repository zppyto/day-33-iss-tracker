import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()

longtitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (latitude, longtitude)

print(data)