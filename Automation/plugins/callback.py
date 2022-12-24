from pyrogram import filters, enums
from Automation.bot import Robot
from Automation.info import Config
from Automation.translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Automation.database.database import *

@Robot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data
    if "about_data" in cb_data:
        await cmd.message.edit(
             text = Translation.ABOUT_TEXT,
             parse_mode = enums.ParseMode.MARKDOWN, 
             disable_web_page_preview=True, 
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                      InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                      InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                     ]
 
                 ] 
             ) 
        )
    elif "help_data" in cb_data:
          await cmd.message.edit(
               text=Translation.HELP_TEXT,
               parse_mode = enums.ParseMode.HTML, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("ABOUT MARKDOWN", callback_data = "markdown_data")
                       ],
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
    elif "back_data" in cb_data:
          await cmd.message.edit(
               text=Translation.START_TEXT.format(cmd.from_user.first_name, Config.ADMIN_USERNAME),
               parse_mode = enums.ParseMode.MARKDOWN, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                      
                       [
                        InlineKeyboardButton("📄 BOT STATUS", callback_data = "status_data")
                       ], 
                       [
                        InlineKeyboardButton("📫 UPDATES", url="https://t.me/ts_bots"),
                        InlineKeyboardButton("📕 ABOUT ME", callback_data="about_data")
                       ],
                       [
                        InlineKeyboardButton("💡 HELP", callback_data="help_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
                   ]
               )
          )
    elif "close_data" in cb_data:
          await cmd.message.delete()
          await cmd.message.reply_to_message.delete()

    elif "markdown_data" in cb_data:
          await cmd.message.edit(
               text=Translation.MARKDOWN_TEXT,
               parse_mode = enums.ParseMode.HTML, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="help_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
    elif "status_data" in cb_data:
          if Config.ADMIN_ID == int(cmd.message.chat.id):
             try:
                caption = await get_caption(cmd.from_user.id)
                caption_text = caption.caption
             except:
                caption_text = "Not Added" 
             await cmd.message.edit(
                  text=Translation.STATUS_DATA.format(caption_text, Config.CAPTION_POSITION),
                  parse_mode = enums.ParseMode.HTML, 
                  disable_web_page_preview=True, 
                  reply_markup=InlineKeyboardMarkup(
                      [
                          [
                           InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                           InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                          ]
 
                      ] 
                  ) 
             )
          else:
             await cmd.message.edit(
                  text=Translation.NOT_ADMIN_TEXT,
                  parse_mode = enums.ParseMode.HTML, 
                  disable_web_page_preview=True, 
                  reply_markup=InlineKeyboardMarkup(
                      [
                          [
                           InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                           InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                          ]
 
                      ] 
                  ) 
             )
 
