from enum import unique
from math import frexp
from typing_extensions import Required
from urllib import request
from models.quote import Quote
from mongoengine import *
from lib.slug import *
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
    def create(self):
        
        self.generateSlug()
     
        self.save()
        return self
    
    def generateSlug(self):
        self.slug = generateSlug(self.text)
        
        