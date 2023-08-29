from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('seller-products',views.SellerProductViewset)


urlpatterns = [
    path('', include(router.urls))
]
