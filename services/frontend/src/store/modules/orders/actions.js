import apiRequest from '../../api.js'

export default {
  async placeOrder(context) {
    let endpoint = 'order/'

    try {
      let currentCart = context.getters['getCurrentCart']

      const items = currentCart.items.map((item) => ({
        name: item.name,
        quantity: item.qty,
        price_per_unit: item.price,
        item_notes: 'No notes for this item',
        item_id: item.id
      }))

      let body = JSON.stringify({
        tax_val: currentCart.tax,
        order_notes: currentCart.order_notes || 'No notes',
        order_type: currentCart.orderType,
        extra_charge: currentCart.extraCharge.price,
        extra_charge_reason: currentCart.extraCharge.reason,
        delivery_charge: currentCart.deliveryCharge,
        order_items: items,
        customer: 1
      })

      let headers = { 'Content-Type': 'application/json' }

      const response = await apiRequest(endpoint, {
        method: 'POST',
        headers,
        body
      })
    } catch (error) {
      console.log(error)
    }
  },

  async loadAllOrders(context) {
    let endpoint = 'order/'
    let headers = { 'Content-Type': 'application/json' }

    try {
      const response = await apiRequest(endpoint, {
        method: 'GET',
        headers
      })

      const responseData = await response.json()

      if (!response.ok) {
        throw new Error(responseData.detail || 'Failed to fetch')
      }

      context.commit('setTotalOrders', responseData.length)
      return responseData
    } catch (error) {
      console.log(error)
    }
  }
}
