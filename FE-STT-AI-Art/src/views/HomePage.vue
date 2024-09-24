<template>
  <div>
    <main class="main-content">
      <div class="mic-icon">
        <img src="../assets/mic-icon.png" alt="Microphone">
      </div>
      <h1>교실의 코드를 입력하세요.</h1>
      <p>담당 선생님께서 띄워주는 숫자를 작성해주세요!</p>

      <!-- 입력 필드 -->
      <input 
        v-model="classCode" 
        class="code-input" 
        type="text" 
        placeholder="코드를 입력하세요" 
        maxlength="9"
      />

      <button class="connect-button" @click="connectToClass">연결하기</button>
    </main>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      classCode: '' // 입력된 코드를 저장하는 데이터
    }
  },
  methods: {
    connectToClass() {
      const correctCode = '123456789'; // 올바른 코드
      if (this.classCode === correctCode) {
        // 올바른 코드가 입력되면 /classroom 페이지로 이동
        this.$router.push({ name: 'classroom' });
      } else {
        alert('잘못된 코드입니다. 다시 입력해주세요.');
      }
    }
  }
}
</script>

<style scoped>
/* 기본 스타일 */
.main-content {
  margin: 20px auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
  padding: 0 20px;
}

.mic-icon {
  margin-top: 30px;
}

.mic-icon img {
  width: 60px;
  height: 60px;
}

.code-input {
  font-size: 32px;
  margin: 20px 0;
  padding: 10px 20px;
  border: 1px solid #51903B;
  border-radius: 8px;
  color: #51903B;
  width: 300px;
  text-align: center;
}

.connect-button {
  background-color: #51903B;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 20px;
}

/* 반응형 디자인 설정 */
@media (max-width: 600px) {
  .main-content {
    max-width: 100%;
    padding: 0 10px;
  }

  .code-input {
    font-size: 24px;
    padding: 8px 15px;
    width: 100%;
  }

  .connect-button {
    padding: 8px 15px;
    font-size: 16px;
  }
}
</style>