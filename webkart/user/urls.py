from django.urls import path

from user import views

urlpatterns = [
  path('create/', views.CreateUserView.as_view(), name='create'),
  path('authenticate/', views.CreateTokenView.as_view(), name='authenticate'),
  path('my-profile/', views.ManageUserView.as_view(), name='my-profile'),
]
