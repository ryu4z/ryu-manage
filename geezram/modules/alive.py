import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from geezram.events import register
from geezram import telethn as tbot


PHOTO = [
 "https://telegra.ph/file/3b757c3986ec72f09096c.jpg",
 "https://telegra.ph/file/b095fea86f234dd53f762.jpg",
 "https://telegra.ph/file/f6f81a6b5b44d8d4fa46e.jpg",

]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hallo [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nsaya Killua Robot, Tidak ada yang spesial dari saya... \n.**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [RYU](https://t.me/ryuSupport)** \n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("RAM Support", "https://t.me/ryusupport?start=help")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)
