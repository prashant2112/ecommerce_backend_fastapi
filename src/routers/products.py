from fastapi import APIRouter,HTTPException
from configrations.db_configrations import products_collection
from database.schemas import product_post, product_get, page_details
from database.models import Product, SizeEnum
from typing import Optional
from fastapi import Query

router = APIRouter()

@router.post("/", status_code=201)
async def Create_Product(new_product: Product):
    added = await products_collection.insert_one(new_product.model_dump(by_alias=True))
    return {"id":str(added.inserted_id)}



@router.get("/")
async def search_products(
    name: Optional[str] = Query(None),
    size: Optional[SizeEnum] = Query(None),
    limit: Optional[int] = Query(10),
    offset: Optional[int] = Query(0)
):
    query = {}

    if name:
        query["name"] = { "$regex": f".*{name}.*"}

    if size:
        query["sizes.size"] = size

    responce = await products_collection.find(query).skip(offset).limit(limit).to_list()
    return {"data":[ product_get(product) for product in responce], "page":[ page_details(limit,offset) ] }
