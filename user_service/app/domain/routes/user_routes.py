from fastapi import APIRouter, Depends, HTTPException
from app.domain.schemas.user_schema import UserOut
from app.domain.services.user_service import UserService
from app.dependencies.service_dependencies import get_user_service
from app.dependencies.auth_dependencies import get_current_user
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/{user_id}", response_model=UserOut)
async def get_user(
    user_id: str,
    current_user: dict = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):
    # Ensure the requesting user can only access their own data
    if current_user["user_id"] != user_id:
        logger.warning(f"Unauthorized access attempt: {current_user['user_id']} tried to access {user_id}")
        raise HTTPException(status_code=403, detail="Not authorized to access this user")
    return await user_service.get_user_details(user_id)