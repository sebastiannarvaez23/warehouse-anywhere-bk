# restframework
from rest_framework import viewsets

# local apps
from reference.models import Reference
from reference.api.serializers import ReferenceSerializer

class ReferenceViewSet(viewsets.ModelViewSet):
    """Box Item view set"""
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer