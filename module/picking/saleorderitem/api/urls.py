# Django
from django.urls import path

# LocalApps
from module.picking.saleorderitem.api.api import SaleOrderItemViewSet

urlpatterns = [
    path('<str:nosaleorder>/', SaleOrderItemViewSet.as_view({'get': 'list'})),
]