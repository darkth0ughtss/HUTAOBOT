# BOT/utils/whisper.py

import shortuuid
from pymongo import MongoClient
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.raw import types
from pyrogram.enums import ParseMode
from ..config import MONGO_URL, bot_token
from .. import app as Client 
# Initialize MongoDB client
client = MongoClient(MONGO_URL)
db = client["THE-BOT"]
collection = db["whispers"]

# Whispers Class
class Whispers:
    @staticmethod
    def add_whisper(WhisperId, WhisperData):
        whisper = {"WhisperId": WhisperId, "whisperData": WhisperData}
        collection.insert_one(whisper)

    @staticmethod
    def del_whisper(WhisperId):
        collection.delete_one({"WhisperId": WhisperId})

    @staticmethod
    def get_whisper(WhisperId):
        whisper = collection.find_one({"WhisperId": WhisperId})
        return whisper["whisperData"] if whisper else None

# Function to parse user message
def parse_user_message(query_text):
    text = query_text.split(" ")
    user = text[0]
    first = True
    message = ""

    if not user.startswith("@") and not user.isdigit():
        user = text[-1]
        first = False

    if first:
        message = " ".join(text[1:])
    else:
        text.pop()
        message = " ".join(text)

    return user, message

# Inline query handler
@Client.on_inline_query()
async def mainwhisper(client, inline_query):
    query = inline_query.query
    if not query:
        return await inline_query.answer(
            [],
            switch_pm_text="Give me a username or ID!",
            switch_pm_parameter="ghelp_whisper",
        )

    user, message = parse_user_message(query)
    if len(message) > 200:
        return

    usertype = "username" if user.startswith("@") else "id"

    if user.isdigit():
        try:
            chat = await client.get_chat(int(user))
            user = f"@{chat.username}" if chat.username else chat.first_name
        except Exception:
            pass

    whisperData = {
        "user": inline_query.from_user.id,
        "withuser": user,
        "usertype": usertype,
        "type": "inline",
        "message": message,
    }
    whisperId = shortuuid.uuid()

    # Add the whisper to the database
    Whispers.add_whisper(whisperId, whisperData)

    answers = [
        InlineQueryResultArticle(
            id=whisperId,
            title=f"🤫 Send a whisper message to {user}!",
            description="Only they can see it!",
            input_message_content=InputTextMessageContent(
                f"<b>🔒 A Whisper Message For {user}</b>\nOnly they can see it!",
                parse_mode=ParseMode.HTML
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "💌 𝗦𝗵𝗼𝘄 𝗪𝗵𝗶𝘀𝗽𝗲𝗿 💌",
                            callback_data=f"whisper_{whisperId}",
                        )
                    ]
                ]
            ),
        )
    ]

    await inline_query.answer(answers)

# Callback query handler
@Client.on_callback_query(filters.regex(r"whisper_"))
async def showWhisper(client, callback_query):
    whisperId = callback_query.data.split("_")[-1]
    whisper = Whispers.get_whisper(whisperId)

    if not whisper:
        await callback_query.answer("This whisper is not valid anymore!", show_alert=True)
        return

    userType = whisper["usertype"]
    from_user_id = callback_query.from_user.id

    if from_user_id == whisper["user"]:
        await callback_query.answer(whisper["message"], show_alert=True)
    elif (
        userType == "username"
        and callback_query.from_user.username
        and callback_query.from_user.username.lower()
        == whisper["withuser"].replace("@", "").lower()
    ):
        await callback_query.answer(whisper["message"], show_alert=True)
    elif userType == "id" and from_user_id == int(whisper["withuser"]):
        await callback_query.answer(whisper["message"], show_alert=True)
    else:
        await callback_query.answer("Not your Whisper!", show_alert=True)


