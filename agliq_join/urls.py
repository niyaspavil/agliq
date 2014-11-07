from django.conf.urls import patterns, include, url

from agliq_join import views

urlpatterns = patterns('',
    url(r'^$', views.agliq_connect, name='agliq_connect'),
    url(r'^callback/$',views.callback,name='agliq_callback'),
)
                       
