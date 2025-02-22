from fastapi import Header, HTTPException
from app.core.security import verify_token
import logging

logger = logging.getLogger(__name__)

async def get_current_user(x_user_id: str = Header(...)):
    """
    Extracts user_id from X-User-ID header set by NGINX after JWT validation.
    """
    if not x_user_id:
        logger.error("Missing X-User-ID header")
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"user_id": x_user_id}