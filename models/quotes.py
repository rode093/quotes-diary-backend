from enum import unique
from math import frexp
from typing_extensions import Required
from urllib import request

from mongoengine import *

class Quotes(DynamicDocument):
    slug=StringField(max_length=48, required=True, unique=True)
    text=StringField(max_length=512, required=True)
    author=StringField(max_length=64, required=False)
    
    @property
    def get(self):
        return {
            "id": str(self.pk),
            "slug": self.slug,
            "text": self.text,
            "author": self.author if hasattr(self, "author") else None
        }
        
  