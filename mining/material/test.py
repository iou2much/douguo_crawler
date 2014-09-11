#-*-coding:utf-8-*-
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba.posseg as pseg

a = u'高筋面粉'
b = u'淡奶油'
c = u'低筋粉'
d = u'高筋粉'

a = pseg.cut(a)
for w in a:
    print '%s/%s'%(w.word,w.flag)
    #print ' '.join(w)
#na = nltk.Text(a)
#print na.similar(d)









#if __name__ == '__main__':
#    import sys,os
#    dir_name = os.path.dirname(__file__) if os.path.dirname(__file__)!='' else '.'
#    sys.path.append(dir_name + '/../..')
#
#from config import CONFIG
#from orm.Material import Material
#def echo():
#    print CONFIG
#    print open(CONFIG['DATA_PATH']+'materials.json','r').read()
##echo()
#
#print Material.objects.only('name')[0].name
#print Material.objects()[0].amount
