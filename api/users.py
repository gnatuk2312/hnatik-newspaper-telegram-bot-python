import requests
import json

from config import API_URL


headers = {"Content-Type": "application/json"}


def get_all_users():
    url = API_URL + "/users"

    return requests.get(url, headers=headers)


def get_user_by_chat_id(chat_id):
    url = API_URL + f"/users/chat/{chat_id}"

    return requests.get(url, headers=headers)


def create_user(username, first_name, last_name, chat_id):
    url = API_URL + "/users"

    user = {
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "chatId": chat_id,
    }
    data = json.dumps(user)

    return requests.post(url, data=data, headers=headers)
