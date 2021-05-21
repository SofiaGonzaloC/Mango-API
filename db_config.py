""" Flask configuration to connect to database """
from flask_pymongo import pymongo
import os

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

client = pymongo.MongoClient(
    f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@classexample0.pptb0.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
    )
db = client.dbExample0