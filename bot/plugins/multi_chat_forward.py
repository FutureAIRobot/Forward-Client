"""
import logging, asyncio
from pyrogram import filters
from bot.importss import Robot, Config
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

media_filter = filters.document | filters.video | filters.audio

@Robot.on_message(filters.chat(-1001793975460) & (media_filter))
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.MULTIFORWARD_ID:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
#           func = message.copy if False else message.forward
            await message.copy(int(to_channel))
            print("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(1)
   except Exception as e:
      logger.exception(e)
"""
