# Django
from django.core.exceptions import PermissionDenied

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from saleorder.models import SaleOrder
from picking.models import Picking, Status
from picking.api.serializers import PickingSerializer

class PickingViewSet(viewsets.ModelViewSet):
    """Picking view set."""
    queryset = Picking.objects.all()
    serializer_class = PickingSerializer

    def list(self, request, *args, **kwargs):
        saleorder = kwargs.get('saleorder')
        print(saleorder)
        try:
            saleorder = SaleOrder.objects.get(no_sale_order=saleorder)
        except:
            saleorder = None

        self.queryset = self.queryset.filter(sale_order=saleorder)
        print(self.queryset)
        if saleorder is not None:
            try:
                print(self.queryset)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if not saleorder:
            raise PermissionDenied('A saleorder parameter is required.')

        return super().list(request, *args, **kwargs)

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Establece un valor por defecto para el campo "status"
        if 'status' not in request.data:
            request.data['status'] = Status.objects.filter(name='PP')

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
