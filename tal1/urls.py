from django.contrib import admin
from django.urls import path, include
from products.views import product_list  # ← العرض الرئيسي للصفحة
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة التحكم الإدارية
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية تعرض قائمة المنتجات
    path('', product_list, name='home'),

    # روابط التطبيقات بمسارات فرعية
    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
]

# دعم تحميل ملفات الوسائط (صور/مرفقات) في بيئة التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
