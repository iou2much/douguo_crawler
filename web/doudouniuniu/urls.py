from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# for development only
# This will only work if DEBUG is True.

urlpatterns = patterns('',
    # Examples:

     url(r'^index/desc/(.+)/q/(.*)$', 'doudouniuniu.views.index',name='index'),
     url(r'^index/desc/(.+)$', 'doudouniuniu.views.index',name='index'),
     #url(r'^index/page/(\w+)/pagesize/(.+)/desc/(.+)$', 'doudouniuniu.views.index',name='index'),
     #url(r'^index/page/(\w+)/pagesize/(.+)/orderby/(.+)$', 'doudouniuniu.views.index',name='index'),
     #url(r'^index/page/(\w+)/pagesize/(.+)$', 'doudouniuniu.views.index',name='index'),
     #url(r'/', 'doudouniuniu.views.index', name='index'),
    # url(r'^$', 'doudouniuniu.views.home', name='home'),
    # url(r'^doudouniuniu/', include('doudouniuniu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
