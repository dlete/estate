from django.conf.urls import patterns, url

from discoveries import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^aa/', views.aa, name='aa'),
    url(r'^ab/', views.ab, name='ab'),
    url(r'^reports/', views.reports, name='reports'),
    url(r'^scan/', views.scan, name='scan'),
)
