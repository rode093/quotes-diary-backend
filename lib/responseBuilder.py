from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
class Response:
    @staticmethod
    def sendResponse(responseData, responseCode=200):
       content = jsonable_encoder(responseData)
       return JSONResponse(content=content, status_code=responseCode)
