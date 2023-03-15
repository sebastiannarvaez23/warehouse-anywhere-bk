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

import time

class BoxItemViewSet(viewsets.ModelViewSet):
    """Box Item view set"""
    queryset = BoxItem.objects.all()
    serializer_class = BoxItemSerializer

    def list(self, request, *args, **kwargs):
        box = kwargs.get('box')
        box = Box.objects.get(id=box)
        
        if box is not None:
            try:
                self.queryset = self.queryset.filter(box=box)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            if not box:
                raise PermissionDenied('A box parameter is required.')
        return super().list(request, *args, **kwargs)

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
