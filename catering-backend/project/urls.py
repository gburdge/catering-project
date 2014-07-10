from apps.public.views import *

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'catering1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/$', CompanyList.as_view(), name='company-list'),
    url(r'^menus/$', MenuList.as_view(), name='menu-list'),
    url(r'^fooditem/$', FoodItem.as_view(), name='food-list'),
    url(r'^order/$', OrderList.as_view(), name='order-list'),
    url(r'^food_order/$', FoodOrderList.as_view(), name='food_order-list'),

    )
