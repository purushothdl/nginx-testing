from fastapi import APIRouter, Depends, HTTPException
from app.domain.schemas.user_schema import UserCreate, UserOut
from app.domain.schemas.token_schema import Token
from app.domain.services.auth_service import AuthService
from app.dependencies.service_dependencies import get_auth_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register_user(
    user: UserCreate, 
    auth_service: AuthService = Depends(get_auth_service)):
    user_id = await auth_service.register(user)
    return {"id": user_id, "email": user.email}

@router.post("/login", response_model=Token)
async def login_user(
    email: str,
    password: str,
    auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.login(email, password)