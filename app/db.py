import os

from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = f"mongodb+srv://connectabilityhelp:{os.getenv('db_pass')}@connectabilitydata.rpu7i0b.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['ConnectAbilityData']