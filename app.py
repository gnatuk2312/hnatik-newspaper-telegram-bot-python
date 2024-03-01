from config import bot

import src.commands.main
import src.newspaper_subscriptions.main

# DONE: Add menu with commands
# DONE: Refactor code
# DONE: Add more options for weather and cryptocurrency
# DONE: Translate all texts into Ukrainian
# DONE: create logic which can take user and send all data that user subscribed on
# TODO: Setup CRON, map through all users and call function which can send subscribed data
# TODO: Setup api caching using Redis
# TODO: Add loading indicator on creating subscriptions
# TODO: Host two app on production
# TODO: Add /deleteallsubscriptions command
# TODO: Add /help command
# TODO: Add /deletesubscription command
# TODO: Add CURRENCY subscription type

print("Bot is running!")
bot.infinity_polling()
