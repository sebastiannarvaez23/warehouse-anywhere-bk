from rest_framework import serializers
from sentry.company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'schema_name',
            'nit',
            'name',
            'address',
            'country',
            'state',
            'city'
        )