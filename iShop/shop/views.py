from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.form import CartAddProductForm


def main(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(available=True)[:4]
    recent_products = Product.objects.filter(available=True).order_by('-id')[:4]
    return render(request,
                  'shop/base.html',
                  {'categories': categories,
                   'featured_products': featured_products,
                   'recent_products': recent_products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})
