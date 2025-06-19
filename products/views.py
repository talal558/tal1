from django.shortcuts import render, get_object_or_404
from .models import Product  # تأكد من وجود هذا الموديل

# عرض جميع المنتجات
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})

# عرض تفاصيل منتج واحد
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
