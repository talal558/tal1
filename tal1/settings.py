from pathlib import Path
from decouple import config, Csv
import os

# =========================
# المسار الأساسي للمشروع
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# مفاتيح وأوضاع التشغيل
# =========================
SECRET_KEY = config('SECRET_KEY', default='django-insecure-dummy-key')
DEBUG = config('DEBUG', default=True, cast=bool)

# =========================
# المضيفون المسموح لهم + دعم Render
# =========================
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost,.onrender.com',
    cast=Csv()
)

# Render قد يوفّر هذا المتغير تلقائياً
RENDER_EXTERNAL_HOSTNAME = os.getenv('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME and RENDER_EXTERNAL_HOSTNAME not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# =========================
# CSRF Trusted Origins (ذكي: إنتاج + محلي)
# =========================
CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='https://*.onrender.com',
    cast=Csv()
)
if DEBUG:
    for origin in ('http://127.0.0.1', 'http://localhost'):
        if origin not in CSRF_TRUSTED_ORIGINS:
            CSRF_TRUSTED_ORIGINS.append(origin)

# =========================
# التحقق من توفر Whitenoise (مرن)
# =========================
try:
    import whitenoise  # noqa: F401
    _WHITENOISE = True
except Exception:
    _WHITENOISE = False

# =========================
# التطبيقات المثبتة
# =========================
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات المحلية
    'accounts',
    'products',
    'orders',

    # مكتبات خارجية
    'cloudinary',
    'cloudinary_storage',
]

# =========================
# الميدلوير (مع تفعيل Whitenoise فقط إذا متاح)
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]
if _WHITENOISE:
    # تقديم الملفات الثابتة بكفاءة في الإنتاج
    MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
MIDDLEWARE += [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# خلف بروكسي Render حتى يتعرّف Django على HTTPS من X-Forwarded-Proto
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# =========================
# روابط المشروع
# =========================
ROOT_URLCONF = 'tal1.urls'
APPEND_SLASH = True

# =========================
# إعدادات القوالب
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # إن أردت أزرار الهيدر ديناميكية أضف:
                # 'tal1.context_processors.nav_buttons',
            ],
        },
    },
]

# =========================
# WSGI
# =========================
WSGI_APPLICATION = 'tal1.wsgi.application'

# =========================
# قاعدة البيانات (مرنة: DATABASE_URL > مفاتيح صريحة > SQLite)
# =========================
DATABASES = {}
_DATABASE_URL = os.getenv('DATABASE_URL')  # يدعمه Render وخدمات أخرى
if _DATABASE_URL:
    try:
        import dj_database_url
        DATABASES['default'] = dj_database_url.parse(
            _DATABASE_URL, conn_max_age=600, ssl_require=not DEBUG
        )
    except Exception:
        # لو dj-database-url غير مثبت، نرجع للخيار التالي
        _DATABASE_URL = None

if not _DATABASE_URL and not DEBUG:
    # PostgreSQL بالإنتاج عند توفر المفاتيح
    name = config('DB_NAME', default=None)
    user = config('DB_USER', default=None)
    password = config('DB_PASSWORD', default=None)
    host = config('DB_HOST', default=None)
    port = config('DB_PORT', default='5432')
    if all((name, user, password, host)):
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': name,
            'USER': user,
            'PASSWORD': password,
            'HOST': host,
            'PORT': port,
        }

if 'default' not in DATABASES:
    # SQLite للتطوير (وأيضًا كخيار احتياطي)
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

# =========================
# التحقق من كلمات المرور
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================
# الإعدادات الدولية
# =========================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# =========================
# الملفات الثابتة (Static)
# =========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']              # أثناء التطوير
STATIC_ROOT = BASE_DIR / 'staticfiles'                # لـ collectstatic في الإنتاج
if _WHITENOISE and not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# =========================
# الملفات المرفوعة (Media)
# =========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =========================
# Cloudinary (رفع وسائط)
# =========================
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default='your_cloud_name'),
    'API_KEY': config('CLOUDINARY_API_KEY', default='your_api_key'),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default='your_api_secret'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# =========================
# إعدادات أمان الإنتاج
# =========================
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE   = config('CSRF_COOKIE_SECURE',   default=False, cast=bool)

SECURE_HSTS_SECONDS = 31536000 if (not DEBUG and SECURE_SSL_REDIRECT) else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG and SECURE_SSL_REDIRECT
SECURE_HSTS_PRELOAD = not DEBUG and SECURE_SSL_REDIRECT

# =========================
# نوع الحقول التلقائية
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# الكاش (تحسين محلي بسيط)
# =========================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "tal1-local-cache"
    }
}

# =========================
# تسجيل الأخطاء (Logging)
# =========================
LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[{levelname}] {asctime} {name}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {'class': 'logging.StreamHandler', 'formatter': 'simple'},
    },
    'root': {'handlers': ['console'], 'level': LOG_LEVEL},
}
