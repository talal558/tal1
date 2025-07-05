from django.shortcuts import render
from django.http import Http404


def order_list(request):
    """
    عرض قائمة جميع الطلبات.
    """
    try:
        # ملاحظة: ستقوم لاحقًا بإضافة الاستعلامات من قاعدة البيانات
        orders = []  # حالياً قائمة وهمية
        context = {'orders': orders}
        return render(request, 'orders/order_list.html', context)
    except Exception:
        raise Http404("قالب order_list.html غير موجود.")


def cart_view(request):
    """
    عرض صفحة سلة المشتريات.
    """
    try:
        return render(request, 'orders/cart.html')
    except Exception:
        raise Http404("قالب cart.html غير موجود.")


def checkout_view(request):
    """
    عرض صفحة الدفع (إتمام الطلب).
    """
    try:
        return render(request, 'orders/checkout.html')
    except Exception:
        raise Http404("قالب checkout.html غير موجود.")


def order_detail(request, order_id):
    """
    عرض تفاصيل طلب معين.
    """
    try:
        context = {'order_id': order_id}
        return render(request, 'orders/order_detail.html', context)
    except Exception:
        raise Http404("قالب order_detail.html غير موجود.")
