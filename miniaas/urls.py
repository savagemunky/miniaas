from django.conf.urls import patterns, include, url
from django.contrib import admin
from ControlServer.views import hello, current_datetime, register

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniaas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^register/$', register)
    # url(r'^$', index)
)
