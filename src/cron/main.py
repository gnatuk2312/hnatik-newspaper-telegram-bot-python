import pycron

from config import bot
from api.users import get_all_users
from src.weather_subscription.main import get_weather_subscription_message_for_user
from src.cryptocurrency_subscription.main import (
    get_cryptocurrency_subscription_message_for_user,
)


@pycron.cron("0 9 * * *")
async def send_newspaper_to_all_users(timestamp):
    users = await get_all_users()

    for user in users:
        chat_id = user["chat_id"]

        weather_message = await get_weather_subscription_message_for_user(user)
        await bot.send_message(chat_id, weather_message, parse_mode="markdown")

        cryptocurrency_message = await get_cryptocurrency_subscription_message_for_user(
            user
        )
        await bot.send_message(chat_id, cryptocurrency_message, parse_mode="markdown")
