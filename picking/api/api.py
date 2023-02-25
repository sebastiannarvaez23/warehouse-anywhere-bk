import time

# Django
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# local apps
from saleorder.models import SaleOrder
from picking.models import Picking, Status
from picking.api.serializers import PickingSerializer

class PickingViewSet(viewsets.ModelViewSet):
    """Picking view set."""
    queryset = Picking.objects.all()
    serializer_class = PickingSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        saleorder = kwargs.get('saleorder')

        try:
            saleorder = SaleOrder.objects.get(no_sale_order=saleorder)
        except:
            saleorder = None

        if saleorder is not None:
            try:
                self.queryset = self.queryset.filter(sale_order=saleorder)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if not saleorder:
            raise PermissionDenied('A saleorder parameter is required.')

        return super().list(request, *args, **kwargs)

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        responsible = User.objects.get(id=request.data['responsible'])
        status_picking = Status.objects.get(name='PP')
        sale_order = SaleOrder.objects.get(no_sale_order=request.data['sale_order'])
        
        # Creamos un nuevo objeto Picking
        picking = Picking.objects.create(
            status=status_picking,
            responsible=responsible,
            sale_order=sale_order
        )

        serializer = self.get_serializer(instance=picking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)