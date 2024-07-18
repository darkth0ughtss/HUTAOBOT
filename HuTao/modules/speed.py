# BOT/handlers/spt_handler.py

from pyrogram import Client, filters
from ..features import speed  # Import the speed test logic
from .. import app as bot # Import your bot instance

@bot.on_message(filters.command("spt") & filters.private)
async def speedtest_handler(client, message):
    """
    Command handler for /spt to perform a speed test.

    Args:
        client (Client): The Pyrogram client instance.
        message (Message): The message object triggering the command.

    Returns:
        None
    """
    await message.reply_text("𝗥𝘂𝗻𝗻𝗶𝗻𝗴 𝗦𝗽𝗲𝗲𝗱𝘁𝗲𝘀𝘁... 𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁.")
    await speed.handle_speedtest(client, message)
