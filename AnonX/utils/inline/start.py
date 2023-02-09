from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ 𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝘾𝙝𝙖𝙩 ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚠️ 𝙃𝙚𝙡𝙥 ⚠️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ 𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝘾𝙝𝙖𝙩 ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚠️ 𝙃𝙚𝙡𝙥 ⚠️", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="➚ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥 ➚", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝘽𝙤𝙩 𝙊𝙬𝙣𝙚𝙧 ❤", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="█ 𝙎𝙤𝙪𝙧𝙘𝙚 𝘾𝙤𝙙𝙚 █", url=config.UPSTREAM_REPO
            )
        ],
     ]
    return buttons
