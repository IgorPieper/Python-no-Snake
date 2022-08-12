import requests
from twilio.rest import Client

# ----------------- OPENWEATHER CONF -------------------- #

OPENWEATHER_KEY = "YOUR_CODE"

parameters = {
    "lat": 0,
    "lon": 0,
    "appid": OPENWEATHER_KEY,
    "exclude": "current,minutely,daily"
}

# ----------------- TWILIO CONF -------------------- #

ACCOUNT_SID = "YOUR_CODE"
AUTH_TOKEN = "YOUR_CODE"

sms_message = "It is going to rain today. Remember to bring an umbrella"
from_number = ""
to_numer = ""

# ----------------- CODE BODY -------------------- #

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly = data["hourly"]
will_rain = False

for n in range(0, 13):
    weather = data["hourly"][n]["weather"][0]["id"]
    if 500 <= weather < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages \
        .create(
        body=sms_message,
        from_=from_number,
        to=to_numer,
    )
    print(message.status)
