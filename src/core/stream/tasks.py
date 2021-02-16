from __future__ import absolute_import, unicode_literals
from datetime import datetime

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task, task
from .models import Stream
from ..helpers.local_time import LOCAL_TIME_ZONE


@periodic_task(run_every=(crontab(minute='*/1')), name="update_stream_state", ignore_result=True)
def update_stream_state():
	now = datetime.now().astimezone(LOCAL_TIME_ZONE)
	print(now)
	Stream.objects.filter(end_time__lt=now).update(past=True,current=False)
	Stream.objects.filter(start_time__lt=now,end_time__gt=now).update(current=True,past=False)
