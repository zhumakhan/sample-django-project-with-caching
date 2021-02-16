from __future__ import (
    absolute_import, unicode_literals
)

from datetime import datetime
from os import environ

from celery import Celery
from django.utils.timezone import localtime

environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


class MyCelery(Celery):
    def now(self) -> datetime:
        return localtime()


celery_app = MyCelery('core')
celery_app.config_from_object(
    obj='django.conf:settings', namespace='CELERY'
)
celery_app.autodiscover_tasks()
