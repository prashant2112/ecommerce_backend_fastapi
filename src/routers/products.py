from fastapi import APIRouter,HTTPException
from src.configrations.db_configrations import products_collection
from src.database.schemas import product_post, product_get, page_details
from src.database.models import Product, SizeEnum
from src.service.productservice import Create_Product_service, search_products_service
from typing import Optional
from fastapi import Query


router = APIRouter()

@router.post("/", status_code=201)
async def Create_Product(new_product: Product):
    added = await Create_Product_service(new_product)
    return {"id":str(added.inserted_id)}



@router.get("/")
async def search_products(
    name: Optional[str] = Query(None),
    size: Optional[SizeEnum] = Query(None),
    limit: Optional[int] = Query(10),
    offset: Optional[int] = Query(0)
):
    responce = await search_products_service(name, size, limit, offset)
    return {"data":[ product_get(product) for product in responce], "page":[ page_details(limit,offset) ] }
