#-*-coding:utf-8-*-
import pylab
import random
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


_matters = json.loads(open('data/matters.json','r').read())
for m in _matters:
    break
matters = {m:_matters[m] for m in _matters if len(_matters[m])>40}

#x_values=[random.randint(0,1000) for x in range(10000)]
#pylab.hist(x_values,100)
#pylab.hist(matters.keys(),100)
pylab.plot(matters.keys(),[len(matters[m]) for m in matters])
pylab.xlabel('bins of size 10')
pylab.ylabel('frequency')
pylab.title('plot of 10,000 random ints 0-1000,bins of size 10')
pylab.show()
