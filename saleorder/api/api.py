# Django
from django.core.exceptions import PermissionDenied

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from saleorder.models import SaleOrder
from saleorder.api.serializers import SaleOrderSerializer
from saleorder.SQLite3.conn import ConnSQLite3 as ConnDB

class SaleOrderViewSet(viewsets.ModelViewSet):
    """View Set class SaleOrderAPIView"""
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

    def list(self, request, *args, **kwargs):
        saleorder = kwargs.get('nosaleorder')

        if saleorder is not None:
            try:
                self.queryset = self.queryset.filter(no_sale_order=saleorder)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if not saleorder:
            raise PermissionDenied('A nosaleorder parameter is required.')

        response = super().list(request, *args, **kwargs)
        response.data = response.data[0]

        return response


    def list_info_indicator(self, request, *args, **kwargs):

        name_customer = kwargs.get('namecustomer')
        no_sale_order = kwargs.get('nosaleorder')

        picking_quantity_by_customer = ConnDB().get_picking_quantity_by_customer(name_customer)
        request_quantity_by_customer = ConnDB().get_request_quantity_by_customer(name_customer)
        picking_quantity_by_saleorder = ConnDB().get_picking_quantity_by_saleorder(no_sale_order)
        request_quantity_by_saleorder = ConnDB().get_request_quantity_by_saleorder(no_sale_order)
        response = {
            "picking_quantity_by_customer":picking_quantity_by_customer['quantity'],
            "request_quantity_by_customer":request_quantity_by_customer['quantity'],
            "picking_quantity_by_saleorder":picking_quantity_by_saleorder['quantity'],
            "request_quantity_by_saleorder":request_quantity_by_saleorder['quantity'],
        }
        return Response(response)
    