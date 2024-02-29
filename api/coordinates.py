import requests

from config import API_NINJAS_KEY

API_URL = "https://api.api-ninjas.com"
headers = {
    "Accepts": "application/json",
    "X-Api-Key": API_NINJAS_KEY,
}


def get_coordinates_by_city(city):
    url = API_URL + "/v1/geocoding"
    params = {"country": "Ukraine", "city": city}

    return requests.get(url, headers=headers, params=params)
