<template>
    <div id="main-teacher-class">  
      <div class="class-icon">
        <img src="@/assets/mic-icon.png" alt="교실 아이콘" />
      </div>
      <h1 class="teacher-name">채성아 선생님의 교실</h1>
      <p class="empty-text">현재 기록이 비어 있습니다.</p>
      <p class="instruction-text">클래스를 만들어서 기록을 시작해보세요!</p>
  
      <button class="create-class-button">클래스 만들기</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MainTeacherclass'
  }
  </script>
  
  <style scoped>
  #main-teacher-class {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: auto;
    background-color: #fff;
    font-family: 'Arial', sans-serif;
  }
  
  .class-icon img {
    width: 80px;
    height: 80px;
  }

  .teacher-name {
    font-size: 24px;
    font-weight: bold;
    color: #4CAF50;
    margin: 20px 0 10px;
  }
  
  .empty-text, .instruction-text {
    font-size: 16px;
    color: #888;
    margin-bottom: 10px;
  }
  
  .create-class-button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .create-class-button span {
    margin-left: 5px;
  }
  </style>