from django.contrib import admin

# Register your models here.
from .models import Product, Service, Shop, School, Review, Request, House


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'charge')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(School)
admin.site.register(Review)
admin.site.register(House)



@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'min_price', 'max_price', 'description')
    search_fields = ('title',)

