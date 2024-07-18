# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/O_okarma
# API BY https://www.github.com/SOME-1HING
# PROVIDED BY https://t.me/ProjectCodeX

# <============================================== IMPORTS =========================================================>
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from .. import app as bot

# <=======================================================================================================>

# <================================================ FUNCTIONS =====================================================>
async def get_cosplay_data():
    cosplay_url = "https://sugoi-api.vercel.app/cosplay"
    async with aiohttp.ClientSession() as session:
        async with session.get(cosplay_url) as response:
            return await response.json()

@bot.on_message(filters.command("cosplay"))
async def cosplay_command(client: Client, message: Message):
    try:
        data = await get_cosplay_data()
        photo_url = data.get("url")  # Corrected key: "url" instead of "cosplay_url"
        if photo_url:
            await message.reply_photo(photo=photo_url)
        else:
            await message.reply_text("🚫 𝗖𝗼𝘂𝗹𝗱 𝗻𝗼𝘁 𝗳𝗲𝘁𝗰𝗵 𝗽𝗵𝗼𝘁𝗼 𝗨𝗥𝗟.")
    except aiohttp.ClientError:
        await message.reply_text("⚠️ 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝗱𝗮𝘁𝗮.")


# <================================================ END =======================================================>
