from django.urls import path
from box_item.api.api import BoxItemViewSet

urlpatterns = [
    path('<str:box>/', BoxItemViewSet.as_view({'get':'list'})),
    path('', BoxItemViewSet.as_view({'post':'create'})),
    #path('<int:pk>', BoxItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]