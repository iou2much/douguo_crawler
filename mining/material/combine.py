#-*-coding:utf-8 -*-
if __name__=='__main__':
    import os,sys
    sys.path.append(os.environ['DOUGUO_BASE'])

from config import CONFIG
from orm.Material import Material

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd
import jieba
jieba.load_userdict(CONFIG['DICT_PATH']+"jieba_user.dict") 
jieba.enable_parallel(4)
import jieba.posseg as pseg

data = Material.objects().only('name')#[:2]

#[{id:,:word:,char:}]
material_names = {}

def init_grams():
    global material_names 
    global data
    for m in data:
        word = []
        mn = {}
        mn['word'] = set()
        mn['char'] = set()
        name = m.name.split(u'的')[-1]
        mn['origin'] = name
        for pair in pseg.cut(name):
            #if pair.flag == 'x':
            #    continue
            if len(pair.word) <=2 and (pair.word.isdigit() or(pair.word.isupper() or pair.word.islower())):
                continue
            word.append(pair.word)
            mn['char'].update(pair.word)

        mn['cut'] = word
        mn['word'].update(word)
        material_names[str(m.id)] = mn
    
def find_similar():
    #similar = {}
    similar_grid = []
    global material_names 
    pair_done = set()
    for mid1 in material_names:
        for mid2 in material_names:

            #对称词对跳过
            if (mid2,mid1) in pair_done:continue
            pair_done.add((mid1,mid2))


            char_inter = material_names[mid1]['char'].intersection(material_names[mid2]['char'])

            if mid1 == mid2 or len(char_inter) == 0 :continue

            word_inter = material_names[mid1]['word'].intersection(material_names[mid2]['word'])

            #不要动这行，以下计算基于这些元素顺序取值
            res = [len(word_inter),len(char_inter),len(material_names[mid1]['word']),len(material_names[mid2]['word']),len(material_names[mid1]['char']),len(material_names[mid2]['char']),''.join(char_inter)]
            #res += [len(material_names[mid1]['cut']),len(material_names[mid2]['cut'])]
            res += [Material.objects(id=mid1).only('name')[0].name, Material.objects(id=mid2).only('name')[0].name]
            #res += []
            #similar[(mid1,mid2)] = tuple(res)
            similar_grid.append([mid1,mid2]+res)
    #for s in similar:
    #    print '%s,%s'%(s,similar[s])
    df = pd.DataFrame(similar_grid)
    #df = pd.DataFrame(similar_grid[:1000])

    cl = len(similar_grid[0])-1
    df[cl+1] = df[2]/df[4]#m1 word ratio
    df[cl+2] = df[2]/df[5]#m2 word ratio
    df[cl+3] = df[3]/df[6]#m1 char ratio
    df[cl+4] = df[3]/df[7]#m2 char ratio
    df[cl+5] = (df[cl+1]+df[cl+2]) + (df[cl+3]+df[cl+4])
    df = df.sort(columns=15,ascending=False)

    df.to_csv('res.csv')
    #sys.exit()
    #df[8] = df[6]+df[7]
    def print_name(row):
        #if row[cl+1]==0 and row[cl+2]==0:return
        if (row[cl+1] == row[cl+2] == row[cl+3] == row[cl+4] ==1) or row[cl+5]>3:
            Material.combine(row[0],row[1],row[8])
            #return
        #return

        elif (row[cl+1]>=0.5 or row[cl+2]>=0.5) and (row[cl+3]>=0.5 or row[cl+4]>=0.5):
            #try:
            m1 = Material.objects(id=row[0]).only('name')
            if m1:
                m1 = m1.get(0)
            m2 = Material.objects(id=row[1]).only('name')
            if m2:
                m2 = m2.get(0)
            if not m1 or not m2:return
            #print Material.objects(id=row[0]).only('name')[0].name, Material.objects(id=row[1]).only('name')[0].name
            Material.combine(row[0],row[1],row[8],check_dict=True)
            #print row[8:]
            #print '-'*30
            
            #print row[cl+1:]
        #elif (row[cl+3]>=0.5 and row[cl+4]==1) or (row[cl+3]==1 and row[cl+4]>=0.5):
        elif row[cl+3]>=0.5 and row[cl+4]>=0.5 :
            #print Material.objects(id=row[0]).only('name')[0].name, Material.objects(id=row[1]).only('name')[0].name
            Material.combine(row[0],row[1],row[8],check_dict=True)
            #pass
            #print row[8:]
            #print '*'*50
        else:
            pass
            #print Material.objects(id=row[0]).only('name')[0].name, Material.objects(id=row[1]).only('name')[0].name
            #pass
            #print row[8:]
            #print '-'*30
    df.apply(print_name,axis=1)


if __name__ == '__main__':
    init_grams()
    find_similar()
#bigram = {}
#for m in data:
#    mn = {}
#    mn['id'] = m.id
#    mn['word'] = m.id
#    for pair in pseg.cut(m.name):
#        print '%s / %s'%(pair.word,pair.flag)
#        character.update(pair.word)
#
#char_list = []
#for c in character:
#    p = pseg.cut(c).next()
#    char_list.append(p.word)
#    #print dir(p)
#    #print '%s / %s'%(p.word,p.flag)




#        chars = set(pair.word)
#        for c in chars:
#            p = pseg.cut(c).next().word
