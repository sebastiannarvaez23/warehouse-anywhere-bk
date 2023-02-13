# Django
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from picking.models import Picking
from box.models import Box, Dimension
from box.api.serializers import BoxSerializer, DimensionSerializer


class BoxViewSet(viewsets.ModelViewSet):
    """Box view set."""
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

    def list(self, request, *args, **kwargs):
        picking = kwargs.get('picking')
        picking = Picking.objects.get(id=picking)

        if picking is not None:
            try:
                self.queryset = self.queryset.filter(picking=picking)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        if not picking:
            raise PermissionDenied('A picking parameter is required.')
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        responsible = User.objects.get(id=request.data['responsible'])
        dimension = Dimension.objects.get(id=request.data['dimension'])
        picking = Picking.objects.get(id=request.data['picking'])

        box = Box.objects.create(
            gross_weight = 0,
            responsible = responsible,
            dimension = dimension,
            picking = picking
        )

        serializer = self.get_serializer(instance=box)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DimensionViewSet(viewsets.ModelViewSet):
    """Box view set."""
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer