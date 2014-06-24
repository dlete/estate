from django.conf.urls import patterns, url

from support import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^reconcile/$', views.reconcile, name='reconcile'),
    url(r'^reconcile/add_to_support/(?P<part_id>\d+)/$', views.add_to_support, name='add_to_support'),
    url(r'^reconcile/add_to_support_many/$', views.add_to_support_many, name='add_to_support_many'),
    url(r'^edit_many_part_supported/$', views.edit_many_part_supported, name='edit_many_part_supported'),
    url(r'^edit_one/(?P<part_id>\d+)/$', views.edit_one, name='edit_one'),
    url(r'^update_one/(?P<part_id>\d+)/$', views.update_one, name='update_one'),
    url(r'^update_many_part_supported/$', views.update_many_part_supported, name='update_many_part_supported'),
)
