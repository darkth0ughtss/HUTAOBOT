import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.enums import ParseMode
from .. import app as bot
from ..imgs_config import HUG_IMAGES , SLAP_IMAGES , KICK_IMAGES , KILL_IMAGES , KISS_IMAGES , PAT_IMAGES , SEX_IMAGES# Assuming you have a similar list of hug images as for kiss images

# Command handler for /hug
@bot.on_message(filters.command("hug") & filters.group)
async def hug_command(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply_text("𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝘂𝘀𝗲𝗿'𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗼𝗿 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗮 𝗵𝘂𝗴 𝗿𝗲𝗾𝘂𝗲𝘀𝘁.")
        return

    user_a = message.from_user

    if message.reply_to_message:
        user_b = message.reply_to_message.from_user
    else:
        username = message.command[1]
        try:
            user_b = await client.get_users(username)
        except Exception as e:
            await message.reply_text(f"𝗖𝗼𝘂𝗹𝗱 𝗻𝗼𝘁 𝗳𝗶𝗻𝗱 𝘂𝘀𝗲𝗿 {username}.")
            return

    # Check if the bot is replying to its own message
    bot_id = (await client.get_me()).id
    if user_b.id == bot_id:
        await message.reply_text("𝑁𝑜 𝑡ℎ𝑎𝑛𝑘𝑠, 𝐼 𝑑𝑜𝑛'𝑡 𝑛𝑒𝑒𝑑 𝑎 ℎ𝑢𝑔 𝑟𝑖𝑔ℎ𝑡 𝑛𝑜𝑤.")
        return

    if user_a.id == user_b.id:
        await message.reply_text("𝑌𝑜𝑢 𝑐𝑎𝑛𝑛𝑜𝑡 𝑠𝑒𝑛𝑑 𝑎 ℎ𝑢𝑔 𝑟𝑒𝑞𝑢𝑒𝑠𝑡 𝑡𝑜 𝑦𝑜𝑢𝑟𝑠𝑒𝑙𝑓.")
        return

    # Create inline button for User B to accept
    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("𝗔𝗰𝗰𝗲𝗽𝘁", callback_data=f"accept_hug:{user_a.id}:{user_b.id}")]
        ]
    )

    # Send the hug request message
    await message.reply_text(
        f"🤗 **[{user_b.first_name}](tg://user?id={user_b.id})**, **[{user_a.first_name}](tg://user?id={user_a.id})** wants to send you a hug! 🤗\n\n"
        "Will you accept the hug?",
        reply_markup=inline_keyboard,
        parse_mode=ParseMode.MARKDOWN
    )

# Callback handler for accepting the hug
@bot.on_callback_query(filters.regex(r"^accept_hug:(\d+):(\d+)$"))
async def accept_hug_callback(client: Client, callback_query):
    data = callback_query.data.split(":")
    user_a_id = int(data[1])
    user_b_id = int(data[2])

    user_a = await client.get_users(user_a_id)
    user_b = await client.get_users(user_b_id)

    if callback_query.from_user.id != user_b.id:
        await callback_query.answer("𝗕𝘀𝗱𝗸 𝗼𝗻𝗹𝘆 𝘁𝗵𝗲 𝗿𝗲𝗰𝗶𝗽𝗶𝗲𝗻𝘁 𝗰𝗮𝗻 𝗮𝗰𝗰𝗲𝗽𝘁 𝘁𝗵𝗶𝘀 𝗵𝘂𝗴 𝗿𝗲𝗾𝘂𝗲𝘀𝘁.", show_alert=True)
        return

    # Get a random hug image URL
    hug_image_url = random.choice(HUG_IMAGES)

    # Delete the acceptance message with the inline button
    await callback_query.message.delete()

    # Send the hug accepted message with the image
    await client.send_photo(
        chat_id=callback_query.message.chat.id,
        photo=hug_image_url,
        caption=f"💞 **[{user_b.first_name}](tg://user?id={user_b.id})** accepted the hug from **[{user_a.first_name}](tg://user?id={user_a.id})**! 💞",
        parse_mode=ParseMode.MARKDOWN
    )

    await callback_query.answer()

