import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store/index.js'

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')
