from django.conf.urls import patterns, include, url

from django.contrib import admin
from img import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^start/$', views.start),
    url(r'^stati/(?P<path>.*)', 'django.views.static.serve',\
        {'document_root': 'h:/photo/img/stati'}),  
    
)
