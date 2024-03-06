import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from redis import Redis

load_dotenv()

TOKEN = os.getenv("TOKEN")
COIN_MARKET_CAP_TOKEN = os.getenv("COIN_MARKET_CAP_TOKEN")
API_NINJAS_KEY = os.getenv("API_NINJAS_KEY")
API_URL = os.getenv("API_URL")

bot = AsyncTeleBot(TOKEN)
redis = Redis(host="localhost", port=6379, decode_responses=True)
