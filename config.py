import sys,os 

CONFIG={}
CONFIG['BASE_PATH'] = os.environ['DOUGUO_BASE']+'/'
CONFIG['DATA_PATH'] = CONFIG['BASE_PATH'] + 'data/'
CONFIG['DICT_PATH'] = CONFIG['BASE_PATH'] + 'mining/dict/'

def setmain():
    sys.path.append(CONFIG['BASE_PATH'])
