"""
URLs for list of links in TinyMCE
"""
from django.urls import re_path

from zinnia_tinymce.views import EntryLinksView
from zinnia_tinymce.views import FileLinksView
from zinnia_tinymce.views import ImageLinksView


urlpatterns = [
    re_path(r'^links.js$',
        EntryLinksView.as_view(),
        name='tinymce-external-links'),
    re_path(r'^images.js$',
        ImageLinksView.as_view(),
        name='tinymce-external-images'),
    re_path(r'^files.js$',
        FileLinksView.as_view(),
        name='tinymce-external-files'),
]
