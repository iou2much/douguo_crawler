# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
class Cookbook(Document):  
    item_id = IntField(unique=True)
    material = ListField(DictField())
    tip = StringField()  
    steps = ListField(StringField())
    view_count = IntField()
    fav_count = IntField()
    publish_time = StringField()
    user_agent = StringField()
    comments = ListField()
