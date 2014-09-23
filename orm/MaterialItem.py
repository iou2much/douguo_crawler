# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
class MaterialItem(Document):  
    name = StringField(unique=True)
    url = StringField()
    img = StringField()

    intro  = StringField()
    effect = StringField()
    category = StringField()
    value = StringField()
    nutrition = StringField()
    usage = StringField()
    storage = StringField()
    people = StringField()
    howtoselect = StringField()
    energy = StringField()
    select = StringField()
