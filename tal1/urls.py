from django.contrib import admin
from django.urls import path, include
from products.views import product_list  # العرض الرئيسي للصفحة

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='home'),
    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
