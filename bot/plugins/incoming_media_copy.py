import os, asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from bot.importss import Config 

COPY = Config.MEDIACOPY_ID

@Client.on_message(filters.media)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001427335527, 
            from_chat_id=-1001531149575, 
            message_id=update.id, 
            caption=f"**{update.caption}**".replace("Latest_Movies_Reborn", f"**DXClassic**"), 
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)



