import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '@/views/home/HomePage.vue'
import UserLogin from '@/views/auth/UserLogin.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/user/login',
    component: UserLogin,
    name: 'Login'
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
