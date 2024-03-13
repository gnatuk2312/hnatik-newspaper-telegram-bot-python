import pycron

from config import bot
from api.users import get_all_users
from src.weather import get_weather_subscription_message_for_user
from src.currency import get_currency_subscription_message_for_user
from src.cryptocurrency import get_cryptocurrency_subscription_message_for_user

UKRAINE_TIMEZONE_UTC = 2


@pycron.cron(f"0 {9 - UKRAINE_TIMEZONE_UTC} * * *")
async def send_newspaper_to_all_users(timestamp):
    users = await get_all_users()

    for user in users:
        try:
            chat_id = user["chat_id"]
            first_name = user["first_name"]

            await bot.send_message(
                chat_id, f"Добрий ранок, {first_name}🌅\nОсь твоя ранкова газета 📰"
            )

            weather_message = await get_weather_subscription_message_for_user(user)
            await bot.send_message(chat_id, weather_message, parse_mode="markdown")

            currency_message = await get_currency_subscription_message_for_user(user)
            await bot.send_message(chat_id, currency_message, parse_mode="markdown")

            cryptocurrency_message = (
                await get_cryptocurrency_subscription_message_for_user(user)
            )
            await bot.send_message(
                chat_id, cryptocurrency_message, parse_mode="markdown"
            )
        except Exception as error:
            print(f"Cron >> send_newspaper_to_all_users > {error}")
            continue
