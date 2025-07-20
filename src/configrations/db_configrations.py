from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import motor.motor_asyncio

MONGO_URI = "mongodb+srv://ptprashant21:3vkrwSdNSHLBQ7cq@cluster0.auxeyt7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

db = client.sample_cart
products_collection = db.get_collection("products")
orders_collection = db.get_collection("orders")  