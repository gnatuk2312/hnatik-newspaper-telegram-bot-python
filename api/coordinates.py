import aiohttp

from config import API_NINJAS_KEY

API_URL = "https://api.api-ninjas.com"
headers = {
    "Accepts": "application/json",
    "X-Api-Key": API_NINJAS_KEY,
}


async def get_coordinates_by_city(city):
    url = API_URL + "/v1/geocoding"
    params = {"country": "Ukraine", "city": city}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            return await response.json()
