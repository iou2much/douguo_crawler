# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  

#from Cookbook import CookbookRef
class Category(Document):  
#class Category(Document):  
    #meta = {'allow_inheritance':True}
    #meta = {'abstract':True}
    name = StringField(unique=True)
    dimension = StringField()
    url = StringField()
    crawled_time = DateTimeField()
    count = IntField()

#    cookbook = ListField(ReferenceField(CookbookRef),default=[])

#class Category(CategoryRef):  
#    from Cookbook import CookbookRef
#    cookbook = ListField(ReferenceField(CookbookRef),default=[])
