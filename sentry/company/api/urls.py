from django.urls import path
from sentry.company.api.api import CompanyViewSet

urlpatterns = [
    path('', CompanyViewSet.as_view({'post': 'create'})),
]