import aiohttp
import json

from config import redis

API_URL = "https://api.open-meteo.com"
headers = {
    "Accepts": "application/json",
}


async def get_weather_by_coordinates(latitude, longitude):
    url = API_URL + "/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,cloud_cover,wind_speed_10m",
    }
    redis_key = f"get_weather_by_coordinates_{latitude}_{longitude}"
    redis_data_expires_in_seconds = 5 * 60

    cache = redis.get(redis_key)

    if cache:
        return json.loads(cache)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            response_json = await response.json()

            response_str = json.dumps(response_json)
            redis.set(redis_key, response_str, ex=redis_data_expires_in_seconds)

            return response_json
