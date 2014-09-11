#-*-coding:utf-8 -*-
if __name__=='__main__':
    import os,sys
    sys.path.append(os.environ['DOUGUO_BASE'])

from config import CONFIG
#from orm.Material import Material
import sys,json,re
reload(sys)
sys.setdefaultencoding('utf-8')
#import jieba.posseg as pseg
import jieba

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

#YOUR_TEXT = "A tag cloud is a visual representation for text data, typically\
#used to depict keyword metadata on websites, or to visualize free form text."
YOUR_TEXT = " 一 二三四 一 六 七 一 二三四 一 六 七"

cook_books = json.loads(open(CONFIG['DATA_PATH']+'winner.json','r').read())
names = []
for cb in cook_books:
   names += jieba.cut(cb['zuone_name'])

#print ' '.join(names)
#tags = make_tags(get_tag_counts(' '.join(names)), maxsize=120)
tags = make_tags(get_tag_counts(YOUR_TEXT), maxsize=120)

create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')


#import sys
#sys.path.append('../')
#
#import jieba
#import jieba.analyse
#from optparse import OptionParser
#
#content = open(file_name, 'rb').read()
#
#tags = jieba.analyse.extract_tags(content, topK=topK)
#
#print ",".join(tags)
#
