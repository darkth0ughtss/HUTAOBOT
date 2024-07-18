from .. import app as bot
from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
from ..config import MONGO_URL, OWNER_ID  # Ensure config is correct and OWNER_ID is a list of IDs
import random

# Initialize MongoDB client
mongo_client = MongoClient(MONGO_URL)
db = mongo_client["THE-BOT"]
users_collection = db["USERS"]
groups_collection = db["GROUPS"]

@bot.on_message(filters.command("botinfo") & filters.user(OWNER_ID))
async def botinfo_handler(client: Client, message: Message):
    try:
        total_users = users_collection.count_documents({})
        total_groups = groups_collection.count_documents({})
        await message.reply_text(f"TOTAL NUMBER OF USERS: {total_users}\nTOTAL NUMBER OF GROUPS: {total_groups}")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

@bot.on_message(filters.new_chat_members)
async def new_group_handler(client: Client, message: Message):
    chat_id = message.chat.id
    chat_title = message.chat.title

    # Save group chat ID and title to the GROUPS collection
    if not groups_collection.find_one({"chat_id": chat_id}):
        groups_collection.insert_one({"chat_id": chat_id, "title": chat_title})

async def send_dice_response(client: Client, message: Message, emoji: str):
    try:
        await client.send_dice(
            chat_id=message.chat.id,
            emoji=emoji,
            reply_to_message_id=message.id
        )
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

@bot.on_message(filters.command("ludo"))
async def ludo_handler(client: Client, message: Message):
    await send_dice_response(client, message, "🎲")

@bot.on_message(filters.command("dart"))
async def dart_handler(client: Client, message: Message):
    await send_dice_response(client, message, "🎯")

@bot.on_message(filters.command("bowl"))
async def bowl_handler(client: Client, message: Message):
    await send_dice_response(client, message, "🎳")

@bot.on_message(filters.command("football"))
async def football_handler(client: Client, message: Message):
    await send_dice_response(client, message, "⚽")

@bot.on_message(filters.command("basket"))
async def basket_handler(client: Client, message: Message):
    await send_dice_response(client, message, "🏀")

@bot.on_message(filters.command("slot"))
async def slot_handler(client: Client, message: Message):
    await send_dice_response(client, message, "🎰")

# New commands

@bot.on_message(filters.command("runs"))
async def runs_handler(client: Client, message: Message):
    responses = ["You scored a six!", "It's a four!", "You got out!", "Single run!", "Double runs!"]
    await message.reply_text(random.choice(responses))

@bot.on_message(filters.command("insult"))
async def insult_handler(client: Client, message: Message):
    insults = ["You're as bright as a black hole, and twice as dense.", "You bring everyone a lot of joy when you leave the room.", "I'd agree with you but then we'd both be wrong."]
    if message.reply_to_message:
        await message.reply_text(random.choice(insults), reply_to_message_id=message.reply_to_message.message_id)
    else:
        await message.reply_text(random.choice(insults))

@bot.on_message(filters.command("shrug"))
async def shrug_handler(client: Client, message: Message):
    await message.reply_text("¯\\_(ツ)_/¯")

@bot.on_message(filters.command("decide"))
async def decide_handler(client: Client, message: Message):
    decisions = ["Yes", "No", "Maybe"]
    await message.reply_text(random.choice(decisions))

@bot.on_message(filters.command("toss"))
async def toss_handler(client: Client, message: Message):
    toss_result = ["Heads", "Tails"]
    await message.reply_text(random.choice(toss_result))

@bot.on_message(filters.command("yes"))
async def yes_handler(client: Client, message: Message):
    await message.reply_text("Yes, check yourself :V")

@bot.on_message(filters.command("no"))
async def no_handler(client: Client, message: Message):
    await message.reply_text("No, check yourself :V")

@bot.on_message(filters.command("shout"))
async def shout_handler(client: Client, message: Message):
    if len(message.command) > 1:
        text_to_shout = message.text.split(None, 1)[1]
        await message.reply_text(text_to_shout.upper())
    else:
        await message.reply_text("Please provide a text to shout.")

