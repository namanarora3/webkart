from rest_framework import serializers

from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'seller', 'name', 'price',
            'description', 'quantity', 'discount'
        ]
        read_only_fields = ['id', 'seller']
        # extra_kwargs = {
        #     'seller': {'required': False}
        # }

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        seller = validated_data.pop('seller',None)
        if seller:
            return ValueError({'error': 'cannot update seller'})
        return super().update(instance, validated_data)

