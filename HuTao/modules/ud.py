import requests
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from .. import app as bot 

async def fetch_definition(term):
    response = await asyncio.to_thread(requests.get, f"https://api.urbandictionary.com/v0/define?term={term}")
    return response

@bot.on_message(filters.command("ud"))
async def ud_handler(client, message):
    text = message.text[len("/ud "):]
    if not text:
        await message.reply_text("𝗣𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘁𝗲𝗿𝗺 𝘁𝗼 𝘀𝗲𝗮𝗿𝗰𝗵.")
        return

    response = await fetch_definition(text)
    if response.status_code != 200:
        await message.reply_text("There was an error contacting the Urban Dictionary API.")
        return

    results = response.json()
    try:
        definition = results["list"][0]["definition"]
        example = results["list"][0]["example"]
        reply_text = f'*{text}*\n\n{definition}\n\n_{example}_'
    except IndexError:
        reply_text = "No results found."

    await message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)
