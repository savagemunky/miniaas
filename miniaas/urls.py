from django.conf.urls import patterns, include, url
from django.contrib import admin
from ControlServer.views import index_view, register_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniaas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ControlServer.views.index_view'),
    url(r'^index/$', 'ControlServer.views.index_view'),
    url(r'^register/$', 'ControlServer.views.register_view'),
    url(r'^main/$', 'ControlServer.views.main_view'),
    url(r'^invalid/$', 'ControlServer.views.invalid_credentials_view'),
    # url(r'^$',),
)
