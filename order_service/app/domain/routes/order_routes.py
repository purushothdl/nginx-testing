from fastapi import APIRouter, Depends, HTTPException
from app.domain.schemas.order_schema import OrderCreate, OrderOut
from app.domain.services.order_service import OrderService
from app.dependencies.service_dependencies import get_order_service
from app.dependencies.auth_dependencies import get_current_user
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/create", response_model=OrderOut)
async def create_order(
    order: OrderCreate,
    current_user: dict = Depends(get_current_user),
    order_service: OrderService = Depends(get_order_service)
):
    user_id = current_user["user_id"]
    order_id = await order_service.create_order(order, user_id)
    return {"id": order_id, "product": order.product, "quantity": order.quantity, "user_id": user_id}

@router.get("/{order_id}", response_model=OrderOut)
async def get_order(
    order_id: str,
    current_user: dict = Depends(get_current_user),
    order_service: OrderService = Depends(get_order_service)
):
    return await order_service.get_order(order_id, current_user["user_id"])

@router.delete("/{order_id}")
async def delete_order(
    order_id: str,
    current_user: dict = Depends(get_current_user),
    order_service: OrderService = Depends(get_order_service)
):
    await order_service.delete_order(order_id, current_user["user_id"])
    return {"message": "Order deleted successfully"}