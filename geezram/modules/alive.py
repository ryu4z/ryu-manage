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
 "https://telegra.ph/file/843a1c944c226afe34001.jpg",
 "https://telegra.ph/file/843a1c944c226afe34001.jpg",
 "https://telegra.ph/file/843a1c944c226afe34001.jpg",

]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hallo [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nsaya Killua Robot, Tidak ada yang spesial dari saya... \n.**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [RYU](https://t.me/ryusupport)** \n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("RYU Support", "https://t.me/ryusupport?start=help")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)
