from app.database.mongodb import get_database
from app.domain.repository.user_repository import UserRepository
from app.domain.services.user_service import UserService

def get_user_repository():
    db = get_database()
    return UserRepository(db["users"])

def get_user_service():
    user_repo = get_user_repository()
    return UserService(user_repo)