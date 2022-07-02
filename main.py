from telethon import TelegramClient, events, Button
from telethon.events import NewMessage
import handler.client
import handler.start
import handler.buttons


client = handler.client.client

with client as mybot:
    mybot.add_event_handler(handler.start.start)


with client as mybot:
    mybot.add_event_handler(handler.buttons.buttons)



print("bot started")
client.start()
client.run_until_disconnected()
