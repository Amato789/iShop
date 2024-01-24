from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Rating
from cart.form import CartAddProductForm
from django.views import View
from .forms import ReviewForm


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
    categories = Category.objects.all()
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    form = ReviewForm()
    return render(
        request,
        'shop/product/detail.html',
        {'product': product, 'cart_product_form': cart_product_form, 'form': form, 'categories': categories}
    )


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.user = user
            form.save()
        return redirect(product.get_absolute_url())


def rate_product(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        prod = Product.objects.get(id=el_id)
        try:
            obj = Rating.objects.get(product=prod, user=request.user)
            obj.star = val
            obj.save()
        except Rating.DoesNotExist:
            Rating.objects.create(product=prod, user=request.user, star=val)

        return JsonResponse({'success': 'true', 'star': val}, safe=False)
    return JsonResponse({'success': 'false'})
