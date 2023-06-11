import time

# restframework
from rest_framework.reverse import reverse

class APIMixin:
    def get_next_url(self, request, attribute, pattern, url_name):
        exist_obj = self.model.objects.filter(**{attribute: int(pattern) + 1}).exists()
        if exist_obj:
            pattern = int(pattern) + 1
            self.next_url = reverse(url_name, args=[pattern], request=request)
            return self.next_url
        return None
