from django.conf.urls import patterns, url

from discoveries import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^reports/', views.reports, name='reports'),
    url(r'^scan/', views.scan, name='scan'),
)
