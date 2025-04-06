from dotenv import load_dotenv
load_dotenv()
import os
from aiogram import Bot
from aiogram.utils.token import TokenValidationError


# Create a bot_instance using the bot token from the config file
bot_instance = Bot(os.environ['BOT_TOKEN'])
