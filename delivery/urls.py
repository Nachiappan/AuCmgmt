from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('delivery.views',
    url(r'^/', 'index'),
    url(r'^new/', 'create'),
    url(r'^(?P<delivery_id>\d+)/', 'view'),
)
