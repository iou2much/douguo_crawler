# coding: utf-8  
import sys
  
from mongoengine import *  
connect('douguo')  
from LogMaterialCombine import LogMaterialCombine

#material 统计后每种食材的用量
class Material(EmbededDocument):  
    name = StringField()  
    amount = ListField(ListField(DictField()))

    __douguo_material__ = set()
    __confuse_word__ = set()
    __synonym__ = []

    @staticmethod
    def combine(mid1,mid2,intersection,check_dict=False):
        #print len(Material.__douguo_material__)
        #print 'check_dict:%s'%check_dict
        if not Material.__douguo_material__ and check_dict:
            df = open('dict/douguo_material.dict','r').read().split('\n')
            for line in df:
                if line:
                    Material.__douguo_material__.add(u'%s'%line.split(' ')[0].strip())

            df = open('dict/confuse_word_ok','r').read().split('\n')
            for line in df:
                if line:
                    Material.__confuse_word__.add(u'%s'%line.split(' ')[0].strip())

            df = open('dict/synonym.dict','r').read().split('\n')
            for line in df:
                if line:
                    #Material.__synonym__.append(line.split(' '))
                    Material.__synonym__.append([u'%s'%w for w in line.split(' ')])
        #print Material.__synonym__
        #sys.exit()

            #df.close()
        #print len(Material.__douguo_material__)
        m1 = Material.objects(id=mid1)
        #m1 = Material(id=mid1).find()
        if m1:
            m1 = m1.get(0)
        m2 = Material.objects(id=mid2)
        #m2 = Material(id=mid2).find()
        if m2:
            m2 = m2.get(0)
        if not m1 or not m2:return
        #print dir(m1)
        #print m1.count()
        #print m1.name ,m2.name
        #if m1.name is None or m2.name is None:return
        #if m1.name is None or m2.name is None:return
        
        to_m = m1 if len(m1.name)<len(m2.name) else m2
        del_m = m2 if len(m1.name)<len(m2.name) else m1
        name = u''
        #必须以这个顺序 不然字重组会乱
        for c in to_m.name:
            if c in intersection:
                name += c
        if name not in Material.__douguo_material__ and check_dict:
            open('dict/confuse_word','a').write(name+'\n')
        #print 'wtffff'
        #print len(Material.__douguo_material__)
        #print len(Material.__confuse_word__)
        #for w in Material.__douguo_material__:
        #    print w
        #for w in Material.__confuse_word__:
        #    print w
        combine___synonym__ = False
        __synonym___set = None
        #if check_dict and name not in Material.__douguo_material__ and name not in Material.__confuse_word__:
        if check_dict:
            #print name
            #print check_dict,name not in Material.__douguo_material__,name not in Material.__confuse_word__
            for ___synonym___set in Material.__synonym__:
                if m1.name in ___synonym___set and m2.name in ___synonym___set:
                    combine___synonym__ = True
                    __synonym___set = ___synonym___set 
                    #print '__synonym___set' 
                    #print __synonym___set 
                    break
            if not combine___synonym__:
                return

        if combine___synonym__:
            if name in __synonym___set:
                name = __synonym___set[0]
        to_m.name = name
        to_m.amount += del_m.amount
        to_m.save()
        del_m.delete()

        #记录哪两个记录合并
        log = LogMaterialCombine()
        log.logCombine(m1,m2)     
