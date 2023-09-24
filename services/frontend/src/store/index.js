import { createStore } from 'vuex'
import authModule from '@/store/modules/auth/index.js'
import globalModule from '@/store/modules/global/index.js'

const store = createStore({
  modules: {
    auth: authModule,
    global: globalModule
  }
})

export default store
