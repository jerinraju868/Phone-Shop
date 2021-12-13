from django.contrib import admin

# Register your models here.
from jshop_app.models import Category, Product


class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CatAdmin)


class ProdAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'desc', 'price', 'stock', 'img']
    list_editable = ['desc', 'price', 'stock', 'img']

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProdAdmin)
