from django.contrib import admin
from django.urls import path, include
from products.views import product_list  # ← view العرض الرئيسي

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔹 هذا يجعل صفحة المنتجات الرئيسية تظهر على الرابط /
    path('', product_list, name='home'),

    # 🔹 هذا يربط المنتجات ببقية المسارات مع namespace
    path('products/', include(('products.urls', 'products'), namespace='products')),

    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
]

# 📦 دعم ملفات الصور والوسائط
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
