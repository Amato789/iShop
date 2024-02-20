from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'message', 'created', 'is_checked']
    list_filter = ['user', 'is_checked']
