"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import braintree
import mimetypes
from decouple import config


mimetypes.add_type("text/css", ".css", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR3 =  Path(__file__).resolve(strict=True).parent.parent #aslinda boyleydi. ecommerce'in icinde bi tane daha ecommerce acinca bi parenti silmek gerekti. eger setting.py sonrada olusturulan ecommerce klasorunden cikartilacaksa iki tane parent yazan kullanilacak veya parents[1] yazilacak
BASE_DIR4 =  Path(__file__).resolve(strict=True).parent.parent.parent

BASE_DIR = BASE_DIR3 / 'settings'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

#SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!


SITE_ID = 2
#ALLOWED_HOSTS = ['165.22.33.200','msrugs.com','www.msrugs.com']

AUTH_USER_MODEL = 'account.Customers'

# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_celery_beat',
    'django_celery_results',
    'debug_toolbar',

    'rest_framework',
    'rest_framework.authtoken',

    'allauth',
    

    'rest_auth',
    'rest_auth.registration',

    'storages',
    'phonenumber_field',
    'localflavor',
    'corsheaders',
    'ckeditor',
    'import_export',
    'editorjs_field',

    'payment.apps.PaymentConfig',
    "products",
    "account",
    "blog",
    "cart",
    'orders',
    'coupons.apps.CouponsConfig',
    'Delivery',
    'marketing',   
    'ship_station'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR4 / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                'products.context_processor.menu',
            ],
        },
    },
]

AUTH_USER_MODEL = 'account.Customers'

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATICFILES_DIRS = [
    BASE_DIR4 / "static_my_proj",
]

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR4, 'static_cdn', 'static_root')



LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'US'


ADMINS = (('EMRE','konakziyaemre@gmail.com'),)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'SAM&M Trade Team <noreply@samnmtrade.com>'

CART_SESSION_ID = 'cart'


CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Braintree settings
BRAINTREE_MERCHANT_ID = config('BRAINTREE_MERCHANT_ID')  # Merchant ID
BRAINTREE_PUBLIC_KEY = config('BRAINTREE_PUBLIC_KEY')   # Public Key
BRAINTREE_PRIVATE_KEY = config('BRAINTREE_PRIVATE_KEY')  # Private key

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

SESSION_ENGINE = "django.contrib.sessions.backends.db"
#SESSION_SAVE_EVERY_REQUEST = False

# CORS_REPLACE_HTTPS_REFERER      = True
# HOST_SCHEME                     = "https://"
# SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT             = False
# SESSION_COOKIE_SECURE           = True
# CSRF_COOKIE_SECURE              = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
# SECURE_HSTS_SECONDS             = 1000000
# SECURE_FRAME_DENY               = True

STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')
STRIPE_PRIVATE_KEY = config('STRIPE_PRIVATE_KEY')

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-csrf-token',
]

CORS_ORIGIN_ALLOW_ALL=True

CORS_ORIGIN_WHITELIST = [
    "https://msrugs.com",
    "https://samnmtrade.com",
    
]

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CKEDITOR_UPLOAD_PATH = "uploads"

IMPORT_EXPORT_USE_TRANSACTIONS = True

EMAIL_SUBJECT_PREFIX = 'SAM&M - '

CELERY_IMPORTS = (
    'orders.tasks',
    'account.tasks',
)



DEBUG_TOOLBAR_PANELS = [
    #'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]