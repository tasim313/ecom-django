from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = 'Default Category'
    list_display = ('id', 'title', 'price', 'discount_price', 'category',)
    search_fields = ('title', 'price', 'discount_price', 'category',)
    actions = ('change_category_to_default')
    list_editable = ('title', 'price', 'discount_price', 'category')


admin.site.register(Products, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'items', 'name')
    search_fields = ('items', 'name')


admin.site.register(Order, OrderAdmin)

admin.site.site_header = "Ecommerce Site"
admin.site.site_title = 'Online Shop'
admin.site.site_index = 'ABC Shopping'

