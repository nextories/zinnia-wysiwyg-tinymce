"""Defaults urls for the Zinnia TinyMCE"""
from django.urls import include, re_path
from django.views.generic.base import TemplateView


urlpatterns = [
    re_path(r'^', include('zinnia_tinymce.urls.links')),
    re_path(r'^filebrowser/', include('zinnia_tinymce.urls.filebrowser')),
    re_path(r'^tinymce_js/', TemplateView.as_view(template_name='admin/zinnia/entry/tinymce_textareas.js', content_type='application/javascript'), name='tinymce-js'),
]
