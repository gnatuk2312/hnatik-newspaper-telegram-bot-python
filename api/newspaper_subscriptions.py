import requests
import aiohttp
import json

from config import API_URL

headers = {"Content-Type": "application/json"}


async def create_newspaper_subscription(subscription_type, params, user_id):
    url = API_URL + "/newspaper-subscriptions"

    newspaper_subscription = {
        "subscriptionType": subscription_type,
        "params": params,
        "userId": user_id,
    }
    data = json.dumps(newspaper_subscription)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as response:
            return await response.json()


async def delete_all_newspaper_subscriptions_by_user_id(user_id):
    url = API_URL + f"/newspaper-subscriptions/{user_id}"

    async with aiohttp.ClientSession() as session:
        async with session.delete(url, headers=headers) as response:
            return response
