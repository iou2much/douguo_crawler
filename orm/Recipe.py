# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
 
class RecipeRef(Document):  
    meta = {'allow_inheritance': True}
    item_id = IntField(unique=True)
    name = StringField()
    intro = StringField()
    create_time = DateTimeField()
    edit_time = DateTimeField()
    crawled_time = DateTimeField()
    view_num = IntField()
    fav_num = IntField()
    #comments = ReferenceField(Document)
    #publisher = ReferenceField(Document)
    #cookbook = ListField(ReferenceField(Document))

class Recipe(RecipeRef):  
    from Cookbook import CookbookRef
    from User import UserRef 
    from Comment import CommentRef 
    comments = ReferenceField(CommentRef)
    publisher = ReferenceField(UserRef)
    cookbook = ListField(ReferenceField(CookbookRef))
