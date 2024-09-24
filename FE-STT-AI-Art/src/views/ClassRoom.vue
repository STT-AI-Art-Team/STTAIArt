<template>
  <div>
    <header class="header">
      <!-- App.vue에서 정의한 헤더를 가져옵니다 -->
    </header>
    <main class="main-content">
      <h1>녹음의 제목을 적어주세요.</h1>
      <p>원하는 그림을 표현하는 창의적인 제목을 지어보세요!</p>
      
      <!-- 제목 입력 필드 -->
      <input 
        v-model="recordingTitle" 
        type="text" 
        placeholder="녹음 제목을 입력하세요" 
        class="title-input"
      />

      <!-- 녹음 버튼 (제목 입력 필드 아래로 이동) -->
      <button @click="toggleRecording" class="record-button">
        <img :src="recording ? require('@/assets/recording.png') : require('@/assets/precord.png')" alt="Recording Icon">
      </button>

      <!-- 녹음 시간 표시 -->
      <p class="time-display">{{ formatTime(elapsedTime) }}</p>

      <!-- 녹음 전송 버튼 -->
      <button @click="saveRecording" class="save-button" :disabled="!audioChunks.length">
        녹음 전송
      </button>
    </main>
  </div>
</template>

<script>
export default {
  name: 'ClassRoom',
  data() {
    return {
      recordingTitle: '', // 녹음 제목
      mediaRecorder: null, // MediaRecorder 객체
      audioChunks: [], // 녹음된 오디오 데이터 조각
      isRecording: false, // 녹음 중인지 여부
      recording: false, // 버튼 아이콘 상태
      elapsedTime: 0, // 경과 시간 (초 단위)
      timer: null // setInterval 핸들러
    }
  },
  methods: {
    async toggleRecording() {
      if (!this.isRecording) {
        // 녹음을 시작
        try {
          const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
          this.mediaRecorder = new MediaRecorder(stream);

          this.mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
              this.audioChunks.push(event.data);
            }
          };

          this.mediaRecorder.start();
          this.isRecording = true;
          this.recording = true;
          this.startTimer();
        } catch (err) {
          console.error('녹음 시작 오류:', err);
        }
      } else {
        // 녹음을 종료
        this.mediaRecorder.stop();
        this.isRecording = false;
        this.recording = false;
        this.elapsedTime = 0; // 녹음 종료 후 시간 초기화
        this.stopTimer();
      }
    },
    saveRecording() {
      if (this.audioChunks.length === 0) return;

      // Blob을 WAV 형식으로 변환
      const blob = new Blob(this.audioChunks, { type: 'audio/wav' });
      const url = URL.createObjectURL(blob);

      // 녹음 파일 다운로드
      const a = document.createElement('a');
      a.href = url;
      a.download = `${this.recordingTitle || '녹음'}.wav`;
      a.click();

      // 상태 초기화
      this.audioChunks = [];
      this.recordingTitle = ''; // 제목 초기화
    },
    startTimer() {
      this.elapsedTime = 0;
      this.timer = setInterval(() => {
        this.elapsedTime += 1;
      }, 1000);
    },
    stopTimer() {
      if (this.timer) {
        clearInterval(this.timer);
        this.timer = null;
      }
    },
    formatTime(seconds) {
      const minutes = Math.floor(seconds / 60);
      const secs = seconds % 60;
      return `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }
  }
}
</script>
<style scoped>
/* 스타일링 추가 */
.title-input {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.record-button {
  display: block;
  margin: 20px auto; /* 제목 입력 필드 아래 중앙 정렬, 여백 증가 */
  padding: 20px; /* 버튼 크기를 키우기 위한 패딩 추가 */
  background-color: #f0f0f0; /* 배경색 추가, 필요에 따라 변경 */
  border: none; /* 기본 테두리 제거 */
  border-radius: 8px; /* 버튼 모서리 둥글게 */
}

.record-button img {
  width: 80px; /* 로고 크기 조정 */
  height: 80px; /* 로고 크기 조정 */
}

.save-button {
  background-color: #51903B;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px; /* 녹음 버튼과 간격 조정 */
}

.time-display {
  margin-top: 10px;
  font-size: 20px;
  font-weight: bold;
}
</style>