import requests
from datetime import datetime
import time

MY_LAT = -16 # Your latitude
MY_LONG = -48 # Your longitude




print(MY_LAT)
print(MY_LONG)
#Your position is within +5 or -5 degrees of the ISS position.

def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude >= MY_LAT+5 and MY_LONG-5 <= iss_longitude >= MY_LONG+5:
        return True

def is_dark():

    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    if hour >= sunset and hour <= sunrise:
        return True







#returns true

#If the ISS is close to my current position
# and it is currently dark


while True:
    time.sleep(60)
    if is_close() and is_dark():
        with smtplib.SMTP('smtp.gmail.com') as connection:

                connection.starttls()  #secures connection
                connection.login(user= MY_EMAIL, password= SENHA)
                connection.sendmail(
                    from_addr= MY_EMAIL,
                    to_addrs= 'pedrodev28@gmail.com',
                    msg='Subject: ISS \n\nLook Up.'
                    )
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




