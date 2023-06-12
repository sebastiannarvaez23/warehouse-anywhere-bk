import time

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# local apps
from sentry.company.models import Company, Domain
from sentry.company.api.serializers import CompanySerializer
from wmsbk.customs.mixins import APIMixin

# decorators
from wmsbk.decorators.response import add_consumption_detail_decorator


class CompanyViewSet(APIMixin, viewsets.ModelViewSet):
    """Company view set."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @add_consumption_detail_decorator
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        company = kwargs.get('nitcompany')
        self.queryset = self.queryset.filter(nit=company)

        if not company:
            return self.custom_response_404(response)
        
        response = self.custom_response_200(response, response.data[0])
        return response

    @add_consumption_detail_decorator
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
        domain.domain = request.data['schema_name'] + ".localhost"
        domain.is_primary = True
        domain.tenant = company
        domain.save()
        serializer = self.get_serializer(instance=company)
        response = self.custom_response_201(Response(serializer.data, status.HTTP_201_CREATED))
        
        return response
