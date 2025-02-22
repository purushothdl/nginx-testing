from app.database.mongodb import get_database
from app.domain.repository.order_repository import OrderRepository
from app.domain.services.order_service import OrderService

def get_order_repository():
    db = get_database()
    return OrderRepository(db["orders"])

def get_order_service():
    order_repo = get_order_repository()
    return OrderService(order_repo)