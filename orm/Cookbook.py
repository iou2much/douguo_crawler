# coding: utf-8  
  
from mongoengine import *  
#from bson import ObjectId
connect('douguo')  
  
#class Cookbook(EmbeddedDocument):
class CookbookRef(Document):
    #meta = {'allow_inheritance': True}
    #id=ObjectId()
    #id=ObjectId()

    #meta = {'abstract': True,'id_field':'item_id'}
    meta = {'abstract': True,'id_field':'id'}
    #meta = {'id_field': 'id'}
    id = ObjectIdField()
    item_id = IntField(unique=True)
    name = StringField()
    #TODO:与Material/MaterialItem 集合未关联
    main_material = ListField(DictField())
    co_material = ListField(DictField())
    tip = StringField()
    steps = ListField(StringField())
    view_count = IntField(default=0)
    fav_count = IntField(default=0)
    publish_time = StringField()
    crawled_time = StringField()
    cost_time = StringField()
    story = StringField()
    is_crawled = IntField()

class Cookbook(CookbookRef):

    from User import UserRef
    from Comment import CommentRef
    from Dish import DishRef
    from Agent import Agent
    from Level import Level
    from Category import Category

    publisher = ReferenceField(UserRef)
    user_agent = ReferenceField(Agent)
    comments = ListField(ReferenceField(CommentRef))
    dishes = ListField(ReferenceField(DishRef))
    level = ReferenceField(Level)
    category = ListField(ReferenceField(Category))
