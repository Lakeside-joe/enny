from django.contrib import admin
from .models import Shopcart

# Register your models here.
@admin.register(Shopcart)
class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['user', 'style', 'c_name', 'quantity', 'c_price', 'amount', 'cart_code', 'paid']
