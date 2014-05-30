from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'estate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^discoveries/', include('discoveries.urls', namespace="discoveries")),
    url(r'^scout/', include('scout.urls', namespace="scout")),
    url(r'^support/', include('support.urls', namespace="support")),
)
