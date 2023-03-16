from rest_framework import serializers
from sentry.company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'nit',
            'name',
            'domain',
            'address',
            'country',
            'region',
            'city'
        )