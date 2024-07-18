from ..db import db

async def add_chat(chat_id):
    chat = await db.chats.find_one({"chat_id": chat_id})
    if not chat:
        await db.chats.insert_one({"chat_id": chat_id})
        return True
    return False

async def get_chat(chat_id):
    return await db.chats.find_one({"chat_id": chat_id})

async def get_all_chats():
    return await db.chats.find().to_list(None)
