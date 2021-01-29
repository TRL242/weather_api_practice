import requests

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

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Take an umbrella!")





