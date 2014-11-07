from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agliq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^agliq_join/', include('agliq_join.urls')),                   
    url(r'^admin/', include(admin.site.urls)),
)
