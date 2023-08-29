from .serializers import ProductSerializer

from core.models import Product

from rest_framework import mixins, permissions, viewsets

from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_seller)


class PublicProductViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, ~IsSeller]
    # lookup_field = 'name' by default ID

    def get_queryset(self,*args, **kwargs):
        return self.queryset

class SellerProductViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    PublicProductViewset
  ):
    permission_classes = [permissions.IsAuthenticated, IsSeller]

    def get_queryset(self):
        return self.queryset.filter(seller=self.request.user)

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


