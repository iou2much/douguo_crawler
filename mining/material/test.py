#-*-coding:utf-8-*-
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba.posseg as pseg

words = [u'高筋面粉', u'淡奶油', u'低筋粉', u'高筋粉']

for i in xrange(len(words)):
    a = words[i]
    a = pseg.cut(a)
    a = nltk.Text(' '.join([ '%s/%s'%(w.word,w.flag) for w in a]))
    #a = nltk.Text(' '.join([ '%s'%w.word for w in a]))
    words[i] = a
    print a
#for w in a:
#    print '%s/%s'%(w.word,w.flag)
#print a
    #print ' '.join(w)
na = words[0]
print str(na)
print(str(words[3]))
print na.similar(str(words[3]))









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
