import time
# restframework
from rest_framework import viewsets, status

# local apps
from module.picking.saleorder.models import SaleOrder
from module.picking.saleorderitem.models import SaleOrderItem
from module.picking.saleorderitem.api.serializers import SaleOrderItemSerializer
from wmsbk.customs.mixins import APIMixin

# decorators
from wmsbk.decorators.response import add_consumption_detail_decorator

class SaleOrderItemViewSet(APIMixin, viewsets.ModelViewSet):
    """View Set class SaleOrderAPIView"""
    queryset = SaleOrderItem.objects.all()
    serializer_class = SaleOrderItemSerializer
    model = SaleOrderItem

    @add_consumption_detail_decorator
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        saleorder_arg = kwargs.get('nosaleorder')
        saleorder = SaleOrder.objects.filter(no_sale_order=saleorder_arg)
        if not saleorder:
            return response(status=status.HTTP_404_NOT_FOUND)
        self.queryset = self.queryset.filter(sale_order=saleorder[0])
        response.next_url = self.get_next_url(
            request, "sale_order", saleorder_arg, "saleorderitem"
        )
        return response