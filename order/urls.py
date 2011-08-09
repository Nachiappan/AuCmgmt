from django.conf.urls.defaults import *

urlpatterns = patterns('order.views',
    url(r'^$', 'index', name = "View_Order"),
    url(r'^new/$', 'create',name = "New_Order"),
    #url(r'^orderlist/$', 'orderlist',name = "orderlist"),
    url(r'^(?P<oid>\d+)/$', 'view',name="view"),
    url(r'^(?P<oid>\d+)/excel_export/', 'excel_export',name="excel_export"),
    url(r'^(?P<oid>\d+)/additems/','additems',name = "additems"),
    url(r'^(?P<oid>\d+)/makepayment/','makepayment',name = "makepayment"),
    url(r'^(?P<oid>\d+)/payment/', include('payment.urls')),
    url(r'^(?P<oid>\d+)/delivery/', 'delivery',name ='delivery'),
)
