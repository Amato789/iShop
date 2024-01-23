from django.contrib import admin
from .models import Category, Product, Brand, ProductImages, Review, Rating
from django.utils.safestring import mark_safe


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100">')

    get_image.short_description = "Изображение"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'available', 'created', 'updated']
    inlines = [ProductImagesInline]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'product']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'product', 'parent', 'text']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'star']
