import time

# Django
from django.core.exceptions import PermissionDenied
from datetime import datetime

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from module.picking.saleorder.models import SaleOrder
from module.picking.saleorder.api.serializers import SaleOrderSerializer
from module.picking.saleorder.postgresql.conn import ConnSQLite3 as ConnDB
from wmsbk.mixins.apimixin import APIMixin
from wmsbk.decorators.response import add_consumption_detail_decorator


class SaleOrderViewSet(APIMixin, viewsets.ModelViewSet):
    """View Set class SaleOrderAPIView"""

    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer
    model = SaleOrder

    @add_consumption_detail_decorator
    def list(self, request, *args, **kwargs):
        saleorder = kwargs.get("nosaleorder")
        self.queryset = self.queryset.filter(no_sale_order=saleorder)
        if not self.queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        response = super().list(request, *args, **kwargs)
        response.data = response.data[0]
        response.next_url = self.get_next_url(
            request, "no_sale_order", saleorder, "saleorder"
        )
        return response

    def list_info_indicator(self, request, *args, **kwargs):
        schema_name = request.user.company.schema_name
        name_customer = kwargs.get("namecustomer")
        no_sale_order = kwargs.get("nosaleorder")
        picking_quantity_by_customer = ConnDB().get_picking_quantity_by_customer(name_customer, schema_name)
        request_quantity_by_customer = ConnDB().get_request_quantity_by_customer(name_customer, schema_name)
        picking_quantity_by_saleorder = ConnDB().get_picking_quantity_by_saleorder(no_sale_order, schema_name)
        request_quantity_by_saleorder = ConnDB().get_request_quantity_by_saleorder(no_sale_order, schema_name)
        response = {
            "picking_quantity_by_customer": picking_quantity_by_customer["quantity"],
            "request_quantity_by_customer": request_quantity_by_customer["quantity"],
            "picking_quantity_by_saleorder": picking_quantity_by_saleorder["quantity"],
            "request_quantity_by_saleorder": request_quantity_by_saleorder["quantity"],
        }
        return Response(response)
