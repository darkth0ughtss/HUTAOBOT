import os
from playwright.async_api import async_playwright
from pyrogram import Client, filters
from pyrogram.types import Message

from .. import app as bot 

async def take_screenshot(url, path):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
        page = await browser.new_page()
        await page.goto(url, wait_until='networkidle')
        await page.screenshot(path=path, full_page=True)
        await browser.close()

@bot.on_message(filters.command("ss"))
async def screenshot_handler(client, message):
    try:
        # Check if a URL is provided
        if len(message.command) < 2:
            await message.reply_text("❌ Please provide a URL.")
            return

        raw_url = message.text.split(" ", 1)[1]

        # Prepend "https://" if not present
        if not raw_url.startswith("http://") and not raw_url.startswith("https://"):
            url = f"https://{raw_url}"
        else:
            url = raw_url

        screenshot_path = f"{raw_url.replace('http://', '').replace('https://', '').replace('/', '_')}.png"

        await take_screenshot(url, screenshot_path)

        await message.reply_photo(screenshot_path)
        os.remove(screenshot_path)
    except Exception as e:
        await message.reply_text(f"❌ An error occurred: {str(e)}")
