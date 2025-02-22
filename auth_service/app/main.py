from fastapi import FastAPI
from app.core.error_handler import add_exception_handlers
from app.core.log_config import setup_logging
from app.domain.routes.auth_routes import router as auth_router

# Setup logging
setup_logging()

app = FastAPI(title="Auth Service")
add_exception_handlers(app)

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Auth Service is running"}