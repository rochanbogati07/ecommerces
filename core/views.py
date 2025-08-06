from django.shortcuts import render,redirect
from django.views import View
from .models import Product
from .models import Order
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Cart,Cartitem

class Homepage(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request,'core/index.html',{'products':products})
    
class Contact(View):
    def get(self,request):
        return render(request,'core/contact.html')
    
class Orderview(View):
    def get(self, request):
        query=Order.objects.all()
        return render(request, 'core/order.html', {'orders': query})
    
class Register(View):
    def get(self,request):
        return render(request, 'core/register.html')
    def post(self,request):
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {'error': 'Username already exists'})
        else:
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return render(request, 'core/register.html', {'success': 'Account created succesfully'})



class Login(View):
    def get(self, request):
        return render(request, 'core/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})


class Cartview(View):
    def get(self, request):
        user = request.user
        cart = Cart.objects.all().values('added_date', 'user__username')
        cartitems = Cartitem.objects.all().values(
            'product__name', 'quantity', 'colour', 'size', 'brand', 'data_added'
        )
        context = {
            'cart': cart,
            'cartitems': cartitems
        }
        return render(request, 'core/cart.html', context)
