from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('payment.views',
    url(r'^$', 'index'),
    url(r'^new/$', 'create'),
    url(r'^(?P<payment_id>\d+)/$', 'view'),
)
