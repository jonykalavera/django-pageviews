# coding: utf-8
from datetime import date, datetime
from django.contrib.contenttypes.models import ContentType
from django.db.models import F, Model

from .models import HitCount
from .settings import PAGEVIEWS_OBJECT_ATTR


class PageViewsMiddleware:

    def process_response(self, request, response, *args, **kwargs):
        if response.status_code == 200:
            content_object = getattr(request, PAGEVIEWS_OBJECT_ATTR, None)
            today = datetime.fromordinal(date.today().toordinal())
            if content_object and isinstance(content_object, Model):
                content_type = ContentType.objects.get_for_model(
                    content_object.__class__)
                hit, hit_created = HitCount.objects.get_or_create(
                    url=request.path,
                    object_id=content_object.pk,
                    content_type=content_type,
                    for_date=today
                )
            else:
                hit, hit_created = HitCount.objects.get_or_create(
                    url=request.path, for_date=today)

            hit.hits = F('hits') + 1
            hit.save()

        return response
