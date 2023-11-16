export default {
  async getAllFoodCategories(context) {
    let url = 'http://localhost:5000/api/v1/home/food_categories'

    const response = await fetch(url, {
      method: 'GET',
      credentials: 'include'
    })

    const responseData = await response.json()

    const categories = []
    for (const key in responseData) {
      const category = {
        categoryID: responseData[key].category_id,
        categoryName: responseData[key].category_name,
        categoryImageURL: responseData[key].category_image_url
      }
      categories.push(category)
    }
    context.commit('addCategory', categories)
  },
  async getAllItems(context, payload) {
    let url = `http://localhost:5000/api/v1/home/food_category/${payload}/food_items`

    const response = await fetch(url, {
      method: 'GET',
      credentials: 'include'
    })

    const responseData = await response.json()
    context.commit('setItems', { id: payload, data: responseData })
  },

  async orderComplete(context) {
    let url = 'http://localhost:5000/api/v1/order/'

    let currentCart = context.getters['getCurrentCart']
    const items = currentCart.items.map((item) => ({
      product_id: item.tem_id,
      quantity: item.qty,
      price_per_unit: item.price,
      item_notes: '',
      product_name: item.item_name
    }))

    let body = JSON.stringify({
      tax_val: currentCart.tax,
      order_notes: 'No notes for now',
      order_items: items
    })
    let headers = { 'Content-Type': 'application/json' }

    const response = await fetch(url, {
      method: 'POST',
      headers,
      body
    })

    context.commit('clearCurrentCart')
  }
}
