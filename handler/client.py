from telethon import TelegramClient

api_id = 19957003
api_hash = 'd3d3c5a2b5f148adebac76f31dd0d21f'
bot_token = '5460951201:AAFX7q_-5RB5M4pIuQzMkd6pJMEwhmRJk-U'

client = TelegramClient('name', api_id, api_hash).start(bot_token=bot_token)