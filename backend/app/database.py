from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise Exception("MONGO_URL not found in .env file")

client = AsyncIOMotorClient(MONGO_URL)

db = client.hrmsdb

def get_collection(name: str):
    return db[name]