#-*-coding:utf-8 -*-
if __name__=='__main__':
    import os,sys
    sys.path.append(os.environ['DOUGUO_BASE'])

from config import CONFIG
import sys,json,re
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba
jieba.load_userdict(CONFIG['DICT_PATH']+"jieba_user.dict")
import nltk
import re,math,json


txt= u" 一 二三四 一 六 七 一 二三四 一 六 七"

cook_books = json.loads(open(CONFIG['DATA_PATH']+'winner.json','r').read())
names = []
deCstr = ur'[#＃，。《》【】（）！？★”“、：…\(\)""\'\' -’\[\]［ ］—@—™~「」_°]'
#deCstr = r'[（ ）]'
re_sub = re.compile(deCstr)
for cb in cook_books:
   #print(cb['zuone_name'].replace(u'长帝烘焙节',''))
   #names += jieba.cut(cb['zuone_name'].replace(u'长帝烘焙节',''))
   #print(re.sub(deCstr,'',cb['zuone_name'].replace(u'长帝烘焙节','').replace(u'长帝烘培节','')))
   names += jieba.cut(re.sub(deCstr,'',cb['zuone_name'].replace(u'长帝烘焙节','').replace(u'长帝烘培节','')))

#sys.exit()
clean_words = []
for w in names:
#    if w in deCstr:continue
    if len(w) == 1:continue
    clean_words.append(w)
    #if len(w) == 1:
    #    print w

t = nltk.Text(clean_words)
dist = nltk.FreqDist(t)
#print txt
#print json.dumps([{'text':d,'size':10+math.ceil(math.log(dist[d]*10)
#)} for d in dist])
print json.dumps([{'text':d,'size':20+math.sqrt(dist[d])*math.log(dist[d])} for d in dist])
#for d in dist:
#    print d,dist[d],math.ceil(math.log(dist[d]*8))
