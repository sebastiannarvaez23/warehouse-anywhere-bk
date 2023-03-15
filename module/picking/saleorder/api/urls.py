#Django
from django.urls import path

# LocalApps
from module.picking.saleorder.api.api import SaleOrderViewSet

urlpatterns = [
    path('<str:nosaleorder>/', SaleOrderViewSet.as_view({'get': 'list'})),
    path('indicator/<str:namecustomer>/<str:nosaleorder>/', SaleOrderViewSet.as_view({'get': 'list_info_indicator'})),
    path('', SaleOrderViewSet.as_view({'post': 'create'})),
    path('<int:pk>/', SaleOrderViewSet.as_view({'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]