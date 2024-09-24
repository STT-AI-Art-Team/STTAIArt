<template>
    <div class="logo-container">
      <img src="@/assets/mic-icon.png" alt="로고" />
      <span>회원가입</span>
    </div>
    <div class="pick-type-container">
      <div class="progress">
        <p>3/3</p>
        <div class="progress-bar">
          <div class="progress-filled"></div>
        </div>
      </div>
      <h2>교사 인증을 진행해주세요.</h2>
      <label for="usercode" class="label">선생님 접근 코드를 작성해주세요.</label>
      <input type="text" id="usercode" v-model="usercode" class="input-field" />
      <p class="small-text">교사 인증 코드를 작성하는 공간입니다.</p>

      <button @click="save" class="save-button">확인하기</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AccessPage',
    data() {
      return {
        usercode: '',
      };
    },
    methods: {
      save() {
        // Check if the input code matches 'test123'
        if (this.usercode === 'test123') {
          // Show a success alert
          alert('회원가입이 완료되었습니다.');
          // Redirect to the Login page
          this.$router.push('/'); //여기 경로 바꿔야 함 - 메인 페이지 중에서 선생님 교실 페이지로
        } else {
          // Show an error alert if the code is incorrect
          alert('인증 코드가 올바르지 않습니다.');
        }
      }
    }
  }
  </script>
  
  <style scoped>
.label {
  display: block; /* 레이블을 블록 요소로 설정 */
  margin-bottom: 5px; /* 레이블 아래쪽 여백 추가 */
  margin-left: 7%; /* 레이블과 입력 필드의 왼쪽 여백을 같게 설정 */
  text-align: left;

} 
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
    height: auto; /* 여기에서 높이 조정 */
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
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
  }
  
  .input-field {
  width: 80%; /* 입력 필드의 너비 */
  padding: 10px; /* 내부 여백 */
  margin: 10px 0; /* 위아래 간격 */
  border: 1px solid #e0e0e0;
  border-radius: 5px; /* 모서리 둥글게 */
}
  
.small-text {
  font-size: 0.8em; /* 글자 크기 조정 */
  color: #888; /* 색상 조정 (선택 사항) */
  margin-top: 5px; /* 위쪽 간격 추가 */
  text-align: left; /* 왼쪽 정렬 */
  margin-left: 7%; /* 레이블과 입력 필드의 왼쪽 여백을 같게 설정 */

}
  .save-button {
    padding: 10px 20px; /* 버튼의 패딩 */
    background-color: #51903B; /* 버튼 배경색 */
    color: white; /* 버튼 텍스트 색상 */
    border: none; /* 테두리 제거 */
    border-radius: 5px; /* 모서리 둥글게 */
    cursor: pointer; /* 포인터 커서 */
    margin-top: 20px; /* 버튼 위쪽 간격 */
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