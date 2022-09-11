from lib.mongodb import MongoDB
from models.quotes import Quotes
from fastapi import FastAPI
from dotenv import dotenv_values

from routes import quotes

config = dotenv_values(".env")
if(config):
    print("Configuration Loaded")

dbConnection= MongoDB(config)

app = FastAPI()

app.include_router(quotes.router)