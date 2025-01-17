"""EntryAdmin for zinnia-tinymce"""
from django.contrib import admin
from django.urls import reverse
from django.forms import Media

from tinymce.widgets import TinyMCE

from zinnia.admin.entry import EntryAdmin
from zinnia.models import Entry
from zinnia.settings import ENTRY_BASE_MODEL


class EntryAdminTinyMCEMixin(object):
    """
    Mixin adding TinyMCE for editing Entry.content field.
    """

    def _media(self):
        """
        The medias needed to enhance the admin page.
        """
        media = super(EntryAdminTinyMCEMixin, self).media

        media += TinyMCE().media + Media(
            js=[reverse('tinymce-js'),
                reverse('tinymce-filebrowser-callback')]
        )

        return media
    media = property(_media)


class EntryAdminTinyMCE(EntryAdminTinyMCEMixin,
                        EntryAdmin):
    """
    Enrich the default EntryAdmin with TinyMCE.
    """
    pass


if ENTRY_BASE_MODEL == 'zinnia.models_bases.entry.AbstractEntry':
    admin.site.unregister(Entry)
    admin.site.register(Entry, EntryAdminTinyMCE)
