from ..db import db
from pymongo import DESCENDING

async def add_user(user_id, username):
    user = await db.users.find_one({"user_id": user_id})
    if not user or user["username"] != username:
        await db.users.update_one(
            {"user_id": user_id},
            {"$set": {"username": username, "score": 0, "played": 0}},
            upsert=True
        )
        return True
    return False

async def id_to_username(user_id):
    user = await db.users.find_one({"user_id": user_id})
    if user:
        return user["username"]
    return None

async def add_score(user_id, score):
    await db.users.update_one(
        {"user_id": user_id},
        {"$inc": {"score": score, "played": 1}}
    )

async def get_top_users():
    return await db.users.find().sort("score", DESCENDING).limit(10).to_list(None)

async def get_user(user_id):
    return await db.users.find_one({"user_id": user_id})

async def get_all_users():
    return await db.users.find().to_list(None)
