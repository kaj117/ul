import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = "5661557412:AAHEliUB2xLhQCCis9Bhk8PsJD4x9erVq-Q"
    # The Telegram API things
    API_ID = 1383845
    # Get these values from my.telegram.org
    API_HASH = "0e3d2c299cc3c5cc26c283cecd2eb97c"
    #yourid
    OWNER_ID = 5027085442
    # Array to store users who are authorized to use the bot
    AUTH_USERS = ""
    SUPER7X_DLBOT_USERS = ""
    #your bot uname
    BOT_USERNAME = "@kaj"
    #channel id -100
    UPDATE_CHANNEL = "-1001796388930"
    #Your MongoDB URI
    MongoDB_URI = "mongodb+srv://kaj:0951357@cluster0.6bbgpi1.mongodb.net/?retryWrites=true&w=majority"
    #postgresql url
    DB_URI = "postgres://urupload_user:CYMU4Y3q6KSXgsrX3BDuKYLBm3cIWF9v@dpg-cedu5ghgp3jvikbsmn2g-a.singapore-postgres.render.com/urupload"
    #db session name
    SESSION_NAME = "TGurluploadbot"
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = ""
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    TIME_GAP = ""

