import asyncio
import pycron
from multiprocessing import Process

from config import bot

import src.cron
import src.commands
import src.newspaper_subscription

# TODO: Setup api caching using Redis
# TODO: Add loading indicator on creating subscriptions
# TODO: Host two app on production
# TODO: Add /deleteallsubscriptions command
# TODO: Add /help command
# TODO: Add /deletesubscription command
# TODO: Add CURRENCY subscription type


def __run_bot():
    print("Bot is running!")
    asyncio.run(bot.polling(non_stop=True))


def __run_cron():
    print("Cron is running!")
    pycron.start()


async def bootstrap():
    Process(target=__run_cron).start()
    Process(target=__run_bot).start()


if __name__ == "__main__":
    asyncio.run(bootstrap())
