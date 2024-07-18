import os
import asyncio
from pyrogram import Client, filters
from ..features.ytsearch import search_song, download_audio, download_video
from .. import app as bot

@bot.on_message(filters.command("song"))
async def song_handler(client, message):
    if len(message.command) < 2:
        await message.reply_text("❌ Please specify the name of the song.")
        return

    song_name = " ".join(message.command[1:])
    await message.reply_text(f"🎵 Searching for '{song_name}' on YouTube...")

    video_info = await asyncio.to_thread(search_song, song_name)
    if not video_info:
        await message.reply_text(f"❌ Song '{song_name}' not found. Please try with a different name.")
        return

    await message.reply_text("📥 Downloading the song...")
    file_path = await asyncio.to_thread(download_audio, video_info['link'])

    if file_path and os.path.exists(file_path):
        caption = f"🎧 **Title:** {video_info['title']}\n" \
                  f"👤 **Uploader:** {video_info['uploader']}\n" \
                  f"⏱ **Duration:** {video_info['duration']}\n" \
                  f"🔗 [YouTube Link]({video_info['link']})"
        await message.reply_audio(audio=file_path, caption=caption)
        os.remove(file_path)
    else:
        await message.reply_text("❌ Failed to download the song. Please try again.")

@bot.on_message(filters.command("vsong"))
async def vsong_handler(client, message):
    if len(message.command) < 2:
        await message.reply_text("❌ Please specify the name of the song.")
        return

    song_name = " ".join(message.command[1:])
    await message.reply_text(f"🎥 Searching for '{song_name}' on YouTube...")

    video_info = await asyncio.to_thread(search_song, song_name)
    if not video_info:
        await message.reply_text(f"❌ Song '{song_name}' not found. Please try with a different name.")
        return

    await message.reply_text("📥 Downloading the video...")
    file_path = await asyncio.to_thread(download_video, video_info['link'])

    if file_path and os.path.exists(file_path):
        caption = f"🎬 **Title:** {video_info['title']}\n" \
                  f"👤 **Uploader:** {video_info['uploader']}\n" \
                  f"⏱ **Duration:** {video_info['duration']}\n" \
                  f"🔗 [YouTube Link]({video_info['link']})"
        await client.send_video(
            chat_id=message.chat.id,
            video=file_path,
            caption=caption,
            supports_streaming=True
        )
        os.remove(file_path)
    else:
        await message.reply_text("❌ Failed to download the video. Please try again.")
