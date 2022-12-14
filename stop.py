from pyrogram import filters
from pyrogram.types import Message

from AdityaHalder import bot
from AdityaHalder.utilities.config import BANNED_USERS
from AdityaHalder.utilities.strings import get_command
from AdityaHalder.utilities.events.command import command
from AdityaHalder.modules.core.call import aditya
from AdityaHalder.modules.database import set_loop
from AdityaHalder.modules.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@bot.on_message(
    command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await aditya.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )
