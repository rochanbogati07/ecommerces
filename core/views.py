from django.shortcuts import render,redirect
from django.views import View
from .models import Product
from .models import Order
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Cart,Cartitem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

@login_required

def Homepage(request):
    
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
    def get(self, request):
        return render(request, 'core/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists ❌")
            return redirect('register')  # ✅ redirect so message shows
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Account created successfully 🎉 You can now log in.")
            return redirect('login')  # ✅ redirect to login page


class Login(View):
    def get(self, request):
        return render(request, 'core/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully ✅")  # ✅ this runs before redirect
            return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password ❌")  # ✅ add error message
            return redirect('login')  # redirect so message displays

class Cartview(View):
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=request.user)
        cartitems = Cartitem.objects.all().values(
            'product__name', 'quantity', 'colour', 'size', 'brand', 'data_added'
        )
        context = {
            'cart': cart,
            'cartitems': cartitems
        }
        return render(request, 'core/cart.html', context)
    


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cartitem.objects.get_or_create(
        user=request.user,            # 👈 assign current user
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.name} added to your cart 🛒")
    return redirect('cart_view')

def cart_view(request):
    cart_items = Cartitem.objects.filter(user=request.user)  # 👈 only user’s items
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'core/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

