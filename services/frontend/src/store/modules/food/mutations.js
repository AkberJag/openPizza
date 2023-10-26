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
    const itemIndex = state.currentCart.items.findIndex((item) => item.item_id === payload.item_id)
    if (itemIndex !== -1) {
      // If the item exists, increase its qty
      state.currentCart.items[itemIndex].qty++
    } else {
      // If the item doesn't exist, add it to the array with qty 1
      state.currentCart.items.push({ ...payload, qty: 1 })
    }
  }
}
