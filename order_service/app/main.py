from fastapi import FastAPI
from app.core.error_handler import add_exception_handlers
from app.core.log_config import setup_logging
from app.domain.routes.order_routes import router as order_router

# Setup logging
setup_logging()

app = FastAPI(title="Order Service")

add_exception_handlers(app)

app.include_router(order_router, prefix="/orders", tags=["orders"])

@app.get("/")
async def root():
    return {"message": "Order Service is running"}