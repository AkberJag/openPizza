import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '@/views/Home/HomePage.vue'
import UserLogin from '@/views/Auth/UserLogin.vue'

const routes = [
    {
        path: '/',
        component: UserLogin,
        name: 'Home'
    },
    {
        path: '/user/login',
        component: UserLogin,
        name: 'Login'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
