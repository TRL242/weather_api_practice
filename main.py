import requests
from signalwire.rest import Client as signalwire_client

PROJECT_ID = "1a2774f3-25c7-4312-8ead-77913ed0a415"
AUTH_TOKEN = "PT1e729d2c4a478bc7bc6a9921b6fbb0ec8a4c0c6eec064e2e"
SPACE_URL = "equushub.signalwire.com"

city_name = " "
api_key = "3b156074d305eb421e2f6a5cff56b92a"
api_url = f"http://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 48.427502,
    "lon": -123.367264,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(api_url, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#get 12 hours from now in data
weather_slice = weather_data["hourly"][:12]

will_rain = True

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Take an umbrella!")
    client = signalwire_client(f"{PROJECT_ID}", f"{AUTH_TOKEN}", signalwire_space_url=f'{SPACE_URL}')

    message = client.messages.create(
        # from number needs to be updated
        from_='+12294427246',
        body='🌧It ga rain bey!☔️',
        to='+16394702628'
    )






print(message.status)