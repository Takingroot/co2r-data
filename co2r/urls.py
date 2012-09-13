from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/products$', 'co2r.products.views.products', name='products'),
        url(r'^api/products/(?P<internal_name>[a-z0-9-_]+)$', 'co2r.products.views.product', name='product'),
        url(r'^api/footprints$', 'co2r.products.views.footprints', name='footprints'),
        url(r'^api/footprint/(?P<internal_name>[a-z0-9-_]+)/(?P<year>[0-9]+)$', 'co2r.products.views.footprint', name='footprint')
    )

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
)
