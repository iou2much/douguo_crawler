#-*-coding:utf-8-*-
from Category import Category 
from Cookbook import Cookbook 
from Category import Category 

import sys

cookbooks = Cookbook.objects()
cats = Category.objects()
total = 0
for c in cats:
    print c.name, c.count,c.url
    total += c.count
#print total
sys.exit()

for c in cats:
    c.count = 0
    c.save()

for cb in cookbooks :
    #去重
    if len(cb.category) != len(set(cb.category)):
        cb.category = list(set(cb.category))
        cb.save()
        print 'save'

    #计算各分类cookbook数
    for c in cb.category:
        if c.count is None:
            c.count = 0
        c.count += 1
        print c.name,c.count
        c.save()
