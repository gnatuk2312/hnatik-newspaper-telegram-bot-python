import requests

from config import COIN_MARKET_CAP_TOKEN

API_URL = "https://pro-api.coinmarketcap.com"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": COIN_MARKET_CAP_TOKEN,
}


def get_cryptocurrency(symbol):
    url = API_URL + "/v1/cryptocurrency/quotes/latest"

    return requests.get(url, headers=headers, params={"symbol": symbol})
