import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import sys, requests, urllib.parse, filetype, os, time, shutil, tldextract, asyncio, json, math

from config import Config
from database.adduser import AddUser
from text import Translation
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import filters
from pyrogram import Client as Kmac
from database.access import kmac
from helpers.display_progress import humanbytes
from helpers.help_uploadbot import DownLoadFile
from helpers.display_progress import progress_for_pyrogram, humanbytes, TimeFormatter
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

@Kmac.on_message(filters.private & filters.regex(pattern=".*http.*"))
async def echo(bot, update):
    await AddUser(bot, update)
    imog = await update.reply_text("<b>𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴...⏳</b>",)
    if os.path.exists(Config.DOWNLOAD_LOCATION + "/" + str(update.chat.id) + ".json"):
        await bot.edit_message_text(
            text=Translation.WAIT_PROCESS_FINISH,
            chat_id=update.chat.id,
            message_id=imog.message_id
        )
        return False
    youtube_dl_username = None
    youtube_dl_password = None
    file_name = None
    url = update.text
    if " | " in url:
        url_parts = url.split("|")
        if len(url_parts) == 2:
            url = url_parts[0]
            file_name = url_parts[1]
        elif len(url_parts) == 4:
            url = url_parts[0]
            file_name = url_parts[1]
            youtube_dl_username = url_parts[2]
            youtube_dl_password = url_parts[3]
        else:
            for entity in update.entities:
                if entity.type == "text_link":
                    url = entity.url
                elif entity.type == "url":
                    o = entity.offset
                    l = entity.length
                    url = url[o:o + l]
        if url is not None:
            url = url.strip()
        if file_name is not None:
            file_name = file_name.strip()
        if youtube_dl_username is not None:
            youtube_dl_username = youtube_dl_username.strip()
        if youtube_dl_password is not None:
            youtube_dl_password = youtube_dl_password.strip()
    else:
        for entity in update.entities:
            if entity.type == "text_link":
                url = entity.url
            elif entity.type == "url":
                o = entity.offset
                l = entity.length
                url = url[o:o + l]
    if Config.HTTP_PROXY != "":
        command_to_exec = [
            "yt-dlp",
            "--no-warnings",
            "--youtube-skip-dash-manifest",
            "-j",
            url,
            "--proxy", Config.HTTP_PROXY
        ]
    else:
        command_to_exec = [
            "yt-dlp",
            "--no-warnings",
            "--youtube-skip-dash-manifest",
            "-j",
            url
        ]
    if youtube_dl_username is not None:
        command_to_exec.append("--username")
        command_to_exec.append(youtube_dl_username)
    if youtube_dl_password is not None:
        command_to_exec.append("--password")
        command_to_exec.append(youtube_dl_password)
    # logger.info(command_to_exec)
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    await bot.edit_message_text(
        text="<b>𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴... ⌛</b>",
        chat_id=update.chat.id,
        message_id=imog.message_id
    )
    time.sleep(0.7)
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if e_response and "nonnumeric port" not in e_response:
        error_message = e_response.replace("𝐩𝐥𝐞𝐚𝐬𝐞 𝐫𝐞𝐩𝐨𝐫𝐭 𝐭𝐡𝐢𝐬 𝐢𝐬𝐬𝐮𝐞 𝐨𝐧 https://yt-dl.org/bug . 𝗠𝗮𝗸𝗲 𝘀𝘂𝗿𝗲 𝘆𝗼𝘂 𝗮𝗿𝗲 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗹𝗮𝘁𝗲𝘀𝘁 𝘃𝗲𝗿𝘀𝗶𝗼𝗻; 𝘀𝗲𝗲 https://yt-dl.org/update  𝗼𝗻 𝗵𝗼𝘄 𝘁𝗼 𝘂𝗽𝗱𝗮𝘁𝗲. 𝗕𝗲 𝘀𝘂𝗿𝗲 𝘁𝗼 𝗰𝗮𝗹𝗹 𝘆𝗼𝘂𝘁𝘂𝗯𝗲-𝗱𝗹 𝘄𝗶𝘁𝗵 𝘁𝗵𝗲 --𝘃𝗲𝗿𝗯𝗼𝘀𝗲 𝗳𝗹𝗮𝗴 𝗮𝗻𝗱 𝗶𝗻𝗰𝗹𝘂𝗱𝗲 𝗶𝘁𝘀 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲 𝗼𝘂𝘁𝗽𝘂𝘁.")
        if "𝐓𝐡𝐢𝐬 𝐯𝐢𝐝𝐞𝐨 𝐢𝐬 𝐨𝐧𝐥𝐲 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐟𝐨𝐫 𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 𝐮𝐬𝐞𝐫𝐬..." in error_message:
            error_message += Translation.SET_CUSTOM_USERNAME_PASSWORD
        await imog.delete(True)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.NO_VOID_FORMAT_FOUND.format(str(error_message)),
            reply_to_message_id=update.message_id,
            parse_mode="html",
            disable_web_page_preview=True
        )
        return False
    if t_response:
        #logger.info(t_response)
        x_reponse = t_response
        if "\n" in x_reponse:
            x_reponse, _ = x_reponse.split("\n")
        response_json = json.loads(x_reponse)
        save_ytdl_json_path = Config.DOWNLOAD_LOCATION + \
            "/" + str(update.from_user.id) + ".json"
        with open(save_ytdl_json_path, "w", encoding="utf8") as outfile:
            json.dump(response_json, outfile, ensure_ascii=False)
        # logger.info(response_json)
        inline_keyboard = []
        duration = None
        if "duration" in response_json:
            duration = response_json["duration"]
        if "formats" in response_json:
            for formats in response_json["formats"]:
                format_id = formats.get("format_id")
                format_string = formats.get("format_note")
                if format_string is None:
                    format_string = formats.get("format")
                format_ext = formats.get("ext")
                approx_file_size = ""
                if "filesize" in formats:
                    approx_file_size = humanbytes(formats["filesize"])
                cb_string_video = "{}|{}|{}".format(
                    "video", format_id, format_ext)
                cb_string_file = "{}|{}|{}".format(
                    "file", format_id, format_ext)
                if format_string is not None and not "audio only" in format_string:
                    ikeyboard = [
                        InlineKeyboardButton(
                            "🎥 𝗩𝗶𝗱𝗲𝗼 " + format_string.split("-")[0] + " " + approx_file_size,
                            callback_data=(cb_string_video).encode("UTF-8")
                        ),
                        InlineKeyboardButton(
                            "📁 𝗙𝗶𝗹𝗲 " + format_ext + " " + approx_file_size,
                            callback_data=(cb_string_file).encode("UTF-8")
                        )
                    ]

                else:
                    # special weird case :\
                    ikeyboard = [
                        InlineKeyboardButton(
                            "🎥 𝗩𝗶𝗱𝗲𝗼 - " + format_ext,
                            callback_data=(cb_string_video).encode("UTF-8")
                        ),
                        InlineKeyboardButton(
                            "📁 𝗙𝗶𝗹𝗲 - " + format_ext,
                            callback_data=(cb_string_file).encode("UTF-8")
                        )
                    ]
                inline_keyboard.append(ikeyboard)
            if duration is not None:
                cb_string_64 = "{}|{}|{}".format("audio", "64k", "mp3")
                cb_string_128 = "{}|{}|{}".format("audio", "128k", "mp3")
                cb_string = "{}|{}|{}".format("audio", "320k", "mp3")
                inline_keyboard.append([
                    InlineKeyboardButton(
                        "🎧 𝗠𝗣𝟯 " + "(" + "64 kbps" + ")", callback_data=cb_string_64.encode("UTF-8")),
                    InlineKeyboardButton(
                        "🎧 𝗠𝗣𝟯 " + "(" + "128 kbps" + ")", callback_data=cb_string_128.encode("UTF-8"))
                ])
                inline_keyboard.append([
                    InlineKeyboardButton(
                        "🎧 𝗠𝗣𝟯 " + "(" + "320 kbps" + ")", callback_data=cb_string.encode("UTF-8"))
                ])
        else:
            format_id = response_json["format_id"]
            format_ext = response_json["ext"]
            cb_string_file = "{}|{}|{}".format(
                "file", format_id, format_ext)
            cb_string_video = "{}|{}|{}".format(
                "video", format_id, format_ext)
            inline_keyboard.append([
                InlineKeyboardButton(
                    "🎥 𝗩𝗶𝗱𝗲𝗼 - " + format_ext,
                    callback_data=(cb_string_video).encode("UTF-8")
                ),
                InlineKeyboardButton(
                    "📁 𝗙𝗶𝗹𝗲 - " + format_ext,
                    callback_data=(cb_string_file).encode("UTF-8")
                )
            ])
            cb_string_file = "{}={}={}".format(
                "file", format_id, format_ext)
            cb_string_video = "{}={}={}".format(
                "video", format_id, format_ext)
            inline_keyboard.append([
                InlineKeyboardButton(
                    "🎥 𝗩𝗶𝗱𝗲𝗼 - " + format_ext,
                    callback_data=(cb_string_video).encode("UTF-8")
                ),
                InlineKeyboardButton(
                    "📁 𝗙𝗶𝗹𝗲 - " + format_ext,
                    callback_data=(cb_string_file).encode("UTF-8")
                )
            ])
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await imog.delete(True)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FORMAT_SELECTION,
            reply_markup=reply_markup,
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
    else:
        # fallback for nonnumeric port a.k.a seedbox.io
        inline_keyboard = []
        cb_string_file = "{}={}={}".format(
            "file", "LFO", "NONE")
        cb_string_video = "{}={}={}".format(
            "video", "OFL", "ENON")
        inline_keyboard.append([
            InlineKeyboardButton(
                "🎥 𝗩𝗶𝗱𝗲𝗼",
                callback_data=(cb_string_video).encode("UTF-8")
            ),
            InlineKeyboardButton(
                "📁 𝗙𝗶𝗹𝗲",
                callback_data=(cb_string_file).encode("UTF-8")
            )
        ])
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await imog.delete(True)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FORMAT_SELECTION,
            reply_markup=reply_markup,
            parse_mode="html",
            reply_to_message_id=update.message_id
        )