import requests

API_URL = "https://api.open-meteo.com"
headers = {
    "Accepts": "application/json",
}


def get_weather_by_coordinates(latitude, longitude):
    url = API_URL + "/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,cloud_cover,wind_speed_10m",
    }

    return requests.get(url, headers=headers, params=params)
