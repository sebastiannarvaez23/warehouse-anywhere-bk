import time

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from sentry.company.models import Company
from sentry.company.api.serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """Company view set."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company = Company.objects.create(
            nit=request.data['nit'],
            name=request.data['name'],
            domain=request.data['domain'],
            address=request.data['address'],
            country=request.data['country'],
            region=request.data['region'],
            city=request.data['city']
        )

        serializer = self.get_serializer(instance=company)
        return Response(serializer.data, status.HTTP_201_CREATED)