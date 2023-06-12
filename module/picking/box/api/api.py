
# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# local apps
from sentry.registration.models import User  
from module.picking.picking.models import Picking
from module.picking.box.models import Box, Dimension
from module.picking.box.api.serializers import BoxSerializer, DimensionSerializer
from wmsbk.customs.mixins import APIMixin

# decorators
from wmsbk.decorators.response import add_consumption_detail_decorator

class BoxViewSet(APIMixin, viewsets.ModelViewSet):
    """Box view set."""
    queryset = Box.objects.all()
    model = Box
    serializer_class = BoxSerializer
    permission_classes = (IsAuthenticated,)

    @add_consumption_detail_decorator
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        picking = kwargs.get('picking')
        picking = Picking.objects.get(id=picking)

        if not picking:
            return self.custom_response_404(response)
        
        queryset = self.queryset.filter(picking=picking)
        serializer = BoxSerializer(queryset, many=True)
        response.data = serializer.data
        response = self.custom_response_200(response, response.data)
        return response
    
    @add_consumption_detail_decorator
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
        response = self.custom_response_201(Response(serializer.data, status=status.HTTP_201_CREATED))
        return response
    
    @add_consumption_detail_decorator
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

        response = self.custom_response_200(Response(serializer.data, status=status.HTTP_200_OK))
        return response

class DimensionViewSet(APIMixin, viewsets.ModelViewSet):
    """Box view set."""
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    permission_classes = (IsAuthenticated,)

    @add_consumption_detail_decorator
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        self.queryset = self.queryset.filter(is_delete=False)
        if not self.queryset:
            return self.custom_response_404(response)
        self.custom_response_200(response, response.data)
        return response
    
    @add_consumption_detail_decorator
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete = True
        instance.save()
        serializer = self.get_serializer(instance)
        response = self.custom_response_204(Response(serializer.data))
        return response