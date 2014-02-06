from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'checkout_django_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^onsite/', 'checkoutapp.views.onsite'),
    url(r'^offsite/', 'checkoutapp.views.offsite'),
    url(r'^return/', 'checkoutapp.views.returnpayment'),
    url(r'^$', 'checkoutapp.views.index')
)
