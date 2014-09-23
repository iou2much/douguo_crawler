# coding: utf-8  
  
from mongoengine import *  
connect('douguo')
  
#user agent
class Agent(Document):  
    name = StringField(unique=True)
