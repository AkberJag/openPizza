export default {
  addCategory(state, payload) {
    state.menuData = payload
  },
  setItems(state, payload) {
    const categoryIndex = state.menuData.findIndex((category) => category.categoryID === payload.id)
    if (categoryIndex !== -1) {
      state.menuData[categoryIndex].items = payload.data
    }
  },
  addItemTocurrentCart(state, payload) {
    state.currentCart.subTotal += payload.price
    state.currentCart.items.push(payload)
  }
}
