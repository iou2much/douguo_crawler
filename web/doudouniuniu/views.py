from django.shortcuts import render
from django.http import HttpResponse
import json

#def index(request, year):
#def index(request,page=1,pagesize=10,desc=True,orderby='zuone_piao'):
def index(request,desc=True,query='',orderby='zuone_piao'):
    data = json.loads(open('static/data/winner.json','r').read())
    page_range = request.META.get('HTTP_RANGE','0-10').split('-')
    if page_range:
        start = int(page_range[0])
        end = int(page_range[1])+1

    if str(desc).lower() == 'true':
        sort = -1
    else:
        sort = 1
    if query!='':
        _data=[]
        for d in data:
            if query in d['zuone_author_name'] or query in d['zuone_name']:
                _data.append(d)
        data = _data
    data = sorted(data, key=lambda x:sort * int(x.get(orderby)))
    resp = HttpResponse(json.dumps(data[start:end]))
    resp['Content-Range'] = '%s-%s/%s'%(0,10,len(data))
    return resp
