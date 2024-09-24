<template>
        <div class="logo-container">
      <img src="@/assets/mic-icon.png" alt="로고" />
      <span>회원가입</span>
    </div>
    <div class="pick-type-container">
      <div class="progress">
        <p>1/3</p>
        <div class="progress-bar">
          <div class="progress-filled"></div>
        </div>
      </div>
      <h2>해당하는 타입을 선택하세요!</h2>
      <p>선생님의 경우, 추후에 인증이 필요할 수 있습니다.</p>
      <div class="options">
        <div class="option" @click="selectType('teacher')">
          <img src="@/assets/teacher-icon.png" alt="선생님" />
        </div>
        <div class="option" @click="selectType('student')">
          <img src="@/assets/student-icon.png" alt="학생" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PickType',
    methods: {
      selectType(type) {
        if (type === 'teacher') {
          // 선생님을 선택했을 때의 로직 처리
          //alert('선생님을 선택하셨습니다.');
          // 만약 선생님도 다른 페이지로 보내려면 추가
          this.$router.push('/make-ID');
        } else if (type === 'student') {
          // 학생을 선택했을 때 'HomePage'로 이동
          this.$router.push('/home'); // '/' 경로가 HomePage일 경우
        }
      }
    }
  }
  </script>
  
  <style scoped>
.pick-type-container {
  text-align: center;
  margin-top: 20px;
  padding: 20px; /* 내부 여백 추가 */
  border: 2px solid #e0e0e0;
  border-radius: 15px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  max-width: 448px;
  width: 100%;
  height: 400px; /* 여기에서 높이 조정 */
  margin-left: auto;
  margin-right: auto;
}
  
.progress {
  text-align: left; /* 왼쪽 정렬 */
  margin-bottom: 10px; /* 아래 요소와의 간격 */
}
  
  .progress-bar {
    background-color: #e0e0e0;
    width: 100%;
    height: 5px;
    margin-top: 5px;
    position: relative;
  }
  
  .progress-filled {
    background-color: #51903B;
    width: 33%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
  }
  
  .options {
    display: flex;
    justify-content: center;
    gap: 50px;
    margin-top: 40px;
  }
  
  .option {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
  }
  
  .option img {
  width: 153px; /* 너비를 230px로 설정 */
  height: 153px; /* 높이를 230px로 설정 */
  margin-bottom: 20px; /* 아래쪽 여백을 줄이기 위해 설정 */
}

  .logo-container {
  text-align: center; /* 중앙 정렬 */
  margin-top: 20px; /* 간격 조정 */
}

.logo-container img {
  width: 122.82px; /* 로고 너비 */
  height: 123.94px; /* 로고 높이 */
}

.logo-container span {
  display: block; /* 텍스트를 블록으로 설정하여 아래에 위치하도록 함 */
  margin-top: 10px; /* 로고와 텍스트 간의 간격 조정 */
}
  </style>