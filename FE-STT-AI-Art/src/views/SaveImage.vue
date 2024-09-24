<template>
    <div class="image-generation-page">
      <h1>만들어진 그림을 저장해보세요!</h1>
      <p>달리는 금색 닭</p>
  
      <!-- 생성된 이미지 표시 -->
      <div v-if="generatedImageUrl" class="image-container">
        <img :src="generatedImageUrl" alt="생성된 이미지" class="generated-image" />
      </div>
  
      <!-- 저장하기 및 다시하기 버튼 -->
      <div class="action-buttons" v-if="generatedImageUrl">
        <!-- 저장하기 버튼 -->
        <a :href="generatedImageUrl" download="generated-image.png" class="save-btn">
          저장하기 ✔️
        </a>
        <!-- 다시하기 버튼 -->
        <button @click="goToRecordPage" class="retry-btn">
          다시하기 🔄
        </button>
      </div>
    </div>
  </template>
  
  <script>
export default {
  name: 'SaveImagePage', // 컴포넌트의 이름을 SaveImagePage로 설정
  data() {
    return {
      generatedImageUrl: '' // 생성된 이미지 URL을 저장
    };
  },
  mounted() {
    // 이 메서드는 실제로 백엔드에서 생성된 이미지 URL을 가져오는 로직을 포함해야 함
    this.generateImage();
  },
  methods: {
    async generateImage() {
      try {
        // 실제 API 호출 부분 (백엔드와 연동하여 이미지 생성)
        const response = await fetch('백엔드_API_엔드포인트', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            message: '달리는 금색 닭', // 메시지 예시
          }),
        });

        // 응답에서 생성된 이미지 URL을 가져옴
        const data = await response.json();
        this.generatedImageUrl = data.imageUrl;
      } catch (error) {
        console.error('이미지 생성 오류:', error);
      }
    },
    goToRecordPage() {
      // 녹음 페이지로 이동하는 로직 (라우터를 통해 페이지 이동)
      this.$router.push({ name: 'record-page' }); // 라우트 이름에 맞게 수정
    }
  }
};

  </script>
  
  <style scoped>
  .image-generation-page {
    text-align: center;
    font-family: 'Arial', sans-serif;
  }
  
  .image-container {
    margin-top: 20px;
  }
  
  .generated-image {
    width: 100%;
    max-width: 500px;
    height: auto;
    border-radius: 10px;
  }
  
  .action-buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
  }
  
  .save-btn, .retry-btn {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 16px;
  }
  
  .retry-btn {
    background-color: #F44336;
  }
  </style>
  