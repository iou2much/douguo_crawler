# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
class MaterialItem(Document):  
    name = StringField()
    url = StringField()
    img = StringField()
    effect = StringField()
