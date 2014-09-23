# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
class Title(Document):  
    title = StringField(unique=True)
