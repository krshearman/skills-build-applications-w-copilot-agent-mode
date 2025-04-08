from pymongo import MongoClient
from django.conf import settings

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(
            host=settings.MONGO_DB_SETTINGS["HOST"],
            port=settings.MONGO_DB_SETTINGS["PORT"]
        )
        self.db = self.client[settings.MONGO_DB_SETTINGS["NAME"]]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close(self):
        self.client.close()

# Example usage:
# mongo_client = MongoDBClient()
# users_collection = mongo_client.get_collection("users")
# mongo_client.close()
