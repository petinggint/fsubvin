import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    startmsg = (
        'The bot is up and running. These bots '
        'can store messages in custom chats, '
        'and users access them through the bot.'
    )
    forcemsg = (
        'To view messages shared by bots. '
        'Join first, then press the Try Again button.'
    )

    API_ID = int(os.environ.get('API_ID', 30829384))
    API_HASH = os.environ.get('API_HASH', 'c4f503fe8c2a44601b756c8b0c2da48c')
    OWNER_ID = int(os.environ.get('OWNER_ID', 432134084))
    MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://root:passwd@mongo')

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '8051091732:AAHOJfHskb4mQ2rPi3tLJEQW_NXhMMrMgFM')
    DATABASE_ID = int(os.environ.get('DATABASE_ID', '-1001505091680'))

    BOT_ID = BOT_TOKEN.split(':', 1)[0]


Config = Config()
