# BOT/handlers/pin_handler.py

import os
import shutil
from pyrogram import filters
from .. import app as bot
from ..features.pin import download_pinterest_media

# Feature: Download Pinterest media
@bot.on_message(filters.command("pnt") & filters.private)
async def pin_command(client, message):
    if len(message.command) < 2:
        await message.reply("❌ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐩𝐫𝐨𝐯𝐢𝐝𝐞 𝐚 𝐏𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐥𝐢𝐧𝐤. 𝐔𝐬𝐚𝐠𝐞: /𝐩𝐢𝐧 '𝐩𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭_𝐥𝐢𝐧𝐤'")
        return
    
    pin_url = message.command[1]
    user_id = message.from_user.id
    message_id = message.id
    download_path = f"downloads/{user_id}_{message_id}"
    os.makedirs(download_path, exist_ok=True)
    
    downloading_message = await message.reply("📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐡𝐞 𝐏𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐦𝐞𝐝𝐢𝐚, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...")

    try:
        # Download the Pinterest media
        media_path = download_pinterest_media(pin_url, download_path)
        
        if media_path:
            # Send the media file to the user
            if media_path.lower().endswith(('mp4', 'mkv', 'webm')):
                await client.send_video(chat_id=message.chat.id, video=media_path)
            else:
                await client.send_photo(chat_id=message.chat.id, photo=media_path)
            
            # Delete the media file from the local storage
            os.remove(media_path)
        else:
            await message.reply("❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐭𝐡𝐞 𝐏𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐦𝐞𝐝𝐢𝐚. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐥𝐢𝐧𝐤 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧.")
    
    except Exception as e:
        await message.reply("❌ 𝐀𝐧 𝐞𝐫𝐫𝐨𝐫 𝐨𝐜𝐜𝐮𝐫𝐫𝐞𝐝")

    # Delete the downloading message
    await client.delete_messages(chat_id=message.chat.id, message_ids=[downloading_message.id])

    # Clean up the download directory
    shutil.rmtree(download_path)
