from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

_client = None

def get_database():
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.MONGODB_URL)
    return _client[settings.DATABASE_NAME]  