from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='list'),  # عرض كل الطلبات
    path('cart/', views.cart_view, name='cart'),  # سلة المشتريات
    path('checkout/', views.checkout_view, name='checkout'),  # صفحة الدفع
    path('<int:order_id>/', views.order_detail, name='detail'),  # تفاصيل الطلب
]
