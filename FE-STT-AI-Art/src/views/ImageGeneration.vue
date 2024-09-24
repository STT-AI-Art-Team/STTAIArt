<template>
    <div class="image-generation-page">
      <h1>멋진 그림을 생성하고 있어요...</h1>
      <p>입력하신 내용을 바탕으로 멋진 그림을 생성하고 있어요...</p>
  
      <!-- 로딩 중일 때 로딩 아이콘을 보여줌 -->
      <div v-if="isLoading" class="loading-container">
        <div class="loading-icon"></div>
        <p>로딩 중</p>
      </div>
  
      <!-- 로딩이 끝나면 그림을 보여줌 -->
      <div v-else>
        <img :src="generatedImageUrl" alt="생성된 이미지" class="generated-image" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ImageGenerationPage',
    data() {
      return {
        isLoading: true, // 로딩 상태 관리
        generatedImageUrl: '' // 생성된 이미지를 저장할 변수
      };
    },
    mounted() {
      // 페이지가 로드되면 OpenAI API 호출
      this.generateImage();
    },
    methods: {
      async generateImage() {
        try {
          // 여기서 실제 API 호출을 합니다 (백엔드와 연동)
          const response = await fetch('백엔드_API_엔드포인트', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              message: '달리는 금색 닭', // 사용자가 입력한 메시지 예시
            }),
          });
  
          // 응답에서 생성된 이미지 URL을 가져옴
          const data = await response.json();
          this.generatedImageUrl = data.imageUrl;
  
          // 이미지가 생성되면 로딩 상태를 종료
          this.isLoading = false;
        } catch (error) {
          console.error('이미지 생성 오류:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .image-generation-page {
    text-align: center;
    font-family: 'Arial', sans-serif;
  }
  
  .loading-container {
    margin-top: 20px;
  }
  
  .loading-icon {
    width: 50px;
    height: 50px;
    border: 5px solid #4CAF50; /* 녹색 외곽선 */
    border-top: 5px solid transparent; /* 상단은 투명하게 해서 회전 효과 */
    border-radius: 50%;
    animation: spin 2s linear infinite; /* 시계 방향 회전 애니메이션 */
    margin: 0 auto;
  }
  
  @keyframes spin {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }
  
  .generated-image {
    margin-top: 20px;
    max-width: 100%;
    height: auto;
  }
  </style>
  