from django.urls import path
from .views import Homepage,Contact
from .views import Register,Login, Orderview, Cartview

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('contact/', Contact.as_view(), name="contact"),
    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('order/', Orderview.as_view(), name="order"),
    path('cartitem/',Cartview.as_view(), name="cartitem"),
]