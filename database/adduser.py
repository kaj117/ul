from pyrogram import Client
from database.access import kmac
from pyrogram.types import Message


async def AddUser(bot: Client, update: Message):
    if not await kmac.is_user_exist(update.from_user.id):
           await kmac.add_user(update.from_user.id)