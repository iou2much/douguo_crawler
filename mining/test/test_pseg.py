#-*-coding:utf-8-*-
if __name__=='__main__':
    import os,sys
    sys.path.append(os.environ['DOUGUO_BASE'])
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from config import CONFIG


import jieba
jieba.load_userdict(CONFIG['DICT_PATH']+"jieba_user.dict")

import jieba.posseg as pseg

print pseg.cut(u'新鲜').next()
