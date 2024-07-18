# handlers/help_handler.py

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery , InputMediaPhoto
from ..imgs_config import help_command_urls
import random
from .. import app as Client
from ..info import *
FEATURES = [
    "𝗔𝗡𝗜𝗠𝗘",
    "𝐀𝐃𝐌𝐈𝐍𝐒",
    "𝐀𝐅𝐊",
    "𝐀𝐏𝐏𝐑𝐎𝐕𝐄",
    "𝐁𝐀𝐍𝐒",
    "𝗖𝗢𝗦𝗣𝗟𝗔𝗬",
    "𝗖𝗢𝗨𝗣𝗟𝗘",
    "𝗖𝗥𝗜𝗖𝗞𝗘𝗧",
    "𝗙𝗢𝗡𝗧",
    "𝗣𝗜𝗡𝗧𝗘𝗥𝗘𝗦𝗧",
    "𝗦𝗘𝗔𝗥𝗖𝗛",
    "𝗦𝗣𝗢𝗧𝗜𝗙𝗬",
    "𝐆𝐈𝐓",
    "𝐈𝐌𝐏𝐎𝐒𝐓𝐄𝐑",
    "𝐌𝐈𝐒𝐂",
    "𝐌𝐔𝐓𝐄𝐒",
    "𝐏𝐔𝐑𝐆𝐄",
    "𝐒𝐖𝐄𝐋𝐂𝐎𝐌𝐄",
    "𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗣𝗛",
    "𝗧𝗥𝗔𝗡𝗦𝗟𝗔𝗧𝗘",
    "𝗧𝗧𝗦",
    "𝗗𝗜𝗖𝗧𝗜𝗢𝗡𝗔𝗥𝗬",
    "𝗪𝗔𝗜𝗙𝗨",
    "𝗬𝗧",        
    "𝗦𝗢𝗡𝗚",        
    "𝗙𝗨𝗡",  
    "𝗨𝗧𝗜𝗟𝗦",   
    "𝗪𝗜𝗦𝗣𝗛𝗘𝗥", 
    "𝗟𝗬𝗥𝗜𝗖𝗦",  
    "𝗪𝗘𝗕𝗦𝗦",    
    "𝗠𝗔𝗧𝗛",  
    "𝗣𝗢𝗞𝗘𝗗𝗘𝗫"

]

FEATURE_DETAILS = {
    "𝗔𝗡𝗜𝗠𝗘": ANIME , 
    "𝐀𝐃𝐌𝐈𝐍𝐒": ADMINS , 
    "𝐀𝐅𝐊": AFK ,
    "𝐀𝐏𝐏𝐑𝐎𝐕𝐄": APPROVE ,
    "𝐁𝐀𝐍𝐒": BANS , 
    "𝗖𝗢𝗦𝗣𝗟𝗔𝗬": "Get a random cosplay photo with /cosplay.",
    "𝗖𝗢𝗨𝗣𝗟𝗘": "Pair random members as couples for the day with /couple, /couples, or /shipping.",
    "𝗖𝗥𝗜𝗖𝗞𝗘𝗧": "Fetch upcoming cricket match details with /cricket. Includes title, date, teams, venue, and next match button.",
    "𝗙𝗢𝗡𝗧": "Apply font styles to text with /font 'text'. Use inline buttons for styles.",
    "𝗣𝗜𝗡𝗧𝗘𝗥𝗘𝗦𝗧": "Download Pinterest media with /pnt 'link'.",
    "𝗦𝗘𝗔𝗥𝗖𝗛": "Search news, web, and images with /bingsearch and /img. Use /news for keyword-based news.",
    "𝗦𝗣𝗢𝗧𝗜𝗙𝗬": "Access Spotify features with commands like /top_playlist, /sp_daily, /sp_trending, etc.",
    "𝐆𝐈𝐓": "Use /git username - to get the info of that user's github account.",
    "𝐈𝐌𝐏𝐎𝐒𝐓𝐄𝐑": IMPOSTER , 
    "𝐌𝐈𝐒𝐂": MISC ,
    "𝐌𝐔𝐓𝐄𝐒": MUTES , 
    "𝐏𝐔𝐑𝐆𝐄": PURGE ,
    "𝐒𝐖𝐄𝐋𝐂𝐎𝐌𝐄": SWELCOME ,
    "𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗣𝗛": "Upload replied media to Telegraph with /tgm.",
    "𝗧𝗥𝗔𝗡𝗦𝗟𝗔𝗧𝗘": "Translate text with /tr 'target_lang'. Detects and translates from replied text.",
    "𝗧𝗧𝗦": "Convert text to speech (TTS) in English with /tts 'text'.",
    "𝗗𝗜𝗖𝗧𝗜𝗢𝗡𝗔𝗥𝗬": "Search Urban Dictionary with /ud 'term' for definitions.",
    "𝗪𝗔𝗜𝗙𝗨": "Fetch random SFW waifu images with /waifu.",
    "𝗬𝗧": "Download YouTube videos with /yt 'link'.",
    "𝗦𝗢𝗡𝗚": "Search and download songs from YouTube with /song 'name'.",
    "𝗨𝗧𝗜𝗟𝗦": "You can use commands like /kiss /hug /sex /kickk /slap in group chats.",
    "𝗪𝗜𝗦𝗣𝗛𝗘𝗥": "Send private whispers '@botusername' in any chat to activate inline queries.",
    "𝗟𝗬𝗥𝗜𝗖𝗦": "Fetch song lyrics with /lyrics 'song_name'.",
    "𝗪𝗘𝗕𝗦𝗦": "Take screenshots of websites with /ss 'website_link'.",
    "𝗠𝗔𝗧𝗛": "Perform math operations with commands like /add, /substract, /multiply, etc.",
    "𝗣𝗢𝗞𝗘𝗗𝗘𝗫": "Get details about a Pokemon with /pokedex 'pokemon_name'."
}


