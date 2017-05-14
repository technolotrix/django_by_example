from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from cart.views import cart_detail

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
        id=id,
        slug=slug,
        available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
        'shop/product/detail.html',
            {'product': product,
            'cart_product_form': cart_product_form})

def product_list(request, category_slug=None):
    category = None
    if category_slug == 'cart':
        return cart_detail(request)

    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
        'shop/product/list.html',
            {'category': category,
                'categories': categories,
                'products': products})
