import time
from rest_framework.reverse import reverse


class APIMixin:
    def get_next_url(self, request, model, attribute, pattern, url_name):
        exist_obj = model.objects.filter(**{attribute: int(pattern) + 1}).exists()
        if exist_obj:
            pattern = int(pattern) + 1
            next_url = reverse(url_name, args=[pattern], request=request)
            return next_url
        return None
