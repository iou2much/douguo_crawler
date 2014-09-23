# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  

class AnswerRef(Document):  
    meta = {'allow_inheritance': True}
    a_id = IntField(unique=True)
    publish_time = DateTimeField()
    crawled_time = DateTimeField()
    content = StringField()
class Answer(AnswerRef):  
    from User import UserRef
    from Cookbook import CookbookRef 
    from Ask import AskRef
    from Comment import CommentRef
    comments = ReferenceField(CommentRef)
    ask  = ReferenceField(AskRef)
    publisher = ReferenceField(UserRef)
    cookbokk = ReferenceField(CookbookRef)
