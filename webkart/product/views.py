from .serializers import ProductSerializer

from core.models import Product

from rest_framework import mixins, permissions, viewsets

from core.permissions import IsSeller, IsBuyer


class PublicProductViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBuyer]
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


