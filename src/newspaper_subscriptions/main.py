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
from api.weather import get_weather_by_coordinates
from api.coordinates import get_coordinates_by_city


class NewspaperSubscriptions:
    @staticmethod
    def is_newspaper_subscription(message):
        for newspaper_subscription in NEWSPAPER_SUBSCRIPTIONS:
            if message.text == newspaper_subscription["subscription"]:
                return True
        return False

    @bot.message_handler(func=is_newspaper_subscription)
    def subscription(message):
        chat_id = message.chat.id
        subscription = message.text

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        for newspaper_subscription in NEWSPAPER_SUBSCRIPTIONS:
            if newspaper_subscription["subscription"] == subscription:
                for param in newspaper_subscription["params"]:
                    button = types.KeyboardButton(param)
                    markup.add(button)

        bot.send_message(
            chat_id,
            f'Що саме тебе цікавить на тему "{subscription}"?',
            reply_markup=markup,
        )

    @staticmethod
    def is_params_cryptocurrency(message):
        for param in PARAMS_CRYPTOCURRENCY:
            if message.text == param:
                return True
        return False

    @bot.message_handler(func=is_params_cryptocurrency)
    def cryptocurrency(message):
        chat_id = message.chat.id
        currency = message.text

        try:
            user = get_user_by_chat_id(chat_id).json()
            create_newspaper_subscription(
                SubscriptionEnum.CRYPTOCURRENCY, currency, user["id"]
            )

            cryptocurrency = get_cryptocurrency(currency).json()
            price = cryptocurrency["data"][currency]["quote"]["USD"]["price"]

            if round(price) > 1:
                price = round(price)
            else:
                price = round(price, 4)

            bot.send_message(
                chat_id,
                f"Підписка успішно створена! 👏 \nЯ додам інформацію про ціну {currency} у твою ранкову газету 🗞 \n\nP.S. Секція у газеті виглядатиме ось так:",
            )
            bot.send_message(
                chat_id,
                f"*{SubscriptionEnum.CRYPTOCURRENCY}* \n\nЦіна *{currency}* становить *{price}$*",
                parse_mode="Markdown",
            )
        except Exception as error:
            print(f"Exception occurred >> {error}")
            bot.send_message(
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
    def weather(message):
        chat_id = message.chat.id
        city = message.text

        try:
            user = get_user_by_chat_id(chat_id).json()
            create_newspaper_subscription(SubscriptionEnum.WEATHER, city, user["id"])

            coordinates = get_coordinates_by_city(city).json()
            latitude = coordinates[0]["latitude"]
            longitude = coordinates[0]["longitude"]

            weather = get_weather_by_coordinates(latitude, longitude).json()
            current = weather["current"]
            units = weather["current_units"]

            temperature = f'{current["temperature_2m"]}{units["temperature_2m"]}'
            apparent_temperature = (
                f'{current["apparent_temperature"]}{units["apparent_temperature"]}'
            )
            relative_humidity = (
                f'{current["relative_humidity_2m"]}{units["relative_humidity_2m"]}'
            )
            cloud_cover = f'{current["cloud_cover"]}{units["cloud_cover"]}'
            wind_speed = f'{current["wind_speed_10m"]}{units["wind_speed_10m"]}'

            bot.send_message(
                chat_id,
                f"Підписка успішно створена! 👏 \nЯ додам інформацію про погоду у місті {city} у твою ранкову газету 🗞 \n\nP.S. Секція у газеті виглядатиме ось так:",
            )
            bot.send_message(
                chat_id,
                f"*{SubscriptionEnum.WEATHER}* \n\n*{city}*: \n• Температура: *{temperature}* (відчувається як *{apparent_temperature}*) \n• Хмарність неба: *{cloud_cover}* \n• Швидкість вітру: *{wind_speed}* \n• Відносна вологість: *{relative_humidity}*",
                parse_mode="Markdown",
            )

        except Exception as error:
            print(f"Exception occurred >> {error}")
            bot.send_message(
                chat_id,
                "Щось пішло не так... Зв'яжіться з адміністрацією - @gnatuk2312",
            )
