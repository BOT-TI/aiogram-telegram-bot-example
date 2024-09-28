from src.utils.configloader import config
from aiogram import Bot

# Create a bot_instance using the bot token from the config file
bot_instance = Bot(config['bot']['token'])
