import { createApp } from 'vue'; // Vue 3의 createApp을 사용합니다.
import App from './App.vue';
import router from './router'; // 라우터 가져오기

const app = createApp(App);
app.use(router); // 라우터를 Vue 애플리케이션에 등록합니다.
app.mount('#app');