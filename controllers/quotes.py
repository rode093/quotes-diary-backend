from lib.responseBuilder import Response
from schema.quotes import Quotes
from models.quote import Quote
from mongoengine import DoesNotExist
from fastapi import APIRouter
from slugify import slugify
router = APIRouter()

@router.get('/')
async def index():
    quotes = Quotes.objects    
    return Response.sendResponse({"quotes": list(map(lambda x: x.get, quotes))})
    # return Response.sendResponse({"quotes": list( quotes)})

@router.get('/details/{slug}')
async def generateSlug(slug: str):
    try :
        quote= Quotes.objects(slug__exact=slug)[:1]
        quote=list(map(lambda x: x.get, quote))
        return Response.sendResponse({"quote":quote })
    except DoesNotExist:
        return Response.sendResponse({"result": "Not Found"}, 404)
    except:
        return Response.sendResponse({"result": "Server Error"}, 500)
    
@router.patch('/{slug}')
async def update(slug: str, quote:Quote):
    try :
        print(quote)
        return Response.sendResponse({"quote":quote })
    except DoesNotExist:
        return Response.sendResponse({"result": "Not Found"}, 404)
    except:
        return Response.sendResponse({"result": "Server Error"}, 500)
    
@router.put('/create')
async def create( quote:Quote):
    try :
        quote = Quotes(
            text=quote.text,
            author=quote.author
        )
        quote.create()
        return Response.sendResponse({"quote":quote })
    except DoesNotExist:
        return Response.sendResponse({"result": "Not Found"}, 404)
    # except:
    #     return Response.sendResponse({"result": "Server Error"}, 500)
    
