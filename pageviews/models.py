# coding: utf-8
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class HitCount(models.Model):
    """
    Hit count model. An optional related object can be set.
    """
    created_at = models.DateTimeField(
        _('Created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
        _('Updated at'), auto_now=True, editable=False)
    url = models.CharField(_('URL'), max_length=2000)
    hits = models.PositiveIntegerField(_('Hits'), default=0)
    # related content_object
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('-created_at', '-updated_at')
        get_latest_by = 'created'
        verbose_name = _(u'Hit')
        verbose_name_plural = _(u'Hits')
