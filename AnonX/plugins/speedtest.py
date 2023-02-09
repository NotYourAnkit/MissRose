import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ [𝙈𝙞𝙨𝙨𝙍𝙤𝙨𝙚](https://t.me/MissRoseMusic_Bot) 𝙏𝙚𝙨𝙩𝙞𝙣𝙜 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩 𝘽𝙖𝙗𝙮 ☠️**")
        test.download()
        m = m.edit("**⇆ [𝙈𝙞𝙨𝙨𝙍𝙤𝙨𝙚](https://t.me/MissRoseMusic_Bot) 𝙏𝙚𝙨𝙩𝙞𝙣𝙜 𝙐𝙥𝙡𝙤𝙖𝙙 𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩 𝘽𝙖𝙗𝙮 ⚠️**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ [𝙈𝙞𝙨𝙨𝙍𝙤𝙨𝙚](https://t.me/MissRoseMusic_Bot) 𝙎𝙝𝙖𝙧𝙞𝙣𝙜 𝙍𝙚𝙨𝙪𝙡𝙩𝙨 𝙊𝙛 𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩 𝘽𝙖𝙗𝙮 😇**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 ᴛʀʏɪɴɢ ᴛᴏ ᴄʜᴇᴄᴋ ᴜᴩʟᴏᴀᴅ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅ...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **[𝙈𝙞𝙨𝙨𝙍𝙤𝙨𝙚](https://t.me/MissRoseMusic_Bot) 𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩 𝙍𝙚𝙨𝙪𝙡𝙩𝙨 😎** ✯
    
<u>**❥͜͡𝘾𝙡𝙞𝙚𝙣𝙩 𝘿𝙚𝙩𝙖𝙞𝙡𝙨 ⚠️ :**</u>
**» __𝙄𝙎𝙋 🚫 :__** {result['client']['isp']}
**» __𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ✨ :__** {result['client']['country']}
  
<u>**❥͜͡𝙎𝙚𝙧𝙫𝙚𝙧 𝘽𝙖𝙗𝙮 🥵 :**</u>
**» __𝙉𝙖𝙢𝙚 🌸 :__** {result['server']['name']}
**» __𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ✨ :__** {result['server']['country']}, {result['server']['cc']}
**» __𝙎𝙥𝙤𝙣𝙨𝙚𝙧 😎 :__** {result['server']['sponsor']}
**» __𝙇𝙖𝙩𝙚𝙣𝙘𝙮 ⚡ :__** {result['server']['latency']}  
**» __𝙋𝙞𝙣𝙜 ⚠️ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
