from pymongo.collection import Collection
import logging
from bson.objectid import ObjectId

logger = logging.getLogger(__name__)

class UserRepository:
    def __init__(self, users_collection: Collection):
        self.users_collection = users_collection

    async def get_user_by_id(self, user_id: str) -> dict:
        try:
            user = await self.users_collection.find_one({"_id": ObjectId(user_id)})
            if user:
                user["id"] = str(user["_id"])
                del user["_id"]
                del user["password"]  
            return user
        except Exception as e:
            logger.error(f"Invalid user ID: {user_id}, error: {str(e)}")
            return None