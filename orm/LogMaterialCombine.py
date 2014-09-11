# coding: utf-8  
  
from mongoengine import *  
connect('douguo')  
#from logMaterialCombine import logMaterialCombine
  
class LogMaterialCombine(Document):
    id1= StringField()  
    id2= StringField()  
    name1= StringField()  
    name2= StringField()  

    @staticmethod
    def logCombine(m1,m2):
        log = LogMaterialCombine()
        log.id1 = str(m1.id)
        log.id2 = str(m2.id)
        log.name1 = m1.name
        log.name2 = m2.name
        log.save()
