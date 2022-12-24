import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import filters, enums
from Automation.bot import Robot
from Automation.info import Config
from Automation.database.database import *


# =
usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()


@Robot.on_message(filters.channel & (filters.document | filters.video | filters.audio))
async def editing(bot, message):
      caption_text = await get_caption(Config.ADMIN_ID)
      try:
         caption_text = caption_text.caption
      except:
         caption_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"**{message.caption}**"                
          else:
             file_caption = ""           
                                                 
      try:
          if caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.id,
                 caption  =caption_text + "\n" + file_caption,
                 parse_mode = enums.ParseMode.MARKDOWN
             )
          elif caption_position == "bottom":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.id,
                 caption = file_caption + "\n\n" + caption_text,
                 parse_mode=enums.ParseMode.MARKDOWN
             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.id,
                 caption = caption_text, 
                 parse_mode=enums.ParseMode.MARKDOWN
             ) 
      except:
          pass
