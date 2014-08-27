#-*-coding:utf-8-*-
from nltk.corpus import udhr
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import nltk

languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

cfd = nltk.ConditionalFreqDist( 
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))
for word in udhr.words('English-Latin1'):
    print word

#cfd.plot(cumulative=True)




#_matters = json.loads(open('data/matters.json','r').read())
#for m in _matters:
#    print m ,len(_matters[m])
#    break
#matters = {m:_matters[m] for m in _matters if len(_matters[m])>40}
#
#cfd = nltk.ConditionalFreqDist((name, len(matters[name])) for name in matters)
#cfd.plot(cumulative=True)
