# Django
from django.core.exceptions import PermissionDenied
from sentry.registration.models import User  

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# local apps
from module.picking.picking.models import Picking
from module.picking.box.models import Box, Dimension
from module.picking.box.api.serializers import BoxSerializer, DimensionSerializer

class BoxViewSet(viewsets.ModelViewSet):
    """Box view set."""
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = (IsAuthenticated,)

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

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        responsible = User.objects.get(id=request.data['responsible'])
        dimension = Dimension.objects.get(id=request.data['dimension'])
        picking = Picking.objects.get(id=request.data['picking'])
        gross_weight = request.data['gross_weight']

        instance.gross_weight = gross_weight
        instance.responsible = responsible
        instance.dimension = dimension
        instance.picking = picking
        instance.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class DimensionViewSet(viewsets.ModelViewSet):
    """Box view set."""
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        try:
            self.queryset = self.queryset.filter(is_delete=False)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)