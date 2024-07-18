import os
import asyncio
import shutil
from pyrogram import Client, filters
from .. import app as bot
from ..features.yt import download_youtube_video

# Feature: Download YouTube video
@bot.on_message(filters.command("yt") & filters.private)
async def yt_command(client, message):
    if len(message.command) < 2:
        await message.reply("𝗣𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 𝗹𝗶𝗻𝗸. 𝗨𝘀𝗮𝗴𝗲: /𝘆𝘁 '𝘆𝗼𝘂𝘁𝘂𝗯𝗲_𝗹𝗶𝗻𝗸'")
        return

    yt_url = message.command[1]
    user_id = message.from_user.id
    message_id = message.id
    download_path = f"downloads/{user_id}_{message_id}"
    os.makedirs(download_path, exist_ok=True)

    downloading_message = await message.reply("𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝘁𝗵𝗲 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 𝘃𝗶𝗱𝗲𝗼, 𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁...")

    try:
        # Download the video asynchronously
        video_path = await asyncio.to_thread(download_youtube_video, yt_url, download_path)

        # Send the video file to the user
        await client.send_video(chat_id=message.chat.id, video=video_path)

        # Delete the video file from the local storage
        os.remove(video_path)

    except Exception as e:
        await message.reply(f"𝐴𝑛 𝑒𝑟𝑟𝑜𝑟 𝑜𝑐𝑐𝑢𝑟𝑟𝑒𝑑: {e}")

    # Delete the downloading message
    await client.delete_messages(chat_id=message.chat.id, message_ids=[downloading_message.id])

    # Clean up the download directory
    shutil.rmtree(download_path)
