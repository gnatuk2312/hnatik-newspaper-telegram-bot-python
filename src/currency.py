from constants import SubscriptionEnum
from api.currency import get_currency


def construct_message_from_currency_data(data, currency):
    COINS_DIVISOR = 100

    bid = data["bid"]["absolute"] / COINS_DIVISOR
    ask = data["ask"]["absolute"] / COINS_DIVISOR

    message = f"\n\nКурс *{currency}*:\n• Купівля: *{bid}*грн\n• Продаж: *{ask}*грн"
    return message


async def get_currency_subscription_message_for_user(user):
    newspaper_messages_arr = [f"*{SubscriptionEnum.CURRENCY}*"]

    for newspaper_subscription in user["newspaper_subscriptions"]:
        subscription_type = newspaper_subscription["subscription_type"]

        if subscription_type != SubscriptionEnum.CURRENCY:
            continue

        try:
            params = newspaper_subscription["params"]
            currency = await get_currency(params)

            message = construct_message_from_currency_data(currency, params)
            newspaper_messages_arr.append(message)

        except Exception as error:
            print(f"CurrencySubscription > exception occurred > {error}")
            newspaper_messages_arr.append(
                "\n\nУпс... Схоже я загубив частину сторінок коли ніс газету тобі 😕"
            )

    return "".join(newspaper_messages_arr)
