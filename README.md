# LittleLemon

## API Paths To Test

### Base URL
http://127.0.0.1:8000/

### Authentication
- POST /api-token-auth/
- POST /auth/token/login/
- POST /auth/token/logout/
- POST /auth/users/

### Menu Endpoints
- GET /restaurant/menu/items/
- POST /restaurant/menu/items/
- GET /restaurant/menu/items/<id>/
- PUT /restaurant/menu/items/<id>/
- PATCH /restaurant/menu/items/<id>/
- DELETE /restaurant/menu/items/<id>/

### Booking Endpoints
- GET /restaurant/booking/tables/
- POST /restaurant/booking/tables/

### Protected Request Header
Authorization: Token <your_token>