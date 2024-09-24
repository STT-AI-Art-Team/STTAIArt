import datetime
from django.db import models

# Create your models here.
class Recording(models.Model):
    title = models.CharField(max_length=200)
    # 녹음 파일 제목 저장
    wavFilePath = models.FileField(upload_to='recordings/', default = 'default.wav')
    # 녹음 파일 위치 저장
    recording_date = models.DateTimeField('date published' , default=datetime.datetime.now)
    # 녹음 파일 날짜 및 시간 저장

    # 제목으로 저장
    def __str__(self):
        return self.title