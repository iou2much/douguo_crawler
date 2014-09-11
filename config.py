import sys,os 

CONFIG={}
CONFIG['BASE_PATH'] = os.environ['DOUGUO_BASE']+'/'
CONFIG['DATA_PATH'] = CONFIG['BASE_PATH'] + 'data/'

def setmain():
    sys.path.append(CONFIG['BASE_PATH'])
