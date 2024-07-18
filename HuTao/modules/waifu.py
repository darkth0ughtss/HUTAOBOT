# handlers/waifu_handler.py
import httpx
from pyrogram import Client, filters
from pyrogram.types import Message
from ..config import bot_token
from .. import app as bot

# Function to fetch a single waifu image from a given category
async def fetch_waifu_image(category: str):
    url = f"https://api.waifu.pics/sfw/{category}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()["url"]
        return None

# Command handler function for /waifu and other categories
@bot.on_message(filters.command(["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hugg", "awoo", "kisss", "lick", "pat", "smug", "bonk", "yeet", "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slapp", "kill", "kickk", "happy", "wink", "poke", "dance", "cringe"], prefixes="/"))
async def waifu_command(client: Client, message: Message):
    command = message.command[0] if message.command else "waifu"
    waifu_image_url = await fetch_waifu_image(command)
    if waifu_image_url:
        await message.reply_photo(waifu_image_url)
    else:
        await message.reply_text(f"𝑆𝑜𝑟𝑟𝑦, 𝐼 𝑐𝑜𝑢𝑙𝑑𝑛'𝑡 𝑓𝑒𝑡𝑐ℎ 𝑎 {command} 𝑖𝑚𝑎𝑔𝑒 𝑎𝑡 𝑡ℎ𝑒 𝑚𝑜𝑚𝑒𝑛𝑡.")

