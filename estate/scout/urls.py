from django.conf.urls import patterns, url

from scout import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sa/$', views.sa, name='sa'),
    url(r'^sb/$', views.sb, name='sb'),
    url(r'^aa/$', views.aa, name='aa'),
    url(r'^ab/$', views.ab, name='ab'),
    url(r'^f2edit/$', views.f2edit, name='f2edit'),
)

