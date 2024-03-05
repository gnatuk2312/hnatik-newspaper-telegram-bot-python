import aiohttp

from config import COIN_MARKET_CAP_TOKEN

API_URL = "https://pro-api.coinmarketcap.com"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": COIN_MARKET_CAP_TOKEN,
}


async def get_cryptocurrency(symbol):
    url = API_URL + "/v1/cryptocurrency/quotes/latest"
    params = {"symbol": symbol}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            return await response.json()
