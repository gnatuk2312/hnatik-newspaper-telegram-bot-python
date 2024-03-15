import asyncio
import pycron
from multiprocessing import Process

from config import bot

import src.cron
import src.commands
import src.newspaper_subscription

# TODO: Add /help command
# TODO: Add /deletesubscription command
# TODO: Add error logging


def __run_bot():
    print("Bot is running!")
    asyncio.run(bot.polling())


def __run_cron():
    print("Cron is running!")
    pycron.start()


async def bootstrap():
    Process(target=__run_cron).start()
    Process(target=__run_bot).start()


if __name__ == "__main__":
    asyncio.run(bootstrap())
