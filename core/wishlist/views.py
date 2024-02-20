from django.shortcuts import render, get_object_or_404, redirect
from .forms import WishlistAddForm
from core.shop.models import Product
from django.views.decorators.http import require_POST


@require_POST
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    form = WishlistAddForm(request.POST)
    if form.is_valid():
        wishlist = form.save(commit=False)
        wishlist.user = user
        wishlist.product = product
        wishlist.save()
    return redirect(request.META['HTTP_REFERER'])
