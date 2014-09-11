import os
import sys 

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'doudouniuniu.settings'
sys.path.append('/data/code/sinaapp/doudouniuniu/1/')
sys.path.append('/data/code/sinaapp/doudouniuniu/1/doudouniuniu/')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
