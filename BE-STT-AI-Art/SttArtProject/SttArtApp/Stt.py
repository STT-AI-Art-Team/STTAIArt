from google.cloud import speech

## 음성을 텍스트로 변환하는 기능을 하는 함수
def stt_file(speech_file: str,) -> speech.RecognizeResponse:
    client = speech.SpeechClient()
    # GCS 요청 수행

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    # 오디오 파일 읽고, content로 파일 내용 읽음

    audio = speech.RecognitionAudio(content=content) # 오디오 파일 내용 설정
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code="ko-KR", # 음성 인식 설정
    )

    response = client.recognize(config=config, audio=audio)
    # 음성 인식 요청 수행

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    return response

speech_file = ["C:/안녕.wav" # chrome에서 녹음
, "C:/sample3.wav"]  # iphone 녹음기에서 녹음

for result in speech_file:
    stt_file(result)
    print(',')