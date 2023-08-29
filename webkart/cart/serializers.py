from rest_framework import serializers

from core.models import CartItem

from product.serializers import ProductSerializer

class CartUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

class CartItemSerializer(CartUpdateSerializer):
    product = ProductSerializer()


