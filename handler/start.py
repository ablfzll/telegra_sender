from telethon import events,Button


@events.register(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Welocme to sender bot ☺️",
                      buttons=[
                          [Button.url("admin bot", url="https://t.me/@C0ID_BACK")],
                          [Button.inline('telegra sender', data=b'telegra')]
                      ])
