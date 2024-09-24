from django.shortcuts import render, HttpResponse
from .models import Recording
# models.py의 Recording을 불러와서 파일 정보를 저장
# 사용자가 업로드한 음성과 stt 결과를 저장함
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

# Create your views here.
class ClassCodeCheck(APIView):
    def post(self, request):
        input_code = request.data.get('classCode')
        correct_code = '123456789'  # 올바른 코드를 설정

        if input_code == correct_code:
            return Response({"message": "올바른 코드입니다.", "redirect": True}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "잘못된 코드입니다. 다시 입력해주세요.", "redirect": False}, status=status.HTTP_400_BAD_REQUEST)

class uploadRecording(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        title = request.data.get('title', 'Untitled')
        # 녹음의 제목을 받아옴. 제목이 입력되지 않았을 시 Untitled
        file = request.FILES['file']
        # 오디오 파일 받아옴

        # 모델 인스턴스 생성 및 DB에 저장
        recording = Recording.objects.create(title=title, wavFilePath=file)

        return Response({'message': '파일 업로드 성공', 'file_url': recording.file.url})