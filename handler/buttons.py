import requests
from bs4 import BeautifulSoup
import time
from telethon import events, Button
import handler.client
from discord_webhook import DiscordWebhook

client = handler.client.client
webHook = 'https://discord.com/api/webhooks/992101863174443039/qcsf3ITXAExwuAcwvjd6AnC-ZWp3zgxKVfevPSD4u-g8Y5dNow_ja2nP9ga4oXS8sAcy'

@events.register(events.callbackquery.CallbackQuery())
async def buttons(event):
    if event.data == b'telegra':
        await event.edit(buttons=[
            [Button.inline('send link', data='send_link')],
            [Button.inline("back", data=b'back')]
        ])
    id = event.original_update.msg_id
    if event.data == b'back':
        await event.delete()
        await event.reply('back to menu ☺️', buttons=[
                          [Button.url("admin bot", url="https://t.me/@C0ID_BACK")],
                          [Button.inline('telegra sender', data=b'telegra')]
                          ])
    if event.data == b'send_link':
        if id:
            await event.delete()
        async with client.conversation(event.sender_id) as conv:
            send = await conv.send_message('I\'m waiting for message')
            global response
            response = conv.get_response()
            response = await response
            await send.delete()
            await event.reply(response.text,
                              buttons=[
                                  [Button.inline('send', data=b'send'), Button.inline(
                                      "dont'send", data=b'dontSend')],
                                  [Button.inline("back", data=b'back')]
                              ])
    if event.data == b'send':
        result = response.text

        if result:
            source = requests.get(result).content.decode()
            soup = BeautifulSoup(source, "html.parser")
            name = soup.find('h1')
            images = soup.findAll('img')
            count = 0
            for image in images:
                linK = "https://telegra.ph/"+image['src']
                webhook = DiscordWebhook(url=webHook, content=linK)
                response = webhook.execute()
                count += 1
                await event.edit('sended {} iamge'.format(count))
                time.sleep(4)
            await event.edit(
                buttons=[
                    [Button.inline("ButtonUrl")],
                    [Button.inline('telegra sender', data=b'telegra')]
                ]
            )
        else:
            print('error')
    if event.data == b'dontSend':
        await event.delete()
        await event.reply('Welocme to sender bot ☺️', buttons=[
                          [Button.url("admin bot", url="https://t.me/@C0ID_BACK")],
                          [Button.inline('telegra sender', data=b'telegra')]
                          ])
