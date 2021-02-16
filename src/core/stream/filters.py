import django_filters
from .models import *


class StreamFilter(django_filters.rest_framework.FilterSet):
    start_time = django_filters.DateTimeFromToRangeFilter()
    end_time = django_filters.DateTimeFromToRangeFilter()
    
    class Meta:
        model = Stream
        fields = ['start_time','end_time','current','past']

