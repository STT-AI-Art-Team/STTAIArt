from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Recording)
# class RecordingAdmin(admin.ModelAdmin):
#     list_display = ('title', 'wavFilePath')
#     # 녹음 파일을 관리

