# Order Service

Manages basic order operations (create, read, delete).

## Setup
1. Ensure `.env` has your `MONGODB_URL` and `SECRET_KEY`.
2. Build and run with Docker:
   ```bash
   docker build -t order_service .
   docker run -d -p 8000:8000 --env-file .env order_service