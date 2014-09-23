# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
  
#class Cookbook(EmbeddedDocument):
class CookbookRef(Document):
    meta = {'abstract': True}

    item_id = IntField(unique=True)
    name = StringField()
    #TODO:与Material/MaterialItem 集合未关联
    material = ListField(DictField())
    tip = StringField()
    steps = ListField(StringField())
    view_count = IntField(default=0)
    fav_count = IntField(default=0)
    publish_time = StringField()
    crawled_time = StringField()
    cost_time = StringField()

    is_crawled = IntField()

    #publisher = ReferenceField(Document)
    #user_agent = ReferenceField(Document)
    #comments = ListField(ReferenceField(Document))
    #dishes = ListField(ReferenceField(Document))
    #level = ReferenceField(Document)

class CookbookTest(CookbookRef):

    from User import UserRef
    from Comment import CommentRef
    from Dish import DishRef
    from Agent import Agent
    from Level import Level

    publisher = ReferenceField(UserRef)
    user_agent = ReferenceField(Agent)
    comments = ListField(ReferenceField(CommentRef))
    dishes = ListField(ReferenceField(DishRef))
    level = ReferenceField(Level)
