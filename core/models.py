from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/products/')
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'{self.name} - the price is {self.price}'
    
    
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    added_date=models.DateTimeField(auto_now=True)

    def __str__(self)-> str:
        return f'cart of {self.user.username} - last updated on {self.added_date}'

class Cartitem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 👈 link each cart item to a user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity}) - {self.user.username}"
    
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.ForeignKey(Cartitem, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    customer_name=models.CharField(max_length=100)
    customer_email=models.EmailField()

    def __str__(self) -> str:
        return f'Order for {self.product.name} - {self.quantity} units by {self.customer_name}'
    
