from django.contrib import admin
from .models import Wishlist
from shop.models import Product


# class WishlistItemInline(admin.TabularInline):
#     model = Product
#     raw_id_fields = ['product']


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'product']
    list_filter = ['user', ]
    # inlines = [WishlistItemInline]
