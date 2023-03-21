from pathlib import Path
import environ

# ENVIRON CONF

env = environ.Env()
environ.Env.read_env()

# ---

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = ['*']

# CORS HTTPONLY CONF ---
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
CORS_ORIGIN_REGEX_WHITELIST = [
    r'localhost:3000',
]
CORS_EXPOSE_HEADERS = ['Content-Type', 'Authorization']
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False

# ---

# APPS THIRD 

THIRD_APPS = [
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
]

# -- TENANT CONF

MULTI_TENANT = True
TENANT_MODEL = "company.Company"
TENANT_DOMAIN_MODEL = "company.Domain"
PUBLIC_SCHEMA_NAME = "public"

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

SHARED_APPS = [
    'django_tenants',
    'sentry.company',
    'sentry.registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
] + THIRD_APPS

TENANT_APPS = [
    'module.storage.reference',
    'module.picking.box',
    'module.picking.picking',
    'module.picking.saleorder',
    'module.picking.boxitem',
    'module.picking.saleorderitem'
]

# ---

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

# SSL / TLS CONF

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
if DEBUG:
    INSTALLED_APPS += ['sslserver']
    # Puedes configurar el puerto y las rutas que desees.
    # En este ejemplo, se ejecuta en el puerto 8000 con SSL/TLS activado.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SSLCERTIFICATE = '/path/to/cert.pem'
    SSLKEY = '/path/to/key.pem'
# ---

# DRF CONF

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':(
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# ---

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

ROOT_URLCONF = 'wmsbk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wmsbk.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'registration.User'


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'