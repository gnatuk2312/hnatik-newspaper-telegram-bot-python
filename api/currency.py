import aiohttp
import json

from config import redis

API_URL = "https://api.goverla.ua"
headers = {
    "Accepts": "application/json",
}


async def get_currency(params):
    currencies = await get_all_currencies()

    rates = currencies["data"]["point"]["rates"]

    for rate in rates:
        if rate["currency"]["name"] == params:
            return rate

    return None


async def get_all_currencies():
    url = API_URL + "/graphql"

    body = """
    query {
        point(alias: "goverla-ua") {
            rates {
                currency {
                    name
                }
                bid {
                    absolute
                }
                ask {
                    absolute
                }
            }
        }
    }
    """

    redis_key = "get_all_currencies"
    redis_data_expires_in_seconds = 30 * 60

    cache = redis.get(redis_key)

    if cache:
        return json.loads(cache)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"query": body}, headers=headers) as response:
            response_json = await response.json()

            response_str = json.dumps(response_json)
            redis.set(redis_key, response_str, ex=redis_data_expires_in_seconds)

            return response_json
