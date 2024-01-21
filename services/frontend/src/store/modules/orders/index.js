import actions from './actions'
import getters from './getters'
import mutations from './mutations'

export default {
  namespaced: true,
  state() {
    return {
      ordersToday: 0,
      totalOrders: 0,
      ordersOnHold: [],
      currentCart: {
        id: 0,
        tax: 0,
        subTotal: 0,
        deliveryCharge: 0,
        extraCharge: { price: 0, reason: '' },
        orderType: 'Dine In',
        customer: null,
        items: [],
        order_notes: ''
      }
    }
  },
  actions,
  getters,
  mutations
}
