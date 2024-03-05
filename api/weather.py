import aiohttp

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

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            return await response.json()
