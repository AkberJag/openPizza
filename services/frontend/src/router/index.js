import { createRouter, createWebHistory } from "vue-router"

import HomePage from '@/views/Home/HomePage.vue'

const routes = [{
    path: '/',
    component: HomePage,
    name: "Home"
}]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;