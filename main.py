import requests
from twilio.rest import Client
import os

api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 6.524379,
    "lon": 3.379206,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

weather_data = response.json()
id_list = []
for index in range(0, 12):
    weather_id = (weather_data["hourly"][index]["weather"][0]["id"])
    id_list.append(weather_id)

rainy_day_id = 700

will_rain = False
for id in id_list:
    if id < rainy_day_id:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+19896468028",
        to="+2349098828475"
    )
    print(message.status)
