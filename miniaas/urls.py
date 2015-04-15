from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniaas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ControlServer.views.main_view'),
    url(r'^containers/$', 'ControlServer.views.containers_view'),
    url(r'^main/$', 'ControlServer.views.main_view'),
    url(r'^stats/$', 'ControlServer.views.stats_view'),
    url(r'^index/$', 'ControlServer.views.index_view'),
    # url(r'^register/$', 'ControlServer.views.register_view'),
    # url(r'^invalid/$', 'ControlServer.views.invalid_credentials_view'),
    # url(r'^$',),
)
