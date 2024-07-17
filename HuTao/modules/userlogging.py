from pyrogram import filters

from HuTao import app
from HuTao.database.users_db import add_chat, add_user


@app.on_message(filters.all & filters.group, group=-10)
async def logger(client, message):
    if message.chat:
        chat_id = message.chat.id
        chat_title = message.chat.title
        await add_chat(chat_id, chat_title)

    if message.from_user:
        user_id = message.from_user.id
        username = message.from_user.username
        chat_id = message.chat.id
        chat_title = message.chat.title
        await add_user(user_id, username, chat_id, chat_title)
        await add_chat(chat_id, chat_title)
    
    if (
        message.reply_to_message
        and message.reply_to_message.from_user
    ):

        user_id = message.reply_to_message.from_user.id
        username = message.reply_to_message.from_user.username
        chat_id = message.chat.id 
        chat_title = message.chat.title
        
        await add_user(user_id, username, chat_id, chat_title)
        await add_chat(chat_id, chat_title)

    if message.forward_from:

        user_id = message.forward_from.id
        username = message.forward_from.username
    
        await add_user(user_id, username, Forwared=True)
