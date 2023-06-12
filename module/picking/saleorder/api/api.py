import time

# restframework
from rest_framework import viewsets
from rest_framework.response import Response

# local apps
from module.picking.saleorder.models import SaleOrder
from module.picking.saleorder.api.serializers import SaleOrderSerializer
from module.picking.saleorder.postgresql.conn import ConnSQLite3 as ConnDB
from wmsbk.customs.mixins import APIMixin
from wmsbk.decorators.response import (
    add_saleorder_consumption_detail_decorator,
    add_consumption_detail_decorator,
)

class SaleOrderViewSet(APIMixin, viewsets.ModelViewSet):
    """View Set class SaleOrderAPIView"""

    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer
    model = SaleOrder

    @add_saleorder_consumption_detail_decorator
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        saleorder = kwargs.get("nosaleorder")
        queryset = self.queryset.filter(no_doc=saleorder)
        if not self.queryset:
            response.next_url = None
            response.before_url = None
            return self.custom_response_404(response)
        serializer = SaleOrderSerializer(queryset, many=True)
        response.data = serializer.data
        response.next_url = self.get_next_url(request, "no_doc", saleorder, "saleorder")
        response.before_url = self.get_before_url(request, "no_doc", saleorder, "saleorder")
        response = self.custom_response_200(response, response.data[0])
        return response

    @add_consumption_detail_decorator
    def list_info_indicator(self, request, *args, **kwargs):
        schema_name = request.user.company.schema_name
        name_customer = kwargs.get("namecustomer")
        no_doc = kwargs.get("nosaleorder")
        picking_quantity_by_customer = ConnDB().get_picking_quantity_by_customer(name_customer, schema_name)
        request_quantity_by_customer = ConnDB().get_request_quantity_by_customer(name_customer, schema_name)
        picking_quantity_by_saleorder = ConnDB().get_picking_quantity_by_saleorder(no_doc, schema_name)
        request_quantity_by_saleorder = ConnDB().get_request_quantity_by_saleorder(no_doc, schema_name)
        data = {
            "picking_quantity_by_customer": picking_quantity_by_customer["quantity"],
            "request_quantity_by_customer": request_quantity_by_customer["quantity"],
            "picking_quantity_by_saleorder": picking_quantity_by_saleorder["quantity"],
            "request_quantity_by_saleorder": request_quantity_by_saleorder["quantity"],
        }
        response = self.custom_response_200(Response(data), data)
        return response
