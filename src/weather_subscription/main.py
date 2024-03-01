from constants import SubscriptionEnum
from api.coordinates import get_coordinates_by_city
from api.weather import get_weather_by_coordinates


def get_weather_by_city(city):
    coordinates = get_coordinates_by_city(city).json()
    latitude = coordinates[0]["latitude"]
    longitude = coordinates[0]["longitude"]

    weather = get_weather_by_coordinates(latitude, longitude).json()
    return weather


def construct_message_from_weather_data(weather, city):
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

    message = f"\n\n*{city}*: \n• Температура: *{temperature}* (відчувається як *{apparent_temperature}*) \n• Хмарність неба: *{cloud_cover}* \n• Швидкість вітру: *{wind_speed}* \n• Відносна вологість: *{relative_humidity}*"
    return message


def get_weather_subscription_message_for_user(user):
    newspaper_messages_arr = [f"*{SubscriptionEnum.WEATHER}*"]

    for newspaper_subscription in user["newspaper_subscriptions"]:
        subscription_type = newspaper_subscription["subscription_type"]

        if subscription_type != SubscriptionEnum.WEATHER:
            pass

        try:
            params = newspaper_subscription["params"]
            weather = get_weather_by_city(params)
            message = construct_message_from_weather_data(weather, params)

            newspaper_messages_arr.append(message)
        except Exception as error:
            print(f"WeatherSubscription > exception occurred > {error}")
            newspaper_messages_arr.append(
                "\n\nУпс... Схоже я загубив частину сторінок коли ніс газету тобі 😕"
            )

    return "".join(newspaper_messages_arr)
