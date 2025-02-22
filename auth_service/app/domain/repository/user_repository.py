from pymongo.collection import Collection
import logging
from bson.objectid import ObjectId

logger = logging.getLogger(__name__)

class UserRepository:
    def __init__(self, users_collection: Collection):
        self.users_collection = users_collection

    async def create_user(self, email: str, hashed_password: str) -> str:
        user_data = {"email": email, "password": hashed_password}
        result = await self.users_collection.insert_one(user_data)
        logger.info(f"Created user with ID: {result.inserted_id}")
        return str(result.inserted_id)

    async def get_user_by_email(self, email: str) -> dict:
        user = await self.users_collection.find_one({"email": email})
        if user:
            user["id"] = str(user["_id"])
            del user["_id"]
        return user

    async def get_user_by_id(self, user_id: str) -> dict:
        try:
            user = await self.users_collection.find_one({"_id": ObjectId(user_id)})
            if user:
                user["id"] = str(user["_id"])
                del user["_id"]
            return user
        except Exception as e:
            logger.error(f"Invalid user ID: {user_id}, error: {str(e)}")
            return None