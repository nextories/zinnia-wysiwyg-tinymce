"""
URLs for filebrowser in TinyMCE
"""
from django.urls import re_path
from django.views.generic import View

from zinnia_tinymce.views import FileBrowserCallBackView
from zinnia_tinymce.views import FileBrowserView
from zinnia_tinymce.views import RemoveFileView


urlpatterns = [
    re_path(r'^$',
        View.as_view(),
        name='tinymce-filebrowser-dispatch'),
    re_path(r'^callback.js$',
        FileBrowserCallBackView.as_view(),
        name='tinymce-filebrowser-callback'),
    re_path(r'^(?P<file_type>\w+)/$',
        FileBrowserView.as_view(),
        name='tinymce-filebrowser'),
    re_path(r'^(?P<file_type>\w+)/remove/(?P<pk>\d+)/$',
        RemoveFileView.as_view(),
        name='tinymce-filebrowser-remove')
]
