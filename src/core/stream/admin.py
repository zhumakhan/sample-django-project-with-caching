from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = (
        'id','url', 'title', 'start_time',)
    search_fields = ('title',)
    ordering = ('-id',)

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = (
        'id','code', 'stream', 'email',)
    search_fields = ('code','email')
    ordering = ('-id',)
    list_filter = ('stream__title',)