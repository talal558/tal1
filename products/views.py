from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    """
    عرض قائمة جميع المنتجات.
    """
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})


def product_detail(request, product_id):
    """
    عرض تفاصيل منتج معين بناءً على المعرّف.
    """
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
