class SubscriptionEnum:
    WEATHER = "Погода"
    CRYPTOCURRENCY = "Криптовалюта"


PARAMS_CRYPTOCURRENCY = ["BTC", "ETH", "BNB", "SOL", "XRP"]
PARAMS_WEATHER = [
    "Тернопіль",
    "Львів",
    "Івано-Франківськ",
    "Київ",
    "Дніпро",
    "Запоріжжя",
]

NEWSPAPER_SUBSCRIPTIONS = [
    {"subscription": SubscriptionEnum.WEATHER, "params": PARAMS_WEATHER},
    {"subscription": SubscriptionEnum.CRYPTOCURRENCY, "params": PARAMS_CRYPTOCURRENCY},
]
