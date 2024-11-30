from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config.logger import logger
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

logger.info("Connecting to MongoDB")
load_dotenv()

class Settings(BaseSettings):
    mongodb_uri: str = os.getenv("MONGODB_URI")
    database_name: str = "studentsDB"



settings = Settings()

def get_database():
    try:
        client = MongoClient(settings.mongodb_uri)
        logger.info("Connected to mongodb successfully")
        db = client[settings.database_name]
        return db
    except ConnectionFailure as e:
        logger.error("Failed to connect to MongoDB: %s", e)
        raise
