from motor.motor_asyncio import AsyncIOMotorClient
from ..config import MONGO_URL
from pymongo import ASCENDING
import asyncio
from sys import exit as exiter
from pymongo import MongoClient
from pymongo.errors import PyMongoError

client = AsyncIOMotorClient(MONGO_URL)
db_name = "WAIFUBOT"  # Replace with your actual database name
DBNAME = "HUTAO"
db = client[db_name]
dbname = client[DBNAME]


async def setup_indexes():
    await db.chats.create_index([("chat_id", ASCENDING)], unique=True)
    await db.users.create_index([("user_id", ASCENDING)], unique=True)

# To ensure indexes are created when starting the app
asyncio.get_event_loop().run_until_complete(setup_indexes())



