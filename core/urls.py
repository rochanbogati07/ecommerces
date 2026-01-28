from django.urls import path
from .views import (
    Homepage, Contact, Register, Login, Orderview, Cartview,
    cart_view, add_to_cart)

urlpatterns = [
    path('', Homepage, name="homepage"),
    path('contact/', Contact.as_view(), name="contact"),
    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('order/', Orderview.as_view(), name="order"),
    path('cartitem/', Cartview.as_view(), name="cartitem"),

    path('cart/', cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    
]
