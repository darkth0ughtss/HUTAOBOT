import random
import os
from pyrogram import filters
from .. import app as bot
from ..imgs_config import wish_videos

# Helper function to get random wish percentage and stylish message
def generate_wish_message(wish_text):
    wish_possibility = random.randint(0, 100)
    emojis = "🌟✨"
    stylish_font = "𝒴𝑜𝓊𝓇 𝓌𝒾𝓈𝒽"
    return f"{stylish_font} : {wish_text}\n\n𝒲𝒾𝓈𝒽 𝒫𝑜𝓈𝓈𝒾𝒷𝒾𝓁𝒾𝓉𝒾𝑒𝓈 : {wish_possibility}% {random.choice(emojis)}"

# Command Handler: Wish Command
@bot.on_message(filters.command("wish"))
async def wish_command(client, message):
    if len(message.command) < 2:
        await message.reply("𝗣𝗹𝗲𝗮𝘀𝗲 𝘂𝘀𝗲 𝘁𝗵𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗹𝗶𝗸𝗲 𝘁𝗵𝗶𝘀: /𝘄𝗶𝘀𝗵 '𝗬𝗼𝘂𝗿 𝘄𝗶𝘀𝗵'")
        return
    
    wish_text = " ".join(message.command[1:])
    
    # Get a random wish video URL
    wish_video_url = random.choice(wish_videos)
    
    # Generate the wish message
    wish_message = generate_wish_message(wish_text)
    
    # Send the wish video and the wish message
    await message.reply_video(wish_video_url, caption=wish_message)
