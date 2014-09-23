#-*-coding:utf-8-*-
from Category import Category 
from Cookbook import Cookbook 
from Category import Category 

import sys

cookbooks = Cookbook.objects(is_crawled=1)#.only('pk','is_crawled','item_id')
#print cookbooks
for cb in cookbooks.as_pymongo() :
    #print cb
    c = Cookbook.objects(item_id=cb['item_id']).only('pk','is_crawled','item_id')[0]
    print c
    print c.item_id
    print c.pk
    print c.id
    print c.is_crawled
    c.is_crawled = 0
    try:
        c.save()
    except:
        pass
