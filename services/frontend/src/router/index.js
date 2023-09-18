import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '@/views/home/HomePage.vue'
import UserLogin from '@/views/auth/UserLogin.vue'
import UserRegister from '@/views/auth/UserRegister.vue'

const routes = [
  {
    path: '/',
    name: 'HomeRoute',
    component: HomePage
  },
  {
    path: '/user/login',
    component: UserLogin,
    name: 'LoginRoute'
  },
  {
    path: '/user/register',
    component: UserRegister,
    name: 'RegisterRoute'
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
