from fastapi import HTTPException
from app.domain.repository.user_repository import UserRepository
import logging

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_user_details(self, user_id: str) -> dict:
        user = await self.user_repo.get_user_by_id(user_id)
        if not user:
            logger.warning(f"User not found: {user_id}")
            raise HTTPException(status_code=404, detail="User not found")
        return user