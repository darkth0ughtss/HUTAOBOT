# BOT/features/speed.py

import asyncio
import speedtest
from ..config import OWNER_ID  # Ensure OWNER_ID is correctly defined in your config

async def perform_speedtest():
    """
    Perform a speed test to measure download, upload speeds, and ping.

    Returns:
        tuple: (download_speed in Mbps, upload_speed in Mbps, ping in ms)
    """
    loop = asyncio.get_event_loop()
    s = speedtest.Speedtest()
    
    download_speed = await loop.run_in_executor(None, s.download)
    upload_speed = await loop.run_in_executor(None, s.upload)
    
    results = s.results.dict()
    download_speed = results["download"] / 10**6  # Convert from bits/s to Mbit/s
    upload_speed = results["upload"] / 10**6  # Convert from bits/s to Mbit/s
    ping = results["ping"]
    
    return download_speed, upload_speed, ping

async def handle_speedtest(client, message):
    """
    Handle the /spt command to perform a speed test.

    Args:
        client (Client): The Pyrogram client instance.
        message (Message): The message object triggering the command.

    Returns:
        None
    """
    if message.from_user.id != OWNER_ID:
        await print("Sed")
        return
    
    try:
        download_speed, upload_speed, ping = await perform_speedtest()
        
        result_message = (
            f"⚡️ 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗦𝗣𝗘𝗘𝗗: {download_speed:.2f} Mbps\n"
            f"🌿 𝗨𝗣𝗟𝗢𝗔𝗗 𝗦𝗣𝗘𝗘𝗗: {upload_speed:.2f} Mbps\n"
            f"🟢 𝗣𝗜𝗡𝗚: {ping:.2f} ms"
        )
        
        await message.reply_text(result_message)
    
    except Exception as e:
        await message.reply_text(f"𝐹𝑎𝑖𝑙𝑒𝑑 𝑡𝑜 𝑝𝑒𝑟𝑓𝑜𝑟𝑚 𝑠𝑝𝑒𝑒𝑑𝑡𝑒𝑠𝑡")
        # Optionally log the exception if you have a logging setup
        print(f"Error performing speedtest")
