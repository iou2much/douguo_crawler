# coding: utf-8  

from mongoengine import *  
connect('douguo')  
  
class CommentRef(Document):  
    #未必取得到id
    meta = {'allow_inheritance': True}

    cid = IntField()
    content = StringField()
    crawled_time = DateTimeField()

class Comment(CommentRef):  
    from User import UserRef
    publisher = ReferenceField(UserRef)
    #??这里用unique_with 会否出问题
    publish_time = DateTimeField(unique_with='publisher')
