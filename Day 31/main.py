import requests
from datetime import datetime
import smtplib
import time

# Find Your own latitude
MY_LAT=30.5134762
# Find Your own Longitude
MY_LONG=76.6612689

# Use your own email for this to work
my_email="abcd1234@gmail.com"

# Use your own app password for this to work
my_password="abcd efgh ijkl mnop"


def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data=response.json()

    longitude=float(data["iss_position"]["longitude"])
    latitude=float(data["iss_position"]["latitude"])

    if MY_LAT-5<= latitude <=MY_LAT+5 and MY_LONG-5<=longitude<=MY_LONG+5:
        return True

def is_night():
    paramters={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }

    response=requests.get(url="https://api.sunrise-sunset.org/json",params=paramters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now=datetime.now().hour

    if(time_now>=sunset or time_now<=sunrise):
        return True
    


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Look Up☝️\n\nThe ISS is above you in the sky."
            ) 