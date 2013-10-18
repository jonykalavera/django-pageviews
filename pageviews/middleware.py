from .models import HitCount
from django.db.models import F


class PageViewsMiddleware:
    
    def process_response(self, request, response, *args, **kwargs):
        if response.status_code == 200:
            content_object = getattr(response, 'content_object', None)
            if content_object:
                content_type = ContentType.objects.get_for_model(
                    content_object._model)
                hit, hit_created = HitCount.objects.get_or_create(
                    url=request.path, 
                    object_id=content_object.pk,
                    content_type=content_type
                    )
            else:
                hit, hit_created = HitCount.objects.get_or_create(url=request.path)
                
            
            hit.hits = F('hits') + 1
            hit.save()

        return response
