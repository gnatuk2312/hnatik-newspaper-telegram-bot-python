from config import bot


class BotMessages:
    @staticmethod
    async def send_loading_message(chat_id):
        return await bot.send_message(chat_id, "Завантаження ⏳")

    @staticmethod
    async def send_exception_message(chat_id):
        return await bot.send_message(
            chat_id,
            "Щось пішло не так... Зв'яжіться з адміністрацією - @gnatuk2312",
        )
