#Django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# LocalApps
from module.picking.saleorder.api.api import SaleOrderViewSet, CollectionViewSet, PayTermViewSet


router = DefaultRouter()
router.register('collection', CollectionViewSet, basename='collection')
router.register('pay-term', PayTermViewSet, basename='pay-term')

urlpatterns = [
    path('deps/', include(router.urls)),
    path('<str:nosaleorder>/', SaleOrderViewSet.as_view({'get': 'list'}), name="saleorder"),
    path('indicator/<str:namecustomer>/<str:nosaleorder>/', SaleOrderViewSet.as_view({'get': 'list_info_indicator'})),
    path('', SaleOrderViewSet.as_view({'post': 'create'})),
    path('<int:pk>/', SaleOrderViewSet.as_view({'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]