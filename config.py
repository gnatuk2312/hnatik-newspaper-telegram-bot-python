import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

TOKEN = os.getenv("TOKEN")
COIN_MARKET_CAP_TOKEN = os.getenv("COIN_MARKET_CAP_TOKEN")
API_NINJAS_KEY = os.getenv("API_NINJAS_KEY")
API_URL = os.getenv("API_URL")

bot = TeleBot(TOKEN)
