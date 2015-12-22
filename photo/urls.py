from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static  
from django.contrib import admin
from img import views, beautify, edit, manage,map0
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^start/$', views.start),
    url(r'^manage/$', manage.manage),
    url(r'^pilbeau/$', beautify.beauti),
    url(r'^editt/$', edit.edit0),
    url(r'^map/$', map0.mapp),
    url(r'^stati/(?P<path>.*)', 'django.views.static.serve',\
        {'document_root': '/data1/www/htdocs/825/lllcccfff/1/img/stati'}),
    url(r'crossdomain.xml$','/data1/www/htdocs/825/lllcccfff/1/crossdomain.xml$',\
        {'template': 'crossdomain.xml', 'mimetype': 'text/plain'})
    
)
#urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
 
