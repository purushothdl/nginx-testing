from fastapi import FastAPI
from app.core.error_handler import add_exception_handlers
from app.core.log_config import setup_logging
from app.domain.routes.user_routes import router as user_router

# Setup logging
setup_logging()

app = FastAPI(title="User Service")

add_exception_handlers(app)

app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "User Service is running"}