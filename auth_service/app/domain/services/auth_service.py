from fastapi import HTTPException
from app.core.security import hash_password, create_access_token, verify_password
from app.domain.repository.user_repository import UserRepository
from app.domain.schemas.user_schema import UserCreate
import logging

logger = logging.getLogger(__name__)

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register(self, user: UserCreate) -> str:
        existing_user = await self.user_repo.get_user_by_email(user.email)
        if existing_user:
            logger.warning(f"Registration failed: Email {user.email} already exists")
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_password = hash_password(user.password)
        user_id = await self.user_repo.create_user(user.email, hashed_password)
        return user_id

    async def login(self, email: str, password: str) -> dict:
        user = await self.user_repo.get_user_by_email(email)
        if not user or not verify_password(password, user["password"]):
            logger.warning(f"Login failed for email: {email}")
            raise HTTPException(status_code=401, detail="Invalid credentials")
        access_token = create_access_token(data={"sub": user["id"]})
        return {"access_token": access_token, "token_type": "bearer"}