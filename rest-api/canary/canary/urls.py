from django.conf.urls import patterns, include, url
from security.api import SystemResource, SensorResource
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(SystemResource())
v1_api.register(SensorResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'canary.views.home', name='home'),
    # url(r'^canary/', include('canary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(v1_api.urls)),
)
