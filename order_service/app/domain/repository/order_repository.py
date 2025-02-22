from pymongo.collection import Collection
import logging
from bson.objectid import ObjectId

logger = logging.getLogger(__name__)

class OrderRepository:
    def __init__(self, orders_collection: Collection):
        self.orders_collection = orders_collection

    async def create_order(self, product: str, quantity: int, user_id: str) -> str:
        order_data = {"product": product, "quantity": quantity, "user_id": user_id}
        result = await self.orders_collection.insert_one(order_data)
        logger.info(f"Created order with ID: {result.inserted_id} for user: {user_id}")
        return str(result.inserted_id)

    async def get_order_by_id(self, order_id: str) -> dict:
        try:
            order = await self.orders_collection.find_one({"_id": ObjectId(order_id)})
            if order:
                order["id"] = str(order["_id"])
                del order["_id"]
            return order
        except Exception as e:
            logger.error(f"Invalid order ID: {order_id}, error: {str(e)}")
            return None

    async def delete_order(self, order_id: str) -> bool:
        try:
            result = await self.orders_collection.delete_one({"_id": ObjectId(order_id)})
            if result.deleted_count > 0:
                logger.info(f"Deleted order with ID: {order_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting order ID: {order_id}, error: {str(e)}")
            return False