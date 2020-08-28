from django.contrib import admin

from shop.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'image', 'description',
                    'available_display', 'available_order', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)