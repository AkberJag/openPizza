import { createRouter, createWebHistory } from 'vue-router'

import store from '../store/index.js'

const routes = [
  {
    path: '/user/login',
    component: () => import('../views/auth/LoginPage.vue'),
    name: 'LoginRoute'
  },
  {
    path: '/user/register',
    component: () => import('../views/auth/RegisterPage.vue'),
    name: 'RegisterRoute'
  },
  {
    path: '/',
    name: 'MenuRoute',
    component: () => import('../views/menu/OrderMenu.vue'),
    meta: { authRequired: true }
  },
  {
    path: '/orders',
    name: 'OrdersRoute',
    component: () => import('../views/orders/OrdersPlaced.vue'),
    meta: { authRequired: true }
  },
  {
    path: '/items/add',
    name: 'AddItemsRoute',
    component: () => import('../views/admin/categoryAndItems/AddItem.vue'),
    meta: { authRequired: true }
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
      store.commit('addToast', {
        toastTitle: 'Not logged in',
        toastBody: `Please login to access that content.`,
        toastClass: 'danger'
      })
    }
  } else {
    next()
  }
})

export default router
