
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from AdityaHalder.utilities.config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from AdityaHalder.utilities.strings import get_command
from AdityaHalder import bot
from AdityaHalder.modules.core.call import aditya
from AdityaHalder.modules.utils import bot_sys_stats
from AdityaHalder.modules.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@bot.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await aditya.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )
