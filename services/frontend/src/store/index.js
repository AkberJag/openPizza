import { createStore } from 'vuex'

import globalModule from '@/store/modules/global/index.js'
import authModule from '@/store/modules/auth/index.js'
import menuModule from '@/store/modules/menu/index.js'
import orderModule from '@/store/modules/orders/index.js'
import adminItemsModule from './modules/admin_items'

const store = createStore({
  modules: {
    global: globalModule,
    auth: authModule,
    foodMenu: menuModule,
    orders: orderModule,
    adminItems: adminItemsModule
  }
})

export default store
