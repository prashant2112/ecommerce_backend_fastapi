from fastapi import FastAPI 
from src.routers import products, orders
# from app.database import connect_to_mongo

app= FastAPI()



app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])


