# Django
from django.core.exceptions import PermissionDenied

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from saleorder.models import SaleOrder
from saleorder_item.models import SaleOrderItem
from saleorder_item.api.serializers import SaleOrderItemSerializer

class SaleOrderItemViewSet(viewsets.ModelViewSet):
    """View Set class SaleOrderAPIView"""
    queryset = SaleOrderItem.objects.all()
    serializer_class = SaleOrderItemSerializer

    def list(self, request, *args, **kwargs):
        saleorder = kwargs.get('nosaleorder')
        saleorder = SaleOrder.objects.get(no_sale_order=saleorder)
        self.queryset = self.queryset.filter(sale_order=saleorder)

        if saleorder is not None:
            try:
                print("hollaa")
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if not saleorder:
            raise PermissionDenied('A nosaleorder parameter is required.')

        return super().list(request, *args, **kwargs)