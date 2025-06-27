from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
from django.contrib import admin
from django.urls import path, include
from products.views import product_list  # ← العرض الرئيسي للصفحة

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

# دعم تحميل ملفات الوسائط (صور/مرفقات)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
