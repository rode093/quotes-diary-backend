from pydantic import BaseModel
from typing import Union

class Quote(BaseModel):
    text: str
    author: Union[str, None] = None
    