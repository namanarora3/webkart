from django.urls import path

from cart import views

urlpatterns = [
    path('user-cart/', views.UpdateCartItem.as_view()),
    path('cart-total/', views.CartTotalView.as_view()),
]
