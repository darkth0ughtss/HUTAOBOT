# handlers/start_handler.py

import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ..imgs_config import start_images , sticker_ids
from .. import app as bot
from pymongo import MongoClient
from ..config import MONGO_URL
import time
import sys
import pyrogram


mongo_client = MongoClient(MONGO_URL)
db = mongo_client["THE-BOT"]
users_collection = db["USERS"]

# Define versions
VERSION = "1.0.5"  # Update this as per your bot's version
PYTHON_VERSION = sys.version.split(" ")[0]
PYROGRAM_VERSION = pyrogram.__version__

# Uptime calculation
start_time = time.time()

@bot.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    random_sticker = random.choice(sticker_ids)
    random_image = random.choice(start_images)
    
    # Delete the start command received from the user
    await message.delete()
    
    # Save user ID to the USERS collection
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id, "first_name": user_first_name})
    
    # Step 0: Send a random sticker
    await message.reply_sticker(random_sticker)
    
    # Step 1: Send "𝚂𝚝𝚊𝚛𝚝𝚒𝚗𝚐....."
    start_msg = await message.reply_text("𝚂𝚝𝚊𝚛𝚝𝚒𝚗𝚐.....")
    await asyncio.sleep(0.35)

    # Step 2: Edit message to "𝚆𝚎𝚕𝚌𝚘𝚖𝚎 {user's first name} 𝚋𝚊𝚋𝚢 𝚑𝚘𝚠 𝚊𝚛𝚎 𝚞𝚑𝚑..."
    await start_msg.edit_text(f"𝚆𝚎𝚕𝚌𝚘𝚖𝚎 {user_first_name} 𝚋𝚊𝚋𝚢 𝚑𝚘𝚠 𝚊𝚛𝚎 𝚞𝚑𝚑...")
    await asyncio.sleep(0.35)

    # Step 3: Delete the message and send "💕"
    await start_msg.delete()
    emoji_msg = await message.reply_text("💕")
    await asyncio.sleep(0.35)

    # Step 4: Edit the emoji to "⚡️"
    await emoji_msg.edit_text("⚡️")
    await asyncio.sleep(0.35)

    # Step 5: Edit the emoji to "✨"
    await emoji_msg.edit_text("✨")
    # Delete the emoji_msg
    await emoji_msg.delete()
    await asyncio.sleep(0.2)

    # Delete the emoji_msg
    await emoji_msg.delete()

    # Final step: Send the welcome message with a random image
    client_me = await client.get_me()
    welcome_text = (
        f'[๏]({random_image}) 𝙾𝚔𝚊𝚎𝚛𝚒, 𝙸\'𝚖 '
        f'{client_me.first_name}!\n'
        '♥ 𝚂𝚘 𝚐𝚕𝚊𝚍 𝚝𝚘 𝚜𝚎𝚎 𝚢𝚘𝚞 𝚑𝚎𝚛𝚎.\n'
        '✨ 𝙸\'𝚖 𝚊𝚗 𝙰𝙸-𝚙𝚘𝚠𝚎𝚛𝚎𝚍 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚋𝚘𝚝, 𝚑𝚎𝚛𝚎 𝚝𝚘 𝚊𝚜𝚜𝚒𝚜𝚝 𝚢𝚘𝚞 𝚠𝚒𝚝𝚑 𝚊𝚕𝚕 𝚢𝚘𝚞𝚛 𝚗𝚎𝚎𝚍𝚜.\n\n'
        '➻ 𝙲𝚑𝚎𝚌𝚔 𝚘𝚞𝚝 𝚖𝚢 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚋𝚎𝚕𝚘𝚠 𝚝𝚘 𝚜𝚎𝚎 𝚠𝚑𝚊𝚝 𝙸 𝚌𝚊𝚗 𝚍𝚘!'
    )
    buttons = [
        [InlineKeyboardButton("💫 𝘈𝘋𝘋 𝘔𝘌 𝘛𝘖 𝘠𝘖𝘜𝘙 𝘎𝘙𝘖𝘜𝘗 💫", url="https://telegram.dog/frierenzbot?startgroup=true")],
        [
            InlineKeyboardButton("✨𝘊𝘖𝘔𝘔𝘈𝘕𝘋𝘚 ✨", callback_data="commands"),
            InlineKeyboardButton("🌿𝘚𝘶𝘱𝘱𝘰𝘳𝘵 🌿", url="https://t.me/DominosXd")
        ],
        [
            InlineKeyboardButton("🔔𝘜𝘱𝘥𝘢𝘵𝘦𝘴🔔", url="https://t.me/DominosNetwork"),
            InlineKeyboardButton("ℹ️ 𝘉𝘖𝘛-𝘐𝘕𝘍𝘖", callback_data="bot_info")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(welcome_text, reply_markup=reply_markup)

 
@bot.on_callback_query(filters.regex("bot_info"))
async def bot_info_callback(client, q):
    # Generate a random ping value between 3 and 18 with two decimal places
    ping_ms = f"{random.uniform(3, 18):.2f}"

    # Calculate uptime
    up = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
    
    txt = (
        f"🏓 Ping : {ping_ms} ms\n"
        f"📈 Uptime : {up}\n"
        f"🤖 Bot's version: {VERSION}\n"
        f"🐍 Python's version: {PYTHON_VERSION}\n"
        f"🔥 Pyrogram's version : {PYROGRAM_VERSION}"
    )
    await q.answer(txt, show_alert=True)
    return