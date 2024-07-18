from pyrogram import Client, filters
from telegraph import Telegraph
from .. import app


# Initialize the Telegraph API
telegraph = Telegraph()
telegraph.create_account(short_name='my_bot')


# Define a handler for /copy command with a Telegraph URL
@app.on_message(filters.command("copy") & filters.private)
async def copy_telegraph_post(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a Telegraph URL.")
        return
    
    url = message.command[1]
    
    if not url.startswith("https://telegra.ph/"):
        await message.reply_text("Invalid Telegraph URL. Please provide a valid URL.")
        return

    try:
        response = telegraph.get_page(url.split('/')[-1], return_content=True)
        
        # Extract content and title from the original post
        title = response['title']
        content = response['content']
        
        # Create a new post with a different author name
        new_author_name = "DominosXD"
        new_author_url = "https://t.me/DominosXD"
        new_post = telegraph.create_page(
            title=title,
            author_name=new_author_name,
            author_url=new_author_url,
            html_content=content
        )
        
        # Reply with the new Telegraph URL
        new_url = f"https://telegra.ph/{new_post['path']}"
        await message.reply_text(f"New post created: {new_url}")
    
    except Exception as e:
        await message.reply_text("There was an error processing the Telegraph URL. Please try again.")
