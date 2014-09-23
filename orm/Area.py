# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
class Area(Document):  
    province = StringField()
    city = StringField(unique_with='province')
