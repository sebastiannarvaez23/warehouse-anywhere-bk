from rest_framework import serializers
from module.picking.picking.models import Picking

class PickingSerializer(serializers.ModelSerializer):
    last_modification = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    status = serializers.CharField(source='status.name', required=False)
    responsible = serializers.CharField(required=False)
    
    class Meta:
        model = Picking
        fields = ('id', 'last_modification', 'status', 'responsible')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['responsible'] = f'{instance.responsible.first_name} {instance.responsible.last_name}'
        return representation