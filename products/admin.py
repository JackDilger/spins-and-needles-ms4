from django.contrib import admin
from .models import Product, Genre


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'price',
        'genre',
        'image',
    )

    ordering = ('sku',)

class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product)
admin.site.register(Genre)
