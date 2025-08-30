from django.urls import path
from . import views

# تعريف اسم التطبيق (namespacing)
app_name = "products"

urlpatterns = [
    # عرض قائمة المنتجات
    path("", views.product_list, name="list"),  # http://127.0.0.1:8000/products/

    # عرض تفاصيل منتج محدد
    path("<int:pk>/", views.product_detail, name="detail"),  # http://127.0.0.1:8000/products/1/
]
