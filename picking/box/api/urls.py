# Django
from django.urls import path, include

# DRF
from rest_framework import routers

# Local Apps
from picking.box.api.api import BoxViewSet, DimensionViewSet

router = routers.DefaultRouter()
router.register(r'', DimensionViewSet)

urlpatterns = [
    path('box/<str:picking>/', BoxViewSet.as_view({'get':'list'})),
    path('dimension/', include(router.urls)),
    path('box/', BoxViewSet.as_view({'post':'create'})),
    path('box/<int:pk>', BoxViewSet.as_view({'patch': 'partial_update', 'delete': 'destroy'})),
    #path('<int:pk>', BoxViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]