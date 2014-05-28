from django.conf.urls import patterns, url

from scout import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^discoveries/', views.discoveries, name='discoveries'),
)

