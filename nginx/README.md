# NGINX API Gateway

Handles routing, load balancing, and JWT validation.

## Setup
- Built and orchestrated via `docker-compose.yml` in the project root.
- Requires `SECRET_KEY` in `nginx/.env` for JWT validation (HS256).

## Features
- Routes `/auth/` to Auth Service (no JWT check).
- Routes `/users/` to User Service (with load balancing, JWT required).
- Routes `/orders/` to Order Service (with load balancing, JWT required).