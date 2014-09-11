import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import pandas as pd
import re
import nltk
import jieba
import jieba.posseg as pseg

data = json.loads(open('../data/cookbook.json','r').read())
df = pd.DataFrame(data[:5])
steps = []
for _s in df['steps']:
    step = []
    for s in _s:
        s = re.sub(r'\r\n','\n',s)
        s = re.sub(r'\t','    ',s)
        s = nltk.clean_html(re.sub(r' +',' ',s))+'\n'
        step.append(s)
    steps.append(''.join(step))
all_steps = ''.join(steps)

#print all_steps
seg_list = pseg.cut(all_steps)
for s in seg_list:
    print s
