from django.conf.urls import patterns, include, url
from django.template import Template
from webstat import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from webstat.webstatif.views import hello

from webstat.webstatif.views import login_redirect



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webstat.views.home', name='home'),
    # url(r'^webstat/', include('webstat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello),
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/login/'}),
    url(r'^accounts/profile/$', hello),
    url(r'^accounts/login/$',login_redirect),
    url(r'^statics/(?P<path>.*)$', 'django.views.static.serve',{'document_root':     settings.MEDIA_ROOT}),
)
