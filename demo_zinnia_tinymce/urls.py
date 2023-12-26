"""Urls for the zinnia-tinymce demo"""
from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin
from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap
from django.views.defaults import bad_request
from django.views.defaults import page_not_found
from django.views.defaults import permission_denied
from django.views.defaults import server_error
from django.views.generic.base import RedirectView
from django.views.static import serve

from zinnia.sitemaps import AuthorSitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import TagSitemap


urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/blog/', permanent=True)),
    re_path(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    re_path(r'^comments/', include('django_comments.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^admin/', include(admin.site.urls)),
]

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns += [
    re_path(r'^sitemap.xml$',
        index,
        {'sitemaps': sitemaps}),
    re_path(r'^sitemap-(?P<section>.+)\.xml$',
        sitemap,
        {'sitemaps': sitemaps}),
]

urlpatterns += [
    re_path(r'^400/$', bad_request),
    re_path(r'^403/$', permission_denied),
    re_path(r'^404/$', page_not_found),
    re_path(r'^500/$', server_error),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]
