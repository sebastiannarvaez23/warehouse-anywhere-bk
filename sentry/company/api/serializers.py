from rest_framework import serializers
from sentry.company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name', required=False)
    
    class Meta:
        model = Company
        fields = (
            'nit',
            'name',
            'domain',
            'address',
            'city',
        )