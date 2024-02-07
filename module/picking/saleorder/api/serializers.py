from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from module.picking.saleorder.models import SaleOrder, Collection, PayTerm

class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name']
        
class PayTermSerializer(ModelSerializer):
    class Meta:
        model = PayTerm
        fields = ['id', 'name']
        
class SaleOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleOrder
        fields = [
            'id',
            'no_doc',
            'publication_date',
            'delivery_date',
            'doc_date',
            'po_comments',
            'customer_name',
            'delivery_address',
            'pay_term',
            'collection'
        ]
        
    def to_representation(self, instance):
        # Llamar a la implementación predeterminada del método to_representation
        ret = super().to_representation(instance)

        # Verificar si la solicitud es de tipo GET
        if self.context['request'].method == 'GET':
            # Incluir los campos adicionales solo en el caso de GET
            ret['pay_term'] = instance.pay_term.name
            ret['collection'] = instance.collection.name

        return ret