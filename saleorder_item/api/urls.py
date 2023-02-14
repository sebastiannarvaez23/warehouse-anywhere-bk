# Django
from django.urls import path

# LocalApps
from saleorder_item.api.api import SaleOrderItemViewSet

urlpatterns = [
    path('<str:nosaleorder>/', SaleOrderItemViewSet.as_view({'get': 'list'})),
]