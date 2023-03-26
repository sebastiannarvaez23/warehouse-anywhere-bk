import time

# Django
from django.core.exceptions import PermissionDenied

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from sentry.company.models import Company, Domain
from sentry.company.api.serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """Company view set."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        company = kwargs.get('nitcompany')
        if company is not None:
            try:
                self.queryset = self.queryset.filter(nit = company)
                response = super().list(request, *args, **kwargs)
                response.data = response.data[0]
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        if not company:
            raise PermissionDenied('A nosaleorder parameter is required.')
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company = Company.objects.create(
            schema_name=request.data['schema_name'],
            nit=request.data['nit'],
            name=request.data['name'],
            address=request.data['address'],
            country=request.data['country'],
            state=request.data['state'],
            city=request.data['city']
        )

        domain = Domain()
        domain.domain = request.data['schema_name']
        domain.is_primary = True
        domain.tenant = company
        domain.save()

        serializer = self.get_serializer(instance=company)
        return Response(serializer.data, status.HTTP_201_CREATED)