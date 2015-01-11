from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'central.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^gestor/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),

)
