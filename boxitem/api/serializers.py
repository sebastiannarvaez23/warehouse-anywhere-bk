from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from boxitem.models import BoxItem

class BoxItemSerializer(ModelSerializer):
    reference = serializers.CharField(source='reference.item_code')
    modelsize = serializers.CharField(source='reference.model_size', read_only=True)
    color = serializers.CharField(source='reference.color', read_only=True)
    
    class Meta:
        model = BoxItem
        fields = (
            'id',
            'reference',
            'quantity',
            'box',
            'modelsize',
            'color',
        )
