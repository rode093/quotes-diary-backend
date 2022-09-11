from math import frexp
from urllib import request


from mongoengine import *

class Quotes(DynamicDocument):
    text=StringField(max_length=512, required=True)
    author=StringField(max_length=64, required=False)
    
    @property
    def get(self):
        return {
            "text": self.Text,
            "author": self.Author if hasattr(self, "Author") else None
        }