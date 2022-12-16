# the logging things

import os
import logging
import platform

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
from pyrogram import __version__, idle
from pyromod import listen
from pyrogram import Client as Kmac
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    
    app = Kmac("urluploadbot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins,
    workers=100)

    app.start()
    me = app.get_me()

    startup_msg = f"Successfully deployed your app at @{me.username}\n"
    startup_msg += f"Pyrogram Version: V{__version__}\n"
    startup_msg += f"Python Version: V{platform.python_version()}\n\n"
    startup_msg += "Thanks for deploying our bot. Please give a star to my repo and join @lkhitech."
    print(startup_msg)

    idle()

    app.stop()
    print("😢.")
