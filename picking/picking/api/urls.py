from django.urls import path
from picking.picking.api.api import PickingViewSet

urlpatterns = [
    path('<str:saleorder>/', PickingViewSet.as_view({'get': 'list'})),
    path('<int:pk>', PickingViewSet.as_view({'delete': 'destroy'})),
    path('', PickingViewSet.as_view({'post': 'create'})),
]