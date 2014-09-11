#-*-coding:utf-8-*-
import json
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Droid Sans Fallback']

_materials = json.loads(open('../data/materials.json','r').read())
materials = [{'name':u'%s'%m,'count':len(_materials[m])} for m in _materials if len(_materials[m])>=10]

df = pd.DataFrame(materials).sort(columns='count',ascending=True)

fig = df.plot(kind='barh',legend=False,fontsize=6).get_figure()
plt.yticks(xrange(df.count()[0]), df['name'])
plt.xlabel(u'使用次数')
plt.ylabel(u'食材')
plt.title(u'全部作品中各食材的使用次数')
fig.savefig('out.png')
