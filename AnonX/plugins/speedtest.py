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
        m = m.edit("**โ [๐๐๐จ๐จ๐๐ค๐จ๐](https://t.me/MissRoseMusic_Bot) ๐๐๐จ๐ฉ๐๐ฃ๐ ๐ฟ๐ค๐ฌ๐ฃ๐ก๐ค๐๐ ๐๐ฅ๐๐๐๐๐๐จ๐ฉ ๐ฝ๐๐๐ฎ โ ๏ธ**")
        test.download()
        m = m.edit("**โ [๐๐๐จ๐จ๐๐ค๐จ๐](https://t.me/MissRoseMusic_Bot) ๐๐๐จ๐ฉ๐๐ฃ๐ ๐๐ฅ๐ก๐ค๐๐ ๐๐ฅ๐๐๐๐๐๐จ๐ฉ ๐ฝ๐๐๐ฎ โ ๏ธ**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**โป [๐๐๐จ๐จ๐๐ค๐จ๐](https://t.me/MissRoseMusic_Bot) ๐๐๐๐ง๐๐ฃ๐ ๐๐๐จ๐ช๐ก๐ฉ๐จ ๐๐ ๐๐ฅ๐๐๐๐๐๐จ๐ฉ ๐ฝ๐๐๐ฎ ๐**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("๐ซ แดสสษชษดษข แดแด แดสแดแดแด แดแดฉสแดแดแด แดษดแด แดแดแดกษดสแดแดแด sแดฉแดแดแด...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""โฏ **[๐๐๐จ๐จ๐๐ค๐จ๐](https://t.me/MissRoseMusic_Bot) ๐๐ฅ๐๐๐๐๐๐จ๐ฉ ๐๐๐จ๐ช๐ก๐ฉ๐จ ๐** โฏ
    
<u>**โฅออก๐พ๐ก๐๐๐ฃ๐ฉ ๐ฟ๐๐ฉ๐๐๐ก๐จ โ ๏ธ :**</u>
**ยป __๐๐๐ ๐ซ :__** {result['client']['isp']}
**ยป __๐พ๐ค๐ช๐ฃ๐ฉ๐ง๐ฎ โจ :__** {result['client']['country']}
  
<u>**โฅออก๐๐๐ง๐ซ๐๐ง ๐ฝ๐๐๐ฎ ๐ฅต :**</u>
**ยป __๐๐๐ข๐ ๐ธ :__** {result['server']['name']}
**ยป __๐พ๐ค๐ช๐ฃ๐ฉ๐ง๐ฎ โจ :__** {result['server']['country']}, {result['server']['cc']}
**ยป __๐๐ฅ๐ค๐ฃ๐จ๐๐ง ๐ :__** {result['server']['sponsor']}
**ยป __๐๐๐ฉ๐๐ฃ๐๐ฎ โก :__** {result['server']['latency']}  
**ยป __๐๐๐ฃ๐ โ ๏ธ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
