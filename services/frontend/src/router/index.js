import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '@/views/home/HomePage.vue'
import UserLogin from '@/views/auth/UserLogin.vue'
import UserRegister from '@/views/auth/UserRegister.vue'

import store from '../store/index.js'

const routes = [
  {
    path: '/',
    name: 'HomeRoute',
    component: HomePage,
    meta: { authRequired: true }
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
  routes,
  linkActiveClass: 'active'
})

// navigation guard
router.beforeEach(function (to, from, next) {
  if (to.meta.authRequired && !store.getters.isAuthenticated) {
    next({ name: 'LoginRoute' })
  } else {
    next()
  }
})

export default router
