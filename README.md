# Ecommerce Backend FastAPI App

This is a FastAPI-based backend for an e-commerce application. It provides RESTful APIs for managing products and orders, using MongoDB as the database (via Motor async driver).

## Features
- **Product Management**: Create and search products with size and quantity options.
- **Order Management**: Place orders for products and retrieve order history.
- **Pagination**: List endpoints support pagination with `limit` and `offset`.

## Project Structure
```
src/
  main.py                # FastAPI entrypoint
  configrations/
    db_configrations.py  # MongoDB connection and collections
  database/
    models.py            # Pydantic models for Product, Order, etc.
    schemas.py           # Serialization/deserialization helpers
  routers/
    products.py          # Product-related API routes
    orders.py            # Order-related API routes
  service/
    orderservice.py      # Business logic for orders
    productservice.py    # (Empty, placeholder for product logic)
```

## API Endpoints

### Products
- `POST /products/` — Create a new product
- `GET /products/` — Search products (by name, size, with pagination)

### Orders
- `POST /orders/` — Place a new order
- `GET /orders/` — List orders (with pagination)

## Database
- Uses MongoDB (collections: `products`, `orders`)
- Connection configured in `src/configrations/db_configrations.py`

## Requirements
See `requirements.txt` for all dependencies. Key packages:
- fastapi
- motor
- pymongo
- pydantic
- uvicorn

## Running the App
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn src.main:app --reload
   ```

## Model Schemas

### Product
```python
class Product(BaseModel):
    name: str
    price: float
    sizes: list[Sizes]

class Sizes(BaseModel):
    size: SizeEnum  # 'small', 'medium', 'large'
    quantity: int
```

### Order
```python
class Order(BaseModel):
    userId: str
    items: list[OrderDetails]
    total: float

class OrderDetails(BaseModel):
    productdetails: ProductDetails
    qty: int

class ProductDetails(BaseModel):
    name: str
    id: str
```

### Create Order Request
```python
class CreateOrder(BaseModel):
    userId: str
    items: list[CreateOrderDetails]

class CreateOrderDetails(BaseModel):
    productId: str
    qty: int
```

## Notes
- MongoDB connection string is set in `db_configrations.py`.
- The app is modular, with routers and services separated for scalability.
- Extend `service/productservice.py` for advanced product logic.

---
**Author:** prashant2112
