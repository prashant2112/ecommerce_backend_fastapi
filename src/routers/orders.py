from fastapi import APIRouter
from src.database.schemas import page_details, order_get
from src.database.models import CreateOrder
from src.service.orderservice import create_order_services,get_orders_service
from typing import Optional
from fastapi import Query

# Router for order-related endpoints
router = APIRouter()

# Endpoint to create a new order
@router.post("/", status_code=201)
async def create_order_endpoint(order_request: CreateOrder):
    added = await create_order_services(order_request)
    return {"id":str(added.inserted_id)} 

# Endpoint to get orders for a specific user
@router.get('/{user_id}')
async def get_orders(
    user_id: str,
    limit: Optional[int] = Query(10),
    offset: Optional[int] = Query(0)
):
    responce = await get_orders_service(user_id, limit, offset)  
    return {"data": [order_get(order) for order in responce],"page":[ page_details(limit,offset)]}
    