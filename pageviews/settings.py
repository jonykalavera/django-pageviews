# coding: utf-8
from django.conf import settings

PAGEVIEWS_OBJECT_ATTR = getattr(
    settings, 'PAGEVIEWS_OBJECT_ATTR', 'content_object')
