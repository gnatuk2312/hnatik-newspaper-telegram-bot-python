import aiohttp
import json

from config import COIN_MARKET_CAP_TOKEN, redis

API_URL = "https://pro-api.coinmarketcap.com"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": COIN_MARKET_CAP_TOKEN,
}


async def get_cryptocurrency(symbol):
    url = API_URL + "/v1/cryptocurrency/quotes/latest"
    params = {"symbol": symbol}
    redis_key = f"get_cryptocurrency_{symbol}"
    redis_data_expires_in_seconds = 3 * 60

    cache = redis.get(redis_key)

    if cache:
        return json.loads(cache)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            response_json = await response.json()

            response_str = json.dumps(response_json)
            redis.set(redis_key, response_str, ex=redis_data_expires_in_seconds)

            return response_json
