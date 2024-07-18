from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["THE-BOT"]
afkdb = db["afk"]
couples_collection = db["couples"]

async def get_couple(chat_id, date):
    return await couples_collection.find_one({"chat_id": chat_id, "date": date})

async def save_couple(chat_id, date, couple):
    await couples_collection.update_one(
        {"chat_id": chat_id, "date": date},
        {"$set": {"c1_id": couple["c1_id"], "c2_id": couple["c2_id"]}},
        upsert=True
    )

async def is_afk(user_id: int) -> bool:
    user = await afkdb.find_one({"user_id": user_id})
    if not user:
        return False, {}
    return True, user["reason"]


async def add_afk(user_id: int, mode):
    await afkdb.update_one(
        {"user_id": user_id}, {"$set": {"reason": mode}}, upsert=True
    )


async def remove_afk(user_id: int):
    user = await afkdb.find_one({"user_id": user_id})
    if user:
        return await afkdb.delete_one({"user_id": user_id})


async def get_afk_users() -> list:
    users = afkdb.find({"user_id": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in await users.to_list(length=1000000000):
        users_list.append(user)
    return users_list
