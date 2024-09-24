<template>
    <div class="message-check">
      <h1>원하는 메시지가 맞나요?</h1>
      <p class="subtext">제대로 인식되지 않았다면 재녹음이 가능해요!</p>
      <div class="message-box">
        <p>꼬꼬닭이 있는데 금색이야 <br /> 이 닭은 막 뛰어다녀 엄청 신나 보여</p>
      </div>
      <div class="audio-control">
        <button @click="listenAgain" class="no-border-btn">
          <img src="@/assets/headphones.png" alt="헤드폰 아이콘" class="headphones-icon" />
          <br />
          다시 듣기
        </button>
      </div>
      <div class="buttons">
        <button class="correct" @click="goToImageGeneration">맞아요</button>
        <button class="incorrect" @click="showPopup = true">아니에요</button> <!-- '아니에요' 버튼 클릭 시 팝업 표시 -->
      </div>
  
      <!-- 팝업 창 -->
      <div v-if="showPopup" class="popup-overlay">
        <div class="popup-content">
          <h2>다시 녹음할 수 있어요!</h2>
          <p>확인을 누르시면 저장된 모든 데이터가 사라지고 녹음 페이지로 돌아갑니다.</p>
          <div class="popup-buttons">
            <button @click="confirmReRecord" class="confirm-btn">확인</button>
            <button @click="showPopup = false" class="cancel-btn">취소</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MessageCheckPage', // 컴포넌트의 이름을 MessageCheckPage로 설정
    data() {
      return {
        showPopup: false // 팝업이 표시되는지 여부를 제어하는 상태 변수
      };
    },
    methods: {
      listenAgain() {
        alert('다시 듣기 기능 실행');
      },
      confirmReRecord() {
        // 확인을 누르면 녹음 페이지로 이동하는 로직 (예시)
        this.showPopup = false; // 팝업을 닫음
        alert('녹음 페이지로 이동합니다.'); // 여기서 실제 로직으로 대체 가능
      },
      goToImageGeneration() {
        // 그림 생성 페이지로 이동
        this.$router.push({ name: 'generate-image' });
      }
    }
  }
  </script>
  
  <style scoped>
  .message-check {
    text-align: center;
    font-family: 'Arial', sans-serif;
  }
  
  .message-box {
    border: 1px solid #8BC34A;
    border-radius: 10px;
    padding: 20px;
    display: inline-block;
    margin: 20px 0;
    color: #4CAF50;
  }
  
  .audio-control {
    margin: 20px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  /* 헤드폰 아이콘 */
  .headphones-icon {
    height: 50px;
    margin-bottom: 10px; /* 아래 텍스트와의 간격 */
  }
  
  /* 투명 배경 및 기본 스타일 제거 */
  .no-border-btn {
    background-color: transparent; /* 배경을 투명하게 설정 */
    border: none; /* 테두리 제거 */
    color: #4CAF50; /* 텍스트 색상 */
    font-size: 16px;
    cursor: pointer;
    padding: 0;
    outline: none;
    text-align: center;
  }
  
  .buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
  }
  
  .correct {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  /* '아니에요' 버튼 기본 상태: 흰 배경에 초록 글씨 */
  .incorrect {
    background-color: white;
    color: #4CAF50;
    padding: 10px 20px;
    border: 2px solid #4CAF50; /* 테두리 추가 */
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s; /* 색상 전환에 부드러운 애니메이션 추가 */
  }
  
  /* 마우스 포인터를 올렸을 때: 빨간 배경, 흰 글씨 */
  .incorrect:hover {
    background-color: #F44336;
    color: white;
  }
  
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5); /* 반투명 배경 */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .popup-content {
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    max-width: 400px;
    width: 100%;
  }
  
  .popup-buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
  }
  
  .confirm-btn {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .cancel-btn {
    background-color: white;
    color: #8BC34A;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  