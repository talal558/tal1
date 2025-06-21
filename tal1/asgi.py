"""
ASGI config for tal1 project.

This file exposes the ASGI callable as a module-level variable named `application`.

For more information on this file, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# تحديد إعدادات المشروع
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tal1.settings")

# إنشاء تطبيق ASGI
application = get_asgi_application()
