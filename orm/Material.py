# coding: utf-8  
import sys
  
from mongoengine import *  
connect('douguo')  
from LogMaterialCombine import LogMaterialCombine
  
class Material(Document):  
    name = StringField()  
    amount = ListField(ListField(DictField()))
    douguo_material = set()
    confuse_word = set()
    synonym = []
    @staticmethod
    def combine(mid1,mid2,intersection,check_dict=False):
        #print len(Material.douguo_material)
        #print 'check_dict:%s'%check_dict
        if not Material.douguo_material and check_dict:
            df = open('dict/douguo_material.dict','r').read().split('\n')
            for line in df:
                if line:
                    Material.douguo_material.add(u'%s'%line.split(' ')[0].strip())

            df = open('dict/confuse_word_ok','r').read().split('\n')
            for line in df:
                if line:
                    Material.confuse_word.add(u'%s'%line.split(' ')[0].strip())

            df = open('dict/synonym.dict','r').read().split('\n')
            for line in df:
                if line:
                    #Material.synonym.append(line.split(' '))
                    Material.synonym.append([u'%s'%w for w in line.split(' ')])
        #print Material.synonym
        #sys.exit()

            #df.close()
        #print len(Material.douguo_material)
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
        if name not in Material.douguo_material and check_dict:
            open('dict/confuse_word','a').write(name+'\n')
        #print 'wtffff'
        #print len(Material.douguo_material)
        #print len(Material.confuse_word)
        #for w in Material.douguo_material:
        #    print w
        #for w in Material.confuse_word:
        #    print w
        combine_synonym = False
        synonym_set = None
        #if check_dict and name not in Material.douguo_material and name not in Material.confuse_word:
        if check_dict:
            #print name
            #print check_dict,name not in Material.douguo_material,name not in Material.confuse_word
            for _synonym_set in Material.synonym:
                if m1.name in _synonym_set and m2.name in _synonym_set:
                    combine_synonym = True
                    synonym_set = _synonym_set 
                    #print 'synonym_set' 
                    #print synonym_set 
                    break
            if not combine_synonym:
                return

        if combine_synonym:
            if name in synonym_set:
                name = synonym_set[0]
        to_m.name = name
        to_m.amount += del_m.amount
        to_m.save()
        del_m.delete()

        #记录哪两个记录合并
        log = LogMaterialCombine()
        log.logCombine(m1,m2)     
