export default {
  getCurrentCart(state) {
    return state.currentCart
  },
  getOrdersOnHold(state) {
    return state.ordersOnHold
  },
  getDeliveryCharge(state) {
    return state.currentCart.deliveryCharge
  },
  getExtraCharge(state) {
    return state.currentCart.extraCharge
  },
  getTotalOrdersToday(state) {
    return state.ordersToday
  },
  getTotalOrders(state) {
    return state.totalOrders
  }
}
