export default {
  addItemToCurrentCart(state, payload) {
    state.currentCart.subTotal += payload[0].price

    const itemIndex = state.currentCart.items.findIndex((item) => item.id === payload[0].id)

    if (itemIndex !== -1) {
      // If the item exists, increase its qty
      state.currentCart.items[itemIndex].qty++
    } else {
      // If the item doesn't exist, add it to the array with qty 1
      state.currentCart.items.push({ ...payload[0], qty: 1, categoryName: payload[1] })
    }
    if (state.currentCart.id === 0) {
      state.currentCart.id = state.ordersToday + 1
    }
  },

  removeItemFromCurrentCart(state, payload) {
    const itemIndex = state.currentCart.items.findIndex((item) => item.id === payload.itemId)

    if (itemIndex !== -1) {
      // decrease its qty
      if (payload.val === -1) {
        // decrease price
        state.currentCart.subTotal -= state.currentCart.items[itemIndex].price

        state.currentCart.items[itemIndex].qty--

        // if items qty become zero, remove it from cart
        if (state.currentCart.items[itemIndex].qty <= 0) {
          state.currentCart.items.splice(itemIndex, 1)
        }
      } else if (payload.val === 1) {
        // increase price
        state.currentCart.subTotal += state.currentCart.items[itemIndex].price
        // increase its qty
        state.currentCart.items[itemIndex].qty++
      }
      // remove the whole item from the array
      else {
        // increase price
        state.currentCart.subTotal -= Math.max(
          state.currentCart.items[itemIndex].price * state.currentCart.items[itemIndex].qty,
          0
        )
        state.currentCart.items.splice(itemIndex, 1)
      }
    }
  },

  clearCurrentCart(state) {
    // clear all items in the cart and set the total to 0
    state.currentCart.subTotal = 0
    state.currentCart.items = []
    state.currentCart.id = 0
  },

  addDeliveryCharge(state, payload) {
    state.currentCart.subTotal -= state.currentCart.deliveryCharge
    state.currentCart.deliveryCharge = payload
    state.currentCart.subTotal += payload
  },

  addExtraCharge(state, payload) {
    state.currentCart.subTotal -= state.currentCart.extraCharge.price
    state.currentCart.extraCharge = payload
    state.currentCart.subTotal += payload.price
  },

  setTax(state, taxAmnt) {
    state.currentCart.tax = taxAmnt
  },

  holdCurrentOrder(state) {
    state.ordersOnHold.push({ ...state.currentCart })
    state.ordersToday++
  },

  onHoldToCart(state, payload) {
    const orderOnHoldIndex = state.ordersOnHold.findIndex((item) => item.id === payload.id)
    if (orderOnHoldIndex !== -1 && payload.action === 'move') {
      state.currentCart = state.ordersOnHold.splice(orderOnHoldIndex, 1)[0]
    } else {
      // delete item from hold
      state.ordersOnHold.splice(orderOnHoldIndex, 1)
    }
  },

  setTotalOrders(state, payload) {
    state.totalOrders = payload
  },

  setOrderNote(state, payload) {
    state.currentCart.order_notes = payload
  }
}
