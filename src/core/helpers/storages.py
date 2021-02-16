from types import MappingProxyType

DEFAULT_STORAGE: str = 'django.core.files.storage.FileSystemStorage'

STORAGES: MappingProxyType = MappingProxyType({
    'LOCAL': DEFAULT_STORAGE,
    'AWS_S3': 'storages.backends.s3boto3.S3Boto3Storage'
})
