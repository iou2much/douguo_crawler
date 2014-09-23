#-*-coding:utf-8-*- 

import sys
from User import User
from Comment import Comment 
from CookbookTest import CookbookTest
from CategoryTest import CategoryTest 
from datetime import datetime

q = {'name':'a'}
c = CategoryTest.objects(**q)
c = c[0]
print dir(c)
print c.url
c.url = 'url_xxxxxxxxx'
c.save()


sys.exit()
c = CategoryTest()
c.name='a'
c.url='a_url'
c.crawled_time = datetime.now()
cb1 = CookbookTest()
cb1.name = 'cb1'
cb1.item_id = 99999999999998
cb1.save()
c.cookbook.append(cb1)
res = c.save()
print c.cookbook
cb2 = CookbookTest()
cb2.name = 'cb2'
cb2.item_id = 99999999999999
cb2.save()
cb3 = CookbookTest()
cb3.name = 'cb3'
cb3.item_id = 99999999999997
cb3.save()
c.url = 'b_url' 
c.cookbook.append(cb2)
c.cookbook.append(cb3)
res = c.save()
print res


#user = User()
#user.name = 'haha'
#user.uid = 1
#comment = Comment()
#comment.uid = 1
#comment.content = 'this is comment'
#comment.publish_time = '2014-9-11 10:01:33'
#c = list()
#c.append(comment)
#user.comments = c
#user.answers = [1,2,3,55,99]
#cb = Cookbook()
#cb.item_id='9991101110'
#cb.save()
#print cb
#user.cookbook = [cb]
#user.save()
