#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import pandas as pd
import re
import nltk
import jieba
import jieba.posseg as pseg

if sys.argv[1] in ('cookbook','materials'):
    file_name = sys.argv[1] 
else:
    print u'请输入要分析的数据'
    sys.exit()

data = json.loads(open('../data/%s.json'%file_name,'r').read())

_data = []
if file_name == 'materials':
    for d in data:
        _d = {}
        _d['name'] = d
        _d['amount'] = data[d]
        _data.append(_d)
data = _data

field = ''
if sys.argv[2] in ('steps','amount'):
    field = sys.argv[2] 
else:
    print '请输入要分析的字段'
    sys.exit()

df = pd.DataFrame(data)
steps = []
for _s in df[field]:
    step = []
    for s in _s:
        s = re.sub(r'\r\n','\n',s)
        s = re.sub(r'\t','    ',s)
        s = nltk.clean_html(re.sub(r' +',' ',s))+'\n'
        step.append(s)
    steps.append(''.join(step))
all_steps = ''.join(steps)

seg_list = pseg.cut(all_steps)
plt = nltk.FreqDist(seg_list)
d = dict(plt)
result = []
for key in d.keys():
    if key.flag == 'x':continue
    print(key,d[key])
