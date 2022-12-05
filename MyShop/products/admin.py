from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug', 'category_image']

class ProductImageAdmin(admin.StackedInline):
    model = productImage

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['product_name', 'slug', 'category', 'price']


@admin.register(variationValue)
class VariationValueAdmin(admin.ModelAdmin):
    list_display = ['variation', 'name', 'product', 'price']