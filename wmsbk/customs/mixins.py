import time

# restframework
from rest_framework.reverse import reverse
from rest_framework import status

class APIMixin:    
    def get_next_url(self, request, field, pattern, url_name):
        next_pattern = int(pattern) + 1
        while next_pattern <= int(self.model.objects.order_by(field).last().no_doc):
            if self.model.objects.filter(**{field:next_pattern}).exists():
                self.next_url = reverse(url_name, args=[next_pattern], request=request)
                return self.next_url
            next_pattern += 1
        return None
    
    def get_before_url(self, request, field, pattern, url_name):
        before_pattern = int(pattern) - 1
        while before_pattern >= int(self.model.objects.order_by(field).first().no_doc):
            if self.model.objects.filter(**{field:before_pattern}).exists():
                self.before_url = reverse(url_name, args=[before_pattern], request=request)
                return self.before_url
            before_pattern -= 1
        return None
    
    def custom_response_200(self, response, data):
        response.status = status.HTTP_200_OK
        response.message = "OK"
        response.data = data
        return response

    def custom_response_201(self, response):
        response.status = status.HTTP_201_CREATED
        response.message = "The item has been created successfully"
        return response

    def custom_response_404(self, response):
        response.status_code = status.HTTP_404_NOT_FOUND
        response.status = status.HTTP_404_NOT_FOUND
        response.message = "The resource requested is not available"
        response.data = []
        return response
