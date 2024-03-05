from telebot import types

from config import bot
from constants import (
    SubscriptionEnum,
    PARAMS_CRYPTOCURRENCY,
    PARAMS_WEATHER,
    NEWSPAPER_SUBSCRIPTIONS,
)
from api.users import get_user_by_chat_id
from api.newspaper_subscriptions import create_newspaper_subscription
from api.cryptocurrency import get_cryptocurrency
from src.weather_subscription.main import (
    get_weather_by_city,
    construct_message_from_weather_data,
)
from src.cryptocurrency_subscription.main import (
    construct_message_from_cryptocurrency_data,
)


class NewspaperSubscriptions:
    @staticmethod
    def is_newspaper_subscription(message):
        for newspaper_subscription in NEWSPAPER_SUBSCRIPTIONS:
            if message.text == newspaper_subscription["subscription"]:
                return True
        return False

    @bot.message_handler(func=is_newspaper_subscription)
    async def subscription(message):
        chat_id = message.chat.id
        subscription = message.text

        try:
            markup = types.ReplyKeyboardMarkup(
                resize_keyboard=True, one_time_keyboard=True
            )

            for newspaper_subscription in NEWSPAPER_SUBSCRIPTIONS:
                if newspaper_subscription["subscription"] == subscription:
                    for param in newspaper_subscription["params"]:
                        button = types.KeyboardButton(param)
                        markup.add(button)

            await bot.send_message(
                chat_id,
                f'Що саме тебе цікавить на тему "{subscription}"?',
                reply_markup=markup,
            )
        except Exception as error:
            print(f"NewspaperSubscriptions >> Exception occurred >> {error}")
            await bot.send_message(
                chat_id,
                "Щось пішло не так... Зв'яжіться з адміністрацією - @gnatuk2312",
            )

    @staticmethod
    def is_params_cryptocurrency(message):
        for param in PARAMS_CRYPTOCURRENCY:
            if message.text == param:
                return True
        return False

    @bot.message_handler(func=is_params_cryptocurrency)
    async def cryptocurrency(message):
        chat_id = message.chat.id
        currency = message.text

        try:
            user = await get_user_by_chat_id(chat_id)
            await create_newspaper_subscription(
                SubscriptionEnum.CRYPTOCURRENCY, currency, user["id"]
            )

            cryptocurrency = await get_cryptocurrency(currency)
            message = construct_message_from_cryptocurrency_data(
                cryptocurrency, currency
            )

            await bot.send_message(
                chat_id,
                f"Підписка успішно створена! 👏 \nЯ додам інформацію про ціну {currency} у твою ранкову газету 🗞 \n\nP.S. Секція у газеті виглядатиме ось так:",
            )
            await bot.send_message(
                chat_id,
                message,
                parse_mode="Markdown",
            )
        except Exception as error:
            print(f"NewspaperSubscriptions >> Exception occurred >> {error}")
            await bot.send_message(
                chat_id,
                "Щось пішло не так... Зв'яжіться з адміністрацією - @gnatuk2312",
            )

    @staticmethod
    def is_params_weather(message):
        for param in PARAMS_WEATHER:
            if message.text == param:
                return True
        return False

    @bot.message_handler(func=is_params_weather)
    async def weather(message):
        chat_id = message.chat.id
        city = message.text

        try:
            user = await get_user_by_chat_id(chat_id)
            await create_newspaper_subscription(
                SubscriptionEnum.WEATHER, city, user["id"]
            )

            weather = await get_weather_by_city(city)
            message = construct_message_from_weather_data(weather, city)

            await bot.send_message(
                chat_id,
                f"Підписка успішно створена! 👏 \nЯ додам інформацію про погоду у місті {city} у твою ранкову газету 🗞 \n\nP.S. Секція у газеті виглядатиме ось так:",
            )
            await bot.send_message(
                chat_id,
                message,
                parse_mode="Markdown",
            )

        except Exception as error:
            print(f"NewspaperSubscriptions >> Exception occurred >> {error}")
            await bot.send_message(
                chat_id,
                "Щось пішло не так... Зв'яжіться з адміністрацією - @gnatuk2312",
            )
