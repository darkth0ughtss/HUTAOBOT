from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import HuTao.key as key
import uuid

text_storage = {}

def store_text(text):
    text_id = str(uuid.uuid4())
    text_storage[text_id] = text
    return text_id

def get_font_buttons(text_id):
    buttons = [
        [
            InlineKeyboardButton("𝐁𝐎𝐋𝐃", callback_data=f"bold:{text_id}"),
            InlineKeyboardButton("𝘐𝘛𝘈𝘓𝘐𝘊", callback_data=f"italic:{text_id}"),
            InlineKeyboardButton("U̲N̲D̲E̲R̲L̲I̲N̲E̲", callback_data=f"underline:{text_id}")
        ],
        [
            InlineKeyboardButton("sᴍᴀʟʟᴄᴀᴘs", callback_data=f"small_caps:{text_id}"),
            InlineKeyboardButton("𝔻𝕆𝕌𝔹𝕃𝔼 𝕊𝕋ℝ𝕌ℂ𝕂", callback_data=f"double_struck:{text_id}"),
            InlineKeyboardButton("𝐼𝑇𝐴𝐿𝐼𝑪 𝑆𝐸𝑅𝐼𝐹", callback_data=f"italic_serif:{text_id}")
        ],
        [
            InlineKeyboardButton("𝘽𝙊𝙇𝘿 𝙄𝙏𝘼𝙇𝙄𝘾", callback_data=f"bold_italic:{text_id}"),
            InlineKeyboardButton("𝙼𝙾𝙽𝙾𝚂𝙿𝙰𝙲𝙴", callback_data=f"monospace:{text_id}"),
            InlineKeyboardButton("🅸🅽🆅🅴🆁🆃🅴🅳 🆂🆀🆄🅰🆁🅴🆂", callback_data=f"inverted_squares:{text_id}")
        ],
        [
            InlineKeyboardButton("ᖴᗩ丅 丅ᗴ᙭丅", callback_data=f"fat_text:{text_id}"),
            InlineKeyboardButton("ＷＩＤＥ ＴＥＸＴ", callback_data=f"wide_text:{text_id}"),
            InlineKeyboardButton("卂丂丨卂几 丂丅ㄚ㇄乇", callback_data=f"asian_style:{text_id}")
        ],
        [
            InlineKeyboardButton("ˢᵁᴾᴱᴿ ˢᶜᴿᴵᴾᵀ", callback_data=f"super_script_small:{text_id}"),
            InlineKeyboardButton("ʟᴜɴɪ ᴛᴏᴏʟ", callback_data=f"luni_tool:{text_id}"),
            InlineKeyboardButton("ⒸⒾⓇⒸⓊⓁⒶⓇ", callback_data=f"circular:{text_id}")
        ],
        [
            InlineKeyboardButton("🇸🇰🇾🇧🇱🇺🇪", callback_data=f"skyblue:{text_id}"),
            InlineKeyboardButton("SQƲΙƓƓLƐ", callback_data=f"squiggle:{text_id}"),
            InlineKeyboardButton("S̶T̶R̶I̶K̶E̶ T̶H̶R̶O̶U̶G̶H̶", callback_data=f"strike_through:{text_id}")
        ],
        [
            InlineKeyboardButton("ᑕOᗰIᑕ", callback_data=f"comic:{text_id}"),
            InlineKeyboardButton("F༙R༙O༙Z༙E༙N༙", callback_data=f"frozen:{text_id}"),
            InlineKeyboardButton("MIXED FONTS NO EMOJIS", callback_data=f"mixed_fonts_no_emojis:{text_id}")
        ],
        [
            InlineKeyboardButton("EMOJI ALPHABET", callback_data=f"emoji_alphabet:{text_id}"),
            InlineKeyboardButton("MIXED FONTS", callback_data=f"mixed_fonts:{text_id}"),
            InlineKeyboardButton("MIXED FONTS EMOJIS", callback_data=f"mixed_fonts_emojis:{text_id}")
        ],
    ]
    return InlineKeyboardMarkup(buttons)

def apply_font(style, text):
    if style == "small_caps":
        return key.map_text(key.small_caps, text)
    elif style == "double_struck":
        return key.map_text(key.double_struck, text)
    elif style == "bold":
        return key.map_text(key.bold, text)
    elif style == "italic":
        return key.map_text(key.italic, text)
    elif style == "bold_italic":
        return key.map_text(key.bold_italic, text)
    elif style == "monospace":
        return key.map_text(key.monospace, text)
    elif style == "inverted_squares":
        return key.map_text(key.inverted_squares, text)
    elif style == "fat_text":
        return key.map_text(key.fat_text, text)
    elif style == "wide_text":
        return key.map_text(key.wide_text, text)
    elif style == "asian_style":
        return key.map_text(key.asian_style, text)
    elif style == "super_script_small":
        return key.map_text(key.super_script_small, text)
    elif style == "luni_tool":
        return key.map_text(key.luni_tool, text)
    elif style == "circular":
        return key.map_text(key.circular, text)
    elif style == "skyblue":
        return key.map_text(key.skyblue, text)
    elif style == "italic_serif":
        return key.map_text(key.italic_serif, text)
    elif style == "squiggle":
        return key.map_text(key.squiggle, text)
    elif style == "strike_through":
        return key.map_text(key.strike_through, text)
    elif style == "comic":
        return key.map_text(key.comic, text)
    elif style == "frozen":
        return key.map_text(key.frozen, text)
    elif style == "underline":
        return key.map_text(key.underline, text)
    elif style == "emoji_alphabet":
        return key.map_text(key.emoji_alphabet, text)
    elif style == "mixed_fonts":
        return key.map_text(key.mixed_fonts, text)
    elif style == "mixed_fonts_emojis":
        return key.map_text(key.mixed_fonts_emojis, text)
    elif style == "mixed_fonts_no_emojis":
        return key.map_text(key.mixed_fonts_no_emojis, text)
    else:
        return text
