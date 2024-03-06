import aiohttp
import json

from config import API_NINJAS_KEY, redis

API_URL = "https://api.api-ninjas.com"
headers = {
    "Accepts": "application/json",
    "X-Api-Key": API_NINJAS_KEY,
}


async def get_coordinates_by_city(city):
    url = API_URL + "/v1/geocoding"
    params = {"country": "Ukraine", "city": city}
    redis_key = f"get_coordinates_by_city_{city}"

    cache = redis.get(redis_key)

    if cache:
        return json.loads(cache)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            response_json = await response.json()

            response_str = json.dumps(response_json)
            redis.set(redis_key, response_str)

            return response_json
