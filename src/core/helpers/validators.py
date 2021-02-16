from types import MappingProxyType
from typing import Tuple

BASE_MODULE = 'django.contrib.auth.password_validation'

DEFAULT_VALIDATORS: Tuple = (
    MappingProxyType({
        'NAME': f'{BASE_MODULE}.UserAttributeSimilarityValidator'
    }), MappingProxyType({
        'NAME': f'{BASE_MODULE}.MinimumLengthValidator'
    }), MappingProxyType({
        'NAME': f'{BASE_MODULE}.NumericPasswordValidator'
    }), MappingProxyType({
        'NAME': f'{BASE_MODULE}.CommonPasswordValidator'
    })
)
