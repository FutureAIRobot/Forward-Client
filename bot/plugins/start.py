import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.importss import Translation, Robot, Config 



@Robot.on_message(filters.command('start') & filters.user(Config.ADMINS))
async def start(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.START_TEXT.format(update.from_user.first_name,), 
          reply_to_message_id = update.id,
          parse_mode = enums.ParseMode.MARKDOWN,
          disable_web_page_preview = True,           
      )


@Robot.on_message(filters.command('help') & filters.user(Config.ADMINS))
async def help(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.HELP_TEXT, 
          reply_to_message_id = update.id,
          parse_mode = enums.ParseMode.HTML,
          disable_web_page_preview = True,           
      )

@Robot.on_message(filters.command('forward_help') & filters.user(Config.ADMINS))
async def forward_files(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.FORWARD_FILES, 
          reply_to_message_id = update.id,
          parse_mode = enums.ParseMode.HTML,
          disable_web_page_preview = True,           
      )
