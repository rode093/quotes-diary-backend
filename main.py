from lib.mongodb import MongoDB
from fastapi import FastAPI
from dotenv import dotenv_values
from fastapi.middleware.cors import CORSMiddleware
from controllers import quotes

config = dotenv_values(".env")
if(config):
    print("Configuration Loaded")

dbConnection= MongoDB(config)

app = FastAPI()
#configure cors middleware
origins = [
    "*",
]
app.add_middleware(CORSMiddleware, allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

#setup roputer
app.include_router(quotes.router, prefix="/quotes")