import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '@/views/home/HomePage.vue'
import OrdersPage from '@/views/home/OrdersPage.vue'
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
    path: '/orders',
    name: 'OrdersRoute',
    component: OrdersPage,
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
router.beforeEach(async (to, from, next) => {
  if (to.meta.authRequired && !store.getters['auth/isAuthenticated']) {
    await store.dispatch('auth/try_auto_login')
    if (store.getters['auth/isAuthenticated']) {
      next()
    } else {
      next({ name: 'LoginRoute' })
    }
  } else {
    next()
  }
})

export default router
