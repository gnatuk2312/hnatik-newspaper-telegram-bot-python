from telebot import types

from config import bot
from constants import NEWSPAPER_SUBSCRIPTIONS
from api.users import get_user_by_chat_id, create_user
from src.weather import get_weather_subscription_message_for_user
from src.cryptocurrency import get_cryptocurrency_subscription_message_for_user


class Commands:
    @bot.message_handler(commands=["start"])
    async def start(message):
        chat = message.chat
        chat_id = chat.id
        username = chat.username
        first_name = chat.first_name
        last_name = chat.last_name

        user = await get_user_by_chat_id(chat_id)
        if not user:
            await create_user(username, first_name, last_name, chat_id)

        await bot.send_message(
            chat_id,
            f"Привіт, {first_name} {last_name} 👋 Мене звати Бот Листоноша! \n\nСкориставшись командою /addsubscription ти можеш підписатись на відповідні теми у моїй газеті 📰 \n\nПісля підписки я почну приносити тобі газету кожного ранку о 9:00 ☀️ \n\nP.S. Натискай /addsubscription щоб переглянути доступні теми",
        )

    @bot.message_handler(commands=["addsubscription"])
    async def add_subscription(message):
        chat_id = message.chat.id

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        for newspaper_subscription in NEWSPAPER_SUBSCRIPTIONS:
            button = types.KeyboardButton(newspaper_subscription["subscription"])
            markup.add(button)

        await bot.send_message(chat_id, "Обирай тему 🗞", reply_markup=markup)

    @bot.message_handler(commands=["readnewspaper"])
    async def read_newspaper(message):
        chat_id = message.chat.id

        loading_message = await bot.send_message(chat_id, "Завантаження ⏳")

        user = await get_user_by_chat_id(chat_id)
        if not user:
            await bot.delete_message(chat_id, loading_message.id)
            await bot.send_message(
                chat_id,
                "Перед використанням цієї команди почни роботу із ботом командою /start",
            )
            return

        weather_message = await get_weather_subscription_message_for_user(user)
        await bot.send_message(chat_id, weather_message, parse_mode="markdown")

        cryptocurrency_message = await get_cryptocurrency_subscription_message_for_user(
            user
        )
        await bot.send_message(chat_id, cryptocurrency_message, parse_mode="markdown")

        await bot.delete_message(chat_id, loading_message.id)
