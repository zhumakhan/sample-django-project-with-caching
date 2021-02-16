from typing import Tuple

DEFAULT_APPS: Tuple = (
    # django apps
    'django.contrib.admin', 
    'django.contrib.staticfiles',
    'django.contrib.contenttypes', 
    'django.contrib.auth',
    'django.contrib.messages', 
    'django.contrib.sessions',
    # side apps
    'corsheaders',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    #'channels',
    
    # project apps
    'core.users', 
    'core.stream',
    'core.payment',
)