BUTTONS_PER_PAGE = 12
BUTTONS_PER_ROW = 3

def get_feature_buttons(page=0):
    start = page * BUTTONS_PER_PAGE
    end = start + BUTTONS_PER_PAGE
    features = FEATURES[start:end]

    buttons = []
    for i in range(0, len(features), BUTTONS_PER_ROW):
        buttons.append([InlineKeyboardButton(features[j], callback_data=f"feature_{start + j}") for j in range(i, min(i + BUTTONS_PER_ROW, len(features)))])

    pagination_buttons = []
    if page > 0:
        pagination_buttons.append(InlineKeyboardButton("𝑷𝑹𝑬𝑽𝑰𝑶𝑼𝑺", callback_data=f"paginate_{page - 1}"))
    if end < len(FEATURES):
        pagination_buttons.append(InlineKeyboardButton("𝑵𝑬𝑿𝑻", callback_data=f"paginate_{page + 1}"))

    if pagination_buttons:
        buttons.append(pagination_buttons)

    return buttons


@Client.on_message(filters.command("help"))
async def help_command(client, message):

    # Delete the /start command message sent by the user
    await message.delete()

    buttons = get_feature_buttons()
    caption = "𝘏𝘌𝘙𝘌 𝘐𝘚 𝘛𝘏𝘌 𝘓𝘐𝘚𝘛 𝘖𝘍 𝘈𝘓𝘓 𝘍𝘌𝘈𝘛𝘜𝘙𝘌𝘚"

    # Select a random image URL
    image_url = random.choice(help_command_urls)

    await client.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex(r"^feature_"))
async def feature_callback(client, callback_query: CallbackQuery):
    feature_index = int(callback_query.data.split("_")[1])
    feature = FEATURES[feature_index]
    details = FEATURE_DETAILS.get(feature, "No details available for this feature.")
    await callback_query.message.edit_caption(
        caption=details,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="help_back")]])
    )

@Client.on_callback_query(filters.regex(r"^paginate_"))
async def paginate_callback(client, callback_query: CallbackQuery):
    page = int(callback_query.data.split("_")[1])
    buttons = get_feature_buttons(page)
    await callback_query.message.edit_caption(
        caption="𝘏𝘌𝘙𝘌 𝘐𝘚 𝘛𝘏𝘌 𝘓𝘐𝘚𝘛 𝘖𝘍 𝘈𝘓𝘓 𝘍𝘌𝘈𝘛𝘜𝘙𝘌𝘚",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex(r"^help_back"))
async def help_back_callback(client, callback_query: CallbackQuery):
    buttons = get_feature_buttons()
    await callback_query.message.edit_caption(
        caption="𝘏𝘌𝘙𝘌 𝘐𝘚 𝘛𝘏𝘌 𝘓𝘐𝘚𝘛 𝘖𝘍 𝘈𝘓𝘓 𝘍𝘌𝘈𝘛𝘜𝘙𝘌𝘚",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex(r"^commands"))
async def commands_callback(client, callback_query: CallbackQuery):
    buttons = get_feature_buttons()
    caption = "𝘏𝘌𝘙𝘌 𝘐𝘚 𝘛𝘏𝘌 𝘓𝘐𝘚𝘛 𝘖𝘍 𝘈𝘓𝘓 𝘍𝘌𝘈𝘛𝘜𝘙𝘌𝘚"

    # Select a random image URL
    image_url = random.choice(help_command_urls)

    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=image_url, caption=caption),
        reply_markup=InlineKeyboardMarkup(buttons)
    )