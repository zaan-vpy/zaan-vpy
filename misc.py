import socket
import time

import heroku3
from pyrogram import filters

from AdityaHalder.utilities import config
from AdityaHalder.modules.core.adb import pymongodb

from .console import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"🥀 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞𝐝 ✨...")


def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID
    if config.MONGO_DB_URL is None:
        for user_id in OWNER:
            SUDOERS.add(user_id)
    else:
        sudoersdb = pymongodb.sudoers
        sudoers = sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        for user_id in OWNER:
            SUDOERS.add(user_id)
            if user_id not in sudoers:
                sudoers.append(user_id)
                sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )
        if sudoers:
            for x in sudoers:
                SUDOERS.add(x)
    LOGGER(__name__).info(f"🥀 𝐎𝐰𝐧𝐞𝐫𝐬 𝐚𝐧𝐝 𝐒𝐮𝐝𝐨𝐞𝐫𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 💞...")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"Heroku App Configured")
            except BaseException:
                LOGGER(__name__).warning(
                    f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )
