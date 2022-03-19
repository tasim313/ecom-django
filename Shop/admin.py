from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discount_price', 'category' ,)


admin.site.register(Products, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'items', 'name')


admin.site.register(Order, OrderAdmin)