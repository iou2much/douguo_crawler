# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
#cookbook level
class Level(Document):  
    level = StringField(unique=True)
