from pydantic_settings import BaseSettings
import motor.motor_asyncio

# Database configuration settings
class Settings(BaseSettings):
    mongo_uri: str = "mongodb+srv://user:pass@localhost:27017"

Settings = Settings()

# MongoDB client and collections
client = motor.motor_asyncio.AsyncIOMotorClient(Settings.mongo_uri)

# Database name and collections
db = client.sample_cart
products_collection = db.get_collection("products")
orders_collection = db.get_collection("orders")  