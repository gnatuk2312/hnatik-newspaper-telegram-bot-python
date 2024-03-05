import aiohttp
import json

from config import API_URL


headers = {"Content-Type": "application/json"}


async def get_all_users():
    url = API_URL + "/users"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()


async def get_user_by_chat_id(chat_id):
    url = API_URL + f"/users/chat/{chat_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()


async def create_user(username, first_name, last_name, chat_id):
    url = API_URL + "/users"

    user = {
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "chatId": chat_id,
    }
    data = json.dumps(user)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as response:
            return await response.json()
