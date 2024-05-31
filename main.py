import requests
from datetime import datetime
import time

MY_LAT = 45.512794
MY_LONG = -122.679565

#Get ISS Position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
MY_LAT_PROX = MY_LAT + 5
MY_LONG_PROX = MY_LONG + 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

#Get sunset and sunrise times
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

#Get time now
time_now = datetime.now().hour

def iss_near_me():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    
def is_it_night():
    if iss_near_me and time_now > sunset and time_now < sunrise:
        return True

while True:
    time.sleep(60)
    if iss_near_me() and is_it_night():
        print("look up!")
    else:
        print("maybe tomorrow!")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



