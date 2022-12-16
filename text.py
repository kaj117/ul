from config import Config as BOT_USERNAME
from pyrogram.emoji import *

class Translation(object):

    ERROR = "<b>⚠️ 𝐄𝐑𝐑𝐎𝐑:</b> {}"

    START_TEXT = """𝐇𝐞𝐥𝐥𝐨 {},
𝐈 𝐀𝐦 𝐀 𝐔𝐑𝐋 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐫 𝐈𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦!,

𝐘𝐨𝐮 𝐜𝐚𝐧 𝐮𝐩𝐥𝐨𝐚𝐝 𝐇𝐓𝐓𝐏/𝐇𝐓𝐓𝐏𝐒 𝐝𝐢𝐫𝐞𝐜𝐭 𝐥𝐢𝐧𝐤𝐬, 𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭!

/help 𝐟𝐨𝐫 𝐦𝐨𝐫𝐞 𝐝𝐞𝐭𝐚𝐢𝐥𝐬!"""

    FORMAT_SELECTION = "𝐒𝐞𝐥𝐞𝐜𝐭 𝐭𝐡𝐞 𝐝𝐞𝐬𝐢𝐫𝐞𝐝 𝐟𝐨𝐫𝐦𝐚𝐭: <a href='{}'>𝐟𝐢𝐥𝐞 𝐬𝐢𝐳𝐞 𝐦𝐢𝐠𝐡𝐭 𝐛𝐞 𝐚𝐩𝐩𝐫𝐨𝐱𝐢𝐦𝐚𝐭𝐞</a> \n𝐈𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐬𝐞𝐭 𝐚 𝐜𝐮𝐬𝐭𝐨𝐦 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥, 𝐬𝐞𝐧𝐝 𝐚 𝐩𝐡𝐨𝐭𝐨 𝐛𝐞𝐟𝐨𝐫𝐞 𝐨𝐫 𝐪𝐮𝐢𝐜𝐤𝐥𝐲 𝐚𝐟𝐭𝐞𝐫 𝐭𝐚𝐩𝐩𝐢𝐧𝐠 𝐨𝐧 𝐚𝐧𝐲 𝐨𝐟 𝐭𝐡𝐞 𝐛𝐞𝐥𝐨𝐰 𝐛𝐮𝐭𝐭𝐨𝐧𝐬.\n𝐘𝐨𝐮 𝐜𝐚𝐧 𝐮𝐬𝐞 /deletethumbnail t𝐨 𝐝𝐞𝐥𝐞𝐭𝐞 𝐭𝐡𝐞 𝐚𝐮𝐭𝐨-𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥."
    SET_CUSTOM_USERNAME_PASSWORD = """𝐈𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐯𝐢𝐝𝐞𝐨𝐬, 𝐩𝐫𝐨𝐯𝐢𝐝𝐞 𝐭𝐡𝐞𝐦 𝐢𝐧 𝐭𝐡𝐞 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 𝐟𝐨𝐫𝐦𝐚𝐭:
URL | filename | username | password"""
    DOWNLOAD_START = "📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠..."
    UPLOAD_START = "📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠..."
    RCHD_TG_API_LIMIT = "𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐢𝐧 {} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬.\n𝐃𝐞𝐭𝐞𝐜𝐭𝐞𝐝 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞: {}\n𝐒𝐨𝐫𝐫𝐲. 𝐁𝐮𝐭, 𝐈 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐩𝐥𝐨𝐚𝐝 𝐟𝐢𝐥𝐞𝐬 𝐥𝐚𝐫𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 𝟐 𝐆𝐁 (𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝟒𝐆) 𝐝𝐮𝐞 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐀𝐏𝐈 𝐥𝐢𝐦𝐢𝐭𝐚𝐭𝐢𝐨𝐧𝐬."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐮𝐬𝐢𝐧𝐠 {BOT_USERNAME} \n\n<b>𝐉𝐨𝐢𝐧 : @lkhitech</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐢𝐧 {} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬.\n𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐢𝐧 {} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬."
    SAVED_CUSTOM_THUMB_NAIL = "𝐂𝐮𝐬𝐭𝐨𝐦 𝐯𝐢𝐝𝐞𝐨/𝐟𝐢𝐥𝐞 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥𝐬 𝐰𝐞𝐫𝐞 𝐬𝐚𝐯𝐞𝐝. 𝐓𝐡𝐢𝐬 𝐢𝐦𝐚𝐠𝐞 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐮𝐬𝐞𝐝 𝐢𝐧 𝐭𝐡𝐞 𝐯𝐢𝐝𝐞𝐨/𝐟𝐢𝐥𝐞."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ 𝐓𝐡𝐞 𝐜𝐮𝐬𝐭𝐨𝐦 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐜𝐥𝐞𝐚𝐫𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲."
    CUSTOM_CAPTION_UL_FILE = "{}"
    THUMBNAIL_CAPTION = f"{BACKHAND_INDEX_POINTING_UP_LIGHT_SKIN_TONE} Your Permanent thumbnail"
    NO_VOID_FORMAT_FOUND = "⚠️ 𝐄𝐑𝐑𝐎𝐑...\n<b>𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐃𝐋</b> 𝐬𝐚𝐢𝐝: {}"
    HELP_USER = """𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐌𝐞 𝐅𝐨𝐥𝐥𝐨𝐰 𝐭𝐡𝐞𝐬𝐞 𝐬𝐭𝐞𝐩𝐬!
    
𝟭. 𝗦𝗲𝗻𝗱 𝘁𝗵𝗲 𝗨𝗥𝗟 (𝗲𝘅𝗮𝗺𝗽𝗹𝗲.𝗱𝗼𝗺𝗮𝗶𝗻/𝗙𝗶𝗹𝗲.𝗺𝗽𝟰 | 𝗡𝗲𝘄 𝗙𝗶𝗹𝗲𝗻𝗮𝗺𝗲.𝗺𝗽𝟰).
𝟮. 𝗦𝗲𝗻𝗱 𝘁𝗵𝗲 𝗶𝗺𝗮𝗴𝗲 𝗮𝘀 𝗮 𝗰𝘂𝘀𝘁𝗼𝗺 𝘁𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 (𝗼𝗽𝘁𝗶𝗼𝗻𝗮𝗹).
𝟯. 𝗦𝗲𝗹𝗲𝗰𝘁 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻.
𝗦𝗩𝗶𝗱𝗲𝗼 - 𝗚𝗶𝘃𝗲 𝘁𝗵𝗲 𝗙𝗶𝗹𝗲 𝗮𝘀 𝗮 𝘃𝗶𝗱𝗲𝗼 𝘄𝗶𝘁𝗵 𝗦𝗰𝗿𝗲𝗲𝗻𝘀𝗵𝗼𝘁𝘀
   𝗗𝗙𝗶𝗹𝗲  - 𝗚𝗶𝘃𝗲 𝗙𝗶𝗹𝗲 (𝘃𝗶𝗱𝗲𝗼) 𝗮𝘀 𝗮 𝗳𝗶𝗹𝗲 𝘄𝗶𝘁𝗵 𝗦𝗰𝗿𝗲𝗲𝗻𝘀𝗵𝗼𝘁𝘀
   𝗩𝗶𝗱𝗲𝗼  - 𝗚𝗶𝘃𝗲 𝘁𝗵𝗲 𝗙𝗶𝗹𝗲 𝗮𝘀 𝗮 𝘃𝗶𝗱𝗲𝗼 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗦𝗰𝗿𝗲𝗲𝗻𝘀𝗵𝗼𝘁𝘀
   𝗙𝗶𝗹𝗲   - 𝗚𝗶𝘃𝗲 𝗮 𝗙𝗶𝗹𝗲 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗦𝗰𝗿𝗲𝗲𝗻𝘀𝗵𝗼𝘁𝘀
"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "𝐑𝐞𝐩𝐥𝐲 /generatecustomthumbnail 𝐭𝐨 𝐚 𝐦𝐞𝐝𝐢𝐚 𝐚𝐥𝐛𝐮𝐦, 𝐭𝐨 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐜𝐮𝐬𝐭𝐨𝐦 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """𝐓𝐡𝐞 𝐦𝐞𝐝𝐢𝐚 𝐚𝐥𝐛𝐮𝐦 𝐬𝐡𝐨𝐮𝐥𝐝 𝐜𝐨𝐧𝐭𝐚𝐢𝐧 𝐨𝐧𝐥𝐲 𝐭𝐰𝐨 𝐩𝐡𝐨𝐭𝐨𝐬. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐫𝐞-𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐦𝐞𝐝𝐢𝐚 𝐚𝐥𝐛𝐮𝐦, 𝐚𝐧𝐝 𝐭𝐡𝐞𝐧 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧, 𝐨𝐫 𝐬𝐞𝐧𝐝 𝐨𝐧𝐥𝐲 𝐭𝐰𝐨 𝐩𝐡𝐨𝐭𝐨𝐬 𝐢𝐧 𝐚𝐧 𝐚𝐥𝐛𝐮𝐦."
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐮𝐬𝐞 𝐭𝐡𝐞 /rename 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐚𝐟𝐭𝐞𝐫 𝐫𝐞𝐜𝐞𝐢𝐯𝐢𝐧𝐠 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐫𝐞𝐧𝐚𝐦𝐞 𝐢𝐭 𝐰𝐢𝐭𝐡 𝐜𝐮𝐬𝐭𝐨𝐦 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐬𝐮𝐩𝐩𝐨𝐫𝐭.
"""
    CANCEL_STR = "𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐂𝐚𝐧𝐜𝐞𝐥𝐥𝐞𝐝"
    ZIP_UPLOADED_STR = "𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 {} 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧 {} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
    SLOW_URL_DECED = "𝗚𝗼𝘀𝗵, 𝘁𝗵𝗮𝘁 𝘀𝗲𝗲𝗺𝘀 𝘁𝗼 𝗯𝗲 𝗮 𝘃𝗲𝗿𝘆 𝘀𝗹𝗼𝘄 𝗨𝗥𝗟. 𝗦𝗶𝗻𝗰𝗲 𝘆𝗼𝘂 𝘄𝗲𝗿𝗲 𝘀𝗰𝗿𝗲𝘄𝗶𝗻𝗴 𝗺𝘆 𝗵𝗼𝗺𝗲, 𝗜 𝗮𝗺 𝗶𝗻 𝗻𝗼 𝗺𝗼𝗼𝗱 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘁𝗵𝗶𝘀 𝗳𝗶𝗹𝗲. 𝗠𝗲𝗮𝗻𝘄𝗵𝗶𝗹𝗲, 𝘄𝗵𝘆 𝗱𝗼𝗻'𝘁 𝘆𝗼𝘂 𝘁𝗿𝘆 𝘁𝗵𝗶𝘀:➡️ https://bit.ly/3YnrGRU 𝗮𝗻𝗱 𝗴𝗲𝘁 𝗺𝗲 𝗮 𝗳𝗮𝘀𝘁 𝗨𝗥𝗟 𝘀𝗼 𝘁𝗵𝗮𝘁 𝗜 𝗰𝗮𝗻 𝘂𝗽𝗹𝗼𝗮𝗱 𝘁𝗼 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺, 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝘀𝗹𝗼𝘄𝗶𝗻𝗴 𝗱𝗼𝘄𝗻 𝗼𝘁𝗵𝗲𝗿 𝘂𝘀𝗲𝗿𝘀."

    ERROR_YTDLP = "𝐌𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐞 𝐥𝐚𝐭𝐞𝐬𝐭 𝐯𝐞𝐫𝐬𝐢𝐨𝐧; 𝐬𝐞𝐞 https://yt-dl.org/update  𝐨𝐧 𝐡𝐨𝐰 𝐭𝐨 𝐮𝐩𝐝𝐚𝐭𝐞. 𝐁𝐞 𝐬𝐮𝐫𝐞 𝐭𝐨 𝐜𝐚𝐥𝐥 𝐲𝐨𝐮𝐭𝐮𝐛𝐞-𝐝𝐥 𝐰𝐢𝐭𝐡 𝐭𝐡𝐞 --𝐯𝐞𝐫𝐛𝐨𝐬𝐞 𝐟𝐥𝐚𝐠 𝐚𝐧𝐝 𝐢𝐧𝐜𝐥𝐮𝐝𝐞 𝐢𝐭𝐬 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝐨𝐮𝐭𝐩𝐮𝐭."
    INCORRECT_REQUEST = "𝐏𝐥𝐞𝐚𝐬𝐞 𝐦𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐲𝐨𝐮 𝐬𝐮𝐛𝐦𝐢𝐭 𝐲𝐨𝐮𝐫 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐜𝐨𝐫𝐫𝐞𝐜𝐭𝐥𝐲."
    WAIT_PROCESS_FINISH = "𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐟𝐢𝐧𝐢𝐬𝐡 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐛𝐞𝐟𝐨𝐫𝐞 𝐬𝐞𝐧𝐝𝐢𝐧𝐠 𝐦𝐨𝐫𝐞 𝐥𝐢𝐧𝐤𝐬! o𝐫 𝐮𝐬𝐞 /cancel 𝐭𝐨 𝐭𝐞𝐫𝐦𝐢𝐧𝐚𝐭𝐞 𝐢𝐧𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐞𝐬."
    PROCESS_CANCELLED = "𝐅𝐢𝐥𝐞 𝐮𝐩𝐥𝐨𝐚𝐝 𝐜𝐚𝐧𝐜𝐞𝐥𝐞𝐝 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐧𝐨𝐰 𝐬𝐞𝐧𝐝 𝐚 𝐧𝐞𝐰 𝐔𝐑𝐋" 
    NO_PROCESS_FOUND = "𝐍𝐨 𝐩𝐞𝐧𝐝𝐢𝐧𝐠 𝐮𝐩𝐥𝐨𝐚𝐝𝐬 𝐰𝐞𝐫𝐞 𝐟𝐨𝐮𝐧𝐝. 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐮𝐩𝐥𝐨𝐚𝐝 𝐟𝐢𝐥𝐞𝐬 𝐛𝐲 𝐬𝐞𝐧𝐝𝐢𝐧𝐠 𝐚 𝐥𝐢𝐧𝐤 𝐧𝐨𝐰!"
    FORMAT_SELECTION = "🔽 𝐒𝐞𝐥𝐞𝐜𝐭 𝐚𝐧𝐝 𝐂𝐡𝐨𝐬𝐞 𝐲𝐨𝐮𝐫 𝐅𝐨𝐫𝐦𝐚𝐭 🔽"
    NOT_AUTH_USER_TEXT = "You Aren't An Approved User Please must Upgrade the plan /upgrade."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload:"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"