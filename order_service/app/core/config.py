from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    DATABASE_NAME: str = "NginxTesting"  

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()