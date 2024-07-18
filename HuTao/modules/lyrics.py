# BOT/handlers/lyrics_handler.py

import logging
from pyrogram import Client, filters
import lyricsgenius
from ..config import genius_api_token
from .. import app as bot 

# Initialize the Genius client
genius = lyricsgenius.Genius(genius_api_token)

logger = logging.getLogger(__name__)

@bot.on_message(filters.command("lyrics"))
def lyrics_handler(client, message):
    try:
        song_title = " ".join(message.command[1:])
        if not song_title:
            message.reply_text("⚠️ Please provide a song title after the command, e.g., /lyrics Hello by Adele")
            return

        song = genius.search_song(song_title)
        if song:
            message.reply_text(f"🎵 Lyrics for {song.title} by {song.artist}:\n\n{song.lyrics}")
        else:
            message.reply_text("❌ Sorry, I couldn't find the lyrics for that song.")
    except Exception as e:
        logger.error(f"Error fetching lyrics: {e}")
        message.reply_text("⚠️ An error occurred while fetching the lyrics. Please try again later.")


__mod__ = "LYRICS"