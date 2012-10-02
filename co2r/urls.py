from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/faqs$', 'co2r.main.views.faqs', name='faqs'),
        url(r'^api/app$', 'co2r.main.views.app_content', name='app_content'),
        url(r'^api/artifacts$', 'co2r.artifacts.views.artifacts', name='artifacts'),
        url(r'^api/artifact/(?P<slug>[a-z0-9-_]+)$', 'co2r.artifacts.views.artifact', name='artifact'),
        url(r'^api/footprints$', 'co2r.artifacts.views.footprints', name='footprints'),
        url(r'^api/footprint/(?P<slug>[a-z0-9-_]+)/(?P<year>[0-9]+)$', 'co2r.artifacts.views.footprint', name='footprint')
    )

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
        url(r'^admins/(?P<path>.*)$', 'serve'),

)
