from lib.responseBuilder import Response
from models.quotes import Quotes
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def index():
    quotes = Quotes.objects
    
    return Response.sendResponse({"quotes": list(map(lambda x: x.get, quotes))})
