# coding: utf-8  
  
from mongoengine import *  
#from mongoengine import fields

connect('douguo')  
  
class UserRef(Document):  
    #meta = {'allow_inheritance': True}
    meta = {'abstract': True,'id_field':'id'}
    #meta = {'abstract': True}
    #meta = {'id_field': 'id'}
    id = ObjectIdField()

    uid = IntField(unique=True)
    #id = IntField()
    #头像url
    head_img = StringField()
    #昵称
    name = StringField()
    gender = IntField(default=0)
    #积分
    score = IntField()
    #area = ReferenceField(Area)
    #简介
    intro = StringField()
    #喜欢
    #TODO:暂存品牌和产品的url,以后有需要再建相应集合去抓数据
    like_brand = ListField(StringField())
    like_product = ListField(StringField())
    crawled_time = DateTimeField()
    is_crawled = IntField(default=0)


class User(UserRef):  

    from Comment import CommentRef
    from Dish import DishRef
    from Recipe import RecipeRef
    from Diet import DietRef
    from Comment import CommentRef
    from Cookbook import CookbookRef
    from Area import Area
    from Title import Title
    from Ask import AskRef
    from Answer import AnswerRef
    #头衔
    title = ReferenceField(Title)
    #title = ReferenceField(Document)
    area = ReferenceField(Area)
    #关注uid
    follow = ListField(ReferenceField(UserRef))
    #follow = ListField(ReferenceField(Document))
    #粉丝uid
    fans = ListField(ReferenceField(UserRef))
    #fans = ListField(ReferenceField(Document))
    #收藏的菜谱
    fav_cookbook  = ListField(ReferenceField(CookbookRef))
    #fav_cookbook  = ListField(ReferenceField(Document))
    #收藏的菜单
    fav_recipe  = ListField(ReferenceField(RecipeRef))
    #fav_recipe  = ListField(ReferenceField(Document))
    #他的问题
    questions = ListField(ReferenceField(AskRef))
    #questions = ListField(ReferenceField(Document))
    #他的回答
    answers = ListField(ReferenceField(AnswerRef))
    #answers = ListField(ReferenceField(Document))
    #留言
    comments = ListField(ReferenceField(CommentRef))
    #comments = ListField(ReferenceField(Document))
    #菜谱 
    cookbooks = ListField(ReferenceField(CookbookRef))
    #cookbooks = ListField(ReferenceField(Document))
    #菜单
    recipes = ListField(ReferenceField(RecipeRef))
    #recipes = ListField(ReferenceField(Document))
    #作品
    dishes = ListField(ReferenceField(DishRef))
    #dishes = ListField(ReferenceField(Document))
    #日记
    diets = ListField(ReferenceField(DietRef))
    #diets = ListField(ReferenceField(Document))
