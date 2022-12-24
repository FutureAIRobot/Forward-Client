import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot.importss import Robot, Config

IDS = Config.MULTI_CHANNEL_FORWARD_IDS

@Robot.on_message(filters.channel)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in IDS:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
#           func = message.copy if False else message.forward
            await message.copy(int(to_channel))
            print("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(1)
   except Exception as e:
      logger.exception(e)
