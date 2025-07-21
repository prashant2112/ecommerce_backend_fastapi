from fastapi import FastAPI 
from src.routers import products, orders


app= FastAPI()


# Include routers for products and orders
app.include_router(products.router, prefix="/products", tags=["Products"])
# Include orders router
app.include_router(orders.router, prefix="/orders", tags=["Orders"])


