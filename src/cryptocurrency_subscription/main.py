from constants import SubscriptionEnum
from api.cryptocurrency import get_cryptocurrency


def construct_message_from_cryptocurrency_data(cryptocurrency, currency):
    price = cryptocurrency["data"][currency]["quote"]["USD"]["price"]

    if round(price) > 1:
        price = round(price)
    else:
        price = round(price, 4)

    message = f"\n\nЦіна *{currency}* становить *{price}$*"
    return message


def get_cryptocurrency_subscription_message_for_user(user):
    newspaper_messages_arr = [f"*{SubscriptionEnum.CRYPTOCURRENCY}*"]

    for newspaper_subscription in user["newspaper_subscriptions"]:
        subscription_type = newspaper_subscription["subscription_type"]

        if subscription_type != SubscriptionEnum.CRYPTOCURRENCY:
            pass

        try:
            params = newspaper_subscription["params"]
            cryptocurrency = get_cryptocurrency(params).json()

            message = construct_message_from_cryptocurrency_data(cryptocurrency, params)
            newspaper_messages_arr.append(message)

        except Exception as error:
            print(f"CryptocurrencySubscription > exception occurred > {error}")
            newspaper_messages_arr.append(
                "\n\nУпс... Схоже я загубив частину сторінок коли ніс газету тобі 😕"
            )

    return "".join(newspaper_messages_arr)
