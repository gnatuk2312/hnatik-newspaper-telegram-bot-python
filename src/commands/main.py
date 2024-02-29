from telebot import types

from config import bot
from constants import NEWSPAPER_SUBSCRIPTIONS
from api.users import get_user_by_chat_id, create_user


class Commands:
    @bot.message_handler(commands=["start"])
    def start(message):
        chat = message.chat
        chat_id = chat.id
        username = chat.username
        first_name = chat.first_name
        last_name = chat.last_name

        user = get_user_by_chat_id(chat_id)
        if not user:
            create_user(username, first_name, last_name, chat_id)

        bot.send_message(
            chat_id,
            f"Привіт, {first_name} {last_name} 👋 Мене звати бот-листоноша! \n\nСкориставшись командою /addsubscription ти можеш підписатись на відповідні теми у моїй газеті 📰 \n\nПісля підписки я почну приносити тобі газету кожного ранку о 9:00 ☀️ \n\nP.S. Натискай /addsubscription щоб переглянути доступні теми",
        )

    @bot.message_handler(commands=["addsubscription"])
    def add_subscription(message):
        chat_id = message.chat.id

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        for newspaper_subscription in NEWSPAPER_SUBSCRIPTIONS:
            button = types.KeyboardButton(newspaper_subscription["subscription"])
            markup.add(button)

        bot.send_message(chat_id, "Обирай тему 🗞", reply_markup=markup)
