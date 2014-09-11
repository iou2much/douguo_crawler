import pandas as pd
df = pd.read_csv('dict/jieba_user.dict')
#print df
us = set()
for w in df:
    print w

