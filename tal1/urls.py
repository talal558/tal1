# tal1/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home  # دالة الصفحة الرئيسية

urlpatterns = [
    path("admin/", admin.site.urls),

    # ✅ اجعل الصفحة الرئيسية على جذر الموقع
    path("", home, name="home"),

    # ✅ روابط التطبيقات (أبقها فقط لو موجودة عندك)
    # تأكد أن لكل تطبيق ملف urls.py و namespace مطابق
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("products/", include(("products.urls", "products"), namespace="products")),
    path("orders/", include(("orders.urls", "orders"), namespace="orders")),
]

# ✅ أثناء التطوير: خدمة الملفات الثابتة والمرفوعة
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # ملاحظة: في الإنتاج يُفضّل استخدام Whitenoise أو CDN للـ staticfiles
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
