import time

# Django
from django.core.exceptions import PermissionDenied

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from module.storage.reference.models import Reference
from module.picking.box.models import Box
from module.picking.boxitem.models import BoxItem
from module.picking.boxitem.api.serializers import BoxItemSerializer
from wmsbk.customs.mixins import APIMixin

# decorators
from wmsbk.decorators.response import add_consumption_detail_decorator

class BoxItemViewSet(APIMixin, viewsets.ModelViewSet):
    """Box Item view set"""
    queryset = BoxItem.objects.all()
    serializer_class = BoxItemSerializer

    @add_consumption_detail_decorator
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        box = kwargs.get('box')
        box = Box.objects.filter(id=box)

        if not box:
            return self.custom_response_404(response)
        
        self.queryset = self.queryset.filter(box=box[0])            
        response = self.custom_response_200(response, response.data)
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        reference = Reference.objects.get(item_code=request.data['reference'])
        box = Box.objects.get(id=request.data['box'])

        boxitem = BoxItem.objects.create(
            quantity = request.data['quantity'],
            reference = reference,
            box = box
        )

        serializer = self.get_serializer(instance=boxitem)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
