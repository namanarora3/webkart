# add item to cart
# remove item from cart
# list a users cart

from rest_framework.views import APIView

from .serializers import CartItemSerializer, CartUpdateSerializer

from rest_framework.response import Response
from rest_framework import status, permissions

from core.models import CartItem, Product

from core.permissions import IsSeller

from decimal import Decimal


class UpdateCartItem(APIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated, ~IsSeller]

    def get(self, request):
        user = request.user
        items = CartItem.objects.filter(
            user=request.user
        )
        serializer = CartItemSerializer(items, many=True)
        # if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = CartUpdateSerializer(data=request.data)

        if serializer.is_valid():
            # get product
            try:
                product = Product.objects.get(
                    id=serializer.data['product']
                )
            except:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            # get quantity and check
            try:
                qty = serializer.data['quantity']
            except:
                return Response({'error': 'Please provide quantity'}, status=status.HTTP_400_BAD_REQUEST)
            if qty > getattr(product, 'quantity'):
                return Response(
                    {'error': 'qty should be less than available qty of product',
                     'max_qty': getattr(product, 'quantity')
                     },
                    status=status.HTTP_404_NOT_FOUND
                )

            item, created = CartItem.objects.get_or_create(
                product=product,
                user=user
            )
            if qty == 0:
                item.delete()
            else:
                setattr(item, 'quantity', qty)
                item.save()
            return self.get(request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartTotalView(APIView):
    permission_classes = [permissions.IsAuthenticated, ~IsSeller]

    def get(self, request):
        user = request.user
        items = CartItem.objects.filter(
            user=request.user
        )
        total = 0
        for item in items:
            total += Decimal(getattr(getattr(item, 'product'),
                             'price'))*getattr(item, 'quantity')
            print(total)
        return Response({'total': total}, status.HTTP_200_OK)
