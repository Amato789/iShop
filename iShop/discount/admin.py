from django.contrib import admin
from .models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount', 'valid_from', 'valid_to', 'active']
    list_filter = ['valid_from', 'valid_to', 'active']
    search_fields = ['product']
