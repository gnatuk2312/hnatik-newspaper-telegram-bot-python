import requests
import json

from config import API_URL

headers = {"Content-Type": "application/json"}


def create_newspaper_subscription(subscription_type, params, user_id):
    url = API_URL + "/newspaper-subscriptions"

    newspaper_subscription = {
        "subscriptionType": subscription_type,
        "params": params,
        "userId": user_id,
    }
    data = json.dumps(newspaper_subscription)

    return requests.post(url, data=data, headers=headers)
