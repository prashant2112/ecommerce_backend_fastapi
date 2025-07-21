from pydantic import BaseModel,Field
from enum import Enum
from typing import Annotated
from pydantic.functional_validators import BeforeValidator

# This model is defined for the ObjectId type used in MongoDB
PyObjectId = Annotated[str, BeforeValidator(str)]

# Enum for product sizes
class SizeEnum(str, Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'

# Model for product sizes
class Sizes(BaseModel):
    size: SizeEnum
    quantity: int

# Model for product details
class Product(BaseModel):
    name: str
    price: float
    sizes: list [Sizes]

# Model for product creation request
class ProductDetails(BaseModel):
    name: str
    id: str

# Model for order details
class OrderDetails(BaseModel):
    productdetails: ProductDetails
    qty: int

""" This model if defined for the order collection schema """
class Order(BaseModel):
    userId: str
    items: list [OrderDetails]
    total: float

# Model for creating an order request
class CreateOrderDetails(BaseModel):
    productId: str
    qty: int

""" This model is defined for the create order request """
class CreateOrder(BaseModel):
    userId: str
    items: list [CreateOrderDetails]
