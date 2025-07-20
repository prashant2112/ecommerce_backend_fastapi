from src.configrations.db_configrations import orders_collection,products_collection
from src.database.schemas import page_details, order_post, order_get
from src.database.models import Order, CreateOrder, OrderDetails, ProductDetails
from bson import ObjectId
from typing import Optional
from fastapi import Query

async def create_order_services(order_request: CreateOrder):
    # Process order
    product_ids = []
    product_qty_map = {}
    for item in order_request.items:
        product_ids.append(ObjectId(item.productId))
        product_qty_map[item.productId] = item.qty
    print(product_ids)
    total = 0.0
    order_details_list = []
    product_query = {"_id":{"$in": product_ids}}
    print(product_query)
    product_list = await products_collection.find(product_query).to_list()
    print(product_list)
    for product in product_list:
        # Todos:
        """ avoiding the size based quantity check for now beacouse the order request dosen't have a size field"""
        # check quantity
        # Create OrderDetails
        # apeend to order_details_list
        # reduce product quantity
        # update product

        # calculate price of the product
        product_id = str(product["_id"])
        order_qty = product_qty_map[product_id]
        Order_price = product["price"]
        # add to total
        total = total + (Order_price * order_qty)
        
        # create and append order details
        product_name = product["name"]

        product_details = ProductDetails(name=product_name, id=product_id)

        order_details = OrderDetails(productdetails=product_details, qty=order_qty)
        print(order_details)

        order_details_list.append(order_details)

    new_order = Order(userId=order_request.userId, items=order_details_list, total=total)
    added = await orders_collection.insert_one(new_order.model_dump(by_alias=True))
    return added



async def get_orders_service(
    user_id: str,
    limit: Optional[int] = Query(10),
    offset: Optional[int] = Query(0)
):
    query={"userId": user_id}
    responce = await orders_collection.find(query).skip(offset).limit(limit).to_list()
    return responce