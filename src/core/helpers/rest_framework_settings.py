from types import MappingProxyType

PAGINATION_CLASS: str = 'rest_framework.pagination.LimitOffsetPagination'

REST_FRAMEWORK_SETTINGS: MappingProxyType = MappingProxyType({
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'core.users.middleware.ExpiringTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAdminUser',
    ), 'DEFAULT_FILTER_BACKENDS': (),
    'DEFAULT_PAGINATION_CLASS': PAGINATION_CLASS, 'PAGE_SIZE': 8
})
