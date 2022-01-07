"""Defaults urls for the Zinnia TinyMCE"""
from django.conf.urls import include, url
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^', include('zinnia_tinymce.urls.links')),
    url(r'^filebrowser/', include('zinnia_tinymce.urls.filebrowser')),
    url(r'^tinymce_js/', TemplateView.as_view(template_name='admin/zinnia/entry/tinymce_textareas.js', content_type='application/javascript'), name='tinymce-js'),
]
