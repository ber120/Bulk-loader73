from distutils.util import strtobool
import os
from dotenv import load_dotenv
from pyrogram.types import BotCommand


# Load environment variables from .env file
load_dotenv()


class Config(object):

    # Your API HASH
    API_HASH = os.environ.get('ca156f58ad03bb5e350c855bb82e9991')

    # Your API ID
    APP_ID = int(os.environ.get('24731191'))

    # Your Bot Token
    BOT_TOKEN = os.environ.get('7366561149:AAFLtJcH211zPAbXvBdTdo-NpU9qBZe64Dg')

    # Your Telegram ID (optional)
    OWNER_ID = os.environ.get('5435086550')

    # Upload method (default to False)
    AS_ZIP = bool(strtobool(os.environ.get('AS_ZIP', 'False')))

    # Channel/Group ID where you dump all the downloaded files.
    DUMP_ID = int(os.environ.get('DUMP_ID')
                  ) if os.environ.get('DUMP_ID') else None

    PLUGINS = {'root': 'Bot.plugins'}

    DOWNLOAD_DIR = "./downloads/"

    BOT_COMMANDS = [
        BotCommand('start', 'start bot'),
        BotCommand('help', 'help messages'),
        BotCommand('thumbnail', 'custom thumbnail'),
        BotCommand('caption', 'custom caption')
    ]
