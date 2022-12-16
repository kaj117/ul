import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import re

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
# the Strings used for this "thing"
from text import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Kmac
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Free User", "2027.01.01.12.00.00")
    Config.SUPER7X_DLBOT_USERS.append(5027085442)
    return expires_at

@Kmac.on_message(filters.private & filters.command(["cancel"]))
async def cancel_process(bot, update):
    save_ytdl_json_path = Config.DOWNLOAD_LOCATION + "/" + str(update.chat.id) + ".json"
    if os.path.exists(save_ytdl_json_path):
        os.remove(save_ytdl_json_path)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.PROCESS_CANCELLED,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.NO_PROCESS_FOUND,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )

@Kmac.on_message(filters.private & filters.reply & filters.text)
async def edit_caption(bot, update):
    try:
        await bot.send_cached_media(
            chat_id=update.chat.id,
            file_id=update.reply_to_message.video.file_id,
            reply_to_message_id=update.message_id,
            caption=update.text
        )
    except:
        try:
            await bot.send_cached_media(
                chat_id=update.chat.id,
                file_id=update.reply_to_message.document.file_id,
                reply_to_message_id=update.message_id,
                caption=update.text
            )
        except:
            pass

@Kmac.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('💡 𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ', url='https://t.me/lkhitech'),
          ]
        ]
       ),
       reply_to_message_id=update.message_id
     )

@Kmac.on_message(filters.private & filters.command(["caption"]))
async def add_caption_help(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ADD_CAPTION_HELP,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Kmac.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('💡 𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟', url='https://t.me/lkhitech'),
          ]
        ]
       ),
       reply_to_message_id=update.message_id
     )

@Kmac.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('💡 𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟', url='https://t.me/lkhiech'),
      ],
      [
          InlineKeyboardButton('💾 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘', url='https://github.com'),
          InlineKeyboardButton('🌐 𝗪𝗘𝗕𝗦𝗜𝗧𝗘', url = 'https://hitechlk.com')
      ]
        ]
      ),
      reply_to_message_id=update.message_id
    )

@Kmac.on_message(filters.private & filters.command(["info"]))
async def add_info_help(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.INFO_TEXT.format(update.from_user.first_name, last_name, update.from_user.username, update.from_user.id, update.from_user.mention, update.from_user.dc_id, update.from_user.language_code, update.from_user.status),
        #parse_mode="html",
        reply_to_message_id=update.message_id
    )