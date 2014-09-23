#-*-coding:utf-8-*-
from Category import Category 

import sys
cats = Category.objects()
#print cats[0].cookbook
#print len(cats)
#sys.exit()
#for i in range(0,237):
zero = 0
for cat in cats:
    if len(cat.cookbook)>0:
        print len(cat.cookbook),len(set(cat.cookbook))
        #print cats[i].cookbook[0].name
        #break
    else:
        zero+=1
print '='*50
print zero
for cat in cats:
    if len(cat.cookbook)>0:
        cat.cookbook = list(set(cat.cookbook))
        cat.save()
for cat in cats:
    if len(cat.cookbook)>0:
        print len(cat.cookbook),len(set(cat.cookbook))

