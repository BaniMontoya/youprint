from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'central.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^gestor/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),

)
