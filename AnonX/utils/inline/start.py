from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="β― πΌππ ππ ππ€ ππ€πͺπ§ πΎπππ© β―",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="β οΈ πππ‘π₯ β οΈ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="πππ©π©ππ£ππ¨", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="β― πΌππ ππ ππ€ ππ€πͺπ§ πΎπππ© β―",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="β οΈ πππ‘π₯ β οΈ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="β ππͺπ₯π₯π€π§π© ππ§π€πͺπ₯ β", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="π½π€π© ππ¬π£ππ§ β€", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="β ππ€πͺπ§ππ πΎπ€ππ β", url=config.UPSTREAM_REPO
            )
        ],
     ]
    return buttons
