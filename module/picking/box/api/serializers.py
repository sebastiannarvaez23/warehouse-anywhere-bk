from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from module.picking.box.models import Box, Dimension

class BoxSerializer(ModelSerializer):
    last_modification = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    dimension = serializers.PrimaryKeyRelatedField(source='dimension.name', read_only=True)
    gross_weight = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    responsible = serializers.CharField(required=False)

    class Meta:
        model = Box
        fields = (
            'id',
            'last_modification',
            'gross_weight',
            'responsible',
            'dimension',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['responsible'] = f'{instance.responsible.first_name} {instance.responsible.last_name}'
        return representation

class DimensionSerializer(ModelSerializer):
    class Meta:
        model = Dimension
        fields = '__all__'