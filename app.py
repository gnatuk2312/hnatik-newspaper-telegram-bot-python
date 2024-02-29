from config import bot

import src.commands.main
import src.newspaper_subscriptions.main

# DONE: Add menu with commands
# DONE: Refactor code
# DONE: Add more options for weather and cryptocurrency
# DONE: Translate all texts into Ukrainian
# TODO: Setup CRON to fetch all subscriptions and send data to all of them
# TODO: Host two app on production
# TODO: Setup api caching using Redis

print("Bot is running!")
bot.infinity_polling()
