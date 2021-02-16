import os
from os.path import dirname, abspath, join
from types import MappingProxyType
from typing import Tuple

from corsheaders.defaults import default_methods, default_headers
from environ import Env


from .helpers.default_apps import DEFAULT_APPS
from .helpers.i18n_settings import (
    DEFAULT_LOCALE_PATHS, DEFAULT_LANGUAGES
)
from .helpers.middlewares import DEFAULT_MIDDLEWARES
from .helpers.rest_framework_settings import (
    REST_FRAMEWORK_SETTINGS
)
# from .helpers.channel_layers_settings import (
#     CHANNEL_LAYERS
# )
from .helpers.storages import STORAGES, DEFAULT_STORAGE
from .helpers.templates import DEFAULT_TEMPLATES
# from .helpers.simple_jwt_settings import SIMPLE_JWT
from .helpers.validators import DEFAULT_VALIDATORS

BASE_DIR: str = dirname(dirname(abspath(__file__)))
# Environment variables
env = Env()
Env.read_env()
# Sentry
# SENTRY_DSN: str = env.str(var='SENTRY_DSN')
# integrations: Tuple = (DjangoIntegration(), CeleryIntegration())
# init(dsn=SENTRY_DSN, integrations=integrations)
# Django
DEBUG:bool =  env.bool(var='DEBUG')
SECRET_KEY: str = env.str(var='SECRET_KEY')
APPEND_SLASH: bool = True
ALLOWED_HOSTS: Tuple = ('*',)
INSTALLED_APPS: Tuple = DEFAULT_APPS
MIDDLEWARE: Tuple = DEFAULT_MIDDLEWARES
ROOT_URLCONF: str = 'core.urls'
TEMPLATES: Tuple = DEFAULT_TEMPLATES
WSGI_APPLICATION: str = 'core.wsgi.application'
DATABASES: MappingProxyType = MappingProxyType({'default': env.db()})

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': "redis://redis:6379/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'example'
    }
}
AUTH_PASSWORD_VALIDATORS: Tuple = DEFAULT_VALIDATORS
AUTH_USER_MODEL = 'users.CustomUser'
#ASGI_APPLICATION = 'core.websocket.routing.application'



# Security
SECURE_BROWSER_XSS_FILTER: bool = True
SESSION_COOKIE_SECURE: bool = False
X_FRAME_OPTIONS: str = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF: bool = True
CSRF_COOKIE_SECURE: bool = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SIMPLE_JWT: Tuple = SIMPLE_JWT
# Localization
LOCALE_PATHS: Tuple = DEFAULT_LOCALE_PATHS
LANGUAGES: Tuple = DEFAULT_LANGUAGES
LANGUAGE_CODE: str = 'en'
USE_I18N: bool = True
USE_L10N: bool = True
TIME_ZONE: str = 'Asia/Almaty'
USE_TZ: bool = True

STATIC_URL: str = '/staticfiles/'
STATIC_ROOT: str = join(BASE_DIR, 'staticfiles')
MEDIA_URL: str = '/media/'
MEDIA_ROOT: str = join(BASE_DIR, 'media')

# Corsheaders
CORS_ORIGIN_ALLOW_ALL: bool = True
CORS_ALLOW_METHODS: Tuple = default_methods
CORS_ALLOW_HEADERS: Tuple = default_headers
CORS_ALLOW_CREDENTIALS: bool = True

# Rest framework
REST_FRAMEWORK: MappingProxyType = REST_FRAMEWORK_SETTINGS

# Channel Layer
# CHANNEL_LAYERS: MappingProxyType = CHANNEL_LAYERS

# Storage
# DEFAULT_FILE_STORAGE: str = STORAGES.get(
#     env.str(var='WHERE_TO_KEEP_MEDIA'), DEFAULT_STORAGE
# )
DEFAULT_FILE_STORAGE: str = STORAGES.get(
    env.str(var='WHERE_TO_KEEP_MEDIA'), DEFAULT_STORAGE
)
# AWS S3
# AWS_ACCESS_KEY_ID: str = env.str(var='AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY: str = env.str(var='AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME: str = env.str(var='AWS_STORAGE_BUCKET_NAME')
# AWS_AUTO_CREATE_BUCKET: bool = env.bool(var='AWS_AUTO_CREATE_BUCKET')
# AWS_DEFAULT_ACL: str = env.str(var='AWS_DEFAULT_ACL')
# AWS_BUCKET_ACL: str = env.str(var='AWS_BUCKET_ACL')
# AWS_S3_SIGNATURE_VERSION: str = env.str(var='AWS_S3_SIGNATURE_VERSION')
# AWS_S3_REGION_NAME: str = env.str(var='AWS_S3_REGION_NAME')
# AWS_S3_ENCRYPTION: bool = env.bool(var='AWS_S3_ENCRYPTION')

# Celery
CELERY_BROKER_URL: str = env.str(var='CELERY_BROKER_URL')
CELERY_RESULT_BACKEND: str = env.str(var='CELERY_RESULT_BACKEND')
CELERY_TIMEZONE: str = 'Asia/Almaty'
CELERY_ENABLE_UTC: bool = True
CELERY_ACCEPT_CONTENT: Tuple = ('application/json',)
CELERY_TASK_SERIALIZER: str = 'json'
CELERY_RESULT_SERIALIZER: str = 'json'
CELERY_TASK_ACKS_LATE: bool = True

# Email

# EMAIL_BACKEND = env.str("EMAIL_BACKEND")
# EMAIL_HOST = env.str("EMAIL_HOST")
# EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = env.int("EMAIL_PORT")
# EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST =  ''
EMAIL_HOST_USER =  ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT=587
EMAIL_USE_TLS=True
# SMS

# SMS_URL = 'https://service.sms-consult.kz/get.ashx'
# SMS_SENDER = 'MESSAGE'
# SMS_LOGIN = env.str(var='SMS_LOGIN')
# SMS_PASSWORD = env.str(var='SMS_PASSWORD')
# SMS_ACTIVATION_TEXT = 'Ваш код на платформе talcapital: {code}'
# SMS_ON = False
# ACTIVATION_TIME = 20
# Token expiration time
TOKEN_EXPIRED_AFTER_SECONDS = 900

DATA_UPLOAD_MAX_MEMORY_SIZE = 26214400  # 25Mb
FILE_UPLOAD_PERMISSIONS = 0o644

#PAYMENT 
#Cloufpayments
C_PUBLIC_ID =  env.str("C_PUBLIC_ID")
C_API_SECRET = env.str('C_API_SECRET')
C_CREATE_EMAIL_CHECK_URL = env.str('C_CREATE_EMAIL_CHECK_URL')

