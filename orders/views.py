from django.shortcuts import render

def cart_view(request):
    return render(request, 'orders/cart.html')

def checkout_view(request):
    return render(request, 'orders/checkout.html')

def order_detail_view(request, order_id):
    return render(request, 'orders/order_detail.html', {'order_id': order_id})
