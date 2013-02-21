from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^wiki/(?P<page_name>[^/]+)/edit/$', 'wiki.views.edit_page'),
    url(r'^wiki/(?P<page_name>[^/]+)/save/$', 'wiki.views.save_page'),
    url(r'^wiki/(?P<page_name>[^/]+)/$', 'wiki.views.view_page'),
)
