#-*-coding:utf-8 -*-
if __name__=='__main__':
    import os,sys
    sys.path.append(os.environ['DOUGUO_BASE'])

from config import CONFIG
from orm.Material import Material
import sys,json,re
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba.posseg as pseg

class MaterialGetter:
    cook_books = json.loads(open(CONFIG['DATA_PATH']+'cookbook.json','r').read())
    material = {}
    
    def __init__(self):
        Material.drop_collection()
        print 'Initiating complete ! Material collection droped !!'
    
    def unit_to_en(self,s):
        units = {
          u'克':u'g',
          u'毫升':u'ml',
          u'颗':u'个'
        }
        for ori in units:
            s = re.sub(ori,units[ori],s)
        return s
        
    def clean(self,s):
        s = re.sub(u'（','(',s)
        s = re.sub(u'【','(',s)
        s = re.sub(u'）',')',s)
        s = re.sub(u'】',')',s)
        s = re.sub('(\(.*?\))','',s)
        s = re.sub(u'^(.*?：)','',s)
        s = re.sub(u'^(.*?:)','',s)
        s = re.sub(u'^(\d+、)','',s)
        return s.strip()
    
    def reverse_num(self,s):
        num_dic={u'一':1,u'二':2,u'三':3,u'四':4,u'五':5,u'六':6,u'七':7,u'八':8,u'九':9,u'零':0}
        for n in num_dic:
            s = re.sub(n,'%s'%num_dic[n],s)
        return s
    
    def save(self):
        micro_material = {}
        for book in self.cook_books:
            for materials in book['material']:
                name = self.clean(materials['name'].strip())
                if name not in self.material:
                    self.material[name] = []
                amount = self.clean(self.unit_to_en(materials['amount'].strip().lower()))
                amount = self.reverse_num(amount)
                if re.match(r'.*\d+.*',amount):
                    self.material[name].append(amount)
                else:
                    if name not in micro_material:
                        micro_material[name] = []
                    micro_material[name].append(amount)
        
        _material = {}
        for n in self.material:
            if len(self.material[n]) > 0:
                _material[n] = self.material[n]
                m = Material()
                m.name = n
                amounts = [pseg.cut(amount) for amount in self.material[n]]
                amount_list = []
                m.amount = []
                for a in amounts:
                    amount = []
                    for _a in a:
                        amount.append({'word':_a.word,'flag':_a.flag})
                    m.amount.append(amount)
                m.save()
        self.material = _material
        #保存数据
        open(CONFIG['DATA_PATH']+'materials.json','w').write(json.dumps(self.material))
        
        

if __name__ == '__main__':
    getter = MaterialGetter()
    getter.save()
#testing
#for s in ["%s\n%s\n"%(name,', '.join(material[name])) for name in material]:
#    print s
#for s in ["%s\n%s\n"%(name,', '.join(micro_material[name])) for name in micro_material]:
#    print s
