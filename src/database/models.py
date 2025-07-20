from pydantic import BaseModel,Field
from enum import Enum
from typing import Annotated, Optional
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class SizeEnum(str, Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'

class Sizes(BaseModel):
    size: SizeEnum
    quantity: int

class Product(BaseModel):
    name: str
    price: float
    sizes: list [Sizes]

class ProductDetails(BaseModel):
    name: str
    id: str

class OrderDetails(BaseModel):
    productdetails: ProductDetails
    qty: int

""" This model if defined for the order collection schema """
class Order(BaseModel):
    userId: str
    items: list [OrderDetails]
    total: float

class CreateOrderDetails(BaseModel):
    productId: str
    qty: int

""" This model is defined for the create order request """
class CreateOrder(BaseModel):
    userId: str
    items: list [CreateOrderDetails]
