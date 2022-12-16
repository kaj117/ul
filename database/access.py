from config import Config
from database.database import Database

kmac = Database(Config.MongoDB_URI, Config.SESSION_NAME)