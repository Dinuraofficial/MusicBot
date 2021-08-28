#Dinura <https://t.me/Dinuranikalansuriya>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from Dinura .plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Dinura  import Musicbot as app
from Dinura  import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm Song Downloader Bot 🎵
   Just send me the song name you want to download.
      eg:```/song Stitches```
      
A bot by @DinuraNikalansuriya
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Channel 🔊", url="https://t.me/TechDroidLK"
                    ),
                    InlineKeyboardButton(
                        text="Dev 🔥", url="https://t.me/Dinuranikalansuriya"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ MusicBot is online.")
idle()
