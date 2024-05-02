from django.contrib import admin

from catalog.models import Product, Category, Blog


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price_of_product', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')
    prepopulated_fields = {'slug': ('product_name',)}


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'sign_of_publication', 'views_count')
    list_filter = ('sign_of_publication',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
