"""
Models for support filebrowser in TinyMCE
"""
import os
import uuid

from django.db import models
from django.utils import timezone
from six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


def upload_path(instance, filename):
    now = timezone.now()
    filename, extension = os.path.splitext(filename)

    return os.path.join(
        now.strftime('%Y'),
        now.strftime('%m'),
        now.strftime('%d'),
        '%s%s' % (str(uuid.uuid4()).replace('-', ''), extension))


@python_2_unicode_compatible
class FileModel(models.Model):
    """
    Uploaded file via TinyMCE
    """
    FILE_TYPES = (
        ('image', _('Image')),
        ('file', _('Document')),
    )

    file_type = models.CharField(
        _('file type'), max_length=35,
        choices=FILE_TYPES)
    uploaded_file = models.FileField(
        _('file / image'),
        upload_to=upload_path)
    creation_date = models.DateTimeField(
        _('creation date'), auto_now_add=True)

    def __str__(self):
        return '%s' % self.uploaded_file.name

    def get_absolute_url(self):
        return self.uploaded_file.url

    class Meta:
        ordering = ['-creation_date']
        verbose_name = _('file')
        verbose_name_plural = _('files')
