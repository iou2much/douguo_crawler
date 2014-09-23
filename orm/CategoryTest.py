# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  

class CategoryTest(Document):  
    from CookbookTest import CookbookTest 
    dimension = StringField()
    name = StringField(unique=True)
    url = StringField()
    cookbook = ListField(ReferenceField(CookbookTest),default=[])
    crawled_time = DateTimeField()
