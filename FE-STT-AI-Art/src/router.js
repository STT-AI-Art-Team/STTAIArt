import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/HomePage.vue';
import ClassroomPage from './views/ClassRoom.vue'; // Assuming ClassRoom.vue is ClassroomPage
import PickTypePage from './views/PickType.vue'; // Import the new PickType.vue
import MakeIDPage from './views/MakeID.vue'; // Import MakeID.vue
import AccessPage from './views/Access.vue'; 
import MessageCheckPage from './views/MessageCheck.vue';
import ImageGenerationPage from './views/ImageGeneration.vue';
import SaveImagePage from './views/SaveImage.vue';
import LoginPage from './views/Login.vue';
import MainteacherclassPage from './views/MainTeacherclass.vue';


const routes = [
  {
    path: '/',
    name: 'pick-type',
    component: PickTypePage // Make PickType.vue the default route
  },
  {
    path: '/home',
    name: 'home',
    component: HomePage
  },
  {
    path: '/classroom',
    name: 'classroom',
    component: ClassroomPage
  },
  {
    path: '/make-id', // Add the new route for MakeID
    name: 'make-id',
    component: MakeIDPage // Set the component for this route
  },
  {
    path: '/access', // Add the new route for MakeID
    name: 'access',
    component: AccessPage // Set the component for this route
  },
  {
    path: '/message-check', // 새로운 경로 추가
    name: 'message-check',
    component: MessageCheckPage // MessageCheck 컴포넌트로 연결
  },
  {
    path: '/generate-image', // 새 경로 추가
    name: 'generate-image',
    component: ImageGenerationPage
  },
  {
    path: '/save-image',
    name: 'save-image',
    component: SaveImagePage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/mainteacherclass',
    name: 'mainteacherclass',
    component: MainteacherclassPage
  }

];

const router = createRouter({
  history: createWebHistory(), // Vue Router 4 using history mode
  routes
});

export default router;