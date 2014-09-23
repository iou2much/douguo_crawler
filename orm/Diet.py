# coding: utf-8  
  
from mongoengine import *  

connect('douguo')  
  
#Embedded to Cookbook
class DietRef(Document):  
    meta = {'allow_inheritance': True}
    dietid = IntField(unique=True)
    publish_time = DateTimeField()
    #c_id = IntField()
    crawled_time = DateTimeField()
    position = StringField()
    content = StringField()

    #comments = ListField(ReferenceField(Document))
    #publisher = ReferenceField(Document)
    #like_by = ListField(ReferenceField(Document))
    #user_agent = ReferenceField(Document)

class Diet(DietRef):  
    from User import UserRef
    from Agent import Agent
    from Comment import CommentRef 
    comments = ListField(ReferenceField(CommentRef))
    publisher = ReferenceField(UserRef)
    like_by = ListField(ReferenceField(UserRef))
    user_agent = ReferenceField(Agent)
