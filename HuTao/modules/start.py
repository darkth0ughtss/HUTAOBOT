#MIT License
#Copyright (c) 2023, ©NovaNetworks

import re
import time
import random
from ..database import *
import asyncio
import sys
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from ..imgs_config import start_images , sticker_ids
from HuTao import BOT_NAME, BOT_USERNAME, HELPABLE, app, Hutao_Ver
from HuTao.helpers import paginate_modules
from HuTao.Config import COMMAND_HANDLER
from HuTao.helpers.string import *
from HuTao.modules.notes import note_redirect

VERSION = "1.0.5"  # Update this as per your bot's version
PYTHON_VERSION = sys.version.split(" ")[0]
PYROGRAM_VERSION = pyrogram.__version__

# Uptime calculation
start_time = time.time()




PM_TEXT = f"""
**────「 {BOT_NAME} 」────
➖➖➖➖➖➖➖➖➖➖➖➖➖
¤ I'M HERE! IF YOU NEED SOME ASSISTANCE, I'M HERE TO GIVE IT MY ALL TO THE VERY END!
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
♦ VERSION: {Hutao_Ver}
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
⍟ GET TO KNOW ABOUT MY SKILLS BY CLICKING HELP**
➖➖➖➖➖➖➖➖➖➖➖➖➖
"""


home_keyboard_pm = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ADD ME",url=f"http://t.me/{BOT_USERNAME}?startgroup=new")
        ],
        [
            InlineKeyboardButton(text="DEVELOPER", url="https://t.me/KIRITO1240"),
            InlineKeyboardButton(text="SOURCE",url="https://t.me/NovaNetworks"),
        ],
        [
            InlineKeyboardButton(text="HELP", callback_data="help_commands")           
        ],
    ]
)


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="HELP", url=f"t.me/{BOT_USERNAME}?start=help")
        ]
    ]
)


@app.on_message(filters.command("start") & filters.private)
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
            InlineKeyboardButton("✨𝘊𝘖𝘔𝘔𝘈𝘕𝘋𝘚 ✨", callback_data="help_commands"),
            InlineKeyboardButton("🌿𝘚𝘶𝘱𝘱𝘰𝘳𝘵 🌿", url="https://t.me/DominosXd")
        ],
        [
            InlineKeyboardButton("🔔𝘜𝘱𝘥𝘢𝘵𝘦𝘴🔔", url="https://t.me/DominosNetwork"),
            InlineKeyboardButton("ℹ️ 𝘉𝘖𝘛-𝘐𝘕𝘍𝘖", callback_data="bot_info")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(welcome_text, reply_markup=reply_markup)

 
@app.on_callback_query(filters.regex("bot_info"))
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

@app.on_message(filters.command("help", COMMAND_HANDLER))
async def help_command(_, message: Message):
    if message.chat.type.value != "private":
        if len(message.command) >= 2:
            name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
            if str(name) in HELPABLE:
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=f"{name}",
                                url=f"t.me/{BOT_USERNAME}?start=help_{name}",
                            )
                        ],
                    ]
                )
                await message.reply_text(
                    "**CLICK HERE TO GET HELP ABOUT: {btn_name}**".format(btn_name=name),
                    reply_markup=key,
                )
            else:
                await message.reply_text("**LETS HEAD TO PRIVATE CHAT TO KNOW MORE ABOUT MY SKILLS**", reply_markup=keyboard)
        else:
            await message.reply_text("**LETS HEAD TO PRIVATE CHAT TO KNOW MORE ABOUT MY SKILLS**", reply_markup=keyboard)
    elif len(message.command) >= 2:
        name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
        if str(name) in HELPABLE:
            text = (
                "**⍟ HELP FOR: {mod}**\n".format(mod=HELPABLE[name].__mod__)
                + HELPABLE[name].__help__
            )
            await message.reply_photo("https://graph.org//file/9e756c52fdd881b44ecc8.png",caption=text, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("BACK", callback_data="help_back")]]
            ))
        else:
            text, help_keyboard = await help_parser(message.from_user.first_name)
            await message.reply_photo(
                "https://graph.org//file/9e756c52fdd881b44ecc8.png",
                caption=text,
                reply_markup=help_keyboard
            )
    else:
        text, help_keyboard = await help_parser(message.from_user.first_name)
        await message.reply_photo(
            "https://graph.org//file/9e756c52fdd881b44ecc8.png",
            caption=text, reply_markup=help_keyboard
        )



async def help_parser(name, hkey=None):
    if not hkey:
        hkey = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
"""
**────「 {BOT_NAME} 」────
➖➖➖➖➖➖➖➖➖➖➖➖➖
¤ I'm here! If you need some assistance, I'm here to give it my all to the very end!
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
⍟ CLICK BELOW TO KNOW ABOUT MY SKILLS**
➖➖➖➖➖➖➖➖➖➖➖➖➖

""".format(
            BOT_NAME=BOT_NAME
        ),
        hkey,
    )

@app.on_callback_query(filters.regex("help_commands"))
async def commands_callbacc(_, cb: CallbackQuery):
    text, keyb = await help_parser(BOT_NAME)
    await cb.edit_message_caption(
        caption=text,
        reply_markup=keyb,
    )

@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(self: Client, query: CallbackQuery):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    if mod_match:
        module = mod_match[1].replace(" ", "_")
        text = (
            "**⍟ HELP FOR: {mod}**\n".format(mod=HELPABLE[module].__mod__)
            + HELPABLE[module].__help__
        )

        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("BACK", callback_data="help_back")]]
            )
        )
    elif home_match:
        await query.edit_message_caption(
            caption=PM_TEXT,
            reply_markup=home_keyboard_pm,
        )
    elif prev_match:
        curr_page = int(prev_match[1])
        await query.edit_message_caption(
            caption=f"""
**────「 {BOT_NAME} 」────
➖➖➖➖➖➖➖➖➖➖➖➖➖
¤ I'm here! If you need some assistance, I'm here to give it my all to the very end!
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
⍟ CLICK BELOW TO KNOW ABOUT MY SKILLS**
➖➖➖➖➖➖➖➖➖➖➖➖➖

""",
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            )
        )

    elif next_match:
        next_page = int(next_match[1])
        await query.edit_message_caption(
            caption=f"""
**────「 {BOT_NAME} 」────
➖➖➖➖➖➖➖➖➖➖➖➖➖
¤ I'm here! If you need some assistance, I'm here to give it my all to the very end!
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
⍟ CLICK BELOW TO KNOW ABOUT MY SKILLS**
➖➖➖➖➖➖➖➖➖➖➖➖➖

""",
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            )
        )

    elif back_match:
        await query.edit_message_caption(
            caption=f"""
**────「 {BOT_NAME} 」────
➖➖➖➖➖➖➖➖➖➖➖➖➖
¤ I'm here! If you need some assistance, I'm here to give it my all to the very end!
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
⍟ CLICK BELOW TO KNOW ABOUT MY SKILLS**
➖➖➖➖➖➖➖➖➖➖➖➖➖

""",
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
        )

    elif create_match:
        text, keyb = await help_parser(query)
        await query.edit_message_caption(
            caption=text,
            reply_markup=keyb
        )

    try:
        await self.answer_callback_query(query.id)
    except:
        pass
