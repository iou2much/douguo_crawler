import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import pandas as pd
import re
import nltk
import jieba

data = json.loads(open('../data/cookbook.json','r').read())
#df = pd.DataFrame(data[:3])
df = pd.DataFrame(data)
steps = []
for _s in df['steps']:
    step = []
    for s in _s:
        s = re.sub(r'\r\n','\n',s)
        s = re.sub(r'\t','    ',s)
        s = nltk.clean_html(re.sub(r' +',' ',s))+'\n'
        step.append(s)
    steps.append(''.join(step))
#print df['steps']
#print ''.join(steps)
all_steps = ''.join(steps)

seg_list = jieba.cut(all_steps)
#print '/ '.join(seg_list)
fdist = nltk.FreqDist(seg_list)
for m in fdist:
    print '%s : %s'%(m,fdist[m])

#cfd = nltk.ConditionalFreqDist(
#(genre, word)
#for genre in brown.categories()
#for word in brown.words(categories=genre))
