#-*-coding:utf-8 -*-
if __name__=='__main__':
    import os,sys
    sys.path.append(os.environ['DOUGUO_BASE'])

from config import CONFIG
from orm.Material import Material

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import pandas as pd
import re
import nltk
import jieba
import jieba.posseg as pseg

data = Material.objects()

units = []
_units = {}
all_amount = {}
known_units = set([u'个',u'种',u'個',u'大个'])
for material in data:
    amounts = material.amount

    if material.name not in all_amount:
        all_amount[material.name] = {'name':material.name,'amount':0.0,'unit':set(),'count':0}

    for amount in amounts:
        #对分词成3个以上的，暂时忽略，如"1/4个",会拆成 "1" "/" "4" "个"
        if len(amount)>2:continue
        all_amount[material.name]['count']+=1
        for a in amount :
            if 'm' != a[u'flag'] or a[u'word'] in known_units:
                _units[a[u'word']]=a[u'flag']
                units.append(a[u'word'])
                all_amount[material.name]['unit'].add(a[u'word'])
            else:
                try:
                    all_amount[material.name]['amount']+=float(a[u'word'])
                except:
                    all_amount[material.name]['unit'].add(a[u'word'])
                    known_units.add(a[u'word'])

df = pd.DataFrame([all_amount[n] for n in all_amount]).sort(columns='amount',ascending=False)
df['unit'] = df['unit'].apply(list)

#for words in df['name'].apply(pseg.cut):
#    for word in words:
#        print word
#    print '='*50
#导出json
df.to_csv('material_amount.csv')
#open('result/material_amount.json','w').write(json.dumps(df.to_dict(outtype='records')))
#print df
#print json.dumps(df.to_dict(outtype='records'))
#df.plot()
#sys.exit()

#plt = nltk.FreqDist(seg_list)
#d = dict(plt)
#result = []
#name_file = open('result/names.dat','w')
#cut_name_file = open('result/cut_names.dat','w')
#for n in df['name']:
#    name_file.write('%s\n'%n)
#name_file.close()
#for key in d.keys():
#    if key.flag == 'x':continue
#    cut_name_file.write("%s : %s\n"%(key,d[key]))
#cut_name_file.close()
