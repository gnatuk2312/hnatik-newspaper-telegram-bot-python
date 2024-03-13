class SubscriptionEnum:
    WEATHER = "Погода"
    CURRENCY = "Валюта"
    CRYPTOCURRENCY = "Криптовалюта"


PARAMS_WEATHER = [
    "Тернопіль",
    "Львів",
    "Івано-Франківськ",
    "Київ",
    "Дніпро",
    "Запоріжжя",
]
PARAMS_CURRENCY = [
    "Долар США",
    "Євро",
    "Польський злотий",
    "Чеська крона",
    "Фунт стерлінгів",
    "Канадський долар",
    "Австралійський долар",
    "Швейцарський франк",
]
PARAMS_CRYPTOCURRENCY = ["BTC", "ETH", "BNB", "SOL", "XRP"]


NEWSPAPER_SUBSCRIPTIONS = [
    {"subscription": SubscriptionEnum.WEATHER, "params": PARAMS_WEATHER},
    {"subscription": SubscriptionEnum.CURRENCY, "params": PARAMS_CURRENCY},
    {"subscription": SubscriptionEnum.CRYPTOCURRENCY, "params": PARAMS_CRYPTOCURRENCY},
]
