#-*-coding:utf-8 -*-
if __name__=='__main__':
    import os,sys
    sys.path.append(os.environ['DOUGUO_BASE'])

from orm.MaterialItem import MaterialItem 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#import json
#import pandas as pd
#import re
#import nltk
#import jieba
#import jieba.posseg as pseg

data = MaterialItem.objects()
user_dict = open('user.dict','a')
for m in data:
    user_dict.write('%s 3\n'%m.name)
user_dict.close()
