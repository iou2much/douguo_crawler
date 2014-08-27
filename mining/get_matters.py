#-*-coding:utf-8 -*-
import sys,json,re
reload(sys)
sys.setdefaultencoding('utf-8')

cook_books = json.loads(open('data/cookbook.json','r').read())
matter = {}

def unit_to_en(s):
    units = {
      u'克':u'g',
      u'毫升':u'ml',
      u'颗':u'个'
    }
    for ori in units:
        s = re.sub(ori,units[ori],s)
    return s
    
def clean(s):
    s = re.sub(u'（','(',s)
    s = re.sub(u'【','(',s)
    s = re.sub(u'）',')',s)
    s = re.sub(u'】',')',s)
    s = re.sub('(\(.*?\))','',s)
    s = re.sub(u'^(.*?：)','',s)
    s = re.sub(u'^(.*?:)','',s)
    s = re.sub(u'^(\d+、)','',s)
    return s.strip()
    #return re.sub(r'\u7c89','',re.sub(u'(（.*?）)','',re.sub('(\(.*?\))','',s)))

def reverse_num(s):
    num_dic={u'一':1,u'二':2,u'三':3,u'四':4,u'五':5,u'六':6,u'七':7,u'八':8,u'九':9,u'零':0}
    for n in num_dic:
        s = re.sub(n,'%s'%num_dic[n],s)
    return s

micro_matter = {}
for book in cook_books:
    for matters in book['matter']:
        name = clean(matters['name'].strip())
        if name not in matter:
            matter[name] = []
        amount = clean(unit_to_en(matters['amount'].strip().lower()))
        amount = reverse_num(amount)
        if re.match(r'.*\d+.*',amount):
            matter[name].append(amount)
        else:
            if name not in micro_matter:
                micro_matter[name] = []
            micro_matter[name].append(amount)

_matter = {}
for n in matter:
    if len(matter[n]) > 0:
        _matter[n] = matter[n]
matter = _matter
#保存数据
open('data/matters.json','w').write(json.dumps(matter))


#testing
for s in ["%s\n%s\n"%(name,', '.join(matter[name])) for name in matter]:
    print s
#for s in ["%s\n%s\n"%(name,', '.join(micro_matter[name])) for name in micro_matter]:
#    print s
