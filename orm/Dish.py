# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
#Embedded to Cookbook
class DishRef(Document):
    meta = {'allow_inheritance': True}
    d_id = IntField(unique=True)
    publish_time = DateTimeField()
    crawled_time = DateTimeField()
    image = StringField()
    content = StringField()

    #publisher = ReferenceField(Document)
    #cookbook = ReferenceField(Document)
    #user_agent = ReferenceField(Document)
    #like_by = ListField(ReferenceField(Document))
    #comments = ListField(ReferenceField(Document))


class Dish(DishRef):
    from Comment import CommentRef
    from User import UserRef
    from Agent import Agent
    from Cookbook import CookbookRef 

    publisher = ReferenceField(UserRef)
    cookbook = ReferenceField(CookbookRef)
    user_agent = ReferenceField(Agent)
    like_by = ListField(ReferenceField(UserRef))
    comments = ListField(ReferenceField(CommentRef))