# Command handler for /kickk
@bot.on_message(filters.command("kickk") & filters.group)
async def kick_command(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply_text("𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝘂𝘀𝗲𝗿'𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗼𝗿 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝘁𝗼 𝗸𝗶𝗰𝗸 𝘁𝗵𝗲𝗺.")
        return

    user_a = message.from_user

    if message.reply_to_message:
        user_b = message.reply_to_message.from_user
    else:
        username = message.command[1]
        try:
            user_b = await client.get_users(username)
        except Exception as e:
            await message.reply_text(f"Could not find user {username}.")
            return

    # Check if the bot is being kicked
    bot_id = (await client.get_me()).id
    if user_b.id == bot_id:
        await message.reply_text("Ouch! Kicking a bot is not nice.")
        return

    if user_a.id == user_b.id:
        await message.reply_text("You cannot kick yourself. That's just silly.")
        return

    # Get a random kick image URL
    kick_image_url = random.choice(KICK_IMAGES)

    # Send the kick message with the image
    await client.send_photo(
        chat_id=message.chat.id,
        photo=kick_image_url,
        caption=f"🥾 **[{user_a.first_name}](tg://user?id={user_a.id})** kicked **[{user_b.first_name}](tg://user?id={user_b.id})**! That must've hurt! 💥",
        parse_mode=ParseMode.MARKDOWN
    )

# Command handler for /kill
@bot.on_message(filters.command("kill") & filters.group)
async def kill_command(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply_text("𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝘂𝘀𝗲𝗿'𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗼𝗿 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝘁𝗼 𝗸𝗶𝗹𝗹 𝘁𝗵𝗲𝗺.")
        return

    user_a = message.from_user

    if message.reply_to_message:
        user_b = message.reply_to_message.from_user
    else:
        username = message.command[1]
        try:
            user_b = await client.get_users(username)
        except Exception as e:
            await message.reply_text(f"Could not find user {username}.")
            return

    # Check if the bot is being killed
    bot_id = (await client.get_me()).id
    if user_b.id == bot_id:
        await message.reply_text("You can't kill a bot! 🛡️")
        return

    if user_a.id == user_b.id:
        await message.reply_text("You can't kill yourself. That's a bit dramatic.")
        return

    # Get a random kill image URL
    kill_image_url = random.choice(KILL_IMAGES)

    # Send the kill message with the image
    await client.send_photo(
        chat_id=message.chat.id,
        photo=kill_image_url,
        caption=f"💀 **[{user_a.first_name}](tg://user?id={user_a.id})** has killed **[{user_b.first_name}](tg://user?id={user_b.id})**! 😱",
        parse_mode=ParseMode.MARKDOWN
    )

# Command handler for /kiss
@bot.on_message(filters.command("kiss") & filters.group)
async def kiss_command(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply_text("𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝘂𝘀𝗲𝗿'𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗼𝗿 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗮 𝗸𝗶𝘀𝘀 𝗿𝗲𝗾𝘂𝗲𝘀𝘁.")
        return

    user_a = message.from_user

    if message.reply_to_message:
        user_b = message.reply_to_message.from_user
    else:
        username = message.command[1]
        try:
            user_b = await client.get_users(username)
        except Exception as e:
            await message.reply_text(f"Could not find user {username}.")
            return

    # Check if the bot is replying to its own message
    bot_id = (await client.get_me()).id
    if user_b.id == bot_id:
        await message.reply_text("Fuck off, I don't want a kiss from you.")
        return

    if user_a.id == user_b.id:
        await message.reply_text("Why are you single? You know, nowadays everyone is committed except you!")
        return

    # Create inline button for User B to accept
    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("𝗔𝗰𝗰𝗲𝗽𝘁", callback_data=f"accept_kiss:{user_a.id}:{user_b.id}")]
        ]
    )

    # Send the kiss request message
    await message.reply_text(
        f"💞 **[{user_b.first_name}](tg://user?id={user_b.id})** see **[{user_a.first_name}](tg://user?id={user_a.id})** wants to kiss you! 💞\n\n"
        "Will you accept the kiss?",
        reply_markup=inline_keyboard,
        parse_mode=ParseMode.MARKDOWN
    )

# Callback handler for accepting the kiss
@bot.on_callback_query(filters.regex(r"^accept_kiss:(\d+):(\d+)$"))
async def accept_kiss_callback(client: Client, callback_query):
    data = callback_query.data.split(":")
    user_a_id = int(data[1])
    user_b_id = int(data[2])

    user_a = await client.get_users(user_a_id)
    user_b = await client.get_users(user_b_id)

    if callback_query.from_user.id != user_b.id:
        await callback_query.answer("𝗕𝘀𝗱𝗸 𝗼𝗻𝗹𝘆 𝘁𝗵𝗲 𝗿𝗲𝗰𝗶𝗽𝗶𝗲𝗻𝘁 𝗰𝗮𝗻 𝗮𝗰𝗰𝗲𝗽𝘁 𝘁𝗵𝗶𝘀 𝗸𝗶𝘀𝘀 𝗿𝗲𝗾𝘂𝗲𝘀𝘁.", show_alert=True)
        return

    # Get a random kiss image URL
    kiss_image_url = random.choice(KISS_IMAGES)

    # Delete the acceptance message with the inline button
    await callback_query.message.delete()

    # Send the kiss accepted message with the image
    await client.send_photo(
        chat_id=callback_query.message.chat.id,
        photo=kiss_image_url,
        caption=f"💓 **[{user_b.first_name}](tg://user?id={user_b.id})** accepted the kiss from **[{user_a.first_name}](tg://user?id={user_a.id})**! 💓",
        parse_mode=ParseMode.MARKDOWN
    )

    await callback_query.answer()

