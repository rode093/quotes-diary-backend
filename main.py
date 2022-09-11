from lib.mongodb import MongoDB
from models.quotes import Quotes
from fastapi import FastAPI
from dotenv import dotenv_values

from lib.responseBuilder import Response

config = dotenv_values(".env")
if(config):
    print("Configuration Loaded")

dbConnection= MongoDB(config)

app = FastAPI()



@app.get("/")
async def index():
    quotes = Quotes.objects
       
    return Response.sendResponse({"quotes": list(map(lambda x: x.get, quotes))})
