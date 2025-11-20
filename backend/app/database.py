# app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MONGO_DB = "landmarks_db"

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DB]


# вспомогательная функция для ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
