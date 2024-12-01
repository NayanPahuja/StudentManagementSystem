from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config.logger import logger
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    mongodb_uri: str = os.getenv("MONGODB_URI")
    database_name: str = "studentsDB"

settings = Settings()

class MongoDB:
    _client = None
    _db = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            try:
                cls._client = MongoClient(settings.mongodb_uri)
                cls._db = cls._client[settings.database_name]
                logger.info("MongoDB connection established")
            except ConnectionFailure as e:
                logger.error("Failed to connect to MongoDB: %s", e)
                raise
        return cls._db

    @classmethod
    def close_connection(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._db = None
            logger.info("MongoDB connection closed")

def get_database():
    return MongoDB.get_client()