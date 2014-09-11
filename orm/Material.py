# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
#class Amount(Document)
#    number = IntField()
#    unit = StringField()

class Material(Document):  
    name = StringField()  
    #amount = ListField(ListField(StringField()))
    amount = ListField(ListField(DictField()))
