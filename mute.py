from pyrogram import filters
from pyrogram.types import Message

from AdityaHalder.utilities.config import BANNED_USERS
from AdityaHalder.utilities.strings import get_command
from AdityaHalder import bot
from AdityaHalder.modules.core.call import aditya
from AdityaHalder.modules.database import is_muted, mute_on
from AdityaHalder.modules.decorators import AdminRightsCheck

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@bot.on_message(
    filters.command(MUTE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await aditya.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention)
    )
