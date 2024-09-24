from django.urls import path
from . import views

urlpatterns = [
    path('api/check-code/', views.ClassCodeCheck.as_view(), name='check-code'),
    # path('upload/', views.uploadRecording.as_view(), name='upload-recording'),
]
