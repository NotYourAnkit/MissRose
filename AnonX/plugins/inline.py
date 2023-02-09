from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            InlineQueryResultPhoto)
from youtubesearchpython.__future__ import VideosSearch

from config import BANNED_USERS, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.inlinequery import answer


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[
                0
            ]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• ʏᴏᴜᴛᴜʙᴇ •",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
📌 **𝙏𝙞𝙩𝙡𝙚 ❤:** [{title}]({link})

⏳ **𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 ☠️:** {duration} Mins
👀 **𝙑𝙞𝙚𝙬𝙨 👀:** `{views}`
⏰ **𝙋𝙪𝙗𝙡𝙞𝙨𝙝𝙚𝙙 𝙊𝙣🌸:** {published}
🎥 **𝙐𝙥𝙙𝙖𝙩𝙚𝙨 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 💀:** [𝙈𝙞𝙨𝙨 𝙍𝙤𝙨𝙚 𝙐𝙥𝙙𝙖𝙩𝙚](https://t.me/MissRoseMusic_Update) 
📎 **𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝘾𝙝𝙖𝙩😎:** [𝘿𝙤𝙥𝙚 𝙎𝙝𝙤𝙥𝙚](https://t.me/DopeShope_xD) 
😈 **𝘽𝙤𝙩 𝙊𝙬𝙣𝙚𝙧 ⚡:** [𝘼𝙉𝙆𝙄𝙏 ⚠️](https://t.me/NotYourAnkit) 

💖 **𝙏𝙝𝙚 𝙎𝙚𝙖𝙧𝙘𝙝 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 ⚠️ {MUSIC_BOT_NAME}**"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(
                query.id, results=answers
            )
        except:
            return
