from django.urls import path
from module.picking.boxitem.api.api import BoxItemViewSet

urlpatterns = [
    path('<str:box>/', BoxItemViewSet.as_view({'get':'list'})),
    path('', BoxItemViewSet.as_view({'post':'create'})),
    path('<int:pk>', BoxItemViewSet.as_view({'delete': 'destroy'})),
    #path('<int:pk>', BoxItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]