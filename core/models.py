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
    carts=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField() 
    colour=models.CharField(null=True, blank=True, max_length=50, default='Black')
    size=models.CharField( blank=True, null=True,max_length=10, choices=[
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    ])
    brand=models.CharField(blank=True, null=True,max_length=100, choices=[
        ('Nike', 'Nike'),
        ('Adidas', 'Adidas'),
        ('Puma', 'Puma'),
        ('Reebok', 'Reebok')
    ])
    data_added=models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:
        return f'{self.product.name} - {self.quantity} added on {self.data_added}'
    
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.ForeignKey(Cartitem, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    customer_name=models.CharField(max_length=100)
    customer_email=models.EmailField()

    def __str__(self) -> str:
        return f'Order for {self.product.name} - {self.quantity} units by {self.customer_name}'
    