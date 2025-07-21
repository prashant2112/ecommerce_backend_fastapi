from fastapi import APIRouter,HTTPException
from src.configrations.db_configrations import products_collection
from src.database.schemas import product_post, product_get, page_details
from src.database.models import Product, SizeEnum
from typing import Optional
from fastapi import Query

async def Create_Product_service(new_product: Product):
    # Validate product data
    added = await products_collection.insert_one(new_product.model_dump(by_alias=True))
    return added


async def search_products_service(
    name: Optional[str] = Query(None),
    size: Optional[SizeEnum] = Query(None),
    limit: Optional[int] = Query(10),
    offset: Optional[int] = Query(0)
):
    # Validate search parameters
    query = {}
    if name:
        query["name"] = { "$regex": f".*{name}.*"}
    if size:
        query["sizes.size"] = sizeS
    # Fetch products from the database
    responce = await products_collection.find(query).skip(offset).limit(limit).to_list()
    return responce