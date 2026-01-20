from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import sys

#Global variables
client=None
inventory_collection=None

def initialize_database():
    global client
    global inventory_collection

    if client is None:
        try:
            #create mongodb client
            client=MongoClient("mongodb://localhost:27017/",
                               serverSelectionTimeoutErrorMS=3000
                               )
            # Force connection check
            client.admin.command("ping")

            #select database
            db=client["quick_commerce"]

            #select collection
            inventory_collection=db["inventory"]

            print("Database is connected successfully")

        except (ConnectionFailure, ServerSelectionTimeoutError):
            print("Error Unable to connect to MongoDB.")
            print("Make sure MongoDB service is running.")
            sys.exit(1)

        except Exception as e:
            print("Unexpected Database Error!!!:", e)
    return inventory_collection