from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    """
    عرض قائمة جميع المنتجات.
    - يجلب جميع المنتجات من قاعدة البيانات.
    - يعرضها داخل القالب: templates/products/products_list.html
    """
    products = Product.objects.all().order_by('-id')  # عرض الأحدث أولاً
    context = {
        'products': products,
    }
    return render(request, 'products/products_list.html', context)


def product_detail(request, product_id):
    """
    عرض تفاصيل منتج محدد.
    - يجلب المنتج المطلوب بالمعرّف (ID).
    - إذا لم يتم العثور عليه، يظهر صفحة خطأ 404.
    - يعرض تفاصيل المنتج داخل القالب: templates/products/product_detail.html
    """
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
