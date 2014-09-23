# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  

class AskRef(Document):  
    meta = {'allow_inheritance': True}
    a_id = IntField(unique=True)
    publish_time = DateTimeField()
    crawled_time = DateTimeField()
    follow_num = IntField()
    content = StringField()

class Ask(AskRef):  
    from User import UserRef
    from Cookbook import CookbookRef 
    from Answer import AnswerRef
    publisher = ReferenceField(UserRef)
    answers = ListField(ReferenceField(AnswerRef))
    cookbook = ReferenceField(CookbookRef)
