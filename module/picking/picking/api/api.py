import time

# Django
from sentry.registration.models import User  

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# local apps
from module.picking.saleorder.models import SaleOrder
from module.picking.picking.models import Picking, Status
from module.picking.picking.api.serializers import PickingSerializer
from wmsbk.customs.mixins import APIMixin

# decorators
from wmsbk.decorators.response import add_consumption_detail_decorator


class PickingViewSet(APIMixin, viewsets.ModelViewSet):
    """Picking view set."""
    queryset = Picking.objects.all()
    serializer_class = PickingSerializer
    model = Picking
    permission_classes = (IsAuthenticated,)

    @add_consumption_detail_decorator
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        saleorder_arg = kwargs.get('saleorder')
        saleorder = SaleOrder.objects.get(no_doc=saleorder_arg)
        if not saleorder:
            return Response(status=status.HTTP_404_NOT_FOUND)
        self.queryset = self.queryset.filter(sale_order=saleorder)
        response.next_url = self.get_next_url(
            request, "sale_order", saleorder_arg, "saleorderitem"
        )
        return response

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        responsible = User.objects.get(id=request.data['responsible'])
        status_picking = Status.objects.get(name='PP')
        sale_order = SaleOrder.objects.get(no_doc=request.data['sale_order'])
        
        # Creamos un nuevo objeto Picking
        picking = Picking.objects.create(
            status=status_picking,
            responsible=responsible,
            sale_order=sale_order
        )

        serializer = self.get_serializer(instance=picking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)