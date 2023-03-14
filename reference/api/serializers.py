from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from picking.picking.models import Picking

class ReferenceSerializer(ModelSerializer):
    reference = serializers.CharField(required=False)
    modelsize = serializers.CharField(required=False)
    color = serializers.PrimaryKeyRelatedField(source='color.name', read_only=True)
    
    class Meta:
        model = Picking
        fields = (
            'id',
            'item_code',
            'name',
            'model_size',
            'color',
        )