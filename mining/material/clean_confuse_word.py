#-*-coding:utf-8-*-
if __name__=='__main__':
    import os,sys
    sys.path.append(os.environ['DOUGUO_BASE'])

from config import CONFIG

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

lines = open(CONFIG['DICT_PATH']+'confuse_word','r').read().split('\n')
words = set()

for line in lines: 
    words.add(line.strip())

f= open(CONFIG['DICT_PATH']+'confuse_word2','w')
for w in words:
    print w
    if w:
        f.write(w+'\n')
f.close()
