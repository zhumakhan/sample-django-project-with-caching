import pytz
from django.conf import settings

LOCAL_TIME_ZONE = pytz.timezone(settings.TIME_ZONE)