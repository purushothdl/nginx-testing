# Auth Service

Handles user registration, login, and JWT token generation.

## Setup
1. Ensure `.env` has your `MONGODB_URL` and `SECRET_KEY`.
2. Build and run with Docker:
   ```bash
   docker build -t auth_service .
   docker run -d -p 8000:8000 --env-file .env auth_service