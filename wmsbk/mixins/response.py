import time
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView


class ConsumptionDetailMixin:
    def add_consumption_detail(self, response, detal_response):
        data = response.data[0]
        response.data = {
            "status": detal_response["status"],
            "message": detal_response["message"],
            "nexturl": detal_response["next_url"],
            "data": data,
        }
        return response.data

    def get_next_url(self, request, model, attribute, pattern, url_name):
        exist_obj = model.objects.filter(**{attribute: int(pattern) + 1}).exists()
        
        if exist_obj:
            pattern = int(pattern) + 1
            next_url = reverse(url_name, args=[pattern], request=request)
            return next_url
        return None