from pyrogram import filters
from pyrogram.types import Message

from AdityaHalder.utilities.config import BANNED_USERS
from AdityaHalder.utilities.strings import get_command
from AdityaHalder.utilities.events.command import command
from AdityaHalder import bot
from AdityaHalder.modules.core.call import aditya
from AdityaHalder.modules.database import is_music_playing, music_off
from AdityaHalder.modules.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@bot.on_message(
    command(PAUSE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await aditya.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention)
    )
