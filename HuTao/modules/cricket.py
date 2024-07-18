import aiohttp
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from .. import app as bot

# API URL for cricket
CRICKET_API_URL = "https://sugoi-api.vercel.app/cricket"

class MatchManager:
    def __init__(self, api_url):
        self.api_url = api_url
        self.matches = []
        self.match_count = 0

    async def fetch_matches(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                self.matches = await response.json()

    def get_next_matches(self, count):
        next_matches = self.matches[self.match_count:self.match_count + count]
        self.match_count += count
        return next_matches

    def reset_matches(self):
        self.matches = []
        self.match_count = 0

async def get_match_text(match, sport):
    match_text = f"🏏 **{match['title']}**\n\n"
    match_text += f"🗓 *Date:* {match['date']}\n"
    match_text += f"🏆 *Team 1:* {match['team1']}\n"
    match_text += f"🏆 *Team 2:* {match['team2']}\n"
    match_text += f"🏟️ *Venue:* {match['venue']}"
    return match_text

def create_inline_keyboard():
    inline_keyboard = [
        [
            InlineKeyboardButton(
                "Next Cricket Match ➡️",
                callback_data="next_cricket_match",
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard)

cricket_manager = MatchManager(CRICKET_API_URL)

@bot.on_message(filters.command("cricket"))
async def get_cricket_matches(client: Client, message: Message):
    try:
        cricket_manager.reset_matches()
        await cricket_manager.fetch_matches()

        if not cricket_manager.matches:
            await message.reply_text("No cricket matches found.")
            return

        next_matches = cricket_manager.get_next_matches(1)
        match = next_matches[0]

        match_text = await get_match_text(match, "cricket")
        reply_markup = create_inline_keyboard()

        await message.reply_text(
            match_text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN
        )

    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

@bot.on_callback_query(filters.regex(r"^next_cricket_match$"))
async def show_next_match(client: Client, callback_query):
    try:
        if not cricket_manager.matches:
            await callback_query.answer("No more cricket matches available.")
            return

        next_matches = cricket_manager.get_next_matches(3)

        if not next_matches:
            await callback_query.answer("No more cricket matches available.")
            return

        match_text = ""
        for match in next_matches:
            match_text += await get_match_text(match, "cricket") + "\n\n"

        reply_markup = create_inline_keyboard()

        await callback_query.message.edit_text(
            match_text,
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
        await callback_query.answer()

    except Exception as e:
        await callback_query.message.reply_text(f"An error occurred: {str(e)}")

