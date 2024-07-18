
from pyrogram import filters
from pyrogram.types import InputMediaPhoto, Message
from .. import app as bot
from ..state import state
import random
import json

BINGSEARCH_URL = "https://sugoi-api.vercel.app/search"
NEWS_URL = "https://sugoi-api.vercel.app/news?keyword={}"

# /news command handler
@bot.on_message(filters.command("news"))
async def news(_, message: Message):
    keyword = message.text.split(" ", 1)[1].strip() if len(message.text.split()) > 1 else ""
    url = NEWS_URL.format(keyword)

    try:
        response = await state.get(url)
        news_data = response.json()

        if "error" in news_data:
            error_message = news_data["error"]
            await message.reply_text(f"Error: {error_message}")
        else:
            if len(news_data) > 0:
                news_item = random.choice(news_data)
                title = news_item["title"]
                excerpt = news_item["excerpt"]
                source = news_item["source"]
                relative_time = news_item["relative_time"]
                news_url = news_item["url"]
                message_text = f"𝗧𝗜𝗧𝗟𝗘: {title}\n𝗦𝗢𝗨𝗥𝗖𝗘: {source}\n𝗧𝗜𝗠𝗘: {relative_time}\n𝗘𝗫𝗖𝗘𝗥𝗣𝗧: {excerpt}\n𝗨𝗥𝗟: {news_url}"
                await message.reply_text(message_text)
            else:
                await message.reply_text("No news found.")

    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")


# /bingsearch command handler
@bot.on_message(filters.command("bingsearch"))
async def bing_search(client, message: Message):
    try:
        if len(message.command) == 1:
            await message.reply_text("𝗣𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝗸𝗲𝘆𝘄𝗼𝗿𝗱 𝘁𝗼 𝘀𝗲𝗮𝗿𝗰𝗵.")
            return

        keyword = " ".join(message.command[1:])
        params = {"keyword": keyword}

        response = await state.get(BINGSEARCH_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            if not results:
                await message.reply_text("No results found.")
            else:
                message_text = ""
                for result in results[:7]:
                    title = result.get("title", "")
                    link = result.get("link", "")
                    message_text += f"{title}\n{link}\n\n"
                await message.reply_text(message_text.strip())
        else:
            await message.reply_text("Sorry, something went wrong with the search.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")


# Command handler for the '/img' command
@bot.on_message(filters.command("img"))
async def bingimg_search(client, message: Message):
    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return await message.reply_text(
            "𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗺𝗲 𝗮 𝗾𝘂𝗲𝗿𝘆 𝘁𝗼 𝘀𝗲𝗮𝗿𝗰𝗵!"
        )  # Return error if no query is provided

    search_message = await message.reply_text("🔎")  # Display searching message

    # Send request to Bing image search API using state function
    bingimg_url = "https://sugoi-api.vercel.app/bingimg?keyword=" + text
    resp = await state.get(bingimg_url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    await message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    await search_message.delete()
    await message.delete()