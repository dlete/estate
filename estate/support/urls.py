from django.conf.urls import patterns, url

from support import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^reconcile/$', views.reconcile, name='reconcile'),
    url(r'^reconcile/add_to_support/(?P<part_id>\d+)/$', views.add_to_support, name='add_to_support'),
    url(r'^reconcile/add_to_support_many/$', views.add_to_support_many, name='add_to_support_many'),
)

