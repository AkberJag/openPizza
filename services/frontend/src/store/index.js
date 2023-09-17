import { createStore } from 'vuex'
import authModule from '@/store/modules/auth/index.js'

const store = createStore({
  modules: {
    auth: authModule
  }
})

export default store