# Command handler for /pat
@bot.on_message(filters.command("pat") & filters.group)
async def pat_command(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply_text("𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝘂𝘀𝗲𝗿'𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗼𝗿 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝘁𝗼 𝗽𝗮𝘁 𝘁𝗵𝗲𝗺.")
        return

    user_a = message.from_user

    if message.reply_to_message:
        user_b = message.reply_to_message.from_user
    else:
        username = message.command[1]
        try:
            user_b = await client.get_users(username)
        except Exception as e:
            await message.reply_text(f"Could not find user {username}.")
            return

    # Check if the bot is being patted
    bot_id = (await client.get_me()).id
    if user_b.id == bot_id:
        await message.reply_text("You can't pat a bot, but thanks for the gesture! 🤖")
        return

    if user_a.id == user_b.id:
        await message.reply_text("You can't pat yourself. You deserve pats from others!")
        return

    # Get a random pat image URL
    pat_image_url = random.choice(PAT_IMAGES)

    # Send the pat message with the image
    await client.send_photo(
        chat_id=message.chat.id,
        photo=pat_image_url,
        caption=f"🤗 **[{user_a.first_name}](tg://user?id={user_a.id})** gave a warm pat to **[{user_b.first_name}](tg://user?id={user_b.id})**! So sweet! 💖",
        parse_mode=ParseMode.MARKDOWN
    )


# Command handler for /sex
@bot.on_message(filters.command("sex") & filters.group)
async def sex_command(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply_text("𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝘂𝘀𝗲𝗿'𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗼𝗿 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗮 𝘀𝗲𝘅 𝗿𝗲𝗾𝘂𝗲𝘀𝘁.")
        return

    user_a = message.from_user

    if message.reply_to_message:
        user_b = message.reply_to_message.from_user
    else:
        username = message.command[1]
        user_b = await client.get_users(username)

    # Check if the bot is the target of the request
    bot_id = (await client.get_me()).id
    if user_b.id == bot_id:
        await message.reply_text("Fuck off, I don't want to have sex with you.")
        return

    if user_a.id == user_b.id:
        await message.reply_text("Why are you single? You know, nowadays everyone is committed except you!")
        return

    # Create inline button for User B to accept
    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("𝗔𝗰𝗰𝗲𝗽𝘁", callback_data=f"accept_sex:{user_a.id}:{user_b.id}")]
        ]
    )

    # Send the sex request message
    await message.reply_text(
        f"💞 **[{user_b.first_name}](tg://user?id={user_b.id})** see **[{user_a.first_name}](tg://user?id={user_a.id})** wants to have sex with you! 💞\n\n"
        "Will you accept?",
        reply_markup=inline_keyboard,
        parse_mode=ParseMode.MARKDOWN
    )

# Callback handler for accepting the sex request
@bot.on_callback_query(filters.regex(r"^accept_sex:(\d+):(\d+)$"))
async def accept_sex_callback(client: Client, callback_query):
    data = callback_query.data.split(":")
    user_a_id = int(data[1])
    user_b_id = int(data[2])

    user_a = await client.get_users(user_a_id)
    user_b = await client.get_users(user_b_id)

    if callback_query.from_user.id != user_b.id:
        await callback_query.answer("Only the recipient can accept this sex request.", show_alert=True)
        return

    # Get a random sex image URL
    sex_image_url = random.choice(SEX_IMAGES)

    # Delete the acceptance message with the inline button
    await callback_query.message.delete()

    # Send the sex accepted message with the image
    await client.send_photo(
        chat_id=callback_query.message.chat.id,
        photo=sex_image_url,
        caption=f"💓 **[{user_b.first_name}](tg://user?id={user_b.id})** had done sex with **[{user_a.first_name}](tg://user?id={user_a.id})**! 💓\n\nWhat do you think will they have a baby ?..",
        parse_mode=ParseMode.MARKDOWN
    )

    await callback_query.answer()



# Command handler for /slap
@bot.on_message(filters.command("slap") & filters.group)
async def slap_command(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        await message.reply_text("𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝘂𝘀𝗲𝗿'𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗼𝗿 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝘁𝗼 𝘀𝗹𝗮𝗽 𝘁𝗵𝗲𝗺.")
        return

    user_a = message.from_user

    if message.reply_to_message:
        user_b = message.reply_to_message.from_user
    else:
        username = message.command[1]
        try:
            user_b = await client.get_users(username)
        except Exception as e:
            await message.reply_text(f"Could not find user {username}.")
            return

    # Check if the bot is being slapped
    bot_id = (await client.get_me()).id
    if user_b.id == bot_id:
        await message.reply_text("Hey, don't slap me! I'm just a bot.")
        return

    if user_a.id == user_b.id:
        await message.reply_text("You cannot slap yourself. That's weird.")
        return

    # Get a random slap image URL
    slap_image_url = random.choice(SLAP_IMAGES)

    # Send the slap message with the image
    await client.send_photo(
        chat_id=message.chat.id,
        photo=slap_image_url,
        caption=f"👋 **[{user_a.first_name}](tg://user?id={user_a.id})** slapped **[{user_b.first_name}](tg://user?id={user_b.id})**! That must've hurt! 💥",
        parse_mode=ParseMode.MARKDOWN
    )

