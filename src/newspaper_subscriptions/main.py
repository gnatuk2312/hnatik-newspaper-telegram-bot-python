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

        bot.send_message(chat_id, f"Choose a {subscription}:", reply_markup=markup)

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
            price = round(cryptocurrency["data"][currency]["quote"]["USD"]["price"])

            bot.send_message(
                chat_id,
                f"Successfully created a {currency} subscription. Price for {currency} for now is ${price}",
            )
        except:
            bot.send_message(chat_id, "Something is wrong on the server...")

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

            temperature = f'{current["temperature_2m"]} {units["temperature_2m"]}'
            apparent_temperature = (
                f'{current["apparent_temperature"]} {units["apparent_temperature"]}'
            )
            relative_humidity = (
                f'{current["relative_humidity_2m"]} {units["relative_humidity_2m"]}'
            )
            cloud_cover = f'{current["cloud_cover"]} {units["cloud_cover"]}'
            wind_speed = f'{current["wind_speed_10m"]} {units["wind_speed_10m"]}'

            bot.send_message(
                chat_id,
                f"Here is some information about the weather in {city}: \n Temperature: {temperature} \n Apparent temperature: {apparent_temperature} \n Relative humidity: {relative_humidity} \n Cloud cover: {cloud_cover} \n Wind speed: {wind_speed}",
            )

        except:
            bot.send_message(chat_id, "Something is wrong on the server...")
