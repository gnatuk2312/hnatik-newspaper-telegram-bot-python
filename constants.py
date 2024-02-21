class SubscriptionEnum:
    WEATHER = "WEATHER"
    CRYPTOCURRENCY = "CRYPTOCURRENCY"


PARAMS_CRYPTOCURRENCY = ["BTC", "ETH"]
PARAMS_WEATHER = ["Ternopil", "Kyiv"]

NEWSPAPER_SUBSCRIPTIONS = [
    {"subscription": SubscriptionEnum.CRYPTOCURRENCY, "params": PARAMS_CRYPTOCURRENCY},
    {"subscription": SubscriptionEnum.WEATHER, "params": PARAMS_WEATHER},
]
