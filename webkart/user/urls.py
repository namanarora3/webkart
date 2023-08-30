from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register('address', views.ManageAddressViewSet)

urlpatterns = [
  path('create/', views.CreateUserView.as_view(), name='create'),
  path('authenticate/', views.CreateTokenView.as_view(), name='authenticate'),
  path('my-profile/', views.ManageUserView.as_view(), name='my-profile'),
  path('address/', include(router.urls)),

]
