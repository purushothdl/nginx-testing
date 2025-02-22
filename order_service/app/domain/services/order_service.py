from fastapi import HTTPException
from app.domain.repository.order_repository import OrderRepository
from app.domain.schemas.order_schema import OrderCreate
import logging

logger = logging.getLogger(__name__)

class OrderService:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def create_order(self, order: OrderCreate, user_id: str) -> str:
        order_id = await self.order_repo.create_order(order.product, order.quantity, user_id)
        return order_id

    async def get_order(self, order_id: str, user_id: str) -> dict:
        order = await self.order_repo.get_order_by_id(order_id)
        if not order:
            logger.warning(f"Order not found: {order_id}")
            raise HTTPException(status_code=404, detail="Order not found")
        if order["user_id"] != user_id:
            logger.warning(f"Unauthorized access to order {order_id} by user {user_id}")
            raise HTTPException(status_code=403, detail="Not authorized to access this order")
        return order

    async def delete_order(self, order_id: str, user_id: str) -> None:
        order = await self.order_repo.get_order_by_id(order_id)
        if not order:
            logger.warning(f"Order not found: {order_id}")
            raise HTTPException(status_code=404, detail="Order not found")
        if order["user_id"] != user_id:
            logger.warning(f"Unauthorized delete attempt on order {order_id} by user {user_id}")
            raise HTTPException(status_code=403, detail="Not authorized to delete this order")
        success = await self.order_repo.delete_order(order_id)
        if not success:
            raise HTTPException(status_code=500, detail="Failed to delete order")