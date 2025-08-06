from django.contrib import admin
from .models import Product,Cart,Order
from .models import Cartitem
from .models import Account

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name', 'colour')

admin.site.register(Product, ProductAdmin)
admin.site.register(Cartitem)
admin.site.register(Cart)
admin.site.register(Order)
from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number')  # optional
