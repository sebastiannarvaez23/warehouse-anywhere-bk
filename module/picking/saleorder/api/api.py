import time

# Django
from django.core.exceptions import PermissionDenied

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from module.picking.saleorder.models import SaleOrder
from module.picking.saleorder.api.serializers import SaleOrderSerializer
from module.picking.saleorder.postgresql.conn import ConnSQLite3 as ConnDB
from module.picking.saleorder.permissions import IsCompanyObject
from rest_framework.reverse import reverse
from wmsbk.mixins.response import ConsumptionDetailMixin


class SaleOrderViewSet(ConsumptionDetailMixin, viewsets.ModelViewSet):
    """View Set class SaleOrderAPIView"""

    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

    def list(self, request, *args, **kwargs):
        saleorder = kwargs.get("nosaleorder")

        if saleorder is None:
            raise PermissionDenied("A nosaleorder parameter is required.")

        self.queryset = self.queryset.filter(no_sale_order=saleorder)
        if not self.queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = super().list(request, *args, **kwargs)
        next_url = self.get_next_url(
            request, SaleOrder, "no_sale_order", saleorder, "saleorder"
        )
        if response.data:
            detail_response = {
                "status": status.HTTP_200_OK,
                "message": "OK",
                "next_url": next_url,
            }
            response.data = self.add_consumption_detail(response, detail_response)
            return response

    def list_info_indicator(self, request, *args, **kwargs):
        schema_name = request.user.company.schema_name
        name_customer = kwargs.get("namecustomer")
        no_sale_order = kwargs.get("nosaleorder")
        picking_quantity_by_customer = ConnDB().get_picking_quantity_by_customer(
            name_customer, schema_name
        )
        request_quantity_by_customer = ConnDB().get_request_quantity_by_customer(
            name_customer, schema_name
        )
        picking_quantity_by_saleorder = ConnDB().get_picking_quantity_by_saleorder(
            no_sale_order, schema_name
        )
        request_quantity_by_saleorder = ConnDB().get_request_quantity_by_saleorder(
            no_sale_order, schema_name
        )
        response = {
            "picking_quantity_by_customer": picking_quantity_by_customer["quantity"],
            "request_quantity_by_customer": request_quantity_by_customer["quantity"],
            "picking_quantity_by_saleorder": picking_quantity_by_saleorder["quantity"],
            "request_quantity_by_saleorder": request_quantity_by_saleorder["quantity"],
        }
        return Response(response)
