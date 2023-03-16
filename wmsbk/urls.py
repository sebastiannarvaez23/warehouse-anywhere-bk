from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de API",
      default_version='v0.1',
      description="Documentación pública de API de WMS",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="narvaezsebas8@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),
    path('picking/', include('module.picking.picking.api.urls')),
    path('box/', include('module.picking.box.api.urls')),
    path('boxitem/', include('module.picking.boxitem.api.urls')),
    path('saleorder/', include('module.picking.saleorder.api.urls')),
    path('saleorderitem/', include('module.picking.saleorderitem.api.urls')),
    path('registration/', include('sentry.registration.api.urls')),
    path('company/', include('sentry.company.api.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]