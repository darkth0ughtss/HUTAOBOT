import os
import asyncio
from pyrogram import Client, filters
from gtts import gTTS
from .. import app as bot

# Ensure this is the path where your bot's media files will be saved
OUTPUT_DIR = "output"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

@bot.on_message(filters.command("tts") & filters.text)
async def tts_handler(client, message):
    if len(message.command) < 2:
        await message.reply_text("𝗣𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝘁𝗵𝗲 𝘁𝗲𝘅𝘁 𝘁𝗼 𝗰𝗼𝗻𝘃𝗲𝗿𝘁 𝘁𝗼 𝘀𝗽𝗲𝗲𝗰𝗵. 𝗨𝘀𝗮𝗴𝗲: /𝘁𝘁𝘀 '𝘁𝗲𝘅𝘁'")
        return

    text = message.text.split(maxsplit=1)[1]
    output_file = os.path.join(OUTPUT_DIR, f"{message.from_user.id}_tts.mp3")

    await asyncio.to_thread(generate_tts, text, output_file)

    await message.reply_audio(audio=output_file, caption="𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗧𝗲𝘅𝘁-𝘁𝗼-𝗦𝗽𝗲𝗲𝗰𝗵 𝗮𝘂𝗱𝗶𝗼.")
    os.remove(output_file)

def generate_tts(text, output_file):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)
