# This file contains the schemas for the database models used in the application.
def product_post(product):
    return{
        "id": str(product["_id"])
    }
    
def product_get(product):
    return{
        "id": str(product["_id"]),
        "name":product["name"],
        "price":product["price"]
    }

def page_details(limit,offset):
    return {
        "next": offset + limit,
        "limit": limit,
        "previous": offset - limit
    }

def order_post(order):
    return{
        "id": str(order["_id"])
    }

def order_get(order):
    return{
        "id": str(order["_id"]),
        "items": (order["items"]),
        "total": (order["total"])
    }
