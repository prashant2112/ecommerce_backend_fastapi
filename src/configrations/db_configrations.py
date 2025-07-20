from pydantic_settings import BaseSettings
import motor.motor_asyncio

class Settings(BaseSettings):
    mongo_uri: str = "mongodb+srv://user:pass@localhost:27017"

Settings = Settings()
# MONGO_URI = "mongodb+srv://ptprashant21:3vkrwSdNSHLBQ7cq@cluster0.auxeyt7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = motor.motor_asyncio.AsyncIOMotorClient(Settings.mongo_uri)

db = client.sample_cart
products_collection = db.get_collection("products")
orders_collection = db.get_collection("orders")  