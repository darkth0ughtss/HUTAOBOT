import os
from pyrogram import filters
from .. import app as bot
from ..features import font

# Command Handler: Apply Font Style
@bot.on_message(filters.command("font"))
async def font_handler(client, message):
    text = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ""
    if not text:
        await message.reply_text("𝑃𝑙𝑒𝑎𝑠𝑒 𝑝𝑟𝑜𝑣𝑖𝑑𝑒 𝑡ℎ𝑒 𝑡𝑒𝑥𝑡. 𝑈𝑠𝑎𝑔𝑒: /𝑓𝑜𝑛𝑡 '𝑡𝑒𝑥𝑡'")
        return
    text_id = font.store_text(text)
    await message.reply_text(
        text,
        reply_markup=font.get_font_buttons(text_id),
        reply_to_message_id=message.id
    )

# Callback Query Handler: Apply Font Style
@bot.on_callback_query(filters.regex(r"^(small_caps|double_struck|italic|bold_italic|monospace|inverted_squares|fat_text|wide_text|asian_style|super_script_small|luni_tool|circular|skyblue|italic_serif|squiggle|strike_through|comic|frozen|underline|emoji_alphabet|mixed_fonts|mixed_fonts_emojis|mixed_fonts_no_emojis|bold):"))
async def font_callback(client, callback_query):
    style, text_id = callback_query.data.split(":", 1)
    text = font.text_storage.get(text_id, "")
    new_text = font.apply_font(style, text)
    await callback_query.message.edit_text(
        new_text,
        reply_markup=font.get_font_buttons(text_id)
    )
    await callback_query.answer()
